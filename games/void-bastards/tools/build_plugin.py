"""Zbuduj paczkę z pluginem BepInEx: polski dla Void Bastards bez podmiany plików gry.

Kompiluje plugin, zamienia pl.json na pl.tsv i składa archiwum z BepInEksem,
pluginem, tekstami i instrukcją. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\void-bastards\\tools\\build_plugin.py --game "C:\\SteamLibrary\\steamapps\\common\\Void Bastards"
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

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]

VERSION = '0.2.1'
DATA = 'Void Bastards_Data'
PLUGIN_FOLDER = 'notgeeseVoidBastards'

BEPINEX_VERSION = '5.4.23.5'
BEPINEX = REPO / 'vendor' / 'bepinex'
BEPINEX_BINARY = BEPINEX / f'BepInEx_win_x64_{BEPINEX_VERSION}.zip'
BEPINEX_SOURCE = BEPINEX / f'BepInEx-source-{BEPINEX_VERSION}.zip'
BEPINEX_CORE = BEPINEX / 'win_x64' / 'BepInEx' / 'core'

COMPILERS = [
    Path(r'C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/Roslyn/csc.exe'),
    Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'),
]

# Gra działa na profilu .NET 3.5 (mscorlib 2.0); plugin kompiluje się wprost na jej bibliotekach.
GAME_REFERENCES = [
    'mscorlib.dll',
    'System.dll',
    'System.Core.dll',
    'UnityEngine.dll',
    'UnityEngine.CoreModule.dll',
    'UnityEngine.TextRenderingModule.dll',  # Font.HasCharacter w raporcie fontów
    'Assembly-CSharp.dll',  # I2 Localization i stary TextMeshPro są wkompilowane tutaj
]

BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def write_terms(destination: Path) -> int:
    """pl.json jest kluczowane terminem I2 — dokładnie tym, po którym pyta gra."""
    terms = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    lines = []
    for key, value in terms.items():
        assert '\t' not in key and '\t' not in value, f'tabulator w {key}'
        lines.append(f'{key}\t' + value.replace('\n', '\\n'))
    # newline='\n': bez tego Python na Windowsie zapisuje CRLF, a \r trafia na koniec
    # każdego tekstu w grze (TextMeshPro cofa po nim pióro — napisy nakładały się).
    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
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
        *[str(p) for p in sorted((ROOT / 'plugin').glob('*.cs'))],
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        log = output.parent / 'compile.log'
        log.write_text((result.stdout or '') + '\n' + (result.stderr or ''), encoding='utf-8')
        raise SystemExit(f'Kompilacja pluginu nie powiodła się; szczegóły w {log}')


def package(work: Path) -> Path:
    out = ROOT / 'dist' / f'Void-Bastards-PL-{VERSION}.zip'
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

        archive.write(work / 'notgeeseVoidBastards.dll', f'BepInEx/plugins/{PLUGIN_FOLDER}/notgeeseVoidBastards.dll')
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
    compile_plugin(args.game.resolve(), work / 'notgeeseVoidBastards.dll')
    archive = package(work)

    print(json.dumps({
        'version': VERSION,
        'terms': terms,
        'plugin_bytes': (work / 'notgeeseVoidBastards.dll').stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
        'bepinex': BEPINEX_VERSION,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
