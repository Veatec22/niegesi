"""Buduje translations/en-pl-review.json z pl.json i oryginałów z gry; sprawdza znaczniki.

Klucze w pl.json:
  s<indeks>                 napis STRG (tłumaczony wszędzie, gdzie kod go używa)
  s<indeks>@<wpis CODE>     napis STRG tylko w tym wpisie kodu (np. „Controls”, który
                            jest też nazwą sekcji w Prefs.ini)
  j:<plik>/<ścieżka>/<pole> wartość w dia_*.json (plugin tłumaczy po tekście, więc ta sama
                            angielska wartość w innych miejscach dostaje to samo tłumaczenie)

    .venv\\Scripts\\python.exe games\\deadbolt\\tools\\review.py --game "C:\\SteamLibrary\\steamapps\\common\\DEADBOLT"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from strings_usage import Data, disasm  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MARKUP = re.compile(r'&[a-z!]{1,2}&|#')


def json_value(game: Path, key: str) -> str:
    path = key[2:].split('/')
    node = json.loads((game / path[0]).read_text(encoding='utf-8'))
    for part in path[1:]:
        node = node[part]
    if not isinstance(node, str):
        raise SystemExit(f'{key}: not a text value')
    return node


def contexts(data: Data, strings) -> dict[int, list[str]]:
    funcs = data.chains('FUNC', 0, 12, 0, 4, 8)
    varis = data.chains('VARI', 3, 20, 0, 12, 16)
    where: dict[int, list[str]] = {}
    for code, start, length in data.code_entries():
        for _, op, arg in disasm(data, start, length, funcs, varis):
            if op == 'push' and arg and arg[0] == 'str':
                names = where.setdefault(arg[1], [])
                short = code.replace('gml_Object_', '').replace('gml_Script_', 'script ')
                if short not in names:
                    names.append(short)
    return where


def check(key: str, en: str, pl: str) -> list[str]:
    problems = []
    if Counter(MARKUP.findall(en)) != Counter(MARKUP.findall(pl)):
        problems.append('znaczniki &..& / # różnią się')
    if key.startswith('s') and en.count("'") != pl.count("'") and "'&!&" in en:
        problems.append("liczba apostrofów w podpowiedzi klawisza")
    # Spacja na początku bywa celowo zdjęta („ times…” -> „. Spróbuj…” za liczbą),
    # ale na końcu oznacza, że kod coś dokleja — ta musi zostać.
    if (en[-1:] == ' ') != (pl[-1:] == ' '):
        problems.append('spacja na końcu (napis jest doklejany)')
    if any(c in pl for c in '„”–—…'):
        problems.append('znak spoza fontów gry (użyj " - ...)')
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--game', type=Path, required=True)
    game = ap.parse_args().game
    data = Data(game / 'data.win')
    strings = data.strings()
    where = contexts(data, strings)
    pl = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    review, errors = [], 0
    for key, polish in pl.items():
        if key.startswith('s'):
            index = int(key[1:].split('@')[0])
            english = strings[index]
            scope = key.split('@')[1] if '@' in key else None
            ctx = f'tylko {scope}' if scope else ', '.join(where.get(index, [])[:4])
        elif key.startswith('j:'):
            english = json_value(game, key)
            ctx = 'dialog ' + key[2:]
        else:
            raise SystemExit(f'nieznany klucz {key}')
        for problem in check(key, english, polish):
            print(f'{key}: {problem}\n  EN {english!r}\n  PL {polish!r}')
            errors += 1
        review.append({'key': key, 'english': english, 'polish': polish, 'context': ctx})
    # Ta sama wartość JSON musi mieć jedno tłumaczenie (plugin tłumaczy po tekście).
    seen = {}
    for r in review:
        if r['key'].startswith('j:'):
            if seen.setdefault(r['english'], r['polish']) != r['polish']:
                print(f"{r['key']}: inne tłumaczenie tej samej wartości JSON")
                errors += 1
    out = ROOT / 'translations/en-pl-review.json'
    out.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(review)} wpisów -> {out}; problemów: {errors}')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
