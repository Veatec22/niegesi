# Cyber Hook — ustalenia techniczne

## Stan

- **Etap:** pełne tłumaczenie 0.2.0 — 686/686 wpisów CSV + 16 kwestii samouczka
  z kluczem będącym tekstem (`translations/raw-keys.json`). Paczka w `dist/`
  i `site/public/pobierz/`, zainstalowana lokalnie. Vertical 0.1.1 potwierdzony w grze.
- **Następny krok:** test dalszych światów, zakończenia i DLC (lista w
  `docs/translation-decisions.md`, sekcja „Mniej pewne”), potem akceptacja lub poprawki.
- Trzy klucze DLC (`dialog_dlc_boss_intro_01_00`, `01_01`, `02_00`) nie mają wpisu
  w CSV żadnego języka — gra pokazuje nazwę klucza także po angielsku. Nie tłumaczymy.

## Istniejące spolszczenia

Gra oficjalnie ma EN, FR, DE, ES, RU, PT-BR, ZH (w plikach jest też JP). Nie znalazłem
dostępnego polskiego spolszczenia ani innych fanowskich tłumaczeń (Steam, GOG,
wyszukiwarki, 2026-09-23).

## Gra

- GOG 1.2.1, build `55931336877424935`, `C:\Games\CyberHook_GOG`.
- Unity 2019.4.28f1, Mono, x64. Kod gry w `GlobalAssembly.dll` (asmdef), nie w
  `Assembly-CSharp.dll`.
- `mscorlib.dll` pełny: jest `GetPEKind`, `AmbiguousMatchException` ma 4 konstruktory
  → BepInEx 5 i Harmony wstają.
- Zasoby: `data.unity3d` (jeden bundle z całym buildem, 104 MB) + `Assetbundles/` (fonty,
  dialogi, UI, poziomy). Dźwięk w FMOD (`StreamingAssets/*.bank`) — dubbingu nie ma.

## Jak gra trzyma teksty

- Każdy język to `Language_SO` (ScriptableObject) z TextAssetem CSV `CyberHook <Język>`
  w `data.unity3d` (`sharedassets1.assets`). Format `KEY,VALUE,DETAILS`, CRLF.
  DETAILS to u twórców zwykle francuski odpowiednik (twórcy są Francuzami).
- `Language_SO.ParseLanguageFile` dzieli po `Environment.NewLine`, przecinki poza
  cudzysłowami, obcina `"` z brzegów, `""` → `"`, `Trim()`. Klucze małymi literami.
  Konsekwencja: tekst z przecinkiem bez cudzysłowów ucina się (np.
  `dialog_ending_credits_00_00` w grze to samo „Hey”). Nasze teksty nie przechodzą
  przez CSV, więc takie błędy naprawiamy przy okazji.
- Wszystko idzie przez `Language_SO.GetTranslatedKey`/`KeyExists`: `StringParser`
  (napisy UI), `TranslatedString` (dialogi, `{0}`), `SO_Level` (nazwy poziomów),
  `OptionField_Enum` (`option_<wartość enuma>`). Zaszytych w kodzie tekstów praktycznie
  nie ma.
- Dialogi: `DialogLine.LineTextKeys[].TextKey` w bundlach `dialogs/*`, `story/*`.
  `Tutorial_Line_04_00` i `Tutorial_Line_04_01` mają zamiast klucza **angielski tekst**
  (z końcowymi spacjami) — gra pokazuje go wprost. Plugin obsługuje takie klucze
  (`KeyExists` zwraca prawdę dla przetłumaczonych). Klucze i oryginał są
  w `translations/raw-keys.json`, tłumaczenie w `en-pl-review.json` pod tym samym kluczem.
- Znaczniki: TMP (`<color>`, `<size>`, `<sprite name="Jump">`, `<br>`) i własne
  `<link="Pause(1)">`, `<link="EventTrigger(...)">` sterujące dialogiem. Build porównuje
  je z oryginałem.
- Wybór języka to enum `OptionEnums.AvailableLanguages` (en, fr, es, de, ru, zh, pt, jp)
  zapisany w `GameData`. Nowej wartości nie da się dodać bez zmiany kodu gry.

## Jak dostarczamy

Plugin BepInEx 5.4.23.5 (`plugin/Plugin.cs`):

- Prefiks na `Language_SO.GetTranslatedKey` i postfiks na `KeyExists`: gdy pytany jest
  angielski `Language_SO`, a aktywny język to `en`, odpowiadamy z `pl.tsv`. Inne języki
  pytają angielski jako zapasowy — wtedy zostaje angielski.
- `option_en` → „Polski”, więc w menu języków polski stoi w miejscu angielskiego.
- Postfiks na `ParseLanguageFile` liczy klucze gry bez tłumaczenia i zapisuje w logu.
- Log przy starcie: wersja pluginu, gry i Unity.

