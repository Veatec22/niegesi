"""Merge translation batches into translations/pl.json and rebuild the review file.

Batches in translations/parts/*.json map EN -> PL. Every plain key must be a
literal the game really uses (work/strings.json from extract_strings.py) or a
dialogue line (except batches named *runtime*, holding values observed only in
the running game's log); template keys with {0}..{9} must keep the same holes in PL.
Dialogue <Tokens> must survive in PL. pl.json is rebuilt as the vertical sample
(keys from prepare_ui.py / prepare_opening.py, current values kept) plus all
batches, so keys removed from a batch disappear. After the user's corrections,
put them into a batch file (e.g. parts/95-user.json), not only into pl.json.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOLE = re.compile(r'\{\d\}')
TOKEN = re.compile(r'<[A-Za-z]+>')


def dialog_lines():
    lines = {}
    for row in json.loads((ROOT / 'work/dialog-review.json').read_text(encoding='utf-8')):
        text = re.sub(r'\s*\{[^}]*\}\s*$', '', row['english'].strip()).lstrip('#= ').strip()
        if text:
            lines.setdefault(text, []).append(row['key'].replace('Dialog/', ''))
    return lines


def main():
    strings = json.loads((ROOT / 'work/strings.json').read_text(encoding='utf-8'))
    literals = {}
    for s in strings:
        literals.setdefault(s['text'], set()).update(s['functions'])
    dialog = dialog_lines()
    pl_path = ROOT / 'translations/pl.json'
    from prepare_opening import DIALOG, NATIVE
    from prepare_ui import UI
    current = json.loads(pl_path.read_text(encoding='utf-8'))
    vertical = set(UI) | set(NATIVE) | set(DIALOG)
    pl = {en: value for en, value in current.items() if en in vertical}
    errors = []
    for part in sorted((ROOT / 'translations/parts').glob('*.json')):
        batch = json.loads(part.read_text(encoding='utf-8'))
        for en, value in batch.items():
            if HOLE.search(en):
                if sorted(HOLE.findall(en)) != sorted(HOLE.findall(value)):
                    errors.append(f'{part.name}: holes differ: {en!r}')
            elif en not in literals and en not in dialog and 'runtime' not in part.name:
                errors.append(f'{part.name}: not a game literal or dialogue line: {en!r}')
            if sorted(TOKEN.findall(en)) != sorted(TOKEN.findall(value)):
                errors.append(f'{part.name}: <Token> mismatch: {en!r}')
            if not value.strip() and en.strip():
                errors.append(f'{part.name}: empty translation: {en!r}')
            pl[en] = value
    items = json.loads((ROOT / 'translations/items.json').read_text(encoding='utf-8'))
    for group in ('nouns', 'modifiers', 'tails'):
        for en in items[group]:
            if en not in literals and not any(en in s for s in literals if len(s) < 80):
                errors.append(f'items.json {group}: unknown word {en!r}')
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    pl_path.write_text(json.dumps(pl, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    review = []
    for en, value in pl.items():
        if en in dialog:
            context = 'Dialog: ' + ', '.join(dialog[en][:3])
        elif en in literals:
            context = 'EXE: ' + ', '.join(sorted(f.replace('gml_Script_', '').replace('gml_Object_', '')
                                                 for f in literals[en])[:3])
        else:
            context = 'Szablon: składany przez grę z fragmentów i wartości {n}'
        review.append(dict(key=en, english=en, polish=value, context=context))
    for en, (noun, gender) in items['nouns'].items():
        review.append(dict(key=f'item-noun:{en}', english=en, polish=noun,
                           context=f'Rzeczownik w nazwach przedmiotów, rodzaj {gender}'))
    for en, forms in items['modifiers'].items():
        review.append(dict(key=f'item-modifier:{en}', english=en, polish=' / '.join(forms),
                           context='Przymiotnik w nazwach przedmiotów: m / ż / n'))
    for en, phrase in items['tails'].items():
        review.append(dict(key=f'item-tail:{en}', english=en, polish=phrase,
                           context='Określenie na końcu nazwy przedmiotu, bez odmiany'))
    (ROOT / 'translations/en-pl-review.json').write_text(
        json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'pl.json: {len(pl)} entries; review: {len(review)} rows')


if __name__ == '__main__':
    main()
