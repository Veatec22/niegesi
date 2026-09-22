"""Raport kontrolny tłumaczenia gry. Tylko raportuje; nigdy nie blokuje.

Użycie: python l10n_report.py games/<gra> [--limit 80]
Czyta translations/en-pl-review.json i opcjonalnie translations/bible.yaml,
zapisuje work/l10n-report.md i wypisuje liczniki sekcji.
"""
import argparse
import collections
import json
import re
from pathlib import Path

import yaml

TOKEN = re.compile(r'\[[a-z]+:[^\]]*\]|\{[^{}]*\}|</?[a-z]+(?:=[^>]*)?>|%[sd]|\\n')
MASC = re.compile(r'\b\w+ł(?:em|bym)\b', re.I)
FEM = re.compile(r'\b\w+ł(?:am|abym)\b', re.I)
# Rzeczowniki i tryb rozkazujący, które tylko wyglądają na formy czasownika.
NOT_VERB = {
    'stołem', 'kołem', 'aniołem', 'popiołem', 'orłem', 'czołem', 'dołem', 'mułem',
    'wołem', 'tyłem', 'kościołem', 'żywiołem', 'ogółem', 'przemysłem', 'pomysłem',
    'zmysłem', 'węzłem', 'masłem', 'hasłem', 'rzemiosłem', 'krzesłem', 'wiosłem',
    'złam', 'połam', 'przełam', 'wyłam', 'odłam', 'nadłam', 'ułam', 'załam',
    'reklam', 'kłam', 'skłam', 'okłam',
}
# Czas teraźniejszy/przyszły czasowników na -łać („wysyłam”, „zdziałam”).
NOT_VERB_SUFFIX = ('syłam', 'działam', 'wołam', 'syłabym')
ADDRESS_TY = re.compile(r'\b\w+ł(?:eś|aś)\b|\bjesteś\b', re.I)
PLURAL_PLACEHOLDER = re.compile(r'\{[^{}]+\}\s+[A-Za-z]+s\b')
EN_WORDS = re.compile(r'\b(?:the|and|you|your|with|this|that|press|click)\b', re.I)


def is_name(word, keep):
    """Słowo z listy nazw, także odmienione („Wastera”) albo z kropkami („Psst...”)."""
    w = re.split(r"['’]", word.lower().strip('.,!?:;„”"()'))[0]
    return w in keep or any(len(k) >= 4 and w.startswith(k) for k in keep)


def load(game):
    review = json.loads((game/'translations/en-pl-review.json').read_text(encoding='utf-8'))
    path = game/'translations/bible.yaml'
    bible = yaml.safe_load(path.read_text(encoding='utf-8')) if path.exists() else {}
    return review, bible or {}


def row_id(row):
    parts = [row.get('table'), row.get('term') or row.get('key')]
    return ' '.join(str(p) for p in parts if p)


