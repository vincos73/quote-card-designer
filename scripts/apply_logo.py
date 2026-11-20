"""Overlay the supplied logo on a finished card and export a new lossless PNG."""
import argparse
from io import BytesIO
import os
from pathlib import Path
import tempfile

from PIL import Image, ImageCms, ImageOps, PngImagePlugin

SRGB_CHROMATICITY = (0.3127, 0.329, 0.64, 0.33, 0.30, 0.60, 0.15, 0.06)


def read_image(path, formats):
    with path.open('rb') as stream:
        header = stream.read(29)
        stream.seek(0)
        with Image.open(stream, formats=formats) as source:
            if getattr(source, 'n_frames', 1) != 1:
                raise ValueError(f'Use a single still image: {path}')
            if source.format == 'PNG' and header[24] > 8:
                raise ValueError(f'Use a color-managed editor for 16-bit PNG: {path}')
            if source.mode not in {'RGB', 'RGBA', 'P', 'L', 'LA', '1'}:
                raise ValueError(f'Unsupported color mode {source.mode}: {path}')
            if source.mode in {'1', 'L', 'LA'} and source.info.get('icc_profile'):
                raise ValueError(f'Use an RGB export for an ICC-tagged grayscale input: {path}')
            # A bare gamma or primaries chunk can describe a non-sRGB space.
            # Never silently treat a custom transfer curve or gamut as sRGB.
            source.load()
            if not source.info.get('icc_profile') and 'srgb' not in source.info:
                gamma = source.info.get('gamma', 0.45455)
                primaries = source.info.get('chromaticity', SRGB_CHROMATICITY)
                if abs(gamma - 0.45455) > 0.0001 or primaries != SRGB_CHROMATICITY:
                    raise ValueError(f'Custom PNG color space requires an ICC profile or sRGB export: {path}')
            return ImageOps.exif_transpose(source).convert('RGBA'), source.info.copy()


def rgb_profile(raw):
    return ImageCms.ImageCmsProfile(BytesIO(raw)) if raw else ImageCms.createProfile('sRGB')


def apply_logo(base_path, logo_path, output, x, y, width=None):
    if output.suffix.lower() != '.png':
        raise ValueError('The output must be a new .png file')
    base, base_info = read_image(base_path, ('PNG', 'JPEG'))
    logo, logo_info = read_image(logo_path, ('PNG',))
    width = logo.width if width is None else width
    height = max(1, round(logo.height * width / logo.width))
    if width <= 0 or min(x, y) < 0 or x + width > base.width or y + height > base.height:
        raise ValueError('Place the entire logo within the card at a positive width')

    source_icc, target_icc = logo_info.get('icc_profile'), base_info.get('icc_profile')
    if source_icc != target_icc:
        colors = ImageCms.profileToProfile(logo.convert('RGB'), rgb_profile(source_icc),
                                           rgb_profile(target_icc), outputMode='RGB')
        colors.putalpha(logo.getchannel('A'))
        logo = colors
    if logo.size != (width, height):
        logo = logo.resize((width, height), Image.Resampling.LANCZOS)
    if logo.getchannel('A').getbbox() is None:
        raise ValueError('The resized logo is fully transparent')
    base.alpha_composite(logo, (x, y))

    # Only the base defines the output color space and physical dimensions.
    # Transparency is already applied in RGBA, including any PNG tRNS chunk.
    base.info.clear()
    pnginfo = PngImagePlugin.PngInfo()
    if not target_icc and any(k in base_info for k in ('srgb', 'gamma', 'chromaticity')):
        pnginfo.add(b'sRGB', bytes([base_info.get('srgb', 0)]))
    options = {'icc_profile': target_icc, 'pnginfo': pnginfo}
    if 'dpi' in base_info:
        options['dpi'] = base_info['dpi']
    with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.png', delete=False) as temp:
        staged = Path(temp.name)
    try:
        base.save(staged, format='PNG', **options)
        # Linking a completed file creates the destination atomically, excluding
        # any pre-existing original or concurrent writer.
        os.link(staged, output)
    finally:
        staged.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base', type=Path, help='Approved card, PNG or JPEG')
    parser.add_argument('logo', type=Path, help='Original PNG logo')
    parser.add_argument('output', type=Path, help='New lossless PNG')
    parser.add_argument('--x', required=True, type=int, help='Left edge of the logo in pixels')
    parser.add_argument('--y', required=True, type=int, help='Top edge of the logo in pixels')
    parser.add_argument('--width', type=int, help='Logo width in pixels, default original width')
    args = parser.parse_args()
    try:
        apply_logo(args.base, args.logo, args.output, args.x, args.y, args.width)
    except (OSError, ValueError, ImageCms.PyCMSError) as error:
        parser.exit(1, f'{parser.prog}: {error}\n')


if __name__ == '__main__':
    main()
