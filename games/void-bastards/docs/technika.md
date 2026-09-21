# Void Bastards — technika i stan prac

21 września 2026. **Pełne tłumaczenie 0.2.0: 2480/2480 wpisów, zbudowane i zainstalowane lokalnie.**
Vertical (selektor, menu, komiks, polskie litery składane w czasie gry) potwierdzony
przez użytkownika na 0.1.1. Pełne przejście czeka. Gry nie uruchamiano.
Paczka `dist/Void-Bastards-PL-0.2.0.zip` leży też w `site/public/pobierz/`;
w `games/catalog.yaml` gra jest na liście **testowe**.

## Istniejące spolszczenia

Nie znaleziono dostępnego spolszczenia ani fanowskiego tłumaczenia. Sprawdzono
wyszukiwania po polsku i angielsku (m.in. Graj po polsku, Steam, ModDB).
Sklep Steam (API `appdetails`) wymienia: English, French, German, Spanish,
Japanese, Korean, Portuguese-Brazil, Russian, Simplified Chinese — bez polskiego.

## Lokalna kopia

- `C:/SteamLibrary/steamapps/common/Void Bastards`, Steam app 857980, buildid 4269398.
- `PlayerSettings.bundleVersion` = **2.0.24**, Unity **2017.4.21f1**, **Mono** (katalog `Managed`).
- `mscorlib.dll` zawiera `GetPEKind` — brak okrojenia opisanego w AGENTS.md; BepInEx 5 powinien wstać.

## Teksty

**I2 Localization** wkompilowane w `Assembly-CSharp.dll` (jak w Shotgun Cop Man).
Tabela `I2Languages`: `resources.assets`, path_id 14623.

- 2483 terminy, 2479 niepustych, 69 674 znaków EN.
- 9 języków: en-US, de-DE, fr-FR, es-ES, zh-CN, ko, ja, ru, pt-BR. Brak PL.
- Starszy układ I2 z polem **Description** — 227 terminów ma notatkę kontekstową
  od twórców (np. o liczbie mnogiej). Trafia do review jako `context`.
- Znaczniki: `{[x]}` (parametry I2), `<b>`, `<size>`, `%d`. Kilka zdań składanych
  z liczbą doklejaną w kodzie — pułapka odmiany liczebników.
- Kategorie: Dialog 174, Key 141, Part 122, Star Map 112, CS 103, Interact 94,
  UpgradeDescription 93×2, Star Map Event 92, Achievement 72, Junk 72 i inne.

`tools/analyze.py --game <katalog gry>` zapisuje review, `work/analysis.json`
i tabele innych języków `work/ref-<kod>.json` (poza gitem).

## Menu języków

`LanguageScreen.onEnter` bierze listę z `LocalizationManager.GetAllLanguages()`,
a `draw` pokazuje nazwę z terminu `Language/<nazwa>`. Nowy język w tabeli I2
powinien więc sam pojawić się w menu — wystarczy dodać termin `Language/Polish`.

## Fonty — główna niewiadoma

Własny interfejs `FUI` rysuje fontami Unity (TTF). Pliki TTF z polskimi znakami:
SequentialistBB (reg/bold/boldital), NotoSans-Condensed, NotoSans-ExtraCondensedBold, Arial.
Brak w Falsescript i CJK. Statyczne atlasy TextMeshPro (stara wersja TMP
wkompilowana w grę, bez atlasów dynamicznych) według wstępnej heurystyki
nie mają polskich liter. Do ustalenia w verticalu, które ekrany używają TMP
i czy potrzebny jest fallback.

`SwitchFontByLanguage` przełącza obiekty według `CurrentLanguage.Contains(...)` —
dla polskiego zostanie obiekt domyślny (łaciński).

## Werdykt

Warto. Droga taka jak w Shotgun Cop Man: plugin BepInEx 5 dopisuje polski
do tabeli I2 w pamięci, bez podmiany plików. Niepewne: pokrycie polskich znaków
w atlasach TMP i napisy na teksturach (komiksowy styl gry).

## Vertical 0.1

- `plugin/Plugin.cs` — wzór z Shotgun Cop Man: Harmony na `LocalizationManager.AddSource`
  i `InitializeIfNeeded`, `AddLanguage("Polish", "pl")`, wypełnienie z `pl.tsv`.
  Dodaje brakujący termin `Language/Polish` = „Polski” (podpis w menu języków).
