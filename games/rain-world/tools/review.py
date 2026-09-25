"""Odśwież translations/en-pl-review.json: EN i uwagi z tekstów gry (work/en.json), PL z pliku.

    .venv\\Scripts\\python.exe games\\rain-world\\tools\\review.py

Plik tłumaczenia jest jedyny (decyzja 0021); nowe wpisy dopisuje `batch.py merge`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries, write_entries  # noqa: E402


def row_for(key: str, text: str, english: dict) -> dict:
    """Wpis review: EN z gry (albo z klucza dla wpisów spolszczenia), PL i uwagi."""
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
    return row


def main() -> int:
    english = json.loads((ROOT / 'work/en.json').read_text(encoding='utf-8'))
    rows = [row_for(e['key'], e['polish'], english) for e in load_entries(ROOT)]
    write_entries(ROOT, rows)
    print(f'{len(rows)} wpisów')
    return 0


if __name__ == '__main__':
    sys.exit(main())
