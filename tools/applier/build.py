"""Buduje NieGesiPatch.exe — aplikator łatek dokładany do paczek deltowych.

Wynik trafia do `tools/applier/bin/` (ignorowane przez Gita). `tools/patch.py release`
woła ten skrypt sam, gdy pliku .exe brakuje albo jest starszy od źródła.

    .venv\\Scripts\\python.exe tools\\applier\\build.py
"""

from __future__ import annotations

import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'NieGesiPatch.cs'
OUT = HERE / 'bin' / 'NieGesiPatch.exe'

COMPILERS = [
    Path(r'C:/Program Files/Microsoft Visual Studio/2022/Community/MSBuild/Current/Bin/Roslyn/csc.exe'),
    Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe'),
]
FRAMEWORK = Path(r'C:/Windows/Microsoft.NET/Framework64/v4.0.30319')


def compiler() -> Path:
    for candidate in COMPILERS:
        if candidate.exists():
            return candidate
    raise SystemExit('Nie znalazłem kompilatora C# (csc.exe).')


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    command = [
        str(compiler()),
        '/nologo',
        '/target:exe',
        '/platform:anycpu',
        '/optimize+',
        '/langversion:5',
        '/codepage:65001',
        f'/r:{FRAMEWORK / "System.Windows.Forms.dll"}',
        f'/out:{OUT}',
        str(SOURCE),
    ]
    subprocess.run(command, check=True)
    print(f'{OUT} ({OUT.stat().st_size} B)')


if __name__ == '__main__':
    main()
