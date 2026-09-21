"""Zbuduj paczkę z pluginem BepInEx: polski dla Skate Story bez podmiany plików gry.

Kompiluje plugin, zamienia pl.json na pl.tsv, wypisuje mapę czcionek z build.py
i składa archiwum z BepInEksem, pluginem, tekstami i instrukcją.

    .venv\\Scripts\\python.exe games\\skate-story\\tools\\build_plugin.py --game "C:\\Games\\Skate Story"
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

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
REPO = ROOT.parents[1]

sys.path.insert(0, str(TOOLS))
from build import FONT_MAP, PL  # mapa czcionek i indeks polskiego slotu — jedno źródło prawdy

VERSION = '0.3'
DATA = 'SkateStory_Data'
PLUGIN_FOLDER = 'NieGesiSkateStory'

# Unity 6 wywraca preloader BepInEksa 5 (brak Module.GetPEKind w tym Mono),
# więc ta gra idzie na wydaniu rozwojowym szóstki.
BEPINEX_VERSION = '6.0.0-be.788'
BEPINEX_COMMIT = '5b766a3b7f6c164d4798924a93f3acf4db769d06'
BEPINEX = REPO / 'vendor' / 'bepinex'
BEPINEX_BINARY = BEPINEX / f'BepInEx-Unity.Mono-win-x64-{BEPINEX_VERSION}.zip'
BEPINEX_SOURCE = BEPINEX / f'BepInEx-source-{BEPINEX_VERSION}.zip'
BEPINEX_CORE = BEPINEX / 'be788' / 'BepInEx' / 'core'

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
    'UnityEngine.TextRenderingModule.dll',
    'I2-Localization.dll',
]

BEPINEX_REFERENCES = ['BepInEx.Core.dll', 'BepInEx.Unity.Mono.dll', '0Harmony.dll']

# Unity 6 okraja mscorlib z metod, których gra nie używa — wypada m.in. Module.GetPEKind,
# bez której preloader BepInEksa nie rusza. Podstawiamy pełną bibliotekę Unity dla tej
# wersji silnika (zbudowana z klas Mono na licencji MIT), tylko ten jeden plik.
# Komplet, nie pojedynczy plik: pełna mscorlib obok okrojonych System.dll i System.Core.dll
# zawiesza grę przed pierwszym ekranem. Tak też robią gotowe paczki „BepInEx with corlibs".
CORLIB_VERSION = '6000.0.45'
CORLIB_ZIP = REPO / 'vendor' / 'unity-corlibs' / f'{CORLIB_VERSION}.zip'
UNITY_LIBS = 'BepInEx/unity-libs'


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def write_tables(work: Path) -> tuple[int, int]:
    terms = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    lines = []
    for key, value in terms.items():
        assert '\t' not in key and '\t' not in value, f'tabulator w {key}'
        lines.append(f'{key}\t' + value.replace('\n', '\\n'))
    (work / 'pl.tsv').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    fonts = [f'{key}\t{value}' for key, value in FONT_MAP.items()]
    (work / 'fonts.tsv').write_text('\n'.join(fonts) + '\n', encoding='utf-8')
    return len(lines), len(fonts)


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
        # Komunikaty kompilatora bywają w kodowaniu, którego konsola nie udźwignie.
        log = output.parent / 'compile.log'
        log.write_text((result.stdout or '') + '\n' + (result.stderr or ''), encoding='utf-8')
        raise SystemExit(f'Kompilacja pluginu nie powiodła się; szczegóły w {log}')


def point_mono_at_unity_libs(config: bytes) -> bytes:
    """Mono ma zaglądać po biblioteki systemowe najpierw do naszego katalogu."""
    text = config.decode('utf-8')
    # Podstawienie przez lambdę, bo ścieżka ma odwrotne ukośniki, a te w szablonie
    # zamiany byłyby czytane jako sekwencje sterujące.
    line = 'dll_search_path_override = ' + UNITY_LIBS.replace('/', '\\')
    patched, count = re.subn(
        r'^dll_search_path_override\s*=.*$',
        lambda _: line,
        text,
        count=1,
        flags=re.MULTILINE,
    )
    assert count == 1, 'nie znalazłem dll_search_path_override w doorstop_config.ini'
    return patched.encode('utf-8')


def package(work: Path) -> Path:
    out = ROOT / 'dist' / f'Skate-Story-PL-{VERSION}.zip'
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        with zipfile.ZipFile(BEPINEX_BINARY) as bepinex:
            for name in bepinex.namelist():
                if name.endswith('/') or name == 'changelog.txt':
                    continue
                data = bepinex.read(name)
                if name == 'doorstop_config.ini':
                    data = point_mono_at_unity_libs(data)
                archive.writestr(name, data)

        corlib_count = 0
        with zipfile.ZipFile(CORLIB_ZIP) as corlibs:
            for name in corlibs.namelist():
                if name.endswith('.dll'):
                    archive.writestr(f'{UNITY_LIBS}/{Path(name).name}', corlibs.read(name))
                    corlib_count += 1
        assert corlib_count >= 10, f'komplet corlibs wygląda na niepełny ({corlib_count} plików)'

        # LGPL-2.1 wymaga dołączenia licencji; źródła kładziemy obok paczki.
        with zipfile.ZipFile(BEPINEX_SOURCE) as source:
            archive.writestr('BepInEx-LICENSE.txt', source.read(f'BepInEx-{BEPINEX_COMMIT}/LICENSE'))

        archive.write(work / 'NieGesiSkateStory.dll', f'BepInEx/plugins/{PLUGIN_FOLDER}/NieGesiSkateStory.dll')
        archive.write(work / 'pl.tsv', f'BepInEx/plugins/{PLUGIN_FOLDER}/pl.tsv')
        archive.write(work / 'fonts.tsv', f'BepInEx/plugins/{PLUGIN_FOLDER}/fonts.tsv')
        archive.write(ROOT / 'docs/INSTALL-plugin.txt', 'READ-ME.txt')
        archive.write(REPO / 'LICENSE', f'BepInEx/plugins/{PLUGIN_FOLDER}/LICENSE-niegesi.txt')

    shutil.copyfile(BEPINEX_SOURCE, out.parent / BEPINEX_SOURCE.name)

    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert 'winhttp.dll' in names, 'brak loadera BepInEx'
        assert 'BepInEx-LICENSE.txt' in names, 'brak licencji BepInEksa'
        assert f'BepInEx/plugins/{PLUGIN_FOLDER}/fonts.tsv' in names
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

    terms, fonts = write_tables(work)
    compile_plugin(args.game.resolve(), work / 'NieGesiSkateStory.dll')
    archive = package(work)

    print(json.dumps({
        'version': VERSION,
        'terms': terms,
        'fonts': fonts,
        'polish_slot': PL,
        'plugin_bytes': (work / 'NieGesiSkateStory.dll').stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
        'bepinex': BEPINEX_VERSION,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
