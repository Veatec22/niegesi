"""Batch helper for translating: show missing entries, put translations (key<TAB>text).

python work/batch.py show <prefix> [limit]   -> prints missing entries with context
python work/batch.py put <file.tsv>          -> merges translations into en-pl-review.json (\\n = newline)
python work/batch.py stats
"""
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import load_entries, polish_by_key, update_polish  # noqa: E402

REVIEW = load_entries(ROOT)


def load():
    return polish_by_key(ROOT)


def main():
    cmd = sys.argv[1]
    pl = load()
    if cmd == 'stats':
        missing = collections.Counter(r['key'].split('/')[0] for r in REVIEW if r['english'].strip() and r['key'] not in pl)
        print(sum(missing.values()), missing.most_common())
    elif cmd == 'show':
        prefixes = tuple(sys.argv[2].split(','))
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10**6
        n = 0
        for r in REVIEW:
            if r['key'].startswith(prefixes) and r['english'].strip() and r['key'] not in pl:
                ctx = (' |ctx: ' + r['context'].replace('\n', ' ')) if r.get('context') else ''
                print(r['key'] + '\t' + r['english'].replace('\n', '\\n') + ctx)
                n += 1
                if n >= limit:
                    break
    elif cmd == 'put':
        english = {r['key']: r['english'] for r in REVIEW}
        added, new = 0, {}
        for line in Path(sys.argv[2]).read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            key, text = line.split('\t', 1)
            assert key in english, 'unknown key ' + key
            text = text.replace('\\n', '\n')
            assert english[key].count('\n') == text.count('\n'), ('newlines', key)
            new[key] = text
            added += 1
        update_polish(ROOT, new)
        print('added', added, 'total', len(load()))


if __name__ == '__main__':
    main()
