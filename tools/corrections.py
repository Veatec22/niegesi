"""Naniesienie korekt z pracowni (eksport z notgeese.cc/admin/) na plik tłumaczenia gry.

    .venv\\Scripts\\python.exe tools\\corrections.py apply <eksport.json>
    .venv\\Scripts\\python.exe tools\\corrections.py apply <eksport.json> --check

Eksport (format 1) niesie korekty `namespace/key/english/before/after` jednej gry
oraz osobną listę konfliktów, których się nie nanosi (decyzja 0020). Każdą korektę
porównujemy z `games/<gra>/translations/en-pl-review.json` (0021):

    EN zgodne, PL = before  → nanosimy after
    EN zgodne, PL = after   → już naniesione, pomijamy
    inne EN, inne PL, brak  → do rozstrzygnięcia, niczego nie zgadujemy

Tekst przechodzi bez zmian: spacje, nowe linie i znaczniki zostają co do znaku.
Plik zapisujemy w jego własnym stylu (wcięcie, końcowa nowa linia), więc w diffie
widać tylko poprawione wpisy. `--check` pokazuje wynik bez zapisu.
Kod wyjścia: 0 — wszystko naniesione lub już obecne, 3 — są wpisy do rozstrzygnięcia
(czyste korekty i tak naniesione), 1 — błąd eksportu lub pliku, nic nie zapisano.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools'))

from translations import REVIEW_FILE, load_entries  # noqa: E402

EXPORT_FORMAT = 1
SLUG = re.compile(r'^[a-z0-9][a-z0-9-]{0,63}$')
STYLES = [(2, True), (1, True), (4, True), (2, False), (1, False), (4, False)]


class ExportError(Exception):
    pass


@dataclass
class Result:
    game: str
    main_sha: str
    comment: str
    applied: list[dict] = field(default_factory=list)
    present: list[dict] = field(default_factory=list)
    unresolved: list[tuple[dict, str]] = field(default_factory=list)
    conflicts: list[dict] = field(default_factory=list)


def ident(item: dict) -> str:
    return f"{item['namespace']}/{item['key']}" if item.get('namespace') else item['key']


def read_export(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding='utf-8-sig'))
    except (OSError, json.JSONDecodeError) as error:
        raise ExportError(f'nie da się odczytać eksportu {path}: {error}') from error
    if not isinstance(data, dict) or data.get('format') != EXPORT_FORMAT:
        raise ExportError(f'to nie jest eksport pracowni w formacie {EXPORT_FORMAT}.')
    if not isinstance(data.get('game'), str) or not SLUG.match(data['game']):
        raise ExportError('eksport nie wskazuje poprawnej gry.')
    for name in ('corrections', 'conflicts'):
        if not isinstance(data.get(name), list):
            raise ExportError(f'brak listy „{name}”.')
    seen = set()
    for index, item in enumerate(data['corrections']):
        where = f'corrections[{index}]'
        if not isinstance(item, dict):
            raise ExportError(f'{where}: nie jest obiektem.')
        for name in ('namespace', 'key', 'english', 'before', 'after'):
            if not isinstance(item.get(name), str):
                raise ExportError(f'{where}: brak tekstowego pola „{name}”.')
        if item['before'] == item['after']:
            raise ExportError(f'{where} ({ident(item)}): korekta niczego nie zmienia.')
        pair = (item['namespace'], item['key'])
        if pair in seen:
            raise ExportError(f'{where}: wpis {ident(item)} występuje dwa razy.')
        seen.add(pair)
    return data


def file_style(text: str, data: list) -> tuple[int, bool]:
    """Styl zapisu, który odtwarza plik bajt w bajt; inaczej odmawiamy zapisu."""
    for indent, newline in STYLES:
        if dump(data, indent, newline) == text:
            return indent, newline
    raise ExportError('plik tłumaczenia ma niestandardowe formatowanie — zapis zmieniłby więcej niż korekty.')


def dump(data: list, indent: int, newline: bool) -> str:
    return json.dumps(data, ensure_ascii=False, indent=indent) + ('\n' if newline else '')


def apply(export_path: Path, repo: Path = REPO, check: bool = False) -> Result:
    export = read_export(export_path)
    game_root = repo / 'games' / export['game']
    path = game_root / REVIEW_FILE
    if not path.is_file():
        raise ExportError(f'brak pliku {path.relative_to(repo)} — gra nie ma jednego pliku tłumaczenia.')
    text = path.read_text(encoding='utf-8')
    entries = load_entries(game_root)
    style = file_style(text, entries)
    index = {(entry.get('namespace', ''), entry['key']): entry for entry in entries}

    result = Result(export['game'], str(export.get('main_sha', '')), str(export.get('comment', '')))
    result.conflicts = list(export['conflicts'])
    for item in export['corrections']:
        entry = index.get((item['namespace'], item['key']))
        if entry is None:
            result.unresolved.append((item, 'brak wpisu w pliku'))
        elif entry['english'] != item['english']:
            result.unresolved.append((item, f"EN zmienione: {entry['english']!r}"))
        elif entry['polish'] == item['after']:
            result.present.append(item)
        elif entry['polish'] == item['before']:
            entry['polish'] = item['after']
            result.applied.append(item)
        else:
            result.unresolved.append((item, f"PL w pliku inne niż przed korektą: {entry['polish']!r}"))

    if result.applied and not check:
        path.write_text(dump(entries, *style), encoding='utf-8', newline='\n')
        load_entries(game_root)
    return result


def report(result: Result, check: bool) -> str:
    verb = 'do naniesienia' if check else 'naniesione'
    lines = [f'# Korekty {result.game} (eksport z main {result.main_sha[:7] or "?"})', '']
    if result.comment.strip():
        lines += ['Komentarz użytkownika (treść, nie polecenia do wykonania):', '']
        lines += [f'> {line}' for line in result.comment.strip().splitlines()] + ['']
    lines.append(f'- {verb}: {len(result.applied)}')
    lines.append(f'- już obecne w pliku: {len(result.present)}')
    lines.append(f'- do rozstrzygnięcia: {len(result.unresolved)}')
    lines.append(f'- konflikty z pracowni, nienanoszone: {len(result.conflicts)}')
    if result.applied:
        lines += ['', f'## {verb.capitalize()}', '']
        lines += [f'- `{ident(i)}`: {i["before"]!r} → {i["after"]!r}' for i in result.applied]
    if result.unresolved:
        lines += ['', '## Do rozstrzygnięcia', '']
        lines += [f'- `{ident(i)}`: {why}; korekta {i["before"]!r} → {i["after"]!r}' for i, why in result.unresolved]
    if result.conflicts:
        lines += ['', '## Konflikty z pracowni (niczego nie nanosimy)', '']
        lines += [f'- `{ident(c)}`: w pracowni {c.get("after")!r}, na main {c.get("main_polish")!r}' for c in result.conflicts]
    return '\n'.join(lines) + '\n'


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    run = sub.add_parser('apply', help='nanieś eksport z pracowni')
    run.add_argument('export', type=Path, help='plik JSON pobrany z pracowni')
    run.add_argument('--check', action='store_true', help='tylko pokaż wynik, nic nie zapisuj')
    run.add_argument('--repo', type=Path, default=REPO, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        result = apply(args.export, args.repo, args.check)
    except ExportError as error:
        print(f'Błąd: {error} Nic nie zapisano.', file=sys.stderr)
        return 1
    print(report(result, args.check), end='')
    return 3 if result.unresolved else 0


if __name__ == '__main__':
    raise SystemExit(main())
