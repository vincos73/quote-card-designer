#!/usr/bin/env python3
"""Read the YAML, verify real font files, then render with native CoreText."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / 'card.yaml'

def main():
    config = yaml.safe_load(CONFIG.read_text())
    source_path = (ROOT / config['extends']).resolve()
    source = yaml.safe_load(source_path.read_text())
    card = source['test_card']
    assert ' '.join(card['quote_lines']) == card['quote']
    assert ' '.join(card['emphasis_lines']) == card['emphasis']
    assert card['emphasis'] in card['quote']
    assert card['author'] is None and card['series_number'] is None
    assert not card['dots']['enabled']
    assert len(card['header']) == 4
    for font in config['fonts'].values():
        path = ROOT / font['local_file']
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != font['sha256']:
            raise ValueError(f"Il font {font['family']} non corrisponde al file fissato nel YAML.")
        font['absolute_file'] = str(path)
    config['card'] = card
    config['comparison']['absolute_image'] = str((ROOT / config['comparison']['generated_image']).resolve())
    build = ROOT / '.build'
    build.mkdir(exist_ok=True)
    job = build / 'layout.json'
    job.write_text(json.dumps(config, ensure_ascii=False, indent=2))
    subprocess.run([
        'swift', '-module-cache-path', '/private/tmp/quote-card-grottesco-swift-cache',
        str(ROOT / 'render.swift'), str(job), str(ROOT)
    ], check=True)

if __name__ == '__main__':
    main()
