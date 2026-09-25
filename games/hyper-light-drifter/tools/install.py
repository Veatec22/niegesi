r"""Instaluje zbudowane pliki do testu albo przywraca oryginały — tylko dla autora.

Użycie:
  .venv\Scripts\python.exe games\hyper-light-drifter\tools\install.py --game "C:\Games\Hyper Light Drifter"
  .venv\Scripts\python.exe games\hyper-light-drifter\tools\install.py --game "C:\Games\Hyper Light Drifter" --restore

Oryginały (sprawdzone sumą) trafiają do backups/hyper-light-drifter/ przed pierwszą podmianą;
kopia, która już istnieje, nie jest nadpisywana.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

from hld import HASHES, REPO, ROOT


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True)
    parser.add_argument('--restore', action='store_true')
    args = parser.parse_args()
    backup = REPO / 'backups/hyper-light-drifter'
    report = json.loads((ROOT / 'dist/build-report.json').read_text(encoding='utf-8'))
    built_hashes = report['build_sha256']

    # Najpierw pełne sprawdzenie, potem dopiero zapis czegokolwiek.
    plan = {}
    for file, expected in HASHES.items():
        target = args.game / file
        current = digest(target.read_bytes())
        saved = backup / file
        if saved.exists():
            assert digest(saved.read_bytes()) == expected, f'zła kopia: {saved}'
        else:
            assert current == expected, f'{file}: nieznana wersja, a kopii brak'
        # Przywracanie może zastąpić starszy build; wraca sprawdzony oryginał.
        assert args.restore or current in {expected, built_hashes[file]}, f'{file}: nieznany plik w grze'
        # Przy przywracaniu bez kopii plik w grze jest oryginałem (sprawdzone wyżej)
        # i to on trafi do kopii poniżej.
        source = saved if args.restore else ROOT / 'dist/build' / file
        if not args.restore:
            assert digest(source.read_bytes()) == built_hashes[file], f'{file}: build się zmienił'
        plan[file] = source

    backup.mkdir(parents=True, exist_ok=True)
    for file in plan:
        saved = backup / file
        if not saved.exists():
            saved.write_bytes((args.game / file).read_bytes())
    for file, source in plan.items():
        target = args.game / file
        temporary = target.with_name(target.name + '.notgeese-tmp')
        temporary.write_bytes(source.read_bytes())
        os.replace(temporary, target)
        want = HASHES[file] if args.restore else built_hashes[file]
        assert digest(target.read_bytes()) == want, file
    print(('Przywrócono' if args.restore else 'Zainstalowano') + f' {len(plan)} pliki; kopie: {backup}')


if __name__ == '__main__':
    main()
