r"""Odświeża translations/en-pl-review.json: klucz, angielski i kontekst z pliku gry, PL z samego pliku.

Użycie: .venv\Scripts\python.exe games\hyper-light-drifter\tools\review.py --game "C:\Games\Hyper Light Drifter"

Kontekst to włoski tekst, który polski zastępuje, i komentarz autorów o limicie znaków.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from hld import ROOT, SLOT, load_texts, value

sys.path.insert(0, str(ROOT.parents[1] / 'tools'))
from translations import polish_by_key, write_entries  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args()
    pl = polish_by_key(ROOT)
    rows = []
    for lines, items in load_texts(args.game).values():
        for e in items:
            row = {'key': e.key, 'english': value(lines, e, 'ENG'), 'polish': pl.get(e.key, '')}
            context = [f'zastępuje {SLOT}: {value(lines, e, SLOT)}']
            if e.note:
                context.append(f'uwaga autorów: {e.note}')
            row['context'] = '; '.join(context)
            rows.append(row)
    write_entries(ROOT, rows)
    print(f'{len(rows)} wpisów -> translations/en-pl-review.json')


if __name__ == '__main__':
    main()
