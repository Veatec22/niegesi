"""Partie tłumaczenia Neon Abyss.

    python tools/batch.py show [prefiks] [limit] -> nieprzetłumaczone jako `klucz @@ tekst`
    python tools/batch.py put PLIK               -> dopisz linie `klucz @@ tekst`; \\n = nowa linia
    python tools/batch.py from-review            -> przenieś poprawki z en-pl-review.json
    python tools/batch.py stats

translations/pl.json to źródło: {"klucz I2": "polski tekst"}, tylko przetłumaczone.
translations/en-pl-review.json powstaje z niego i z angielskiego w work/source.json
(tools/extract.py) — do przeglądu; po poprawkach `from-review` zanosi je do pl.json.
Wpisy tekstowe, które są w istocie nazwami zasobów (ścieżki fontów, nazwy grafik),
nie są do tłumaczenia i plugin kopiuje je z angielskiego.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PL = ROOT / 'translations/pl.json'
REVIEW = ROOT / 'translations/en-pl-review.json'
TOKEN = re.compile(r'\{[^}]*\}|<[^>]*>|\[i2s_[^\]]*\]')
RESOURCE = re.compile(r'^(Fonts & Materials/.*|[a-z0-9]+(_[a-z0-9]+)+|-+|\.+|\?+|v\{\[Version\]\})$')


def english():
    data = json.loads((ROOT / 'work/source.json').read_text(encoding='utf-8'))
    index = [language['code'] for language in data['languages']].index('en-US')
    return {t['key']: t['values'][index] for t in data['terms']
            if t['type'] == 0 and t['values'][index].strip() and not RESOURCE.match(t['values'][index])}


def check(key, source, text):
    assert text.strip(), ('pusty', key)
    assert '\\n' not in text, ('dosłowne \\n', key)
    assert sorted(TOKEN.findall(source)) == sorted(TOKEN.findall(text)), ('znaczniki', key)


def save(source, polish):
    polish = dict(sorted(polish.items()))
    PL.write_text(json.dumps(polish, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    rows = [{'key': key, 'english': text, 'polish': polish.get(key, '')} for key, text in source.items()]
    REVIEW.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else 'stats'
    source = english()
    polish = json.loads(PL.read_text(encoding='utf-8'))
    unknown = polish.keys() - source.keys()
    assert not unknown, ('klucze spoza gry', sorted(unknown)[:5])

    if command == 'show':
        prefix = sys.argv[2] if len(sys.argv) > 2 else ''
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
        todo = [(k, v) for k, v in source.items() if k not in polish and k.startswith(prefix)]
        for key, text in todo[:limit]:
            print(f'{key} @@ ' + text.replace('\n', '\\n'))
        print(f'# {min(limit, len(todo))} z {len(todo)}', file=sys.stderr)
    elif command == 'put':
        added = 0
        for line in Path(sys.argv[2]).read_text(encoding='utf-8').splitlines():
            if not line.strip() or line.startswith('#'):
                continue
            key, text = line.split(' @@ ', 1)
            key, text = key.strip(), text.strip().replace('\\n', '\n')
            assert key in source, ('nieznany klucz', key)
            check(key, source[key], text)
            polish[key] = text
            added += 1
        save(source, polish)
        print(f'dopisano {added}, razem {len(polish)}/{len(source)}')
    elif command == 'from-review':
        rows = json.loads(REVIEW.read_text(encoding='utf-8'))
        changed = 0
        for row in rows:
            if row['polish'] and polish.get(row['key']) != row['polish']:
                check(row['key'], source[row['key']], row['polish'])
                polish[row['key']] = row['polish']
                changed += 1
        save(source, polish)
        print(f'zmienione {changed}')
    elif command == 'stats':
        save(source, polish)
        print(json.dumps({'translated': len(polish), 'total': len(source)}))
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