- Diagnostyka: po przełączeniu na polski plugin wypisuje do `BepInEx/LogOutput.log`
  każdy font (Unity `Font` i `TMP_FontAsset`) z listą brakujących polskich liter.
  To ma rozstrzygnąć niewiadomą fontów faktami, nie tylko screenami.
- Build: `tools/build_plugin.py --game <katalog>` (kompilacja na bibliotekach gry,
  profil .NET 3.5), paczka `dist/Void-Bastards-PL-0.1.zip` z BepInEx 5.4.23.5.
- Instalacja testowa: `tools/install_local.py --game <katalog>` z pokwitowaniem
  w `backups/void-bastards/`; `--restore` usuwa dokładnie dodane pliki.
- Tłumaczenie według skilla `lokalizacja`: `translations/biblia.yaml`
  (B.A.C.S. — mężczyzna, głos Kevana Brightinga; płeć gracza losowa, więc do gracza
  i w jego kwestiach formy bezrodzajowe). Raport kontrolny czysty poza „Synchronizacja
  pionowa” (ryzyko długości).

## Test 0.1 i poprawka 0.1.1 — polskie litery w TextMeshPro

Test użytkownika 0.1: „Polski” jest w menu języków i działa, log ma
„Polski dodany jako język 10 z 10: 204 tekstów”. Menu pokazuje jednak kwadraty
zamiast „Ź” i „Ę” (WYJDŹ, JĘZYK). Raport fontów się nie wykonał — `Update` pluginu
nie był wołany (obiekt BepInEksa w tej grze nie dostaje klatek).

Przyczyna: `FUI` rysuje tekst przez komponenty TextMeshPro (`buttonLabelFont` itd.
to `TextMeshPro`), a statyczne atlasy SDF nie mają polskich liter. Stary TMP w grze
nie generuje glifów w locie. FUI rysuje też `subMeshes`, czyli glify z fontów zapasowych.

0.1.1 (`plugin/PolishGlyphs.cs`): dla każdego `TMP_FontAsset` bez polskich liter
plugin kopiuje przez RenderTexture atlas tego fontu, bierze glif bazowy (E, Z, L, a…)
i dorysowuje znak diakrytyczny jako pole odległości (ogonek, kreska, kropka,
przekreślenie; grubość mierzona z „I”/„l” tego fontu). Z takich liter powstaje mały
atlas i `TMP_FontAsset`, wpięty jako pierwszy w `fallbackFontAssets` oryginału.
Krój pozostaje ten sam, do paczki nie trafia żaden font ani atlas.
Uruchomienie: łatka na setter `LocalizationManager.CurrentLanguage`, po dodaniu
języka i po każdym `sceneLoaded`. W logu: „Font TMP „…”: złożono …”.

Niepewne do testu: położenie i proporcje znaków diakrytycznych w poszczególnych
fontach, zgodność układu y glifów ze starym TMP (y liczone od góry atlasu).

Test 0.1.1 (użytkownik): polskie litery w menu i komiksie wyświetlają się poprawnie.
Jedyny brak: dolny cudzysłów „ w foncie komiksu. 0.1.2 składa „ z ” (i ‚ z ’)
przesuniętego na linię bazową.

## Pełne tłumaczenie — 0.2.0

Tłumaczenie partiami przez `work/batch.py` (`show <prefiks>` wypisuje brakujące wpisy
z kontekstem twórców, `put <plik.tsv>` dopisuje i pilnuje liczby nowych linii).
Standard: skill `lokalizacja`, biblia `translations/biblia.yaml`, decyzje
`docs/decyzje-tlumaczenia.md`, raport `work/l10n-report.md` (czysty poza 18
zgłoszeniami długości do obejrzenia w grze).

Plugin 0.2.0 = 0.1.2 bez zmian w kodzie; `PolishGlyphs.cs` składa też „ z ” (0.1.2).

## Następny krok

Test pełnej wersji: warsztat (nazwy części i ulepszeń), mapa gwiezdna (zdarzenia,
cechy statków), profil postaci (cechy, wykroczenia), rozmowy piratów.
