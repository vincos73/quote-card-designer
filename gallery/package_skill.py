"""Package the selected V1 profiles and their declared local resources."""
from pathlib import Path
import argparse
import zipfile

import yaml

from style_resources import load_style_document
from package_resources import INLINE_NOTE, ResourceBundle

ROOT = Path(__file__).resolve().parent.parent
INDEX_KEYS = ('id', 'family', 'name', 'aliases', 'summary', 'tags', 'profile')


def package(destination=None):
    catalog = yaml.safe_load((ROOT / 'references/catalogo-v1.yaml').read_text())
    library = yaml.safe_load((ROOT / 'references/catalogo-stili.yaml').read_text())
    frontmatter = (ROOT / 'SKILL.md').read_text().split('---', 2)[1]
    metadata = yaml.safe_load(frontmatter)
    version = metadata['metadata']['version']
    selection = library['release_selection']
    selected = [s for s in library['styles'] if s.get('release_candidate')]
    identifiers = [s['id'] for s in catalog['styles']]
    if len(identifiers) != len(set(identifiers)):
        raise ValueError('Duplicate V1 style identifiers')
    if set(identifiers) != {s['id'] for s in selected} or identifiers != selection['styles']:
        raise ValueError('V1 index and library selection differ')
    if any(s.get('v1_shortlisted') for s in selected):
        raise ValueError('Selected styles must not also be candidates')
    if version != catalog['catalog_version'] or version != selection['catalog_version']:
        raise ValueError('Skill and catalog versions differ')
    if catalog['families'] != library['families']:
        raise ValueError('V1 and library categories differ')

    files = {ROOT / 'SKILL.md', ROOT / 'agents/openai.yaml',
             ROOT / 'references/catalogo-v1.yaml'}
    files.update(ROOT / name for name in INLINE_NOTE.findall((ROOT / 'SKILL.md').read_text()))
    by_id = {s['id']: s for s in selected}
    families = {f['id'] for f in catalog['families']}
    names = {}
    composition_count = 0
    for style in catalog['styles']:
        if style != {k: by_id[style['id']][k] for k in INDEX_KEYS}:
            raise ValueError(f"V1 metadata differs for {style['id']}")
        if style['family'] not in families:
            raise ValueError(f"Unknown family for {style['id']}")
        for name in (style['id'], style['name'], *style['aliases']):
            key = name.casefold().strip()
            if key in names and names[key] != style['id']:
                raise ValueError(f'Ambiguous style name or alias: {name}')
            names[key] = style['id']
        profile = ROOT / style['profile']
        document, companions = load_style_document(profile)
        composition_count += bool(document.get('Composition Library'))
        files.update([profile, *companions])
    policy = yaml.safe_load((ROOT / 'gallery/package-resources.yaml').read_text())
    bundle = ResourceBundle(ROOT, policy)
    for path in files:
        bundle.add(path)
    contents = bundle.prepare()

    destination = Path(destination) if destination else ROOT / f'build/quote-card-designer-{version}.zip'
    if destination.exists():
        raise FileExistsError(f'Package already exists: {destination}')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, 'x', zipfile.ZIP_DEFLATED) as archive:
        for relative, raw in sorted(contents.items()):
            archive.writestr(f"{metadata['name']}/{relative}", raw)
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip():
            raise ValueError('Corrupt archive')
    print(f'{destination}: {len(identifiers)} styles, {composition_count} composition libraries, '
          f'{len(contents)} files, {destination.stat().st_size / 1024 / 1024:.2f} MiB, '
          f'{len(bundle.externalized)} verified archive resources')
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New ZIP output path')
    package(parser.parse_args().output)
