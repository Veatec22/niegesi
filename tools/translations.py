"""Jedyny plik tłumaczenia gry: translations/en-pl-review.json (decyzje 0013 i 0021).

Buildy czytają polskie teksty stąd, a nie z własnych kopii. Plik jest listą wpisów
`{key, namespace?, english, polish, context?, note?, max_length?}`; identyfikatorem
wpisu jest para (namespace, key). Tekstów nie przycinamy ani nie normalizujemy.

    from translations import polish_by_key
    terms = polish_by_key(ROOT)          # {key: polski tekst}, kolejność pliku

Gra z niepustym namespace buduje własne identyfikatory z `load_entries(ROOT)`.
Narzędzia, które zmieniają teksty (warsztat tłumacza, korekty), zapisują przez
`write_entries` albo `update_polish` — w stylu istniejącego pliku, żeby diff pokazywał
tylko zmienione wpisy.
"""

from __future__ import annotations

import json
from pathlib import Path

REVIEW_FILE = Path('translations') / 'en-pl-review.json'
STYLES = [(2, True), (1, True), (4, True), (2, False), (1, False), (4, False)]


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


def untranslated(entry: dict) -> bool:
    """Pusty PL przy niepustym EN: wpis jeszcze bez tłumaczenia, w grze zostaje oryginał."""
    return entry['polish'] == '' and entry['english'].strip() != ''


def polish_by_key(game_root: Path, keep_empty: bool = False) -> dict[str, str]:
    """Mapa klucz → PL dla gier bez namespace, bez wpisów nieprzetłumaczonych.

    `keep_empty=True` dla gier, w których pusty PL jest celowy (np. zbędny sufiks).
    """
    entries = load_entries(game_root)
    spaced = [e['key'] for e in entries if e.get('namespace')]
    if spaced:
        raise SystemExit(f'{review_path(game_root)}: wpisy z namespace ({spaced[0]}…) — użyj load_entries.')
    return {e['key']: e['polish'] for e in entries if keep_empty or not untranslated(e)}


def dump(entries: list[dict], indent: int = 2, newline: bool = True) -> str:
    return json.dumps(entries, ensure_ascii=False, indent=indent) + ('\n' if newline else '')


def file_style(text: str) -> tuple[int, bool] | None:
    """Wcięcie i końcowa nowa linia, które odtwarzają plik bajt w bajt; None, gdy żadne."""
    data = json.loads(text)
    for indent, newline in STYLES:
        if dump(data, indent, newline) == text:
            return indent, newline
    return None


def write_entries(game_root: Path, entries: list[dict]) -> None:
    """Zapis w stylu obecnego pliku (nowy plik: wcięcie 2, nowa linia na końcu)."""
    path = review_path(game_root)
    style = file_style(path.read_text(encoding='utf-8')) if path.exists() else None
    path.write_text(dump(entries, *(style or (2, True))), encoding='utf-8', newline='\n')
    load_entries(game_root)


def update_polish(game_root: Path, polish: dict[str, str]) -> int:
    """Ustaw PL istniejących wpisów bez namespace; nieznany klucz to błąd. Zwraca liczbę zmian."""
    entries = load_entries(game_root)
    index = {e['key']: e for e in entries if not e.get('namespace')}
    unknown = [key for key in polish if key not in index]
    if unknown:
        raise SystemExit(f'{review_path(game_root)}: brak wpisów {unknown[:5]} — nowy wpis wymaga EN z gry.')
    changed = 0
    for key, text in polish.items():
        if index[key]['polish'] != text:
            index[key]['polish'] = text
            changed += 1
    if changed:
        write_entries(game_root, entries)
    return changed
