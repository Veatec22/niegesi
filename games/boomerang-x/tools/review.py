"""Write translations/en-pl-review.json: the English table beside the Polish.

Reads the original DLL, not a built one - the build overwrites each row's
`description` with Polish, so the developers' notes survive only here. They are
the context a translator wants. Length is not a constraint worth reporting: the
build lends room between rows, and `max_char_limit` is the authors' own note
about what fits on screen, which the game does not enforce either.
"""
import argparse
import json
from pathlib import Path

import table

HERE = Path(__file__).resolve().parent
GAME = HERE.parent
RELATIVE = Path('BOOMERANG X_Data') / 'Managed' / 'Assembly-CSharp.dll'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True,
                        help='The original Assembly-CSharp.dll, or the game folder holding it')
    parser.add_argument('--translations', type=Path, default=GAME / 'translations' / 'pl.json')
    parser.add_argument('--out', type=Path, default=GAME / 'translations' / 'en-pl-review.json')
    args = parser.parse_args()

    source = args.source / RELATIVE if args.source.is_dir() else args.source
    polish = json.loads(args.translations.read_text(encoding='utf-8'))

    entries = []
    for row in table.rows(table.Assembly(source)):
        entries.append({'key': row['id'],
                        'english': row['columns']['english']['text'],
                        'polish': polish.get(row['id'], ''),
                        'context': row['description'],
                        'max_char_limit': row['max_char_limit']})

    args.out.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + '\n',
                        encoding='utf-8')
    print(json.dumps({'written': str(args.out), 'rows': len(entries),
                      'translated': sum(1 for e in entries if e['polish'])}))


if __name__ == '__main__':
    main()
