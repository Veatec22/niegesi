# Shotgun Cop Man PL

*Part of [Nie gęsi](../../README.md) — Polish translations of games that never got one.*

> — Stój, Szatanie! Jesteś aresztowany!  
> — Pierdol się, Shotgun Cop Man!

An unofficial Polish translation of **Shotgun Cop Man**.

It adds **Polish (`pl`) as an eleventh language**. It covers all 485 entries of the localization table found in the game: menus, controls, tutorial, dialogue, level editor, in-game achievements and Pedro's lines.

## Who the files are for

| Audience | Files | Use |
| --- | --- | --- |
| Game developer | [`translations/pl.json`](translations/pl.json), [`translations/en-pl-review.json`](translations/en-pl-review.json) | Adding Polish to the Unity/I2 project. The JSON files are keyed by term ID and have to be mapped into the project; they are not claimed to be a ready-made I2 import format. |
| Players and testers | The built `Shotgun Cop Man_Data` folder | Drag and drop over the game folder. See [INSTALL.txt](docs/INSTALL.txt). Build it yourself as below — there is no prebuilt download at the moment. |
| Translation contributors | [`translations/pl.json`](translations/pl.json), [`tools/build.py`](tools/build.py) | Editing the strings and rebuilding the package from your own original game file. |

## Building the package

Requirements: Python 3.11 and the original `resources.assets` from a supported version of the game. The tool installs nothing into the game and never starts it. The virtual environment lives at the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe games\shotgun-cop-man\tools\build.py --original "D:\Backup\Shotgun Cop Man_Data\resources.assets"
```

Output: `games/shotgun-cop-man/dist/Shotgun Cop Man_Data/resources.assets` and `dist/Shotgun-Cop-Man-PL-0.1.zip`. The `dist` directory is not tracked by Git. Pass `--output` to put it elsewhere.

The tool accepts exactly one original file — the `resources.assets` of the supported game build, pinned by SHA-256 in [`tools/build.py`](tools/build.py) — and refuses any other version, including an already modified one. A mismatch prints the expected checksum and writes nothing. Do not run it with Python's `-O` flag. After a game update the compatibility has to be analysed again — bumping the checksum is not enough.

The build verifies that all 4850 original translations are preserved, that 485 Polish strings, their flags and the language record are appended, that the remaining asset objects are untouched, and that the ZIP is valid. Strings are edited in `pl.json`; the matching entries in `en-pl-review.json` have to be updated alongside them.

## Installing

The built package contains a `Shotgun Cop Man_Data` folder with `resources.assets`, plus `READ-ME.txt`.

1. Close the game and keep a copy of the original `Shotgun Cop Man_Data/resources.assets`.
2. Drag the `Shotgun Cop Man_Data` folder into the game folder and confirm the overwrite.
3. Start the game, choose **Options → Language → Polski** and apply.

Restore and compatibility instructions: [INSTALL.txt](docs/INSTALL.txt).

## Testing status

Structurally verified against the original: 4850 existing strings preserved, 485 Polish ones added, the rest of the asset untouched. In-game testing is still open — selecting the new language and having it remembered, and the new dialogue, tutorial, editor and Pedro text. Recorded voices and the achievement descriptions shown by the Steam client are not changed.

## Game material

This directory contains translation text and tooling only — no executables, no game assets. Nothing here is affiliated with or endorsed by the game's authors; *Shotgun Cop Man*, its text and its characters belong to them. The released package is only usable together with a legally owned copy of the game.

## License

[MIT](../../LICENSE), same as the rest of the repository.
