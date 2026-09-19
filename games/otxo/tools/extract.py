"""Dump the English source text and refresh the review file.

Reads the game's own script_english.ini, pairs every entry with whatever is in
translations/pl.json, and writes translations/en-pl-review.json - one row per
key, English beside Polish, in the file's own order.

Never writes into the game directory.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import script_ini

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True, help='The OTXO folder, never written to')
    args = parser.parse_args()

    english = script_ini.load(args.game / 'script_english.ini')
    polish_path = ROOT / 'translations/pl.json'
    polish = json.loads(polish_path.read_text(encoding='utf-8')) if polish_path.exists() else {}

    rows = []
    for key, text in english.items():
        row = {'key': key, 'english': text}
        if key in polish:
            row['polish'] = polish[key]
        rows.append(row)

    out = ROOT / 'translations/en-pl-review.json'
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'entries': len(rows), 'translated': len(polish),
                      'english_characters': sum(len(r['english']) for r in rows),
                      'output': str(out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