Fonty (`plugin/PolishGlyphs.cs`, port z Void Bastards na TMP 2.x): atlasy SDF gry mają
z polskich liter tylko ó/Ó (niektóre), źródłowe TTF w bundlu `fonts` też nie (Equalize,
Neon Overdrive, Square — brak; Blockletter bez ś/Ś). Plugin dla każdego `TMP_FontAsset`
bez liter składa mały atlas zapasowy z litery bazowej tego samego fontu i dorysowanego
znaku, wpina go na początek `fallbackFontAssetTable`. Wyzwalacze: `TMP_FontAsset.Awake`
zaznacza nowy font, składanie następuje przed najbliższym tłumaczeniem tekstu, po zmianie
języka i po wczytaniu sceny. Dotyczy tylko sytuacji, gdy aktywny jest `en`.

Fonty angielskiego `Language_SO.CustomFonts`: Equalize SDF, Lucida console SDF,
Blockletter SDF Squared, Neon Overdrive SDF (dynamiczny, z GAGAGAGA jako źródłem).

## Budowanie

```powershell
.venv\Scripts\python.exe games\cyber-hook\tools\extract.py --game "C:\Games\CyberHook_GOG"
.venv\Scripts\python.exe games\cyber-hook\tools\build_plugin.py --game "C:\Games\CyberHook_GOG"
.venv\Scripts\python.exe games\cyber-hook\tools\review.py
.venv\Scripts\python.exe games\cyber-hook\tools\install_local.py --game "C:\Games\CyberHook_GOG"
.venv\Scripts\python.exe games\cyber-hook\tools\install_local.py --game "C:\Games\CyberHook_GOG" --restore
```

`extract.py` czyta surowe bajty TextAssetu (UnityPy przy dekodowaniu gubi `\r`)
i zapisuje `work/source/<język>.json` (referencja dla tłumacza i dla builda).
`build_plugin.py` sprawdza klucze i wstawki, kompiluje plugin (Roslyn `csc` z VS 2022)
i składa `dist/Cyber-Hook-PL-<wersja>.zip` (~660 KB, nasze ~40 KB).

## Test w grze

**0.1.0 (2026-09-23, screeny użytkownika):** menu i reszta w porządku, dwa błędy:

- Wstęp (terminal, speaker „World”, font `Fixedsys SDF`) — kwadraty zamiast ę, ł, ż.
  Log: polskie litery dostały tylko 4 fonty użyte wcześniej w menu. Przyczyna: font,
  którego gra jeszcze nie wyświetliła, ma w `characterTable` puste `glyph` (wypełnia je
  dopiero `ReadFontAssetDefinition`). Plugin uznawał, że nie ma liter bazowych, i odkładał
  font na zawsze. Numero mówi `Fixedsys SDF_Numero` — ten sam problem.
- Dialog Drona — kreska nad ś ucięta. Dron nie ma własnego `TypingFont`, mówi fontem
  pola dialogu, `Neon Overdrive SDF` (dynamiczny; nie był uzupełniony, litery szły
  łańcuchem zapasowym z `Square SDF Equalize`). Pole 400×88 siedzi w oknie z komponentem
  `Mask`, którego górna krawędź jest tuż nad wersalikami; kreska sięgała ~50% wysokości
  litery ponad nie.

**0.1.1:** przed składaniem plugin woła `characterLookupTable` (wypełnia glify); font
dynamiczny najpierw dorysowuje litery bazowe (`TryAddCharacters`); font bez gotowego
atlasu jest ponawiany, a nie odkładany. Znak nad literą mieści się do linii wydłużeń
górnych fontu (`faceInfo.ascentLine`), a gdy miejsca brak, jest zwarty (min. 1,3 grubości
kreski); grubość znaku nie większa niż 1/5 wysokości litery. `DialogTextDisplay.Init`
dostaje górny margines 0,25 rozmiaru fontu, żeby maska okna nie ucinała znaków.

Do sprawdzenia:

1. Ekran tytułowy — „Naciśnij - Dowolny klawisz -”, menu główne.
2. Options → Gameplay → Language: pozycja „Polski” (w miejscu English).
3. Opcje: zakładki i opisy z polskimi literami (Rozdzielczość, Głośność, Wygładzanie).
4. Nowa gra: wstęp Numero („Inicjalizacja obiektu…”, „Wykryto biegacza”), Dron
   („Jestem Dron, miło cię poznać!”), ikony klawiszy w zdaniach.
5. Pauza i ekran końca poziomu.
6. `BepInEx/LogOutput.log`: „Wczytano 342 wpisów”, „345 z 687 tekstów … zostaną po
   angielsku”, linie „Font TMP „…”: złożono …”.

## Nota o materiale gry

`work/source/*.json` to teksty gry wyciągnięte do pracy (jak `ref-*.json` w innych grach).
Paczka nie niesie żadnego pliku ani fragmentu zasobu gry; build odrzuca archiwum
z plikami `CyberHook_Data`, `.assets`, `.unity3d`, `.bank`.
