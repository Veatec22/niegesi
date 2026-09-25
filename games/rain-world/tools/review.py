"""Złóż translations/en-pl-review.json z pl.json i angielskich tekstów gry (work/en.json).

    .venv\\Scripts\\python.exe games\\rain-world\\tools\\review.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    polish = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    english = json.loads((ROOT / 'work/en.json').read_text(encoding='utf-8'))
    rows = []
    for key, text in polish.items():
        source = english.get(key, {})
        row = {'key': key, 'english': source.get('english', key.split(':', 1)[1]), 'polish': text}
        notes = []
        if source.get('context'):
            notes.append('w kodzie: ' + ', '.join(source['context'].split(', ')[:3]))
        if source.get('source') and source['source'] != 'base':
            notes.append('dodatek: ' + source['source'])
        if key not in english:
            notes.append('wpis dodany przez spolszczenie')
        if notes:
            row['note'] = '; '.join(notes)
        rows.append(row)
    (ROOT / 'translations/en-pl-review.json').write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(rows)} wpisów')
    return 0


if __name__ == '__main__':
    sys.exit(main())
