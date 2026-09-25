"""Jedyny plik tłumaczenia gry: translations/en-pl-review.json (decyzje 0013 i 0021).

Buildy czytają polskie teksty stąd, a nie z własnych kopii. Plik jest listą wpisów
`{key, namespace?, english, polish, context?, note?, max_length?}`; identyfikatorem
wpisu jest para (namespace, key). Tekstów nie przycinamy ani nie normalizujemy.

    from translations import polish_by_key
    terms = polish_by_key(ROOT)          # {key: polski tekst}, kolejność pliku

Gra z niepustym namespace buduje własne identyfikatory z `load_entries(ROOT)`.
"""

from __future__ import annotations

import json
from pathlib import Path

REVIEW_FILE = Path('translations') / 'en-pl-review.json'


def review_path(game_root: Path) -> Path:
    return Path(game_root) / REVIEW_FILE


def load_entries(game_root: Path) -> list[dict]:
    """Wpisy w kolejności pliku; zatrzymuje się na błędzie kształtu, nie zgaduje."""
    path = review_path(game_root)
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        raise SystemExit(f'{path}: plik musi być listą wpisów.')
    seen: set[tuple[str, str]] = set()
    for index, entry in enumerate(data):
        where = f'{path}: wpis {index}'
        if not isinstance(entry, dict):
            raise SystemExit(f'{where}: nie jest obiektem.')
        for field in ('key', 'english', 'polish'):
            if not isinstance(entry.get(field), str):
                raise SystemExit(f'{where}: brak tekstowego pola „{field}”.')
        namespace = entry.get('namespace', '')
        if not isinstance(namespace, str):
            raise SystemExit(f'{where}: „namespace” musi być tekstem.')
        ident = (namespace, entry['key'])
        if ident in seen:
            raise SystemExit(f'{where}: zdublowany wpis {namespace + "/" if namespace else ""}{entry["key"]}.')
        seen.add(ident)
    return data


def polish_by_key(game_root: Path) -> dict[str, str]:
    """Mapa klucz → PL dla gier bez namespace."""
    entries = load_entries(game_root)
    spaced = [e['key'] for e in entries if e.get('namespace')]
    if spaced:
        raise SystemExit(f'{review_path(game_root)}: wpisy z namespace ({spaced[0]}…) — użyj load_entries.')
    return {e['key']: e['polish'] for e in entries}
