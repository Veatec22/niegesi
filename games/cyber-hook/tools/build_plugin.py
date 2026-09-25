"""Zbuduj paczkę z pluginem BepInEx: polski dla Cyber Hook bez podmiany plików gry.

Sprawdza teksty z en-pl-review.json względem angielskich tekstów gry (work/source/en.json
z extract.py), kompiluje plugin, zamienia je na pl.tsv i składa archiwum z BepInEksem, pluginem,
tekstami i instrukcją. Nie dotyka katalogu gry.

    .venv\\Scripts\\python.exe games\\cyber-hook\\tools\\build_plugin.py --game "C:\\Games\\CyberHook_GOG"
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
sys.path.insert(0, str(REPO / 'tools'))

from translations import polish_by_key  # noqa: E402

VERSION = '0.2.0'
DATA = 'CyberHook_Data'
PLUGIN = 'notgeeseCyberHook'
PACKAGE = 'Cyber-Hook-PL'

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
    'UnityEngine.TextCoreModule.dll',  # Glyph, GlyphRect, FaceInfo w TMP 2.x
    'UnityEngine.TextRenderingModule.dll',  # Font — źródło fontów dynamicznych
    'UnityEngine.UI.dll',              # TMP_Text dziedziczy po Graphic
    'Unity.TextMeshPro.dll',
    'GlobalAssembly.dll',              # Language_SO, LanguageManager
]
BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']

# Znaczniki TMP i wstawki gry, które muszą przejść do tłumaczenia bez zmian.
TOKENS = re.compile(r'\{\d+\}|<sprite[^>]*>|<link=[^>]*>|</?(?:color|size|link)\b[^>]*>|<br>')


def tokens(text: str) -> list[str]:
    return sorted(TOKENS.findall(text.replace('"', '')))


def check(terms: dict[str, str]) -> dict:
    """Klucz musi być kluczem gry; wstawki {0}, <sprite>, <link> i <br> jak w oryginale."""
    source = json.loads((ROOT / 'work/source/en.json').read_text(encoding='utf-8'))
    english = {row['key'].lower().strip(): row['text'] for row in source}
    extra = json.loads((ROOT / 'translations/raw-keys.json').read_text(encoding='utf-8')) \
        if (ROOT / 'translations/raw-keys.json').exists() else {}
    problems = []
    for key, value in terms.items():
        norm = key.lower().strip()
        original = english.get(norm, extra.get(key))
        if original is None:
            problems.append(f'{key}: nie ma takiego klucza w grze')
            continue
        if '\t' in value or '\n' in value or '\r' in value:
            problems.append(f'{key}: tabulator albo koniec linii w tekście (gra łamie wiersze przez <br>)')
        if tokens(original) != tokens(value):
            problems.append(f'{key}: wstawki {tokens(original)} != {tokens(value)}')
    if problems:
        raise SystemExit('en-pl-review.json ma błędy:\n  ' + '\n  '.join(problems))
    return {'game_keys': len(english), 'translated': sum(1 for k in terms if k.lower().strip() in english)}


def write_terms(terms: dict[str, str], destination: Path) -> int:
    lines = [f'{key}\t{value}' for key, value in terms.items()]
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
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z CyberHook.exe)')
    args = parser.parse_args()

    terms = polish_by_key(ROOT)
    stats = check(terms)

    work = ROOT / 'work' / 'plugin'
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    entries = write_terms(terms, work / 'pl.tsv')
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
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
