"""Build portable skill resources without implicitly shipping the study archive."""
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import yaml


LOCAL_RESOURCE = re.compile(r'[\w./-]+\.(?:yaml|yml|md|png|jpe?g|webp|svg|pdf|ttf|otf|woff2?|txt)')
INLINE_NOTE = re.compile(r'(?<![\w:/.-])(?:[\w.-]+/)*[\w.-]+\.md(?![\w.-])')
# Inline links/images (including angle brackets and titles) and reference definitions.
MARKDOWN_TARGET = re.compile(
    r'(?:\]\(\s*|^ {0,3}\[[^\]\n]+\]:\s*)(?P<target><[^>\n]+>|[^\s)]+)',
    re.MULTILINE,
)
ARCHIVE_NOTE = (
    '> Le risorse di studio collegate all’archivio GitHub non sono incluse nella skill. '
    'I collegamenti identificano la revisione verificata; non sono input di generazione.\n\n'
)


def map_markdown_links(text, transform):
    def replace(match):
        target = match.group('target')
        angled = target.startswith('<') and target.endswith('>')
        updated = transform(target[1:-1] if angled else target)
        if angled:
            updated = f'<{updated}>'
        start = match.start('target') - match.start()
        end = match.end('target') - match.start()
        return match.group()[:start] + updated + match.group()[end:]
    return MARKDOWN_TARGET.sub(replace, text)


class ResourceBundle:
    def __init__(self, root, policy):
        self.root = Path(root).resolve()
        if policy.get('schema_version') != 1:
            raise ValueError('Unsupported package resource policy')
        self.repository = policy['archive_repository'].rstrip('/')
        self.revision = policy['archive_revision']
        if not re.fullmatch(r'https://github\.com/[\w.-]+/[\w.-]+', self.repository):
            raise ValueError('Expected a GitHub archive repository URL')
        if not re.fullmatch(r'[0-9a-f]{40}', self.revision):
            raise ValueError('The archive needs an immutable full Git revision')
        self.runtime = {self.resolve(self.root / 'SKILL.md', p) for p in policy['runtime_assets']}
        self.archive = {self.resolve(self.root / 'SKILL.md', p) for p in policy['archive_assets']}
        if self.runtime & self.archive:
            raise ValueError('A resource cannot be both operational and archived')
        self.files = set()
        self.contents = {}
        self.externalized = {}

    def resolve(self, source, target):
        relative = Path(unquote(target))
        if relative.is_absolute():
            raise ValueError(f'Absolute resource path in {source}: {target}')
        path = (Path(source).parent / relative).resolve()
        if not path.is_relative_to(self.root) or not path.is_file():
            raise ValueError(f'Missing or invalid resource in {source}: {target}')
        return path

    def add(self, path):
        path = Path(path).resolve()
        if not path.is_relative_to(self.root) or not path.is_file():
            raise ValueError(f'Missing or invalid package file: {path}')
        if path in self.archive:
            raise ValueError(f'Archived resource cannot be included implicitly: {path}')
        self.files.add(path)

    def archive_url(self, path):
        if path not in self.externalized:
            relative = path.relative_to(self.root).as_posix()
            result = subprocess.run(
                ['git', '-C', str(self.root), 'show', f'{self.revision}:{relative}'],
                capture_output=True,
            )
            if result.returncode or result.stdout != path.read_bytes():
                raise ValueError(f'Archive does not contain this exact resource: {relative}')
            self.externalized[path] = f'{self.repository}/blob/{self.revision}/{quote(relative, safe="/")}'
        return self.externalized[path]

    def dependency(self, source, target, root_relative=False):
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            return target
        base = self.root / 'SKILL.md' if root_relative and url.path.startswith('references/') else source
        path = self.resolve(base, url.path)
        if path in self.archive:
            archived = urlsplit(self.archive_url(path))
            return urlunsplit(archived._replace(query=url.query, fragment=url.fragment))
        if path in self.files or path in self.runtime or path.suffix == '.md':
            self.add(path)
            return target
        raise ValueError(f'Undeclared resource role in {source}: {target}; classify it in package-resources.yaml')

    def yaml_value(self, value, source):
        if isinstance(value, dict):
            approved = value.get('Approved Image Inputs', [])
            for item in approved:
                path = self.resolve(source, item)
                if path not in self.runtime:
                    raise ValueError(f'Approved image input must be an operational asset: {path}')
            return {key: self.yaml_value(item, source) for key, item in value.items()}
        if isinstance(value, list):
            return [self.yaml_value(item, source) for item in value]
        if not isinstance(value, str) or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', value):
            return value
        for note in INLINE_NOTE.findall(value):
            self.dependency(source, note, root_relative=True)
        if LOCAL_RESOURCE.fullmatch(value):
            return self.dependency(source, value, root_relative=True)
        return value

    def prepare(self):
        while pending := self.files - self.contents.keys():
            for path in sorted(pending):
                raw = path.read_bytes()
                if path.suffix in {'.yaml', '.yml'}:
                    original = yaml.safe_load(raw)
                    exported = self.yaml_value(original, path)
                    if exported != original:
                        raw = ('# Risorse di studio esterne: archivio GitHub verificato, non input di generazione.\n'
                               + yaml.safe_dump(exported, allow_unicode=True, sort_keys=False, width=100)).encode()
                elif path.suffix == '.md':
                    original = raw.decode()
                    exported = map_markdown_links(original, lambda target: self.dependency(path, target))
                    if exported != original:
                        # Explain the external archive only in documents whose links changed.
                        first, _, rest = exported.partition('\n')
                        exported = first + '\n\n' + ARCHIVE_NOTE + rest.lstrip('\n') if first.startswith('# ') else ARCHIVE_NOTE + exported
                        raw = exported.encode()
                self.contents[path] = raw
        self.validate_links()
        return {path.relative_to(self.root).as_posix(): raw for path, raw in self.contents.items()}

    def validate_links(self):
        def check(source, target):
            url = urlsplit(target)
            if not url.scheme and not url.netloc and url.path:
                path = self.resolve(source, url.path)
                if path not in self.contents:
                    raise ValueError(f'Unresolved link in packaged document {source}: {target}')
            return target
        for source, raw in self.contents.items():
            if source.suffix == '.md':
                map_markdown_links(raw.decode(), lambda target: check(source, target))
