"""Pixel, color and output guarantees for stamping a logo on a finished card."""
from pathlib import Path
import sys
import tempfile
import unittest

from PIL import Image, ImageCms, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
from apply_logo import apply_logo


class LogoOverlayTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        directory = Path(folder.name)
        self.base = directory / 'base.png'
        self.logo = directory / 'logo.png'
        self.output = directory / 'out.png'

    def test_alpha_holes_and_translucent_pixels(self):
        base = Image.new('RGBA', (7, 6), (200, 100, 50, 255))
        base.putpixel((3, 2), (13, 24, 35, 0))
        base.save(self.base)
        logo = Image.new('RGBA', (3, 1))
        logo.putdata([(24, 48, 72, 255), (0, 0, 0, 0), (0, 0, 0, 128)])
        logo.save(self.logo)
        apply_logo(self.base, self.logo, self.output, 2, 2)
        expected = base.copy()
        expected.putpixel((2, 2), (24, 48, 72, 255))
        expected.putpixel((4, 2), (100, 50, 25, 255))
        with Image.open(self.output) as result:
            self.assertEqual(result.tobytes(), expected.tobytes())
        with self.assertRaises(FileExistsError):
            apply_logo(self.base, self.logo, self.output, 0, 0)
        with Image.open(self.output) as preserved:
            self.assertEqual(preserved.tobytes(), expected.tobytes())

    def test_icc_and_rgb_transparency_preserved_with_scaled_logo(self):
        profile = ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
        base = Image.new('RGB', (15, 15), (20, 30, 40))
        base.save(self.base, icc_profile=profile, transparency=(20, 30, 40))
        Image.new('RGBA', (10, 4), (255, 255, 255, 255)).save(self.logo)
        apply_logo(self.base, self.logo, self.output, 4, 5, width=5)
        with Image.open(self.output) as result:
            self.assertEqual(result.info['icc_profile'], profile)
            self.assertEqual(result.getchannel('A').getbbox(), (4, 5, 9, 7))
            self.assertEqual(result.getpixel((5, 5)), (255, 255, 255, 255))
            self.assertEqual(result.getpixel((0, 0)), (20, 30, 40, 0))

    def test_jpeg_is_compared_in_reading_orientation(self):
        jpeg = self.base.with_suffix('.jpg')
        exif = Image.Exif()
        exif[274] = 6
        base = Image.new('RGB', (4, 2), (14, 91, 43))
        base.putpixel((2, 1), (231, 86, 18))
        base.save(jpeg, exif=exif)
        Image.new('RGBA', (1, 1), 'white').save(self.logo)
        with Image.open(jpeg) as source:
            expected = ImageOps.exif_transpose(source).convert('RGBA')
        expected.putpixel((1, 2), (255, 255, 255, 255))
        apply_logo(jpeg, self.logo, self.output, 1, 2)
        with Image.open(self.output) as result:
            self.assertEqual(result.size, (2, 4))
            self.assertEqual(result.tobytes(), expected.tobytes())

    def test_invalid_placements_and_invisible_logo_leave_no_output(self):
        Image.new('RGBA', (12, 12), 'white').save(self.base)
        Image.new('RGBA', (4, 2), 'black').save(self.logo)
        for x, y, width in [(-1, 1, 4), (1, 11, 4), (5, 1, 8), (1, 1, 0)]:
            with self.subTest(x=x, y=y, width=width), self.assertRaises(ValueError):
                apply_logo(self.base, self.logo, self.output, x, y, width)
        Image.new('RGBA', (4, 2)).save(self.logo)
        with self.assertRaises(ValueError):
            apply_logo(self.base, self.logo, self.output, 0, 0)
        self.assertFalse(self.output.exists())
