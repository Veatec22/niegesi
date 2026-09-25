"""Wyciągnij teksty Cyber Hook z data.unity3d do work/source/<język>.json.

Gra trzyma każdy język jako TextAsset „CyberHook <Język>” — CSV KEY,VALUE,DETAILS
z końcami CRLF. Czytamy surowe bajty (UnityPy przy dekodowaniu gubi \\r) i parsujemy
dokładnie tak jak Language_SO.ParseLanguageFile: podział po CRLF, przecinki poza
cudzysłowami, obcięcie cudzysłowów z brzegów, "" -> ", trim. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\cyber-hook\\tools\\extract.py --game "C:\\Games\\CyberHook_GOG"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
from pathlib import Path

import UnityPy

ROOT = Path(__file__).resolve().parents[1]
DATA = 'CyberHook_Data'
SPLIT = re.compile(r',(?=(?:[^"]*"[^"]*")*(?![^"]*"))')
LANGUAGES = {
    'English': 'en', 'French': 'fr', 'German': 'de', 'Spanish': 'es', 'Russian': 'ru',
    'Brazilian Portuguese': 'pt', 'Japanese': 'jp', 'Simplified Chinese': 'zh',
}


def text_bytes(raw: bytes) -> bytes:
    """TextAsset: nazwa (int32 + bajty, wyrównanie do 4), potem m_Script (int32 + bajty)."""
    name_length = struct.unpack_from('<i', raw, 0)[0]
    offset = 4 + name_length
    offset += (-offset) % 4
    length = struct.unpack_from('<i', raw, offset)[0]
    return raw[offset + 4:offset + 4 + length]


def parse(data: bytes) -> list[dict]:
    """Wiersze w kolejności pliku, jak w grze. Nagłówek KEY,VALUE,DETAILS pomijamy."""
    rows = []
    seen = set()
    for line in [line for line in data.decode('utf-8').split('\r\n') if line][1:]:
        cells = [cell.strip('"') for cell in SPLIT.split(line)]
        if len(cells) < 2 or not cells[0].strip():
            continue
        key = cells[0]
        game_key = key.lower().strip()
        if game_key in seen:
            continue
        seen.add(game_key)
        rows.append({
            'key': key,
            'text': cells[1].replace('""', '"').strip(),
            'details': cells[2].replace('""', '"').strip() if len(cells) > 2 else '',
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z CyberHook.exe)')
    args = parser.parse_args()

    bundle = args.game / DATA / 'data.unity3d'
    env = UnityPy.load(str(bundle))
    out = ROOT / 'work' / 'source'
    out.mkdir(parents=True, exist_ok=True)
    counts = {}
    for obj in env.objects:
        if obj.type.name != 'TextAsset':
            continue
        name = obj.read().m_Name
        if not name.startswith('CyberHook '):
            continue
        code = LANGUAGES[name[len('CyberHook '):]]
        rows = parse(text_bytes(obj.get_raw_data()))
        (out / f'{code}.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        counts[code] = len(rows)

    print(json.dumps({
        'data.unity3d': hashlib.sha256(bundle.read_bytes()).hexdigest()[:16],
        'entries': counts,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
