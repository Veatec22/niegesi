"""Zbuduj paczkę z pluginem BepInEx: polski dla Broforce bez podmiany plików gry.

Kompiluje plugin, zamienia pl.json na pl.tsv, odświeża en-pl-review.json i składa
archiwum z BepInEksem, pluginem, tekstami i instrukcją. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\broforce\\tools\\build_plugin.py --game "C:\\Games\\Broforce"
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
VERSION = '0.2.0'
DATA = 'Broforce_Data'
PLUGIN_FOLDER = 'notgeeseBroforce'
PLUGIN_DLL = 'notgeeseBroforce.dll'
PACKAGE = f'Broforce-PL-{VERSION}.zip'

BEPINEX_VERSION = '5.4.23.5'
BEPINEX = REPO / 'vendor' / 'bepinex'
BEPINEX_BINARY = BEPINEX / f'BepInEx_win_x64_{BEPINEX_VERSION}.zip'
BEPINEX_SOURCE = BEPINEX / f'BepInEx-source-{BEPINEX_VERSION}.zip'
BEPINEX_CORE = BEPINEX / 'win_x64' / 'BepInEx' / 'core'

COMPILERS = [
    Path(r'C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/Roslyn/csc.exe'),
    Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'),
]

# mscorlib i System z gry, moduły Unity, kod gry (Localisation) i BitCode (Singleton, baza LanguageManagera).
GAME_REFERENCES = [
    'mscorlib.dll',
    'System.dll',
    'System.Core.dll',
    'UnityEngine.dll',
    'UnityEngine.CoreModule.dll',
    'UnityEngine.TextRenderingModule.dll',
    'UnityEngine.UI.dll',
    'Assembly-CSharp.dll',
    'BitCode.dll',
]

BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']
SOURCES = ['Plugin.cs', 'PolishGlyphs.cs', 'PolishText3D.cs']


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def load_terms() -> dict[str, str]:
    return json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))


def write_terms(terms: dict[str, str], destination: Path) -> int:
    """pl.json -> pl.tsv: klucz, tabulator, tekst; nowe linie jako \\n."""
    lines = []
    for key, value in terms.items():
        assert '\t' not in key and '\t' not in value, f'tabulator w {key}'
        assert '\r' not in value, f'CR w {key}'
        lines.append(f'{key}\t' + value.replace('\n', '\\n'))
    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    return len(lines)


def check_terms(terms: dict[str, str], english: dict[str, str]) -> list[str]:
    """Klucze spoza banku gry i rozjechane placeholdery — to by się w grze nie pokazało albo wysypało."""
    import re
    problems = []
    for key, value in terms.items():
        if key not in english:
            problems.append(f'{key}: nie ma takiego klucza w banku gry')
            continue
        want = sorted(re.findall(r'\{\d+\}', english[key]))
        have = sorted(re.findall(r'\{\d+\}', value))
        if want != have:
            problems.append(f'{key}: placeholdery {have} zamiast {want}')
        if english[key].count('<') != value.count('<'):
            problems.append(f'{key}: inna liczba znaczników niż w oryginale')
    return problems


def read_english(game: Path) -> dict[str, str]:
    """Angielski bank tekstów prosto z resources.assets (do korekty i kontroli kluczy)."""
    sys.path.insert(0, str(ROOT / 'tools'))
    from bank import read_banks
    return read_banks(game / DATA / 'resources.assets')['en']


def write_review(terms: dict[str, str], english: dict[str, str]) -> int:
    """en-pl-review.json: każdy wpis banku gry, polski tam, gdzie już jest."""
    review = []
    for key, value in english.items():
        if key.startswith('LANGUAGE_'):
            continue
        review.append({'key': key, 'english': value, 'polish': terms.get(key, '')})
    path = ROOT / 'translations/en-pl-review.json'
    path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return len(review)


def compile_plugin(game: Path, output: Path) -> None:
    managed = game / DATA / 'Managed'
    references = []
    for name in GAME_REFERENCES:
        path = managed / name
        if not path.exists():
            raise SystemExit(f'Brak {path} — czy to na pewno katalog gry?')
        references.append(f'/r:{path}')
    for name in BEPINEX_REFERENCES:
        path = BEPINEX_CORE / name
        if not path.exists():
            raise SystemExit(f'Brak {path} — rozpakuj {BEPINEX_BINARY.name} do vendor/bepinex/win_x64.')
        references.append(f'/r:{path}')

    command = [
        str(compiler()),
        '/nologo', '/noconfig', '/nostdlib+', '/optimize+', '/warn:4',
        '/target:library',
        f'/out:{output}',
        *references,
        *(str(ROOT / 'plugin' / name) for name in SOURCES),
    ]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        print(result.stdout or '', result.stderr or '', sep='\n')
        raise SystemExit('Kompilacja pluginu nie powiodła się.')


def package(work: Path) -> Path:
    out = ROOT / 'dist' / PACKAGE
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        # BepInEx prosto z oficjalnego wydania; changelog pomijamy, to śmieć w katalogu gry.
        with zipfile.ZipFile(BEPINEX_BINARY) as bepinex:
            for name in bepinex.namelist():
                if name.endswith('/') or name == 'changelog.txt':
                    continue
                archive.writestr(name, bepinex.read(name))

        # LGPL-2.1 wymaga dołączenia licencji; źródła leżą obok paczki.
        with zipfile.ZipFile(BEPINEX_SOURCE) as source:
            archive.writestr('BepInEx-LICENSE.txt', source.read(f'BepInEx-{BEPINEX_VERSION}/LICENSE'))

        archive.write(work / PLUGIN_DLL, f'BepInEx/plugins/{PLUGIN_FOLDER}/{PLUGIN_DLL}')
        archive.write(work / 'pl.tsv', f'BepInEx/plugins/{PLUGIN_FOLDER}/pl.tsv')
        archive.write(ROOT / 'docs/INSTALL-plugin.txt', 'READ-ME.txt')
        archive.write(REPO / 'LICENSE', f'BepInEx/plugins/{PLUGIN_FOLDER}/LICENSE-notgeese.txt')

    # Źródła BepInEksa jako osobny plik obok paczki — ten sam adres pobrania.
    shutil.copyfile(BEPINEX_SOURCE, out.parent / BEPINEX_SOURCE.name)

    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert 'winhttp.dll' in names, 'brak loadera BepInEx'
        assert 'BepInEx-LICENSE.txt' in names, 'brak licencji BepInEksa'
        assert f'BepInEx/plugins/{PLUGIN_FOLDER}/pl.tsv' in names
        game_files = [n for n in names if n.startswith(DATA) or n.endswith(('.assets', '.assetbundle', '.resS'))]
        assert not game_files, f'paczka nie niesie plików gry: {game_files}'

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z Broforce.exe)')
    args = parser.parse_args()
    game = args.game.resolve()

    terms = load_terms()
    english = read_english(game)
    problems = check_terms(terms, english)
    if problems:
        print('\n'.join(problems))
        raise SystemExit('Teksty nie pasują do banku gry.')
    reviewed = write_review(terms, english)

    work = ROOT / 'work' / 'plugin'
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    count = write_terms(terms, work / 'pl.tsv')
    compile_plugin(game, work / PLUGIN_DLL)
    archive = package(work)

    print(json.dumps({
        'version': VERSION,
        'terms': count,
        'bank': reviewed,
        'plugin_bytes': (work / PLUGIN_DLL).stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
        'bepinex': BEPINEX_VERSION,
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
