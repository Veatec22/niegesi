"""Polskie teksty Heat Signature z translations/en-pl-review.json (decyzje 0013, 0021).

Dwa rodzaje wpisów w jednym pliku:

- tekst gry: `key` = angielski literał (EXE, dialog albo szablon z {0}), `polish`;
- gramatyka nazw przedmiotów, które gra składa z [określeń] i rzeczownika. Po polsku
  rzeczownik idzie pierwszy, przymiotniki za nim, zgodne w rodzaju (m/f/n), a określenia
  z grupy „tail” na końcu:
  `item-noun:<EN>` — rzeczownik, pole `gender` = m / f / n;
  `item-modifier:<EN>` — trzy formy przymiotnika „m / ż / n”;
  `item-tail:<EN>` — określenie końcowe bez odmiany.

Nowe partie tłumaczenia dopisuje `assemble.py` przez `merge`.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries, untranslated, write_entries  # noqa: E402

ITEM = 'item-'
GENDERS = {'m', 'f', 'n'}


def plain() -> dict[str, str]:
    """EN → PL tekstów gry w kolejności pliku, bez nieprzetłumaczonych i bez gramatyki przedmiotów."""
    result = {}
    for e in load_entries(ROOT):
        if e['key'].startswith(ITEM) or untranslated(e):
            continue
        if e['key'] != e['english']:
            raise SystemExit(f'{e["key"]!r}: klucz tekstu gry musi być jego angielskim brzmieniem.')
        result[e['key']] = e['polish']
    return result


def items() -> dict:
    """Gramatyka przedmiotów: nouns {EN: [rzeczownik, rodzaj]}, modifiers {EN: [m, ż, n]}, tails {EN: tekst}."""
    out = {'nouns': {}, 'modifiers': {}, 'tails': {}}
    for e in load_entries(ROOT):
        kind, _, english = e['key'].partition(':')
        if kind == 'item-noun':
            if e.get('gender') not in GENDERS:
                raise SystemExit(f'{e["key"]}: pole „gender” musi być jednym z {sorted(GENDERS)}.')
            out['nouns'][english] = [e['polish'], e['gender']]
        elif kind == 'item-modifier':
            forms = e['polish'].split(' / ')
            if len(forms) != 3 or not all(f.strip() == f and f for f in forms):
                raise SystemExit(f'{e["key"]}: PL musi mieć trzy formy „m / ż / n”, jest {e["polish"]!r}.')
            out['modifiers'][english] = forms
        elif kind == 'item-tail':
            out['tails'][english] = e['polish']
        elif e['key'].startswith(ITEM):
            raise SystemExit(f'{e["key"]}: nieznany rodzaj wpisu przedmiotu.')
    return out


def merge(batch: dict[str, str], context: dict[str, str], overwrite: bool = True) -> tuple[int, int]:
    """Dopisz teksty gry EN → PL: nowe przed gramatyką przedmiotów, istniejące zmień
    (albo zostaw, gdy `overwrite=False`). Zwraca (zmienione, dodane)."""
    entries = load_entries(ROOT)
    index = {e['key']: e for e in entries}
    changed = added = 0
    fresh = []
    for en, pl in batch.items():
        if en.startswith(ITEM):
            raise SystemExit(f'{en!r}: gramatykę przedmiotów poprawia się we wpisach item-*.')
        if en in index:
            if overwrite and index[en]['polish'] != pl:
                index[en]['polish'] = pl
                changed += 1
        else:
            fresh.append({'key': en, 'english': en, 'polish': pl, 'context': context.get(en, '')})
            added += 1
    first_item = next((i for i, e in enumerate(entries) if e['key'].startswith(ITEM)), len(entries))
    entries[first_item:first_item] = fresh
    if changed or added:
        write_entries(ROOT, entries)
    return changed, added
