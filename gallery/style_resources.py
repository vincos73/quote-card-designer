"""Resolve a style's optional composition library for export and packaging."""
from copy import deepcopy
from pathlib import Path
import re

import yaml


def load_style_document(profile_path: Path) -> tuple[dict, list[Path]]:
    """Return a self-contained document plus local resources to package.

    Source profiles can link one library relative to their own directory.
    Catalogue exports embed that library under a separate top-level key.
    Existing profiles without a library pass through unchanged.
    """
    document = yaml.safe_load(profile_path.read_text())
    if not isinstance(document, dict) or not isinstance(document.get('Design Style'), dict):
        raise ValueError(f'Invalid style profile: {profile_path}')
    reference = document.get('Composition Library')
    if reference is None:
        return document, []

    resources = []
    if isinstance(reference, str):
        relative = Path(reference)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError(f'Composition library must be inside the style directory: {profile_path}')
        library_path = (profile_path.parent / relative).resolve()
        if not library_path.is_relative_to(profile_path.parent.resolve()):
            raise ValueError(f'Composition library escapes the style directory: {profile_path}')
        companion = yaml.safe_load(library_path.read_text())
        library = companion.get('Composition Library') if isinstance(companion, dict) else None
        resources.append(library_path)
    elif isinstance(reference, dict):
        library = reference
    else:
        raise ValueError(f'Invalid composition library declaration: {profile_path}')

    name = document['Design Style'].get('Name')
    if not isinstance(library, dict) or library.get('Style Name') != name:
        raise ValueError(f'Composition library does not match style {name!r}: {profile_path}')
    if not isinstance(library.get('Selection'), dict) or not library['Selection']:
        raise ValueError(f'Missing composition selection guidance: {profile_path}')
    families = library.get('Families')
    if not isinstance(families, list) or not families:
        raise ValueError(f'Missing composition families: {profile_path}')
    identifiers = set()
    required = ('Name', 'Use When', 'Structure', 'Text Adaptation', 'Format Adaptation')
    for family in families:
        identifier = family.get('id') if isinstance(family, dict) else None
        if not isinstance(identifier, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', identifier):
            raise ValueError(f'Invalid composition family ID in {profile_path}')
        if identifier in identifiers:
            raise ValueError(f'Duplicate composition family {identifier!r}: {profile_path}')
        identifiers.add(identifier)
        for key in required:
            if not isinstance(family.get(key), str) or not family[key].strip():
                raise ValueError(f'Missing {key!r} in composition {identifier!r}: {profile_path}')

    document = deepcopy(document)
    document['Composition Library'] = library
    return document, resources
