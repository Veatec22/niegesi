# Laika: Aged Through Blood — ustalenia techniczne

## Stan

- **Etap:** pełne tłumaczenie 0.2.0 — 3470/3470 wpisów (UI 378, postacie 79, miejsca 83,
  przedmioty 265, zadania 218, dialogi 2447 z tekstem). Vertical 0.1.2 potwierdzony w grze.
- Po fullu niezależny przegląd (`docs/localization-review.md`) — wynik i poprawki niżej
  w sekcji testów oraz w `docs/translation-decisions.md`.
- **Następny krok:** przejście dalszej części gry (lista „Mniej pewne” w decyzjach),
  akceptacja decyzji albo poprawki.

## Istniejące spolszczenia

Steam wymienia 8 języków (EN, FR, DE, ES, RU, ZH, JA, KO), bez polskiego. Nie znalazłem
dostępnego polskiego spolszczenia (Steam, Nexus, wyszukiwarki; 2026-09-23). Na Nexusie
jest fanowskie tłumaczenie portugalskie przez BepInEx + XUnity AutoTranslator
(nexusmods.com/laikaagedthroughblood/mods/5) — potwierdza, że BepInEx w tej grze wstaje.

## Gra

- GOG, build `57119379309637473`, `C:\Games\Laika Aged Through Blood`.
- Unity 2021.3.29, Mono, x64. Kod gry w `Assembly-CSharp.dll`, lokalizacja w
  `Assembly-CSharp-firstpass.dll`.
- `mscorlib.dll` pełny (4,6 MB, jest `GetPEKind`) → BepInEx 5 i Harmony wstają.
- Zasoby w jednym `data.unity3d` (748 MB) + `resources.resource`. Dźwięk w FMOD
  (`StreamingAssets/*.bank`); dubbing jest w wymyślonym języku, napisy z arkuszy.

## Jak gra trzyma teksty

- **M2H Localization** (`Language`, `LocalizationSettings`, `LanguageCode` w firstpass).
  Arkusz to TextAsset `Resources/Languages/<KOD>_<ARKUSZ>`: `UI`, `CHARACTERS`, `ZONES`,
  `ITEMS`, `QUESTS`, `DIALOGUES`. XML `<entries><entry name="KLUCZ">tekst</entry>`.
  Kody: EN, ES, FR, DE, RU, JA, KO, ZH_CN (PT_UI i ZH_UI to puste szkielety).
- Arkusze bez kodu (`_UI` itd.) mają zamiast tekstu limit długości wpisu — 264 wpisy.
  `extract.py` zapisuje go w `limit`, build ostrzega o przekroczeniu. Limity są orientacyjne:
  wiele angielskich tekstów samouczka też je przekracza.
- `Language.DoSwitch`: dla każdego arkusza `GetLanguageFileContents`, XmlReader →
  `Trim` → `\\n` na nową linię → `StringExtensions.UnescapeXML`. Wybór zapisuje
  w `PlayerPrefs["M2H_lastLanguage"]`, statyczny konstruktor `Language` go przywraca.
- Lista języków gry (`Language.LoadAvailableLanguages`) to wartości enuma `LanguageCode`
  (jest w nim `PL`), dla których `HasLanguageFile(kod, pierwszy arkusz)` zwraca prawdę.
- Menu języków (`Laika.UI.Settings.SettingsViewItem`): nazwy z `get_LanguageNamesList`
  (8 zaszytych napisów) i równoległa lista kodów `languageCodes` z konstruktora; wybór →
  `LanguageManager.SwitchLanguage(kod)`. Podświetlenie bieżącego szuka nazwy z wpisu
  `UI_SETTINGS_LANGUAGE_<KOD>`.
- Dialogi: TextAssety `D_*` to skrypty (`target LAIKA` / klucz kwestii); tekst i mówiący
  są w kluczu `D_<scena>_<MÓWIĄCY>_<nr>`.
- Znaczniki: TMP `<color=#…>`, `<sprite name=…>`, `<br>`, wstawki `{0}`, `{1}`.

## Jak dostarczamy

Plugin BepInEx 5.4.23.5 (`plugin/Plugin.cs`), osobny język „POLSKI”:

- Prefiks `Language.HasLanguageFile`: dla `PL` prawda, jeśli istnieje arkusz `EN_…` —
  gra sama dopisuje PL do listy dostępnych języków.
- Prefiks `Language.GetLanguageFileContents`: gdy bieżący język to PL, arkusz budowany
  z angielskiego XML-a z podmienionymi tekstami z `pl.tsv`. Czego nie mamy, zostaje
  po angielsku; liczba braków na arkusz trafia do logu. Do `UI` dochodzi
  `UI_SETTINGS_LANGUAGE_PL = POLSKI`.
- Postfiks `SettingsViewItem.LanguageNamesList` i prefiks `SetLayout`: „POLSKI” i `PL`
  na końcu obu list.
- Fonty (`plugin/PolishGlyphs.cs`, z Cyber Hook, rozszerzone): dla każdego fontu TMP
  bez polskich liter najpierw font dynamiczny dorysowuje je sam; jeśli nie, zapasowy font
  dynamiczny z TTF tego samego kroju, jeśli gra go wczytała (TTF-y Oswald, Like A Cave,
  FriendlyFire, SourceCodePro mają polskie litery); na końcu składanie z liter bazowych.
  Nigdy `Resources.LoadAll` — wywraca grę (0.1.1).
  Lista znaków tytułowego `SDF_LikeACaveMinus` zawiera ąćęłńśźż — twórcy szykowali się
  na polski. Wyzwalacze: przełączenie języka, wczytanie sceny, nowy `TMP_FontAsset`
  przed najbliższym `Language.Get`. Wszystko tylko przy aktywnym PL.
