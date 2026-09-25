"""Test install of the built package into the local game, or its removal. Never starts the game.

The package only adds files. Install refuses to overwrite a file it did not put there
itself (another mod, a different BepInEx); the receipt in backups/cyber-hook lists every
added file with its SHA-256, and --restore removes exactly those files if unchanged.
Folders and logs that BepInEx creates at runtime (config, cache, LogOutput.log) remain.

    .venv\\Scripts\\python.exe games\\cyber-hook\\tools\\install_local.py --game "C:\\Games\\CyberHook_GOG"
    .venv\\Scripts\\python.exe games\\cyber-hook\\tools\\install_local.py --game "..." --restore
"""
import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
EXE = 'CyberHook.exe'
RECEIPT = REPO / 'backups' / 'cyber-hook' / 'install-receipt.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def target(game, name):
    path = (game / name).resolve()
    assert path.is_relative_to(game) and path != game, name
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--game', type=Path, required=True)
    ap.add_argument('--package', type=Path, help='domyślnie najnowszy ZIP z dist/')
    ap.add_argument('--restore', action='store_true')
    args = ap.parse_args()
    game = args.game.resolve()
    assert (game / EXE).is_file(), 'To nie jest katalog gry'
    running = subprocess.run(['tasklist', '/FI', f'IMAGENAME eq {EXE}', '/FO', 'CSV', '/NH'], capture_output=True).stdout
    if EXE.encode() in running:
        raise SystemExit('Zamknij grę. Narzędzie nie zatrzymuje ani nie uruchamia gry.')
    previous = json.loads(RECEIPT.read_text(encoding='utf-8')) if RECEIPT.exists() else None
    if previous:
        assert previous['game'] == str(game), 'Pokwitowanie dotyczy innej instalacji'

    if args.restore:
        assert previous and not previous.get('restored'), 'Brak aktywnej instalacji'
        for row in previous['files']:
            path = target(game, row['path'])
            if path.exists():
                assert sha(path.read_bytes()) == row['sha256'], 'Zmieniony po instalacji: ' + row['path']
        for row in previous['files']:
            path = target(game, row['path'])
            if path.exists():
                path.unlink()
        previous['restored'] = True
        RECEIPT.write_text(json.dumps(previous, indent=2) + '\n', encoding='utf-8')
        print('Usunięto pliki paczki. Zostały katalogi i logi utworzone przez BepInEx.')
        return

    package = args.package or max((ROOT / 'dist').glob('Cyber-Hook-PL-*.zip'), key=lambda p: p.stat().st_mtime)
    owned = {r['path']: r['sha256'] for r in previous['files']} if previous and not previous.get('restored') else {}
    with zipfile.ZipFile(package) as archive:
        contents = {n: archive.read(n) for n in archive.namelist() if not n.endswith('/')}
    for name in contents:
        path = target(game, name)
        if path.exists() and (name not in owned or sha(path.read_bytes()) != owned[name]):
            raise SystemExit('Plik nie pochodzi z naszej instalacji, nie nadpisuję: ' + name)
    rows = []
    for name, data in contents.items():
        path = target(game, name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        assert sha(path.read_bytes()) == sha(data)
        rows.append({'path': name, 'sha256': sha(data)})
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps({'game': str(game), 'package': package.name, 'package_sha256': sha(package.read_bytes()),
                                   'files': rows, 'restored': False}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'installed': len(rows), 'package': package.name, 'receipt': str(RECEIPT)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
