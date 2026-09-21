# My Friend Pedro PL — full translation 0.2

Separate Polish (`pl`) language, **721/721 I2 entries**: dialogue, menus, tutorials,
enemy barks, HUD, results, modifiers, achievement strings and credits. Names, key
labels and deliberate gaming abbreviations may match English. All original ten
languages are preserved. No executable or assembly is modified. Voice recordings,
image text and achievement descriptions in the GOG/Steam client are outside scope.

## Status and review

The user confirmed the vertical works in-game (selector, persistence, glyphs and
opening gameplay) and authorized the full translation. Full campaign visual QA is
still pending. Agents never launch the game.

- [Searchable EN/PL review](translations/en-pl-review.html)
- [EN/PL JSON](translations/en-pl-review.json)
- [Polish source](translations/pl.json)
- [Terminology and review notes](translations/REVIEW.md)

## Build

Supported source: local GOG installation, Unity 2017.4.19f1. resources.assets SHA-256:
`4a81ed99cd1e8e5e4665bde87b80d4bd551bf95c088c1b3a80ed2ecfbb9764fd`.

```powershell
.venv\Scripts\python.exe games\my-friend-pedro\tools\build.py --original "<original resources.assets>" --extract
.venv\Scripts\python.exe games\my-friend-pedro\tools\build.py --original "<original resources.assets>"
```

After installation use `backups/my-friend-pedro/resources.assets` as the original.
Build never installs or launches the game. Output is under dist/: the asset and
My-Friend-Pedro-PL-0.2.zip. After --extract, run tools/review.py to refresh HTML.

The I2 LanguageSource is resources.assets object 2279. The parser differs from
Shotgun Cop Man: languages precede terms. The build pins the original checksum,
checks a binary round trip, validates review and translation tokens, adds Polish
and reopens the saved asset to prove only object 2279 changed and original language
columns are intact. OptionsMenuScript builds its selector from GetAllLanguages.

Basic Noto fonts have all Polish glyphs; actual fonts/atlases and rendering must
still be verified visually. No claim that all UI uses these specific font assets.

## Installation and remaining QA

See [INSTALL.txt](docs/INSTALL.txt). Original: `backups/my-friend-pedro/resources.assets`.
Confirmed vertical backup: `backups/my-friend-pedro-vertical/resources.assets`.
Paths are relative to the repository root. No saves are changed.

The build validates complete coverage, review sync, all button/animation tokens and
dialogue boundaries, original language preservation and every other asset object.
The ZIP is reopened and checked against the generated asset.

Next user checks: longer dialogues, modifiers, difficulty descriptions and level
result screens. Report clipped text or incorrect translations with a screen/key.
The user already confirmed the vertical; no repeated approval is required.

[Technical research](../../docs/research/2026-09-20-kandydaci-technika.md),
[web sources](../../docs/research/2026-09-20-kandydaci-zrodla.md).
