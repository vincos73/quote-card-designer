"""Regression checks for portable resources and explicit archive boundaries."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_resources import ResourceBundle


class PackageResourcesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.write('SKILL.md', '# Test skill\n')
        self.policy = dict(schema_version=1,
                           archive_repository='https://github.com/example/styles',
                           archive_revision='a' * 40, runtime_assets=[], archive_assets=[])

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode())
        return path

    def freeze_archive(self):
        for args in (['init', '-q'], ['add', '.'],
                     ['-c', 'user.name=Package test', '-c', 'user.email=test@example.invalid',
                      '-c', 'commit.gpgsign=false', 'commit', '-qm', 'Archive fixture']):
            subprocess.run(['git', '-C', str(self.root), *args], check=True, capture_output=True)
        self.policy['archive_revision'] = subprocess.check_output(
            ['git', '-C', str(self.root), 'rev-parse', 'HEAD'], text=True).strip()

    def bundle(self, *files):
        result = ResourceBundle(self.root, self.policy)
        for name in files:
            result.add(self.root / name)
        return result

    def test_operational_inputs_notes_and_fonts_remain_local_and_identical(self):
        self.write('reference.png', b'operational image bytes')
        self.write('font.otf', b'font bytes')
        self.write('license.txt', 'Test font license')
        self.write('notes.md', '[Licenza](license.txt)\n')
        original = {'Reference Basis': {'Approved Image Inputs': ['reference.png']},
                    'Font': 'font.otf', 'Notes': 'notes.md'}
        self.write('profile.yaml', yaml.safe_dump(original))
        self.policy['runtime_assets'] = ['reference.png', 'font.otf', 'license.txt']
        files = self.bundle('profile.yaml').prepare()
        self.assertEqual(set(files), {'profile.yaml', 'notes.md', 'reference.png', 'font.otf', 'license.txt'})
        for name, raw in files.items():
            self.assertEqual(raw, (self.root / name).read_bytes())

    def test_archive_links_are_pinned_and_studies_are_not_included(self):
        self.write('study image.png', b'study bytes')
        self.write('old.yaml', 'Design Style: {Name: Previous direction}\n')
        self.write('profile.yaml', 'Design Style:\n  Previous Profile: old.yaml\n  Notes: notes.md\n')
        self.write('notes.md', '# Notes\n\n[Study](<study image.png> "Caption")\n'
                   '![Preview][study]\n[study]: study%20image.png#detail\n')
        self.freeze_archive()
        self.policy['archive_assets'] = ['study image.png', 'old.yaml']
        original = (self.root / 'notes.md').read_bytes()
        bundle = self.bundle('profile.yaml')
        files = bundle.prepare()
        self.assertEqual(set(files), {'profile.yaml', 'notes.md'})
        profile = yaml.safe_load(files['profile.yaml'])
        base = f"{self.policy['archive_repository']}/blob/{self.policy['archive_revision']}/"
        self.assertEqual(profile['Design Style']['Previous Profile'], base + 'old.yaml')
        self.assertEqual(profile['Design Style']['Notes'], 'notes.md')
        self.assertIn(base + 'study%20image.png#detail', files['notes.md'].decode())
        self.assertIn('"Caption"', files['notes.md'].decode())
        self.assertIn('non sono incluse', files['notes.md'].decode())
        self.assertEqual((self.root / 'notes.md').read_bytes(), original)

    def test_stale_archive_refuses_to_claim_the_local_revision_is_online(self):
        self.write('study.png', b'old image')
        self.write('notes.md', '[Study](study.png)')
        self.freeze_archive()
        self.policy['archive_assets'] = ['study.png']
        self.write('study.png', b'new unpublished image')
        with self.assertRaisesRegex(ValueError, 'exact resource'):
            self.bundle('notes.md').prepare()

    def test_missing_link_fails_instead_of_creating_an_incomplete_zip(self):
        self.write('notes.md', '[Study](absent.png)')
        with self.assertRaisesRegex(ValueError, 'Missing or invalid resource'):
            self.bundle('notes.md').prepare()

    def test_unclassified_transitive_asset_fails_even_when_it_exists(self):
        self.write('notes.md', '[More](more.md)')
        self.write('more.md', '[Asset](image.webp)')
        self.write('image.webp', b'bytes')
        with self.assertRaisesRegex(ValueError, 'Undeclared resource role'):
            self.bundle('notes.md').prepare()

    def test_operational_input_cannot_be_reclassified_as_archive(self):
        self.write('reference.png', b'bytes')
        self.write('profile.yaml', 'Reference Basis:\n  Approved Image Inputs: [reference.png]\n')
        self.policy['archive_assets'] = ['reference.png']
        with self.assertRaisesRegex(ValueError, 'operational asset'):
            self.bundle('profile.yaml').prepare()

    def test_resource_roles_cannot_overlap(self):
        self.write('reference.png', b'bytes')
        self.policy['archive_assets'] = self.policy['runtime_assets'] = ['reference.png']
        with self.assertRaisesRegex(ValueError, 'both operational and archived'):
            self.bundle('SKILL.md')

    def test_symlink_outside_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / 'image.png'
            external.write_bytes(b'bytes')
            (self.root / 'escape.png').symlink_to(external)
            self.write('notes.md', '[Image](escape.png)')
            with self.assertRaisesRegex(ValueError, 'Missing or invalid resource'):
                self.bundle('notes.md').prepare()

    def test_http_links_and_local_anchors_need_no_packaged_file(self):
        original = '# Notes\n[Source](https://example.org/paper.pdf) [Section](#notes)'
        self.write('notes.md', original)
        self.assertEqual(self.bundle('notes.md').prepare()['notes.md'], original.encode())

    def test_note_in_prose_with_colon_is_a_real_dependency(self):
        self.write('notes.md', 'A relevant limitation.')
        self.write('profile.yaml', 'Validation: "Notes: see notes.md before recommending."\n')
        self.assertIn('notes.md', self.bundle('profile.yaml').prepare())


if __name__ == '__main__':
    unittest.main()
