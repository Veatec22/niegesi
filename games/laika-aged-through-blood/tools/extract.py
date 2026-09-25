"""Wyciągnij angielskie teksty Laiki z data.unity3d do work/source/en.json.

Gra używa M2H Localization: każdy arkusz każdego języka to TextAsset
`Languages/<KOD>_<ARKUSZ>` w Resources, XML `<entries><entry name="KLUCZ">tekst</entry>`.
Arkusz bez kodu (`_UI` itd.) trzyma limity długości wpisów — liczba albo pusto.

Tekst dekodujemy tak jak gra (Language.DoSwitch): XML → Trim → `\\n` na nową linię
→ StringExtensions.UnescapeXML. Wynik: lista wpisów w kolejności pliku, z arkuszem,
limitem i mówiącym (z klucza dialogu).

    .venv\\Scripts\\python.exe games\\laika-aged-through-blood\\tools\\extract.py --game "C:\\Games\\Laika Aged Through Blood"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import UnityPy

ROOT = Path(__file__).resolve().parents[1]
DATA = 'Laika Aged through Blood_Data'
SHEETS = ('UI', 'CHARACTERS', 'ZONES', 'ITEMS', 'QUESTS', 'DIALOGUES')
NAME = re.compile(r'^([A-Z_]*?)_?(' + '|'.join(SHEETS) + r')$')
SPEAKER = re.compile(r'_([A-Z][A-Z0-9_]*?)_(\d+)$')


def decode(text: str) -> str:
    text = text.strip().replace('\\n', '\n')
    for escaped, plain in (('&apos;', "'"), ('&quot;', '"'), ('&gt;', '>'), ('&lt;', '<'), ('&amp;', '&')):
        text = text.replace(escaped, plain)
    return text


def entries(raw: bytes) -> list[tuple[str, str]]:
    root = ET.fromstring(raw.decode('utf-8-sig'))
    return [(e.get('name'), decode(e.text or '')) for e in root.iter('entry')]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z Laika Aged through Blood.exe)')
    args = parser.parse_args()

    env = UnityPy.load(str(args.game / DATA / 'data.unity3d'))
    sheets: dict[tuple[str, str], bytes] = {}
    for obj in env.objects:
        if obj.type.name != 'TextAsset':
            continue
        asset = obj.read()
        match = NAME.match(asset.m_Name)
        if not match:
            continue
        script = asset.m_Script
        raw = script.encode('utf-8', 'surrogateescape') if isinstance(script, str) else bytes(script)
        sheets[(match.group(1), match.group(2))] = raw

    missing = [s for s in SHEETS if ('EN', s) not in sheets]
    if missing:
        raise SystemExit(f'Nie znalazłem angielskich arkuszy: {missing}')

    limits = {}
    for sheet in SHEETS:
        if ('', sheet) in sheets:
            limits.update({k: int(v) for k, v in entries(sheets[('', sheet)]) if v.isdigit()})

    rows = []
    for sheet in SHEETS:
        for key, text in entries(sheets[('EN', sheet)]):
            if not key or not key.strip():
                continue
            row = {'sheet': sheet, 'key': key, 'text': text}
            if key in limits:
                row['limit'] = limits[key]
            speaker = SPEAKER.search(key) if sheet == 'DIALOGUES' else None
            if speaker:
                row['speaker'] = speaker.group(1)
            rows.append(row)

    out = ROOT / 'work' / 'source'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'en.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    languages = sorted({code for code, sheet in sheets if code and sheet == 'DIALOGUES'})
    print(json.dumps({
        'entries': len(rows),
        'with_text': sum(1 for r in rows if r['text']),
        'per_sheet': {s: sum(1 for r in rows if r['sheet'] == s) for s in SHEETS},
        'limits': len(limits),
        'languages': languages,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
