"""Zbuduj spolszczenie Rain World jako mod Remix: plugin + polskie teksty.

Kompiluje plugin (plugin/Plugin.cs) na bibliotekach z instalacji gry, zamienia
pl.json na pliki text/text_pol/ w formacie gry i składa ZIP do wypakowania
w katalogu gry. Paczka zawiera wyłącznie folder moda i instrukcję — BepInEx gra
ma własny, a plików gry nie ruszamy. Nie pisze niczego poza dist/ i work/.

    .venv\\Scripts\\python.exe games\\rain-world\\tools\\build.py [--game "C:\\Games\\Rain World"]
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rw  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
VERSION = '0.2.0'
MOD_ID = 'notgeese-polski'
MOD_PATH = f'{rw.DATA}/StreamingAssets/mods/{MOD_ID}'
PACKAGE = f'Rain-World-PL-{VERSION}.zip'
DLL = 'notgeeseRainWorld.dll'

COMPILERS = [
    Path(r'C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/Roslyn/csc.exe'),
    Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'),
]
GAME_REFERENCES = ['mscorlib.dll', 'System.dll', 'System.Core.dll', 'UnityEngine.dll',
                   'UnityEngine.CoreModule.dll', 'Assembly-CSharp.dll', 'Assembly-CSharp-firstpass.dll']
BEPINEX_REFERENCES = ['BepInEx.dll', '0Harmony.dll']

# Znaczniki, które gra podstawia albo interpretuje — muszą przejść do tłumaczenia bez zmian.
PLACEHOLDER = re.compile(r'<(?!LINE>)(?:[A-Za-z_][A-Za-z0-9_]*|[A-Z][A-Z_ ]*)>|\{[A-Za-z0-9_]*\}')

MODINFO = {
    'id': MOD_ID,
    'name': 'Polski (Not Geese)',
    'version': VERSION,
    'authors': 'Not Geese',
    'description': 'Spolszczenie Rain World. Dodaje język POLSKI w Opcje > Język. '
                   'Nie podmienia plików gry; teksty bez tłumaczenia zostają po angielsku.',
    'requirements': [],
    'requirements_names': [],
    'tags': [],
    'checksum_override_version': False,
}


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def compile_plugin(game: Path, output: Path) -> None:
    references = []
    for name in GAME_REFERENCES:
        path = game / rw.DATA / 'Managed' / name
        if not path.exists():
            raise SystemExit(f'Brak {path} — czy to na pewno katalog gry?')
        references.append(f'/r:{path}')
    for name in BEPINEX_REFERENCES:
        # Gra ma własnego BepInEksa; plugin wiąże się z tym, który gracz już ma.
        path = game / 'BepInEx' / 'core' / name
        if not path.exists():
            raise SystemExit(f'Brak {path} — Rain World bez wbudowanego BepInEksa? (wymaga wersji 1.9+)')
        references.append(f'/r:{path}')
    command = [str(compiler()), '/nologo', '/noconfig', '/nostdlib+', '/optimize+', '/warn:4',
               '/target:library', f'/out:{output}', *references, str(ROOT / 'plugin' / 'Plugin.cs')]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if result.returncode != 0:
        print(result.stdout or '', result.stderr or '', sep='\n')
        raise SystemExit('Kompilacja pluginu nie powiodła się.')


def check(key: str, english: str, polish: str, problems: list[str]) -> None:
    if sorted(PLACEHOLDER.findall(english)) != sorted(PLACEHOLDER.findall(polish)):
        problems.append(f'{key}: znaczniki {PLACEHOLDER.findall(english)} -> {PLACEHOLDER.findall(polish)}')
    if '\n' in polish or '\r' in polish:
        problems.append(f'{key}: znak nowej linii (w grze łamanie to <LINE>)')
    if key.startswith('str:') and '|' in polish:
        problems.append(f'{key}: znak | rozbiłby wpis strings.txt')


def write_strings(folder: Path, polish: dict[str, str], english: dict[str, dict], problems: list[str]) -> int:
    lines = []
    for key, text in polish.items():
        if not key.startswith('str:'):
            continue
        k = key[4:]
        if '|' in k or not text:
            problems.append(f'{key}: pusty tekst albo | w kluczu')
            continue
        source = english.get(key, {}).get('english', k)
        check(key, source, text, problems)
        lines.append(f'{k}|{text}')
    # Pierwszy znak 0 = plik niezaszyfrowany (gra go zdejmuje przed parsowaniem).
    (folder / 'strings.txt').write_text('0' + '\r\n'.join(lines), encoding='utf-8', newline='')
    return len(lines)


def write_dialogue(game: Path, folder: Path, polish: dict[str, str], problems: list[str]) -> tuple[int, int]:
    key = None
    files = lines_done = 0
    for source in rw.SOURCES:
        for path in rw.dialogue_files(game, source):
            wanted = {k for k in polish if k.startswith(f'dlg:{path.name}#')}
            if not wanted:
                continue
            key = key or rw.encryption_string(game)
            text, parsed = rw.read_dialogue(path, key)
            raw = text.split('\r\n')
            for line in parsed:
                entry = f'dlg:{path.name}#{line.index}'
                if entry in polish:
                    check(entry, line.text, polish[entry], problems)
                    raw[line.index] = line.prefix + polish[entry] + line.suffix
                    lines_done += 1
            # Nagłówek „0-N…” zaczyna się od 0, więc gra czyta plik jako otwarty tekst.
            (folder / path.name).write_text('\r\n'.join(raw), encoding='utf-8', newline='')
            files += 1
    return files, lines_done


def package(stage: Path) -> Path:
    out = ROOT / 'dist' / PACKAGE
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(stage.rglob('*')):
            if path.is_file():
                archive.write(path, f'{MOD_PATH}/{path.relative_to(stage).as_posix()}')
        archive.write(ROOT / 'docs' / 'INSTALL.txt', 'READ-ME.txt')

    with zipfile.ZipFile(out) as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        # Paczka nie niesie zawartości gry: wszystko poza instrukcją leży w naszym folderze moda.
        stray = [n for n in names if n != 'READ-ME.txt' and not n.startswith(MOD_PATH + '/')]
        assert not stray, f'pliki poza folderem moda: {stray}'
        assert f'{MOD_PATH}/plugins/{DLL}' in names
        assert f'{MOD_PATH}/text/text_pol/strings.txt' in names
        assert f'{MOD_PATH}/modinfo.json' in names
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, default=rw.DEFAULT_GAME)
    args = parser.parse_args()
    game = args.game.resolve()

    polish = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    english_path = ROOT / 'work' / 'en.json'
    if not english_path.exists():
        raise SystemExit('Brak work/en.json — uruchom najpierw tools/extract.py.')
    english = json.loads(english_path.read_text(encoding='utf-8'))
    unknown = [k for k in polish if k not in english and k != 'str:POLISH']
    if unknown:
        print('Klucze spoza gry (literówka albo zmiana wersji):', unknown[:10])

    stage = ROOT / 'dist' / MOD_ID
    if stage.exists():
        shutil.rmtree(stage)
    text = stage / 'text' / 'text_pol'
    text.mkdir(parents=True)
    (stage / 'plugins').mkdir()

    problems: list[str] = []
    strings = write_strings(text, polish, english, problems)
    files, lines = write_dialogue(game, text, polish, problems)
    if problems:
        print('\n'.join(problems))
        raise SystemExit(f'{len(problems)} problemów w tłumaczeniu — paczka nie powstała.')

    compile_plugin(game, stage / 'plugins' / DLL)
    (stage / 'modinfo.json').write_text(json.dumps(MODINFO, ensure_ascii=False, indent='\t'), encoding='utf-8')
    shutil.copyfile(REPO / 'LICENSE', stage / 'LICENSE-notgeese.txt')

    archive = package(stage)
    total = len(english)
    done = sum(1 for k in polish if k in english)
    print(json.dumps({
        'version': VERSION,
        'strings': strings,
        'dialogue_files': files,
        'dialogue_lines': lines,
        'entries': {'done': done, 'total': total},
        'plugin_bytes': (stage / 'plugins' / DLL).stat().st_size,
        'package': str(archive),
        'package_bytes': archive.stat().st_size,
        'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest()[:16],
    }, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
