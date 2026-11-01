"""Check the actual release selection after extracting a fresh archive."""
from pathlib import Path
import posixpath
import re
import sys
import tempfile
import unittest
from urllib.parse import unquote, urlsplit
import zipfile

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_skill import ROOT, package
from style_resources import load_style_document


class PackagedSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        output = Path(cls.temp.name).resolve()
        archive = package(output / 'candidate.zip')
        with zipfile.ZipFile(archive) as source:
            if source.testzip() is not None:
                raise AssertionError('Corrupt archive')
            source.extractall(output / 'extracted')
        cls.extracted = output / 'extracted/quote-card-designer'
        cls.catalog = yaml.safe_load((ROOT / 'references/catalogo-v1.yaml').read_text())
        cls.policy = yaml.safe_load((ROOT / 'gallery/package-resources.yaml').read_text())

    def test_every_selected_style_and_composition_loads_offline(self):
        for style in self.catalog['styles']:
            with self.subTest(style=style['id']):
                actual, _ = load_style_document(self.extracted / style['profile'])
                expected, _ = load_style_document(ROOT / style['profile'])
                self.assertEqual(actual.get('Composition Library'), expected.get('Composition Library'))
                self.assertEqual(actual['Design Style']['Name'], expected['Design Style']['Name'])

    def test_export_changes_only_declared_archive_paths_in_yaml(self):
        base = f"{self.policy['archive_repository']}/blob/{self.policy['archive_revision']}/"

        def export_expected(value, directory):
            if isinstance(value, dict):
                return {key: export_expected(item, directory) for key, item in value.items()}
            if isinstance(value, list):
                return [export_expected(item, directory) for item in value]
            if isinstance(value, str):
                for path in self.policy['archive_assets']:
                    if value in (path, posixpath.relpath(path, directory)):
                        return base + path
            return value

        for path in self.extracted.rglob('*.yaml'):
            relative = path.relative_to(self.extracted)
            with self.subTest(file=str(relative)):
                expected = export_expected(yaml.safe_load((ROOT / relative).read_text()), relative.parent.as_posix())
                self.assertEqual(yaml.safe_load(path.read_text()), expected)

    def test_markdown_links_resolve_with_no_access_to_the_source_tree(self):
        for path in self.extracted.rglob('*.md'):
            for target in re.findall(r'\]\(([^\s)]+)\)', path.read_text()):
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                with self.subTest(file=str(path.relative_to(self.extracted)), link=target):
                    resource = (path.parent / unquote(url.path)).resolve()
                    self.assertTrue(resource.is_relative_to(self.extracted))
                    self.assertTrue(resource.is_file())

    def test_operational_assets_are_exact_and_archive_is_not_embedded(self):
        for name in self.policy['runtime_assets']:
            self.assertEqual((self.extracted / name).read_bytes(), (ROOT / name).read_bytes())
        for name in self.policy['archive_assets']:
            self.assertFalse((self.extracted / name).exists(), name)
        binary = {p.relative_to(self.extracted).as_posix() for p in self.extracted.rglob('*')
                  if p.is_file() and p.suffix not in {'.yaml', '.yml', '.md'}}
        self.assertEqual(binary, set(self.policy['runtime_assets']))


if __name__ == '__main__':
    unittest.main()
