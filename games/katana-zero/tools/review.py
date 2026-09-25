"""Plik do korekty i kontrola znaczników.

    .venv\\Scripts\\python.exe games\\katana-zero\\tools\\review.py

Odświeża translations/en-pl-review.json (klucz, angielski, polski z samego pliku — decyzja
0021 —, rosyjski jako kontekst slotu, który zajmujemy) i sprawdza, czy tłumaczenie niesie te same znaczniki co oryginał:
kolory i efekty w nawiasach kwadratowych oraz łamania linii. Gwiazdki to pauzy
w wypowiedzi — ich liczbę tylko zgłaszamy, bo polski szyk bywa inny.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import polish_by_key, write_entries  # noqa: E402

TAG = re.compile(r'\[[^\]]*\]')


def main() -> int:
    texts = {t['key']: t for t in json.loads((ROOT / 'work' / 'texts.json').read_text(encoding='utf-8'))}
    pl = polish_by_key(ROOT)
    errors, notes = [], []
    rows = []
    for key, t in texts.items():
        if key not in pl:
            continue
        en, tr = t['en'], pl[key]
        if TAG.findall(en) != TAG.findall(tr):
            errors.append(f'{key}: znaczniki {TAG.findall(en)} -> {TAG.findall(tr)}')
        if en.count('\n') != tr.count('\n'):
            errors.append(f'{key}: łamania linii {en.count(chr(10))} -> {tr.count(chr(10))}')
        if en.replace('*', '').strip() and TAG.sub('', en).count('*') != TAG.sub('', tr).count('*'):
            notes.append(f'{key}: pauzy * {TAG.sub("", en).count("*")} -> {TAG.sub("", tr).count("*")}')
        rows.append({'key': key, 'english': en, 'polish': tr, 'context': t['ru']})
    write_entries(ROOT, rows)
    for n in notes:
        print('uwaga:', n)
    for e in errors:
        print('BŁĄD:', e)
    print(f'{len(rows)} wpisów w pliku korekty, {len(errors)} błędów, {len(notes)} uwag')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