def short(text, n=140):
    text = text.replace('\n', '⏎')
    return text if len(text) <= n else text[:n-1] + '…'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('game', type=Path)
    ap.add_argument('--limit', type=int, default=80, help='max wpisów na sekcję w pliku')
    args = ap.parse_args()
    game = args.game.resolve()
    review, bible = load(game)
    rows = [r for r in review if r.get('english', '').strip()]

    keep = [str(x).lower() for x in bible.get('bez_tlumaczenia') or []]
    keep += [str(p.get('nazwa', '')).lower() for p in bible.get('postacie') or []]
    keep += [w for phrase in list(keep) if ' ' in phrase for w in phrase.split()]
    stems = [str(f).lower() for t in bible.get('terminy') or [] for f in t.get('formy') or []]
    settings = bible.get('ustawienia') or {}
    dialog_re = re.compile(settings['dialog_klucz']) if settings.get('dialog_klucz') else None
    ignores = [(i['sprawdzenie'], re.compile(i['klucz'])) for i in bible.get('ignoruj') or []]

    found = collections.OrderedDict((name, []) for name in (
        'brak', 'tokeny', 'plec', 'adresat', 'terminy', 'spojnosc', 'angielski',
        'liczebniki', 'dlugosc', 'wielkie_litery', 'typografia'))

    def report(check, row, note):
        rid = row_id(row)
        if any(c == check and rx.search(rid) for c, rx in ignores):
            return
        found[check].append((rid, row['english'], row.get('polish', ''), note))

    for row in rows:
        en, pl = row['english'], row.get('polish', '')
        if not pl.strip():
            report('brak', row, 'brak tłumaczenia')
            continue
        if collections.Counter(TOKEN.findall(en)) != collections.Counter(TOKEN.findall(pl)):
            report('tokeny', row, 'inne tokeny/znaczniki niż w oryginale')
        if PLURAL_PLACEHOLDER.search(en):
            report('liczebniki', row, 'liczba w placeholderze — sprawdź 1 / 2–4 / 5+')
        low = pl.lower()
        en_words = re.findall(r"[A-Za-z][A-Za-z'’-]*", TOKEN.sub(' ', en))
        only_names = en_words and all(is_name(w, keep) for w in en_words)
        if pl.strip() == en.strip() and re.search(r'[A-Za-z]{3}', en) and not only_names and low.strip() not in keep:
            report('angielski', row, 'identyczne z oryginałem')
        elif len(EN_WORDS.findall(pl)) >= 2:
            report('angielski', row, 'angielskie słowa w tekście')

        # Typografia
        if re.search(r'"[^"]+"', pl):
            report('typografia', row, 'proste cudzysłowy zamiast „”')
        if re.search(r'\w - \w', pl) and not re.search(r'\w\s+- ', en):
            report('typografia', row, 'dywiz zamiast myślnika')
        if re.search(r'\s[?!:;](?:\s|$)', pl):
            report('typografia', row, 'spacja przed znakiem interpunkcyjnym')
        if (en[:1] == ' ') != (pl[:1] == ' ') or (en[-1:] == ' ') != (pl[-1:] == ' '):
            report('typografia', row, 'inna spacja na początku/końcu niż w oryginale (doklejana liczba?)')
        if '  ' in pl.strip() and '  ' not in en.strip():
            report('typografia', row, 'podwójna spacja')

        # Wielkie litery w krótkich napisach UI
        words = pl.split()
        if 2 <= len(words) <= 6 and not pl.isupper():
            caps = [w for prev, w in zip(words, words[1:])
                    if w[:1].isupper() and not w.isupper() and not prev.endswith(('.', '!', '?', '…'))
                    and not is_name(w, keep + stems)]
            en_caps = [w for w in en.split()[1:] if w[:1].isupper()]
            if len(caps) >= 2 and len(en_caps) >= 2:
                report('wielkie_litery', row, 'Title Case przeniesiony z angielskiego?')

        # Długość
        rid = row_id(row)
        is_dialog = bool(dialog_re and dialog_re.search(rid))
        if is_dialog:
            if len(pl) > 60 and len(pl) > len(en) * 1.35:
                report('dlugosc', row, f'napis {len(pl)} zn. vs {len(en)} w EN')
        elif len(en) <= 30 and len(pl) > max(len(en) * 1.6, len(en) + 10):
            report('dlugosc', row, f'UI {len(pl)} zn. vs {len(en)} w EN')

    # Płeć mówiącego i forma zwracania się
    for person in bible.get('postacie') or []:
        if not person.get('klucz'):
            continue
        rx = re.compile(person['klucz'])
        wrong = MASC if person.get('plec') == 'k' else FEM if person.get('plec') == 'm' else None
        formal = str(person.get('mowi_do_gracza', '')).startswith(('pan', 'pani'))
        for row in rows:
            if not rx.search(row_id(row)) or not row.get('polish'):
                continue
            if wrong:
                hits = [w for w in wrong.findall(row['polish'])
                        if w.lower() not in NOT_VERB and not w.lower().endswith(NOT_VERB_SUFFIX)]
                if hits:
                    report('plec', row, f"{person.get('nazwa', person['id'])} ({person['plec']}): {', '.join(hits)}")
            if formal and ADDRESS_TY.search(row['polish']):
                report('adresat', row, f"{person.get('nazwa', person['id'])} mówi do gracza per pan — forma na „ty”?")

    # Terminy z biblii
    for term in bible.get('terminy') or []:
        en_rx = re.compile(r'\b' + term['en'] + r'\b', re.I)
        forms = [f.lower() for f in term.get('formy') or [term['pl'][:5]]]
        for row in rows:
            if en_rx.search(row['english']) and row.get('polish') and not any(f in row['polish'].lower() for f in forms):
                report('terminy', row, f"{term['en']} → {term['pl']}")

    # Ten sam krótki oryginał, różne tłumaczenia
    groups = collections.defaultdict(list)
    for row in rows:
        if len(row['english']) <= 60 and row.get('polish'):
            groups[row['english'].strip().lower()].append(row)
    for items in groups.values():
        variants = {r['polish'].strip().lower() for r in items}
        if len(variants) > 1:
            for r in items:
                report('spojnosc', r, f'{len(variants)} warianty dla tego samego EN')

    titles = {
        'brak': 'Brak tłumaczenia', 'tokeny': 'Tokeny i znaczniki',
        'plec': 'Płeć mówiącego (według biblii)', 'adresat': 'Forma zwracania się',
        'terminy': 'Terminy z biblii', 'spojnosc': 'Spójność: ten sam oryginał, różne PL',
        'angielski': 'Angielskie resztki', 'liczebniki': 'Liczebniki przy placeholderach',
        'dlugosc': 'Długość (ryzyko ucięcia)', 'wielkie_litery': 'Wielkie litery',
        'typografia': 'Typografia',
    }
    out = [f'# Raport kontrolny — {game.name}', '',
           'Tylko do przejrzenia. Zgłoszenie to miejsce do obejrzenia, nie wyrok.', '',
           f'Wpisy z tekstem: {len(rows)}. Biblia: {"tak" if bible else "brak"}.', '']
    out += ['| Sekcja | Zgłoszenia |', '| --- | ---: |']
    out += [f'| {titles[k]} | {len(v)} |' for k, v in found.items()]
    for key, items in found.items():
        if not items:
            continue
        out += ['', f'## {titles[key]} ({len(items)})', '']
        for rid, en, pl, note in items[:args.limit]:
            out += [f'- `{rid}` — {note}', f'  - EN: {short(en)}', f'  - PL: {short(pl)}']
        if len(items) > args.limit:
            out.append(f'- … i {len(items) - args.limit} więcej')
    target = game/'work/l10n-report.md'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(' '.join(f'{k}={len(v)}' for k, v in found.items()))
    print(target)


if __name__ == '__main__':
    main()
