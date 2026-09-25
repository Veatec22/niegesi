r"""Zapisuje translations/en-pl-review.json: klucz, angielski, polski i kontekst z pliku gry.

Użycie: .venv\Scripts\python.exe games\hyper-light-drifter\tools\review.py --game "C:\Games\Hyper Light Drifter"

Kontekst to włoski tekst, który polski zastępuje, i komentarz autorów o limicie znaków.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from hld import ROOT, SLOT, load_texts, value


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args()
    pl = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    rows = []
    for lines, items in load_texts(args.game).values():
        for e in items:
            row = {'key': e.key, 'english': value(lines, e, 'ENG'), 'polish': pl.get(e.key, '')}
            context = [f'zastępuje {SLOT}: {value(lines, e, SLOT)}']
            if e.note:
                context.append(f'uwaga autorów: {e.note}')
            row['context'] = '; '.join(context)
            rows.append(row)
    out = ROOT / 'translations/en-pl-review.json'
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(rows)} wpisów -> {out}')


if __name__ == '__main__':
    main()
