"""Polskie teksty Dread Templar z translations/en-pl-review.json (decyzje 0013, 0021).

Gra trzyma teksty jako kategoria → klucz → pola (`text`, `name`). Plik tłumaczenia ma
jeden wpis na pole tekstowe: `namespace` = kategoria, `key` = `<klucz>/<pole>`.
Pola liczbowe (identyfikator mówiącego) nie są tekstem do tłumaczenia; w wersji
polskiej zostają takie jak w angielskiej, więc build bierze je z gry.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries, untranslated  # noqa: E402

import game  # noqa: E402


def review_rows(english: dict, polish: dict[tuple[str, str], str]) -> list[dict]:
    """Wpisy pliku tłumaczenia w kolejności gry; `polish` jak z `translated()`."""
    rows = []
    for category, key, entry in game.entries(english):
        for field, text in entry.items():
            if isinstance(text, str):
                ref = (category, f'{key}/{field}')
                rows.append({'namespace': category, 'key': ref[1], 'english': text, 'polish': polish.get(ref, '')})
    return rows


def translated() -> dict[tuple[str, str], str]:
    return {(e['namespace'], e['key']): e['polish'] for e in load_entries(ROOT) if not untranslated(e)}


def polish_tree(english: dict | None = None) -> dict:
    """Kategoria → klucz → pola po polsku, w kolejności gry.

    Z `english` (blok `eng` z gry) drzewo ma też pola liczbowe i wszystkie kategorie —
    tak, jak zapisuje je build podmieniający resources.assets. Bez niego: same teksty.
    """
    polish = translated()
    if english is None:
        tree: dict = {}
        for (category, ref), text in polish.items():
            key, field = ref.rsplit('/', 1)
            tree.setdefault(category, {}).setdefault(key, {})[field] = text
        return tree
    tree = {category: {} for category in game.CATEGORIES}
    for category, key, entry in game.entries(english):
        fields = {}
        for field, value in entry.items():
            if not isinstance(value, str):
                fields[field] = value
            elif (category, f'{key}/{field}') in polish:
                fields[field] = polish[(category, f'{key}/{field}')]
        if fields:
            tree[category][key] = fields
    return tree
