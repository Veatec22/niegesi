"""Zbuduj paczkę z pluginem BepInEx: polski dla Dread Templar bez podmiany plików gry.

Zamienia pl.json na pl.tsv (rodzaj wpisu, kategoria/klucz, tekst), kompiluje plugin
i składa archiwum z BepInEksem, tekstami i instrukcją. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\dread-templar\\tools\\build_plugin.py --game "C:\\Games\\Dread Templar"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
REPO = ROOT.parents[1]

sys.path.insert(0, str(TOOLS))
from game import CATEGORIES  # ten sam podział co przy metodzie z podmianą pliku

VERSION = '0.2'
DATA = 'DreadTemplar_Data'
PLUGIN_FOLDER = 'notgeeseDreadTemplar'

BEPINEX_VERSION = '5.4.23.5'
BEPINEX = REPO / 'vendor' / 'bepinex'
BEPINEX_BINARY = BEPINEX / f'BepInEx_win_x64_{BEPINEX_VERSION}.zip'
BEPINEX_SOURCE = BEPINEX / f'BepInEx-source-{BEPINEX_VERSION}.zip'
BEPINEX_CORE = BEPINEX / 'win_x64' / 'BepInEx' / 'core'

COMPILERS = [
    Path(r'C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/Roslyn/csc.exe'),
    Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'),
]

GAME_REFERENCES = [
    'mscorlib.dll',
    'System.dll',
    'System.Core.dll',
    'UnityEngine.dll',
    'UnityEngine.CoreModule.dll',
    'Assembly-CSharp.dll',
]

BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def escape(value: str) -> str:
    """Odwrotny ukośnik, nowa linia i tabulator — ten ostatni dzieli kolumny."""
    return value.replace('\\', '\\\\').replace('\n', '\\n').replace('\t', '\\t')


def write_terms(destination: Path) -> tuple[int, int]:
    """pl.json: kategoria → klucz → {text, name}. Plugin pyta o „kategoria/klucz"."""
    polish = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    unknown = [c for c in polish if c not in CATEGORIES]
    assert not unknown, f'nieznane kategorie: {unknown}'

    lines = []
    texts = names = 0
    for category, entries in polish.items():
        for key, entry in entries.items():
            path = f'{category}/{key}'
            assert '\t' not in path, path
            text = entry.get('text')
            # Część wpisów niesie liczby (identyfikator mówiącego) zamiast tekstu.
            if isinstance(text, str) and text:
                lines.append(f't\t{path}\t' + escape(text))
                texts += 1
            name = entry.get('name')
            # Imiona bywają liczbami (identyfikator mówiącego) — te pomijamy.
            if isinstance(name, str) and name:
                lines.append(f'n\t{path}\t' + escape(name))
                names += 1

    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return texts, names


def compile_plugin(game: Path, output: Path) -> None:
    managed = game / DATA / 'Managed'
    references = []
    for name in GAME_REFERENCES:
        path = managed / name
        if path.exists():
            references.append(f'/r:{path}')
        elif name != 'UnityEngine.CoreModule.dll':
            raise SystemExit(f'Brak {path} — czy to na pewno katalog gry?')
    for name in BEPINEX_REFERENCES:
        path = BEPINEX_CORE / name
        if not path.exists():
            raise SystemExit(f'Brak {path} — rozpakuj {BEPINEX_BINARY.name} do {BEPINEX_CORE.parents[1]}.')
        references.append(f'/r:{path}')

    command = [
        str(compiler()),
        '/nologo', '/noconfig', '/nostdlib+', '/optimize+', '/warn:4',
        '/target:library',
        f'/out:{output}',
        *references,
        str(ROOT / 'plugin' / 'Plugin.cs'),
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        log = output.parent / 'compile.log'
        log.write_text((result.stdout or '') + '\n' + (result.stderr or ''), encoding='utf-8')
        raise SystemExit(f'Kompilacja pluginu nie powiodła się; szczegóły w {log}')


def package(work: Path) -> Path:
    out = ROOT / 'dist' / f'Dread-Templar-PL-{VERSION}.zip'
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        with zipfile.ZipFile(BEPINEX_BINARY) as bepinex:
            for name in bepinex.namelist():
                if name.endswith('/') or name == 'changelog.txt':
                    continue
                archive.writestr(name, bepinex.read(name))

        # LGPL-2.1 wymaga dołączenia licencji; źródła kładziemy obok paczki.
        with zipfile.ZipFile(BEPINEX_SOURCE) as source:
            archive.writestr('BepInEx-LICENSE.txt', source.read(f'BepInEx-{BEPINEX_VERSION}/LICENSE'))

        archive.write(work / 'notgeeseDreadTemplar.dll', f'BepInEx/plugins/{PLUGIN_FOLDER}/notgeeseDreadTemplar.dll')
        archive.write(work / 'pl.tsv', f'BepInEx/plugins/{PLUGIN_FOLDER}/pl.tsv')
        archive.write(ROOT / 'docs/INSTALL-plugin.txt', 'READ-ME.txt')
        archive.write(REPO / 'LICENSE', f'BepInEx/plugins/{PLUGIN_FOLDER}/LICENSE-notgeese.txt')

    shutil.copyfile(BEPINEX_SOURCE, out.parent / BEPINEX_SOURCE.name)

    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert 'winhttp.dll' in names, 'brak loadera BepInEx'
        assert 'BepInEx-LICENSE.txt' in names, 'brak licencji BepInEksa'
        assert not any(name.endswith(('.assets', '.resS', '.resource')) for name in names), \
            'paczka nie może zawierać zasobów gry'
        assert not any(name.startswith(DATA) or name.startswith('level') for name in names), \
            'paczka nie może zawierać plików gry'

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z plikiem .exe)')
    args = parser.parse_args()

    work = ROOT / 'work' / 'plugin'
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    texts, names = write_terms(work / 'pl.tsv')
    compile_plugin(args.game.resolve(), work / 'notgeeseDreadTemplar.dll')
    archive = package(work)

    print(json.dumps({
        'version': VERSION,
        'texts': texts,
        'names': names,
        'plugin_bytes': (work / 'notgeeseDreadTemplar.dll').stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
        'bepinex': BEPINEX_VERSION,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
