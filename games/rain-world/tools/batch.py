"""Partie do tłumaczenia: wydziel nieprzetłumaczone wpisy i scal gotowe z en-pl-review.json.

    batch.py make --kind strings --size 200     # work/batches/NNN.json: klucz -> en, ru, kontekst
    batch.py make --kind dialogue --size 120    # całe pliki rozmów po kolei, aż do rozmiaru
    batch.py show 001                           # zwarty podgląd: numer, [klucz], en, ru, kontekst
    batch.py merge work/batches/NNN.pl.json     # klucz -> polski; scala do translations/en-pl-review.json
    batch.py merge work/batches/NNN.pl.tsv      # numer<TAB>polski (numeracja z show)
    batch.py status

Plik tłumaczenia trzyma kolejność work/en.json (dodatkowe wpisy spolszczenia na początku).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'work'
BATCHES = WORK / 'batches'
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))
sys.path.insert(0, str(ROOT / 'tools'))

from review import row_for  # noqa: E402
from translations import load_entries, write_entries  # noqa: E402

COMMENTARY = re.compile(r'^dlg:[a-z]{2}_[^#]*-(white|artificer|inv|saint|rivulet|spear|gourmand)\.txt#')


def load():
    english = json.loads((WORK / 'en.json').read_text(encoding='utf-8'))
    ref = json.loads((WORK / 'ref-rus.json').read_text(encoding='utf-8'))
    polish = {e['key']: e['polish'] for e in load_entries(ROOT)}
    return english, ref, polish


def kind_of(key: str) -> str:
    if key.startswith('str:'):
        return 'strings'
    return 'commentary' if COMMENTARY.match(key) else 'dialogue'


def make(kind: str, size: int, source: str | None) -> Path:
    english, ref, polish = load()
    todo = [k for k in english if k not in polish and kind_of(k) == kind
            and (source is None or english[k]['source'] == source)]
    if kind == 'strings':
        # Razem to, co stoi w tej samej klasie gry — menu obok menu, stworzenia obok stworzeń.
        order = {k: i for i, k in enumerate(english)}
        todo.sort(key=lambda k: ((english[k].get('context') or '~').split(', ')[0], order[k]))
        chosen = todo[:size]
    else:
        # Całe pliki: rozmowa tłumaczona w kawałkach gubi ton i płeć mówiącego.
        chosen, current = [], None
        for k in todo:
            name = k.split('#')[0]
            if name != current and len(chosen) >= size:
                break
            current = name
            chosen.append(k)
    BATCHES.mkdir(parents=True, exist_ok=True)
    number = len(list(BATCHES.glob('[0-9][0-9][0-9].json'))) + 1
    out = BATCHES / f'{number:03}.json'
    rows = {}
    for k in chosen:
        row = {'en': english[k]['english']}
        ru = ref.get(k) or ref.get(k.lower())
        if ru and ru != english[k]['english']:
            row['ru'] = ru
        if english[k].get('context'):
            row['ctx'] = ', '.join(english[k]['context'].split(', ')[:3])
        if english[k]['source'] != 'base':
            row['src'] = english[k]['source']
        rows[k] = row
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{out.name}: {len(rows)} wpisów, zostaje {len(todo) - len(rows)} ({kind})')
    return out


def show(number: str) -> None:
    rows = json.loads((BATCHES / f'{number}.json').read_text(encoding='utf-8'))
    for i, (key, row) in enumerate(rows.items(), 1):
        name = key.split(':', 1)[1]
        label = '' if name == row['en'] else f'[{name}] '
        # Rosyjski rozstrzyga krótkie, dwuznaczne etykiety (czasownik czy rzeczownik) i płeć
        # w rozmowach; przy długich zdaniach interfejsu tylko zajmuje miejsce.
        useful = 'ru' in row and (key.startswith('dlg:') or len(row['en'].split()) <= 4)
        extra = f" || {row['ru']}" if useful else ''
        where = f"  <{row.get('src', '')}{' ' if row.get('src') and row.get('ctx') else ''}{row.get('ctx', '')}>"             if row.get('ctx') or row.get('src') else ''
        print(f'{i}	{label}{row["en"]}{extra}{where}')


def read_new(path: Path) -> dict[str, str]:
    if path.suffix == '.json':
        return json.loads(path.read_text(encoding='utf-8'))
    # NNN.pl.tsv: numer<TAB>tekst, numeracja jak w `show NNN`.
    rows = list(json.loads((BATCHES / (path.name.split('.')[0] + '.json')).read_text(encoding='utf-8')))
    new = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        number, text = line.split('	', 1)
        new[rows[int(number) - 1]] = text
    missing = len(rows) - len(new)
    if missing:
        print(f'Uwaga: {missing} wpisów partii bez tłumaczenia')
    return new


def merge(path: Path) -> None:
    english, _, polish = load()
    new = read_new(path)
    unknown = [k for k in new if k not in english and k not in polish]
    if unknown:
        raise SystemExit(f'Klucze spoza gry: {unknown[:5]}')
    empty = [k for k, v in new.items() if not isinstance(v, str) or not v.strip()]
    if empty:
        raise SystemExit(f'Puste tłumaczenia: {empty[:5]}')
    polish.update(new)
    extra = {k: v for k, v in polish.items() if k not in english}
    ordered = {**extra, **{k: polish[k] for k in english if k in polish}}
    existing = {e['key']: e for e in load_entries(ROOT)}
    rows = []
    for key, text in ordered.items():
        row = existing.get(key) or row_for(key, text, english)
        row['polish'] = text
        rows.append(row)
    write_entries(ROOT, rows)
    print(f'Scalono {len(new)}; w pliku tłumaczenia {len(rows)} wpisów')


def status() -> None:
    english, _, polish = load()
    for kind in ('strings', 'dialogue', 'commentary'):
        keys = [k for k in english if kind_of(k) == kind]
        done = sum(1 for k in keys if k in polish)
        print(f'{kind:11} {done:5}/{len(keys)}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('--kind', choices=['strings', 'dialogue', 'commentary'], required=True)
    m.add_argument('--size', type=int, default=200)
    m.add_argument('--source')
    v = sub.add_parser('show')
    v.add_argument('number')
    g = sub.add_parser('merge')
    g.add_argument('path', type=Path)
    sub.add_parser('status')
    args = parser.parse_args()
    if args.cmd == 'make':
        make(args.kind, args.size, args.source)
    elif args.cmd == 'show':
        show(args.number)
    elif args.cmd == 'merge':
        merge(args.path)
    else:
        status()
    return 0


if __name__ == '__main__':
    sys.exit(main())
