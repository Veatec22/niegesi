"""Translation batches for Holy Shoot.

    python tools/batch.py show [ns]      -> untranslated entries as `ns|key @@ text`
    python tools/batch.py put FILE       -> merge `ns|key @@ text` lines; \\n = new line
    python tools/batch.py from-review    -> take corrections made in en-pl-review.json
    python tools/batch.py stats

translations/pl.json is the source: {"namespace|key": "polski tekst"}, only
translated entries. translations/en-pl-review.json is generated from it and the
game's English locres (namespace, key, english, polish) for human review; after
correcting it, run `from-review` to carry the changes back into pl.json.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent / 'sprawl' / 'tools'))
import locres  # noqa: E402

PL = ROOT / 'translations/pl.json'
REVIEW = ROOT / 'translations/en-pl-review.json'
TOKEN = re.compile(r'\{[^}]+\}')


def ident(namespace, key):
    return f'{namespace}|{key}'


def source():
    return {ident(ns, key): text for (ns, key), text in locres.load(ROOT / 'work/en.locres').texts().items()}


def review_rows(english, polish):
    rows = []
    for name in sorted(english):
        ns, key = name.split('|', 1)
        rows.append({'namespace': ns, 'key': key, 'english': english[name], 'polish': polish.get(name, '')})
    return rows


def check(name, english, text):
    assert english.count('\n') == text.count('\n'), ('new lines', name)
    assert sorted(TOKEN.findall(english)) == sorted(TOKEN.findall(text)), ('tokens', name)


def save(english, polish):
    polish = dict(sorted(polish.items()))
    PL.write_text(json.dumps(polish, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    REVIEW.write_text(json.dumps(review_rows(english, polish), ensure_ascii=False, indent=1) + '\n',
                      encoding='utf-8')


def main():
    command = sys.argv[1]
    english = source()
    polish = json.loads(PL.read_text(encoding='utf-8'))
    if command == 'show':
        prefix = sys.argv[2] if len(sys.argv) > 2 else None
        for name, text in sorted(english.items()):
            if name not in polish and (prefix is None or name.split('|', 1)[0] == prefix):
                print(f'{name} @@ ' + text.replace('\r', '').replace('\n', '\\n'))
    elif command == 'put':
        count = 0
        for line in Path(sys.argv[2]).read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            name, text = line.split(' @@ ', 1)
            source_text = english[name]
            text = text.replace('\\n', '\r\n' if '\r\n' in source_text else '\n')
            check(name, source_text, text)
            # Keep leading/trailing spaces of the original: the game glues values to them.
            lead = source_text[:len(source_text) - len(source_text.lstrip(' '))]
            trail = source_text[len(source_text.rstrip(' ')):]
            polish[name] = lead + text.strip(' ') + trail
            count += 1
        save(english, polish)
        print('put', count, 'translated', len(polish), 'of', len(english))
    elif command == 'from-review':
        rows = json.loads(REVIEW.read_text(encoding='utf-8'))
        changed = 0
        for row in rows:
            name = ident(row['namespace'], row['key'])
            if row['polish'] and polish.get(name) != row['polish']:
                check(name, english[name], row['polish'])
                polish[name] = row['polish']
                changed += 1
        save(english, polish)
        print('from review', changed, 'changed')
    elif command == 'stats':
        print(len(polish), 'of', len(english))


if __name__ == '__main__':
    main()
