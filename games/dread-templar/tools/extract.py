"""Dump the English source text and refresh the review file.

Reads an original resources.assets, pairs every English entry with whatever is
already in translations/pl.json, and writes translations/en-pl-review.json.
Never writes into the game directory.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import game

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True, help='Original "DreadTemplar_Data" folder, never written to')
    args = parser.parse_args()

    data = game.load(args.game / 'resources.assets')
    english = data['eng']
    assert data['pol'] == {}, 'This build already carries Polish text.'

    polish_path = ROOT / 'translations/pl.json'
    polish = json.loads(polish_path.read_text(encoding='utf-8')) if polish_path.exists() else {}

    review, missing = {}, 0
    for category, key, entry in game.entries(english):
        translated = polish.get(category, {}).get(key, {})
        row = {'en': entry}
        if translated:
            row['pl'] = translated
        else:
            missing += 1
        review[f'{category}/{key}'] = row

    out = ROOT / 'translations/en-pl-review.json'
    out.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    characters = sum(len(str(v)) for _, _, e in game.entries(english) for v in e.values())
    print(json.dumps({'entries': len(review), 'translated': len(review) - missing,
                      'missing': missing, 'english_characters': characters,
                      'output': str(out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
