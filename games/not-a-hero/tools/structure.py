"""Zapisz translations/structure.yaml: grupy i rozmowy NOT A HERO dla pracowni korekty.

    .venv\\Scripts\\python.exe games\\not-a-hero\\tools\\structure.py

Klucz tekstu z .ini to `Src/<plik>|<sekcja>|<wiersz>`. Plik tłumaczenia trzyma wiersze
w kolejności tekstowej (|17|10 przed |17|2), więc rozmowy układają je po numerze:
każda liczbowa sekcja talk.ini (odprawa) i ENDS.ini (podsumowanie poziomu) to monolog
BunnyLorda. Sekcje z nazwą (ADJECTIVE, OBJECTS, INSULTS…) to listy słów podstawianych
do zdań za $ZMIENNE$ — osobna grupa, nie rozmowy. Uruchom po zmianie kluczy.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries  # noqa: E402

HEADER = '''# Grupy i rozmowy NOT A HERO dla pracowni korekty — plik generuje tools/structure.py,
# nie edytuj ręcznie. Format: docs/specs/editorial-workspace.md, „Plik struktury”.
'''

GROUPS = [
    ('wordlists', 'Słowa podstawiane za $ZMIENNE$ (talk.ini, ENDS.ini)', r'^Src/(talk|ENDS)\.ini\|[A-Z]'),
    ('briefings', 'Odprawy BunnyLorda (talk.ini)', r'^Src/talk\.ini\|'),
    ('endings', 'Podsumowania poziomów (ENDS.ini)', r'^Src/ENDS\.ini\|'),
    ('radio', 'Rozmowy radiowe agentów (chat.ini)', r'^Src/chat\.ini\|'),
    ('levels', 'Poziomy, cele i osiągnięcia', r'^Src/LEVELS/'),
    ('menu', 'Menu i napisy w pliku gry', r'^(menu|exe)\|'),
    ('graphics', 'Grafiki z tekstem i karty postaci', r'^(image|card)\|'),
]
LINE = re.compile(r'^Src/(talk|ENDS)\.ini\|([^|]+)\|(\d+)$')


def main() -> int:
    sections: dict[tuple[str, str], list[tuple[int, str]]] = {}
    for e in load_entries(ROOT):
        m = LINE.match(e['key'])
        if m and m.group(2).isdigit():
            sections.setdefault((m.group(1), m.group(2)), []).append((int(m.group(3)), e['key']))
    sequences = []
    for (file, section), lines in sections.items():
        if len(lines) < 2:
            continue
        numbers = sorted(n for n, _ in lines)
        continuous = numbers == list(range(numbers[0], numbers[0] + len(numbers)))
        sequences.append({
            'id': f'{file.lower()}-{section.lower()}',
            'name': f'{"Odprawa" if file == "talk" else "Podsumowanie poziomu"} {section}',
            'group': 'briefings' if file == 'talk' else 'endings',
            'order': {'certainty': 'pewna' if continuous else 'odtworzona',
                      'source': 'numer wiersza sekcji w kluczu' + ('' if continuous else ' (z lukami)')},
            'speakers': {'certainty': 'pewna', 'source': 'talk.ini i ENDS.ini mówi BunnyLord (bible.yaml)'},
            'lines': [{'key': key, 'speaker': 'bunnylord'} for _, key in sorted(lines)],
        })
    data = {
        'format': 1,
        'groups': [{'id': g, 'name': n} for g, n, _ in GROUPS],
        'rules': [{'group': g, 'match': p} for g, _, p in GROUPS],
        'sequences': sequences,
    }
    text = HEADER + '\n' + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=140)
    (ROOT / 'translations/structure.yaml').write_text(text, encoding='utf-8', newline='\n')
    print(f'{len(GROUPS)} grup, {len(sequences)} rozmów, {sum(len(s["lines"]) for s in sequences)} kwestii w rozmowach')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
