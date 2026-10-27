"""Build the public V1 catalog from its versioned sources and approved previews."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent
DEFAULT_OUT = ROOT.parents[1] / 'build/catalogo-v1-dist'


def build(output: Path) -> None:
    src = ROOT / 'src'
    data = json.loads((src / 'style-data.json').read_text())
    manifest = json.loads((ROOT / 'asset-manifest.json').read_text())
    expected = {asset['style_id']: asset for asset in manifest['assets']}
    ids = [style['id'] for style in data['items']]
    families = {family['id'] for family in data['families']}
    if len(ids) != len(set(ids)) or set(ids) != set(expected):
        raise ValueError('Catalog and image manifest do not match')
    if any(style['family'] not in families for style in data['items']):
        raise ValueError('Unknown category')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'assets').mkdir(exist_ok=True)
    for style in data['items']:
        relative = Path(style['asset'])
        if relative.is_absolute() or '..' in relative.parts or relative.parts[0] != 'assets':
            raise ValueError('Invalid asset path')
        source = ROOT / relative
        if hashlib.sha256(source.read_bytes()).hexdigest() != expected[style['id']]['asset_sha256']:
            raise ValueError(f"Image checksum mismatch: {style['id']}")
        shutil.copy2(source, output / relative)
    encoded = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    page = (src / 'index.html').read_text().replace('__CATALOG_VERSION__', data['version']).replace('__STYLE_COUNT__', str(len(ids))).replace('__STYLE_DATA__', encoded)
    (output / 'index.html').write_text(page)
    for name in ('catalog.css', 'catalog.js'):
        shutil.copy2(src / name, output / 'assets' / name)
    print(f'{output}: {len(ids)} stili, {len(families)} categorie')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUT)
    build(parser.parse_args().output)
