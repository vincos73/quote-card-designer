"""Check the shared card structure before a gallery is published."""
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
import sys


class GalleryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.cards = {}
        self.images = []
        self.card_families = {}
        self.family_options = {}
        self.family_counts = {}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()
        if tag == "article" and "style" in classes:
            identifier = attributes.get("id")
            if not self.stack or self.stack[-1][1].get("id") != "catalogo":
                raise ValueError(f"Scheda fuori dalla griglia del catalogo: {identifier}")
            if not identifier or identifier in self.cards:
                raise ValueError(f"ID scheda assente o duplicato: {identifier}")
            self.cards[identifier] = 0
            self.card_families[identifier] = attributes.get("data-family")
        if tag == "button" and "family-option" in classes:
            family = attributes.get("data-family-filter")
            if family is None or family in self.family_options:
                raise ValueError(f"Filtro categoria assente o duplicato: {family}")
            self.family_options[family] = attributes
        if tag == "button" and "family-tag" in classes:
            card = next((item[1].get("id") for item in reversed(self.stack)
                         if item[0] == "article"), None)
            if card is None or attributes.get("data-family-filter") != self.card_families[card]:
                raise ValueError(f"Etichetta categoria non coerente: {card}")
        if tag == "img" and any("preview" in item[1].get("class", "").split() for item in self.stack):
            card = next((item[1]["id"] for item in reversed(self.stack)
                         if item[0] == "article" and "style" in item[1].get("class", "").split()), None)
            if card is None:
                raise ValueError("Anteprima fuori da una scheda")
            self.cards[card] += 1
            self.images.append(attributes.get("src", ""))
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append((tag, attributes))

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1][0] != tag:
            raise ValueError(f"Chiusura HTML non coerente: {tag}")
        self.stack.pop()

    def handle_data(self, data):
        if not data.strip() or not self.stack or "family-number" not in self.stack[-1][1].get("class", "").split():
            return
        option = next((item[1] for item in reversed(self.stack)
                       if "family-option" in item[1].get("class", "").split()), None)
        if option is None or not data.strip().isdigit():
            raise ValueError("Conteggio categoria non valido")
        self.family_counts[option["data-family-filter"]] = int(data.strip())


def validate_gallery(page, directory):
    parser = GalleryParser()
    parser.feed(page)
    parser.close()
    if parser.stack or not parser.cards:
        raise ValueError("Galleria vuota o HTML incompleto")
    actual_counts = Counter(parser.card_families.values())
    if not actual_counts.keys() <= (parser.family_options.keys() - {""}):
        raise ValueError("Una scheda usa una categoria senza filtro")
    for family in parser.family_options:
        expected = len(parser.cards) if family == "" else actual_counts[family]
        if parser.family_counts.get(family) != expected:
            raise ValueError(f"Conteggio categoria errato: {family}")
    for source in parser.images:
        if not source or not (Path(directory) / source).is_file():
            raise ValueError(f"Asset di anteprima mancante: {source}")
    return parser


if __name__ == "__main__":
    path = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent / "dist/index.html")
    result = validate_gallery(path.read_text(), path.parent)
    print(f"Galleria verificata: {len(result.cards)} schede nella griglia, {len(result.images)} anteprime, {len(result.family_options)-1} categorie con conteggi coerenti.")
