"""Odśwież translations/en-pl-review.json: EN i kontekst z gry, PL z dotychczasowego pliku.

Kolejność jak w arkuszach gry (UI, postacie, miejsca, przedmioty, zadania, dialogi).
Wpisy bez tłumaczenia mają pusty `polish`, żeby było widać zakres. W `context` arkusz,
mówiący (z klucza dialogu) i limit długości z arkusza limitów gry.

    .venv\\Scripts\\python.exe games\\laika-aged-through-blood\\tools\\review.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import polish_by_key, write_entries  # noqa: E402


def main():
    source = json.loads((ROOT / 'work/source/en.json').read_text(encoding='utf-8'))
    terms = polish_by_key(ROOT)
    rows = []
    for row in source:
        if not row['text']:
            continue
        context = [row['sheet']]
        if 'speaker' in row:
            context.append('mówi ' + row['speaker'])
        if 'limit' in row:
            context.append(f'limit {row["limit"]} znaków')
        rows.append({'key': row['key'], 'english': row['text'], 'polish': terms.get(row['key'], ''),
                     'context': ', '.join(context)})
    write_entries(ROOT, rows)
    print(json.dumps({'rows': len(rows), 'translated': sum(1 for r in rows if r['polish'])}))


if __name__ == '__main__':
    main()
