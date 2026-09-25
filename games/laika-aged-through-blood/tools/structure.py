"""Zapisz translations/structure.yaml: grupy i rozmowy Laiki dla pracowni korekty.

    .venv\\Scripts\\python.exe games\\laika-aged-through-blood\\tools\\structure.py

Grupy są stałe (reguły po prefiksach kluczy). Rozmowy (sekwencje) powstają z kluczy
dialogów D_<scena>_<MÓWCA>_<n>: mówcę podaje kontekst „mówi X”, numer kwestii — koniec
klucza. Sekwencją jest tylko scena liniowa z co najmniej dwiema kwestiami; sceny z odnogami
(ten sam numer kwestii kilka razy, np. A_MAYA_1 i LAIKA_1) zostają w grupie w kolejności
pliku, bo pracownia nie pokazuje jeszcze grafu. Mówcę przypisuje wzorzec `regex_klucza`
postaci z bible.yaml; kwestia bez pasującej postaci nie ma mówcy. Uruchom po zmianie
kluczy dialogów (dotłumaczenie, nowa wersja gry).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries  # noqa: E402

HEADER = '''# Grupy i rozmowy Laiki dla pracowni korekty — plik generuje tools/structure.py,
# nie edytuj ręcznie. Format: docs/specs/editorial-workspace.md, „Plik struktury”.
'''

GROUPS = [
    ('menu', 'Menu, ustawienia i interfejs', [r'^UI_(?!TUT)', r'^task$']),
    ('tutorial', 'Samouczek', [r'^UI_TUT', r'^D_Tutorial']),
    ('prologue', 'Prolog, krótkofalówka i śmierć (D_0)', [r'^D_0_']),
    ('mines', 'Kopalnie (D_1)', [r'^D_1_']),
    ('lighthouse', 'Latarnia (D_2)', [r'^D_2_']),
    ('big-tree', 'Wielkie Drzewo (D_3)', [r'^D_3_']),
    ('floating-city', 'Latające Miasto (D_4)', [r'^D_4_']),
    ('finale', 'Trzy główne zadania (D_6)', [r'^D_6_']),
    ('flashbacks', 'Wspomnienia (D_F)', [r'^D_F_']),
    ('village', 'Wioska, bunkier i Herman (D_K)', [r'^D_K_']),
    ('villagers', 'Rozmowy z mieszkańcami (D_B)', [r'^D_B_']),
    ('activities', 'Prezenty, muzycy, mapy i taśmy (D_A)', [r'^D_A_']),
    ('side', 'Zadania poboczne (D_S)', [r'^D_S_']),
    ('meals', 'Posiłki, świece i kowal (D_M)', [r'^D_M_']),
    ('quests', 'Dziennik zadań', [r'^Q_D']),
    ('items', 'Przedmioty, broń, kasety i przepisy', [r'^I_', r'^R_C']),
    ('zones', 'Miejsca', [r'^ZN_']),
    ('characters', 'Postacie', [r'^CH_']),
    ('achievements', 'Osiągnięcia', [r'^AC_']),
]


def group_of(key: str) -> str | None:
    for group, _, patterns in GROUPS:
        if any(re.search(p, key) for p in patterns):
            return group
    return None


def speakers(bible: dict) -> list[tuple[re.Pattern, str]]:
    return [(re.compile(p['regex_klucza']), p['id']) for p in bible.get('postacie', []) if p.get('regex_klucza')]


def scenes(entries: list[dict]) -> dict[str, list[tuple[int, str]]]:
    """Scena → [(numer kwestii, klucz)] dla dialogów z mówcą w kontekście."""
    found: dict[str, list[tuple[int, str]]] = {}
    for e in entries:
        m = re.search(r'mówi (\S+?)(,|$)', e.get('context', ''))
        if not e['key'].startswith('D_') or not m:
            continue
        cut = e['key'].rfind(f'_{m.group(1)}_')
        number = e['key'][cut + len(m.group(1)) + 2:]
        if cut < 0 or not number.isdigit():
            continue
        found.setdefault(e['key'][:cut], []).append((int(number), e['key']))
    return found


def slug(scene: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', scene.lower()).strip('-')


def main() -> int:
    entries = load_entries(ROOT)
    bible = yaml.safe_load((ROOT / 'translations/bible.yaml').read_text(encoding='utf-8'))
    who = speakers(bible)
    sequences = []
    for scene, lines in scenes(entries).items():
        numbers = sorted(n for n, _ in lines)
        if len(lines) < 2 or len(set(numbers)) != len(numbers):
            continue
        group = group_of(scene + '_')
        continuous = numbers == list(range(numbers[0], numbers[0] + len(numbers)))
        out_lines = []
        for _, key in sorted(lines):
            speaker = next((sid for pattern, sid in who if pattern.search(key)), None)
            out_lines.append({'key': key, **({'speaker': speaker} if speaker else {})})
        sequences.append({
            'id': slug(scene), 'name': scene, 'group': group,
            'order': {'certainty': 'pewna' if continuous else 'odtworzona',
                      'source': 'numeracja kwestii w kluczach sceny' + ('' if continuous else ' (z lukami)')},
            'speakers': {'certainty': 'pewna', 'source': 'kod mówiącego w kluczu; postać według regex_klucza w bible.yaml'},
            'lines': out_lines,
        })
    data = {
        'format': 1,
        'groups': [{'id': g, 'name': name} for g, name, _ in GROUPS],
        'rules': [{'group': g, 'match': p} for g, _, patterns in GROUPS for p in patterns],
        'sequences': sequences,
    }
    text = HEADER + '\n' + yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120)
    (ROOT / 'translations/structure.yaml').write_text(text, encoding='utf-8', newline='\n')
    print(f'{len(GROUPS)} grup, {len(sequences)} rozmów, {sum(len(s["lines"]) for s in sequences)} kwestii w rozmowach')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
