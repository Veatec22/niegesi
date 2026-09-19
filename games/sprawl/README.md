# SPRAWL PL

*Part of [Nie gęsi](../../README.md) — Polish translations of games that never got one.*

An unofficial Polish translation of **SPRAWL**. Work in progress: 75 of 717 entries, the menu and the HUD, built to prove the pipeline end to end before the rest of the text follows.

## How it works

SPRAWL is Unreal Engine 4.27, and unlike the other games here it needs no surgery at all. Its text lives where Unreal puts text — one compiled resource per culture:

```
Sprawl/Content/Localization/Game/<culture>/Game.locres
```

Eleven cultures shipped: de, en, es-ES, fr, it, ja, ko, pt-BR, tr, uk, zh-Hans. Polish did not — but the project's own `Game.locmeta` lists **32** target cultures, and `pl` is among them. As with the other three games in this repository, the slot was planned and never filled.

There is **no language selector in the build**. Strings for one exist in the resource (eleven language names, two entries each) but no menu reaches them, and nothing in the game's saves or configs records a language. The engine simply asks the operating system. So on a Polish Windows the game already requests culture `pl`, finds nothing, and falls back to English — which means the entire translation is one file appearing in the right place. `-culture=pl` on the command line forces it on any system.

A culture's resource does not have to be complete: whatever it leaves out falls back to the native one. The game's own Ukrainian file carries 671 of English's 717 keys, which is what makes shipping a partial translation safe, and what this work-in-progress relies on.

## Who the files are for

| Audience | Files | Use |
| --- | --- | --- |
| Game developer | [`translations/en-pl-review.json`](translations/en-pl-review.json) | Every entry with its namespace, key, English source and Polish translation. 693 of the 717 keys are readable String Table names — `LEVEL_E2M1_NAME`, `E1M5_PAIN`, `BERSERKER` — so the file maps straight back onto the project. |
| Players | The built `Game.locres` | One file, a few kilobytes. See [INSTALL.txt](docs/INSTALL.txt). |
| Translation contributors | [`translations/pl.json`](translations/pl.json), [`tools/build.py`](tools/build.py) | Editing the strings and rebuilding. |

## Building

Requirements: Python 3.11 and the game's own `en/Game.locres`, which lives inside `Sprawl-WindowsNoEditor.pak`. The pak's index is not encrypted, but its entries are Oodle-compressed and SPRAWL links Oodle statically, so extracting it needs a tool that carries its own decompressor — [FModel](https://fmodel.app/) with UE version `GAME_UE4_27`, *Export Folder → Raw Data*. Put the result at `translations/en.locres`; it is a game asset and is not tracked by Git.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe games\sprawl\tools\extract.py
.venv\Scripts\python.exe games\sprawl\tools\build.py
```

`extract.py` refreshes the review file from the source; `build.py` writes `dist/Sprawl/Content/Localization/Game/pl/Game.locres`. The source resource is pinned by SHA-256 in [`tools/build.py`](tools/build.py); any other version is refused and nothing is written.

## Verification

`.locres` version 3 stores a checksum for every namespace, key and source string, computed by a function of Unreal's own. Rather than guess at it, [`tools/locres.py`](tools/locres.py) never computes a hash: a translation is built from the English resource and carries its hashes through unchanged, which every key being translated already has.

That this is faithful is not an argument but a test — **re-serializing the game's own `en/Game.locres` and `uk/Game.locres` returns both files byte for byte**, 124 065 and 187 293 bytes. The writer is proven against two real shipped resources before it writes anything of ours.

The build then checks itself: every translated key exists in the English resource, the rebuilt file reads back exactly as written, and every namespace hash, key hash and source hash matches the English original it came from.

## Testing status

The 75 menu and HUD entries are built and installed as a loose file. What is not yet confirmed: whether a shipping build picks up a loose `.locres` at all, or whether the file has to be delivered inside a `_P.pak` mounted over the original. That is the point of this slice.

## Game material

This directory contains translation text and tooling only — no executables, no game assets. The extracted `en.locres` stays out of Git. Nothing here is affiliated with or endorsed by Maete Interactive or Rogue Games; *SPRAWL*, its text and its characters belong to their authors.

## License

[MIT](../../LICENSE), same as the rest of the repository.
