"""Apply the Swiss index layout to an existing complete development gallery."""
from pathlib import Path
import argparse
import re

CSS = Path(__file__).with_name('swiss-gallery.css')


def to_swiss(page: str) -> str:
    if 'class="gallery-layout"' in page:
        raise ValueError('Swiss layout is already applied')
    match = re.search(r'(<main>)(.*?)(<section class="gallery" id="catalogo".*?</section>)(.*?</main>)', page, re.S)
    if not match:
        raise ValueError('Gallery structure does not match expected markup')
    before, cards, after = match.group(2), match.group(3), match.group(4)
    def extract(pattern: str) -> str:
        nonlocal before
        found = re.search(pattern, before, re.S)
        if not found:
            raise ValueError(f'Missing gallery component: {pattern}')
        value = found.group(0)
        before = before[:found.start()] + before[found.end():]
        return value
    family = extract(r'<fieldset class="family-filters">.*?</fieldset>')
    release = extract(r'<fieldset class="release-filters">.*?</fieldset>')
    result = page[:match.start()] + '<div class="gallery-layout"><aside class="gallery-sidebar" aria-label="Filtri">' + family + release + '</aside><main class="gallery-main">' + before + cards + after + '</div>' + page[match.end():]
    return result.replace('</style>', '\n' + CSS.read_text() + '\n</style>', 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.write_text(to_swiss(args.input.read_text()))
