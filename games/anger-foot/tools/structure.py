"""Zapisz translations/structure.yaml: grupy i rozmowy Anger Foot dla pracowni korekty.

    .venv\\Scripts\\python.exe games\\anger-foot\\tools\\structure.py

Klucz dialogu to `Dialogue/<obszar>/<scena> <n> [<mówiący> > <adresat>]` (tools/review.py),
więc każda scena to rozmowa: kolejność z numeru, mówca z klucza. Mówcę przypisuje
tabela SPEAKERS do postaci z bible.yaml; bezimienni NPC idą do npc-m / npc-k po płci
w kluczu, a głosy bez postaci w biblii (komputer, interkom, zwierzęta) zostają bez mówcy.
Uruchom po zmianie kluczy dialogów.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries  # noqa: E402

HEADER = '''# Grupy i rozmowy Anger Foot dla pracowni korekty — plik generuje tools/structure.py,
# nie edytuj ręcznie. Format: docs/specs/editorial-workspace.md, „Plik struktury”.
'''

GROUPS = [
    ('menu', 'Menu i ustawienia', r'^UI/(Main Menu|Pause Menu|Settings Menu|Game Settings|Input Mapping Dialog|Resolution Confirmation Dialog)/'),
    ('levels', 'Poziomy, mapa i cele', r'^UI/(Level Names|World Map|Challenge Levels|Level Goal Types|Star Goals|Level Complete Screen|Boss Defeated Screen)/'),
    ('shoes', 'Buty i znajdźki', r'^UI/(Shoes|Shoe Collection|Collectibles|Collectible Types)/'),
    ('tutorial', 'Samouczki, podpowiedzi i HUD', r'^UI/(Tutorials|Hints|HUD)/'),
    ('story', 'Intro, postacie i telewizja', r'^UI/(Intro Cinematic|Character Names|TV Channel Text)/'),
    ('achievements', 'Osiągnięcia', r'^UI/Achievements/'),
    ('credits', 'Napisy końcowe', r'^UI/Credits/'),
    ('ui-other', 'Interfejs — pozostałe', r'^UI/'),
    ('apartments', 'Dialogi — Apartamentowce', r'^Dialogue/Apartments/'),
    ('sewers', 'Dialogi — Kanały', r'^Dialogue/Sewers/'),
    ('offices', 'Dialogi — Biurowce', r'^Dialogue/Offices/'),
    ('dungeons', 'Dialogi — Lochy', r'^Dialogue/Dungeons/'),
    ('crime-tower', 'Dialogi — Wieża Zbrodni', r'^Dialogue/Crime Tower/'),
]

SPEAKERS = {
    'Anger Girl (Female)': 'anger-girl',
    'Crime Minister (Male)': 'minister',
    'Office Boss (Female)': 'prezeska',
    'Pizza Pig (Male)': 'pizza-swinia',
    'Goo Cop (Male)': 'glut-glina',
    'Trash Boss (Neutral)': 'smieciowy-boss',
    'Trash Boss Brain (Neutral)': 'smieciowy-boss',
    'Pizza Delivery Guy (Male)': 'npc-m',
}
LINE = re.compile(r'^(Dialogue/[^/]+/.+?) (\d+) \[(.+?) > (.+?)\]$')


def speaker(name: str) -> str | None:
    if name in SPEAKERS:
        return SPEAKERS[name]
    if re.fullmatch(r'NPC( \d+)? \(Male\)', name):
        return 'npc-m'
    if re.fullmatch(r'NPC( \d+)? \(Female\)', name):
        return 'npc-k'
    return None


def main() -> int:
    bible = yaml.safe_load((ROOT / 'translations/bible.yaml').read_text(encoding='utf-8'))
    known = {p['id'] for p in bible['postacie']}
    assert set(SPEAKERS.values()) <= known, set(SPEAKERS.values()) - known
    scenes: dict[str, list[tuple[int, str, str]]] = {}
    for e in load_entries(ROOT):
        m = LINE.match(e['key'])
        if m:
            scenes.setdefault(m.group(1), []).append((int(m.group(2)), e['key'], m.group(3)))
    sequences = []
    for scene, lines in scenes.items():
        numbers = sorted(n for n, _, _ in lines)
        if len(lines) < 2 or numbers != list(range(numbers[0], numbers[0] + len(numbers))):
            continue
        group = next((g for g, _, p in GROUPS if re.search(p, scene + '/')), None)
        if group is None:
            continue  # nowy obszar: najpierw grupa w GROUPS
        out = []
        for _, key, name in sorted(lines):
            who = speaker(name)
            out.append({'key': key, **({'speaker': who} if who else {})})
        sequences.append({
            'id': re.sub(r'[^a-z0-9]+', '-', scene.split('/', 2)[2].lower()).strip('-'),
            'name': scene.split('/', 2)[2], 'group': group,
            'order': {'certainty': 'pewna', 'source': 'numer kwestii w kluczu'},
            'speakers': {'certainty': 'pewna', 'source': 'mówiący w kluczu [mówiący > adresat]; NPC po płci (npc-m, npc-k)'},
            'lines': out,
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