- Log przy starcie: wersja pluginu, gry i Unity.

Po odinstalowaniu przy zapisanym `PL` gra nie znajdzie języka i przełączy się na pierwszy
dostępny (M2H loguje błąd) — dlatego instrukcja każe najpierw wrócić na angielski.

## Budowanie

```powershell
.venv\Scripts\python.exe games\laika-aged-through-blood\tools\extract.py --game "C:\Games\Laika Aged Through Blood"
.venv\Scripts\python.exe games\laika-aged-through-blood\tools\build_plugin.py --game "C:\Games\Laika Aged Through Blood"
.venv\Scripts\python.exe games\laika-aged-through-blood\tools\review.py
.venv\Scripts\python.exe games\laika-aged-through-blood\tools\install_local.py --game "C:\Games\Laika Aged Through Blood"
.venv\Scripts\python.exe games\laika-aged-through-blood\tools\install_local.py --game "C:\Games\Laika Aged Through Blood" --restore
```

`extract.py` czyta arkusze z `data.unity3d` (UnityPy, ok. 2 min) do `work/source/en.json`.
`build_plugin.py` sprawdza klucze, znaczniki i limity, kompiluje plugin (Roslyn `csc`
z VS 2022) i składa `dist/Laika-Aged-Through-Blood-PL-<wersja>.zip` (~667 KB).

Do rozpoznania kodu gry służył jednorazowy dezasembler IL na refleksji (poza repo);
wystarczył do ustalenia ścieżek wyżej.

## Test w grze

**0.1.0 (2026-09-24, zrzut użytkownika):** „POLSKI” jest na liście, ale Apply nic nie robi.
`Player.log`: „Could not switch from language EN to PL” — lista `Language.availableLanguages`
nie miała PL. Plugin wstał przed inicjalizacją gry, ale pierwsza zmiana języka przy starcie nie
trafiła do postfiksu `DoSwitch`: najpewniej zakładanie łatek na klasę `Language` odpaliło jej
statyczny konstruktor (lista języków, przywrócenie zapisanego) przed łatką `HasLanguageFile`.

**0.1.1:** prefiks `Language.SwitchLanguage(LanguageCode)` dopisuje PL do listy gry, jeśli
go brak (log: „Lista języków gry powstała bez PL — dopisano”). Zapisany `M2H_lastLanguage`
plugin czyta przed zakładaniem łatek i po wczytaniu pierwszej sceny przywraca PL, bo gra
w konstruktorze nadpisałaby go językiem zastępczym. Test (2026-09-24): PL dopisany (log
potwierdza przyczynę), arkusze zbudowane, ale gra się wywróciła przy uzupełnianiu fontów.
`Player.log`: seria „The referenced script … is missing” i „different serialization layout”
(obiekty `D_0_BossKilled`, `Dialogue Display`). Przyczyna: szukanie TTF przez
`Resources.LoadAll<Font>("")`, które wczytuje wszystkie zasoby z Resources, łącznie
z prefabami scen. Fonty `LiberationSans SDF` dostały litery z TTF, zanim doszło do fontów gry.

**0.1.2:** szukanie TTF tylko wśród już wczytanych (`FindObjectsOfTypeAll<Font>`), bez
`LoadAll`; font bez wczytanego TTF przechodzi do składania liter. **Potwierdzony w grze
(2026-09-24):** polskie znaki, menu, prolog, przywrócenie PL po restarcie działają. Log: fonty
gry `FriendlyFire SDF` i `SDF_LikeACaveMinus` mają własne polskie litery; `LiberationSans`
dostaje je z TTF, azjatyckie fonty (ZCOOL, AOTF, Kosugi, Dokdo, Nanum) — składane.
Gra 1.0.13 (GOG). Lista kontrolna z verticalu:

1. Settings → Game → Language: na końcu listy „POLSKI”; po wybraniu menu po polsku.
2. `BepInEx/LogOutput.log`: „Wczytano 661 wpisów”, „Język gry: PL”, linie „Arkusz …”
   i „Font TMP „…”: …” — z nich widać, które fonty miały polskie litery.
3. Menu główne, ustawienia (zakładki, opisy), ostrzeżenie o treści na starcie.
4. Nowa gra: rozmowy przez krótkofalówkę (Puppy, Maya, Starsza), nazwa miejsca
   „Tam, Gdzie Czają się Ptaki”, samouczki sterowania z ikonami klawiszy, dziennik
   z zadaniem „Gniew i żal”.
5. Polskie litery w dymkach, samouczkach i nazwach (ą ę ł ś ż ź ć ń ó, „ ”).
6. Restart gry: czy zostaje polski.

**0.2.0 (2026-09-24):** pełne tłumaczenie po niezależnym review i rozstrzygnięciach
użytkownika; paczka 745 007 B w `dist/` i `site/public/pobierz/`, zainstalowana lokalnie.
Test dalszej części gry czeka — lista w `docs/translation-decisions.md` („Mniej pewne”).

## Nota o materiale gry

`work/source/en.json` to teksty gry wyciągnięte do pracy. Paczka nie niesie żadnego pliku
ani fragmentu zasobu gry; build odrzuca archiwum z plikami `Laika Aged through Blood_Data`,
`.assets`, `.unity3d`, `.resource`, `.bank`. Fonty zapasowe powstają w czasie gry z plików
gry na komputerze gracza.
