# My Friend Pedro — technika

Ustalenia i instrukcje dla osób, które budują paczkę albo poprawiają teksty.
Gracz potrzebuje tylko [README](../README.md).

## Pilotaż kierunku i review — 2026-09-24

Uzupełniamy proces redakcyjny na istniejącym pełnym przekładzie. Vertical jest już
potwierdzony przez użytkownika; nie wymaga ponownej akceptacji. Aktualne wydanie
0.3.1 korzysta z pluginu, zgodnie z `game.yaml`; opis podmiany zasobów poniżej jest historyczny.

Sprawdzono zgodność 721 wpisów EN/PL z `translations/pl.json` (brak rozjazdów).
Przygotowano 19 wpisów próbki oraz trzy tematy kierunku w
[translation-decisions.md](translation-decisions.md): głos Pedra, adaptacja sucharów
i nazwy osiągnięć. Użytkownik zaakceptował wszystkie trzy rekomendacje. Zapisano
biblię i zmieniono `w102-18`, `w410-1`, `achN4` oraz błąd sensu `w102-14`.

Osobny reviewer zakończył odczyt 721/721 wpisów, ponownie czytając polskie dialogi
i oceniając decyzje na całej grze. [Raport](localization-review.md) zawiera pokrycie,
hashe wejścia, dwie poprawki i trzy otwarte propozycje. Prowadzący potwierdził i wdrożył
`w54-1` (obwód) oraz `w57-4` (bez dopisanych lat rozłąki). Łącznie zmieniono sześć wpisów
względem 0.3. Pełna kampania i nowe teksty 0.3.1 nadal czekają na test użytkownika.

Paczka `dist/My-Friend-Pedro-PL-0.3.1.zip` (661725 B) zbudowana i skopiowana do
`site/public/pobierz/`; `game.yaml` wskazuje nowy plik. Sprawdzono kompletność
BepInEx, zgodność jego plików z oficjalnym ZIP-em, obecność licencji i źródeł obok
paczki oraz zgodność wszystkich 721 wpisów TSV z JSON-ami. Nie instalowano 0.3.1.
Raport po oznaczeniu uzasadnionych wyjątków w biblii zostawia 18 ostrzeżeń długości;
nie są to potwierdzone błędy UI. Trzy propozycje redakcyjne czekają na rozmowę.

## Aktualne budowanie pluginu

```powershell
.venv/Scripts/python.exe games/my-friend-pedro/tools/review.py
.venv/Scripts/python.exe games/my-friend-pedro/tools/build_plugin.py --game "C:/Games/My Friend Pedro"
```

`build_plugin.py` kompiluje plugin i pakuje teksty TSV, BepInEx oraz instrukcję
`docs/INSTALL-plugin.txt`. Nie podmienia zasobów gry ani nie instaluje wyniku.
Źródła konkretnej wersji BepInEx leżą obok ZIP-a. Poniższy `build.py` opisuje
historyczną metodę zasobową; jego parser i walidator mogą nadal służyć do porównań
z oryginalnym `resources.assets`, ale nie używamy go do wydawania paczki.

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „My Friend Pedro PL — full translation 0.2”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

Separate Polish (`pl`) language, **721/721 I2 entries**: dialogue, menus, tutorials,
enemy barks, HUD, results, modifiers, achievement strings and credits. Names, key
labels and deliberate gaming abbreviations may match English. All original ten
languages are preserved. No executable or assembly is modified. Voice recordings,
image text and achievement descriptions in the GOG/Steam client are outside scope.

### Status and review

The user confirmed the vertical works in-game (selector, persistence, glyphs and
opening gameplay) and authorized the full translation. Full campaign visual QA is
still pending. Agents never launch the game.

- [Searchable EN/PL review](../translations/en-pl-review.html)
- [EN/PL JSON](../translations/en-pl-review.json)
- [Polish source](../translations/pl.json)
- [Terminology and review notes](../translations/REVIEW.md)

### Build

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

### Installation and remaining QA

See [INSTALL.txt](../docs/INSTALL.txt). Original: `backups/my-friend-pedro/resources.assets`.
Confirmed vertical backup: `backups/my-friend-pedro-vertical/resources.assets`.
Paths are relative to the repository root. No saves are changed.

The build validates complete coverage, review sync, all button/animation tokens and
dialogue boundaries, original language preservation and every other asset object.
The ZIP is reopened and checked against the generated asset.

Next user checks: longer dialogues, modifiers, difficulty descriptions and level
result screens. Report clipped text or incorrect translations with a screen/key.
The user already confirmed the vertical; no repeated approval is required.

[Technical research](../../../temp/research/2026-09-20-kandydaci-technika.md),
[web sources](../../../temp/research/2026-09-20-kandydaci-zrodla.md).
