"""Test autora: skopiuj zbudowany mod do gry albo go usuń.

Mod to nowy folder w StreamingAssets/mods — żaden plik gry nie jest nadpisywany,
więc zamiast kopii zapasowej wystarcza usunięcie folderu (--remove). Włączenie moda
w menu REMIX i wybór języka zostają po stronie gracza, tak jak w instrukcji.

    .venv\\Scripts\\python.exe games\\rain-world\\tools\\install.py [--game ...] [--remove]
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rw  # noqa: E402
from build import MOD_ID, ROOT  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, default=rw.DEFAULT_GAME)
    parser.add_argument('--remove', action='store_true')
    args = parser.parse_args()

    target = rw.streaming(args.game) / 'mods' / MOD_ID
    if target.exists():
        shutil.rmtree(target)
    if args.remove:
        print(f'Usunięto {target}')
        return 0
    source = ROOT / 'dist' / MOD_ID
    if not source.exists():
        raise SystemExit('Brak dist/niegesi-polski — uruchom najpierw tools/build.py.')
    shutil.copytree(source, target)
    print(f'Zainstalowano {target}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
