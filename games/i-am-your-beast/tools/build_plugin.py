"""Zbuduj paczkę z pluginem BepInEx: polski dla I Am Your Beast bez podmiany plików gry.

Sprawdza pl.json względem angielskich tekstów z translations/en-pl-review.json, kompiluje
plugin, zapisuje pl.tsv (klucz, odcisk angielskiego, tekst) i składa archiwum z BepInEksem,
pluginem, tekstami i instrukcją. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\i-am-your-beast\\tools\\build_plugin.py --game "C:\\Games\\I Am Your Beast"
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
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]

VERSION = '0.2.0'
DATA = 'I Am Your Beast_Data'
PLUGIN = 'notgeeseIAmYourBeast'
PACKAGE = 'I-Am-Your-Beast-PL'

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
    'netstandard.dll',
    'System.dll',
    'System.Core.dll',
    'UnityEngine.dll',
    'UnityEngine.CoreModule.dll',
    'UnityEngine.TextRenderingModule.dll',
    'UnityEngine.TextCoreFontEngineModule.dll',
    'UnityEngine.UI.dll',                 # TMP_Text dziedziczy po Graphic
    'Unity.TextMeshPro.dll',
    'AudioTextSynchronizer.dll',          # PhraseAsset, TextSynchronizer
    'Assembly-CSharp.dll',                # Fleece
]
BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']

# Wstawki, które gra podmienia sama (klawisz, broń, liczba sekund, akcja w podpowiedzi)
# oraz znaczniki TMP. Muszą przejść do tłumaczenia bez zmian.
TOKENS = re.compile(r'\[KEY\]|\[WEAPON\]|\bVALUE\b|\[Quick Turn\]|</?[a-z]+(?:=[^>]*)?>')


def fingerprint(text: str) -> int:
    """FNV-1a samych liter i cyfr ASCII — to samo co Texts.Fingerprint w pluginie."""
    value = 2166136261
    for c in text:
        if ord(c) > 127 or not c.isalnum():
            continue
        value = ((value ^ ord(c)) * 16777619) & 0xFFFFFFFF
    return value


def escape(text: str) -> str:
    return text.replace('\\', '\\\\').replace('\t', '\\t').replace('\n', '\\n')


def check(terms: dict[str, str]) -> tuple[list[tuple[str, str, str]], dict]:
    review = json.loads((ROOT / 'translations/en-pl-review.json').read_text(encoding='utf-8'))
    english = {row['key']: row['english'] for row in review}
    polish_review = {row['key']: row['polish'] for row in review}
    problems, rows = [], []
    for key, value in terms.items():
        if key not in english:
            problems.append(f'{key}: nie ma takiego klucza w en-pl-review.json')
            continue
        if polish_review[key] != value:
            problems.append(f'{key}: pl.json i en-pl-review.json się różnią')
        if not value:
            continue
        if '\r' in value or '\t' in value:
            problems.append(f'{key}: \\r albo tabulator w tekście')
        source = english[key]
        if Counter(TOKENS.findall(source)) != Counter(TOKENS.findall(value)):
            problems.append(f'{key}: wstawki {TOKENS.findall(source)} != {TOKENS.findall(value)}')
        if key.startswith('phrase/') and '\n' in value:
            problems.append(f'{key}: odcinek sceny w jednej linii')
        rows.append((key, source, value))
    missing = [key for key in english if key not in terms]
    if missing:
        problems.append(f'{len(missing)} kluczy z en-pl-review.json nie ma w pl.json, np. {missing[:3]}')
    if problems:
        raise SystemExit('pl.json ma błędy:\n  ' + '\n  '.join(problems))
    groups = Counter(key.split('/')[0] for key, _, _ in rows)
    totals = Counter(key.split('/')[0] for key, text in english.items() if text.strip())
    return rows, {'translated': dict(groups), 'with_text': dict(totals)}


def write_terms(rows: list[tuple[str, str, str]], destination: Path) -> int:
    lines = [f'{escape(key)}\t{fingerprint(source):08x}\t{escape(value)}' for key, source, value in rows]
    # newline='\n': bez tego Python na Windowsie zapisuje CRLF.
    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    return len(lines)


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


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
    out = ROOT / 'dist' / f'{PACKAGE}-{VERSION}.zip'
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

        archive.write(work / f'{PLUGIN}.dll', f'BepInEx/plugins/{PLUGIN}/{PLUGIN}.dll')
        archive.write(work / 'pl.tsv', f'BepInEx/plugins/{PLUGIN}/pl.tsv')
        archive.write(ROOT / 'docs/INSTALL-plugin.txt', 'READ-ME.txt')
        archive.write(REPO / 'LICENSE', f'BepInEx/plugins/{PLUGIN}/LICENSE-notgeese.txt')

    shutil.copyfile(BEPINEX_SOURCE, out.parent / BEPINEX_SOURCE.name)

    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert 'winhttp.dll' in names, 'brak loadera BepInEx'
        assert 'BepInEx-LICENSE.txt' in names, 'brak licencji BepInEksa'
        assert not any(name.endswith(('.assets', '.resS', '.resource', '.unity3d', '.bank')) for name in names), \
            'paczka nie może zawierać plików gry'
        assert not any(name.startswith(DATA) for name in names), 'paczka nie może zawierać plików gry'

    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z I Am Your Beast.exe)')
    args = parser.parse_args()

    terms = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    rows, stats = check(terms)

    work = ROOT / 'work' / 'plugin'
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    entries = write_terms(rows, work / 'pl.tsv')
    compile_plugin(args.game.resolve(), work / f'{PLUGIN}.dll')
    archive = package(work)

    print(json.dumps({
        'version': VERSION,
        'entries': entries,
        **stats,
        'plugin_bytes': (work / f'{PLUGIN}.dll').stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
        'bepinex': BEPINEX_VERSION,
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
