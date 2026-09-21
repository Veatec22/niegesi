"""Zbuduj paczkę z pluginem BepInEx: polski dla Boomerang X bez podmiany plików gry.

Kompiluje plugin, zamienia pl.json na pl.tsv i składa archiwum z BepInEksem,
pluginem, tekstami i instrukcją. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\boomerang-x\\tools\\build_plugin.py --game "C:\\SteamLibrary\\steamapps\\common\\Boomerang X"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]

VERSION = '0.2'
DATA = 'BOOMERANG X_Data'
PLUGIN_FOLDER = 'NieGesiBoomerangX'

BEPINEX_VERSION = '5.4.23.5'
BEPINEX = REPO / 'vendor' / 'bepinex'
BEPINEX_BINARY = BEPINEX / f'BepInEx_win_x64_{BEPINEX_VERSION}.zip'
BEPINEX_SOURCE = BEPINEX / f'BepInEx-source-{BEPINEX_VERSION}.zip'
BEPINEX_CORE = BEPINEX / 'win_x64' / 'BepInEx' / 'core'

COMPILERS = [
    Path(r'C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/Roslyn/csc.exe'),
    Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'),
]

# Tabela tekstów i menedżer języków są wkompilowane w Assembly-CSharp.dll.
GAME_REFERENCES = [
    'mscorlib.dll',
    'System.dll',
    'System.Core.dll',
    'UnityEngine.dll',
    'UnityEngine.CoreModule.dll',
    'Assembly-CSharp.dll',
]

BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']

# Ta gra jest zbudowana z okrajaniem kodu zarządzanego, więc preloader BepInEksa
# wywraca się na Module.GetPEKind. Podstawiamy własny punkt wejścia, który robi
# to samo bez tego wywołania. Szczegóły w tools/loader/NieGesiLoader.cs.
LOADER_SOURCE = REPO / 'tools' / 'loader' / 'NieGesiLoader.cs'
LOADER_NAME = 'NieGesiLoader.dll'

# Okrojony jest też System.Core: nie ma w nim System.Linq.IGrouping, którego
# BepInEx używa w swojej konfiguracji. Podstawiamy tę jedną bibliotekę — nie
# mscorlib, bo dwie kopie rdzenia środowiska zawieszają grę.
CORLIB_VERSION = '2020.1.17'
CORLIB_ZIP = REPO / 'vendor' / 'unity-corlibs' / f'{CORLIB_VERSION}.zip'
CORLIB_FILES = ['System.Core.dll']
UNITY_LIBS = 'BepInEx/unity-libs'


def point_doorstop_at_loader(config: bytes) -> bytes:
    """Doorstop ma uruchomić nasz punkt wejścia zamiast preloadera BepInEksa."""
    text = config.decode('utf-8')
    line = 'target_assembly = ' + f'BepInEx{chr(92)}core{chr(92)}{LOADER_NAME}'
    patched, count = re.subn(r'^target_assembly\s*=.*$', lambda _: line,
                             text, count=1, flags=re.MULTILINE)
    assert count == 1, 'nie znalazłem target_assembly w doorstop_config.ini'

    search = 'dll_search_path_override = ' + UNITY_LIBS.replace('/', chr(92))
    patched, count = re.subn(r'^dll_search_path_override\s*=.*$', lambda _: search,
                             patched, count=1, flags=re.MULTILINE)
    assert count == 1, 'nie znalazłem dll_search_path_override w doorstop_config.ini'
    return patched.encode('utf-8')


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def write_terms(destination: Path) -> int:
    """pl.json jest kluczowane identyfikatorem wiersza tabeli — tym, o który pyta gra."""
    terms = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    lines = []
    for key, value in terms.items():
        assert '\t' not in key and '\t' not in value, f'tabulator w {key}'
        lines.append(f'{key}\t' + value.replace('\n', '\\n'))
    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return len(lines)


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


def compile_loader(game: Path, output: Path) -> None:
    """Punkt wejścia idzie w całości przez refleksję — wystarczy mu mscorlib i System."""
    managed = game / DATA / 'Managed'
    command = [
        str(compiler()),
        '/nologo', '/noconfig', '/nostdlib+', '/optimize+', '/warn:4',
        '/target:library',
        f'/out:{output}',
        f'/r:{managed / "mscorlib.dll"}',
        f'/r:{managed / "System.dll"}',
        str(LOADER_SOURCE),
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        log = output.parent / 'loader.log'
        log.write_text((result.stdout or '') + '\n' + (result.stderr or ''), encoding='utf-8')
        raise SystemExit(f'Kompilacja punktu wejścia nie powiodła się; szczegóły w {log}')


def package(work: Path) -> Path:
    out = ROOT / 'dist' / f'Boomerang-X-PL-{VERSION}.zip'
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        with zipfile.ZipFile(BEPINEX_BINARY) as bepinex:
            for name in bepinex.namelist():
                if name.endswith('/') or name == 'changelog.txt':
                    continue
                data = bepinex.read(name)
                if name == 'doorstop_config.ini':
                    data = point_doorstop_at_loader(data)
                archive.writestr(name, data)

        archive.write(work / LOADER_NAME, f'BepInEx/core/{LOADER_NAME}')

        with zipfile.ZipFile(CORLIB_ZIP) as corlibs:
            for name in CORLIB_FILES:
                archive.writestr(f'{UNITY_LIBS}/{name}', corlibs.read(name))


        # LGPL-2.1 wymaga dołączenia licencji; źródła kładziemy obok paczki.
        with zipfile.ZipFile(BEPINEX_SOURCE) as source:
            archive.writestr('BepInEx-LICENSE.txt', source.read(f'BepInEx-{BEPINEX_VERSION}/LICENSE'))

        archive.write(work / 'NieGesiBoomerangX.dll', f'BepInEx/plugins/{PLUGIN_FOLDER}/NieGesiBoomerangX.dll')
        archive.write(work / 'pl.tsv', f'BepInEx/plugins/{PLUGIN_FOLDER}/pl.tsv')
        archive.write(ROOT / 'docs/INSTALL-plugin.txt', 'READ-ME.txt')
        archive.write(REPO / 'LICENSE', f'BepInEx/plugins/{PLUGIN_FOLDER}/LICENSE-niegesi.txt')

    shutil.copyfile(BEPINEX_SOURCE, out.parent / BEPINEX_SOURCE.name)

    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert 'winhttp.dll' in names, 'brak loadera BepInEx'
        assert 'BepInEx-LICENSE.txt' in names, 'brak licencji BepInEksa'
        assert not any(name.endswith(('.assets', '.resS', '.resource')) for name in names), \
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

    terms = write_terms(work / 'pl.tsv')
    compile_plugin(args.game.resolve(), work / 'NieGesiBoomerangX.dll')
    compile_loader(args.game.resolve(), work / LOADER_NAME)
    archive = package(work)

    print(json.dumps({
        'version': VERSION,
        'terms': terms,
        'plugin_bytes': (work / 'NieGesiBoomerangX.dll').stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
        'bepinex': BEPINEX_VERSION,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
