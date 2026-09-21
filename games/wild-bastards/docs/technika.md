# Wild Bastards — technika i stan prac

21 września 2026. **Pełne tłumaczenie 0.2.0 (4426/4426) zbudowane i zainstalowane lokalnie; czeka na test w grze.**
Vertical 0.1.1 potwierdzony przez użytkownika.

## Istniejące spolszczenia

Nie znaleziono dostępnego spolszczenia ani fanowskiego tłumaczenia. Sprawdzono
wyszukiwania po polsku i angielsku. Sklep Steam (API `appdetails`) wymienia:
English, French, Italian, German, Spanish, Japanese — bez polskiego.

## Lokalna kopia

- `C:/SteamLibrary/steamapps/common/Wild Bastards`, Steam app 1660840, buildid 16213058.
- `PlayerSettings.bundleVersion` = **1.0.0.26658**, Unity **2021.3.32f1**, **Mono** (`Managed`).
- `mscorlib.dll` zawiera `GetPEKind` — brak okrojenia; BepInEx 5 powinien wstać.

## Teksty

**I2 Localization** wkompilowane w `Assembly-CSharp.dll`, plus pomocnik `Localize`
gry. Tabela `I2Languages`: `resources.assets`, path_id 54563.

- 4543 terminy, 4428 niepustych, 147 999 znaków EN — dwa razy więcej niż Void Bastards.
- 10 języków: en, fr, it, de, es, zh, ko, ja, ru, pt. Brak PL. Nowszy układ I2 bez Description.
- Znaczniki: `<color=…>` (~210), własne parametry wartości `<d>`, `<d2>`, `<d3>`, `<p>`,
  `<p2>`, `<n>`, `<s>` (liczby, procenty, nazwa planety), `{0}`–`{2}` (imiona banitów),
  `<sprite name=…>`, `[BLANK]`. Wszystkie trzeba zachować 1:1.
- Kategorie: Dialog 723, UIMG 312, SME 270, TalentName/Desc 229/228, UIPM 220,
  ItemName/Description 161, TraitName/Desc, Options, Hint, Location i inne.

`tools/analyze.py --game <katalog gry>` — jak w Void Bastards.

## Menu języków

`UIMGMainMenu` pokazuje gotowy `languagePanel` z przyciskami z prefabu;
`OnSetLanguage(string)` ustawia `LocalizationManager.CurrentLanguage`, zapisuje
`HydraOptions` i przeładowuje scenę. Lista nie jest dynamiczna — plugin musi
dołożyć przycisk „Polski” (jak w Turbo Overkill) i dopisać język do I2 zanim
opcje wczytają zapisany wybór.

## Fonty

TextMeshPro z Unity 2021 obsługuje atlasy dynamiczne. TTF w grze z pełnymi
polskimi znakami: SouthbankSpurs (+Italic), GrindstoneDisplay, JosefinSans,
LiberationSans, Consola. Statyczne atlasy SDF mają według wstępnej heurystyki
luki — plan: fallback przez dynamiczny `TMP_FontAsset` z lokalnego TTF gry,
bez dołączania fontów do paczki.

## Werdykt

Warto, ale to większy projekt niż Void Bastards: dwa razy więcej tekstu,
przycisk języka do dołożenia i fallback fontów. Pułapki: imiona banitów
w placeholderach (płeć i odmiana), składane opisy przedmiotów z parametrami.

## Vertical 0.1

- `plugin/Plugin.cs` — I2 jak w Void Bastards: `AddLanguage("Polish", "pl")` przy
  `AddSource`/`InitializeIfNeeded`, wypełnienie z `pl.tsv`.
- `plugin/LanguageButton.cs` — postfix `UIMGMainMenu.Start`: klon ostatniego przycisku
  z trwałym `OnSetLanguage(...)`, podpis „Polski”, usunięty komponent I2 `Localize`,
  nowy `onClick` → `OnSetLanguage("Polish")`, flaga PL, jeśli przycisk ma obraz „flag”.
  W logu: każdy przycisk języka z argumentem i tekstami oraz rodzaj układu panelu.
- `plugin/PolishFonts.cs` — atlasy SDF gry są statyczne, bez `m_SourceFontFile`
  i bez ąćęłńśźż (odczyt typetree). TTF tych samych rodzin leżą w Resources
  (`Fonts/SouthbankSpurs`, `Fonts/GrindstoneDisplay`, `Fonts/JosefinSans-Regular`),
  więc dla każdego atlasu plugin tworzy `TMP_FontAsset.CreateFontAsset(TTF, …, Dynamic)`
  i wpina go jako pierwszy fallback. DroneRanger nie ma TTF z polskimi literami —
  zostaje zapasowy font gry (LiberationSans, dynamiczny).
- Tłumaczenie według skilla `lokalizacja`: `translations/biblia.yaml`.
  Gra ma warianty rodzajowe kluczy (`HUD/Dead`/`HUD/DeadFem`) — „Ranny”/„Ranna”.
  Terminy: banita, popis (stunt), bimber (juice/shine), starcie (showdown), furtka
  (backdoor), asy, kumpel. Raport kontrolny czysty poza 6 zgłoszeniami długości.
- Build: `tools/build_plugin.py --game <katalog>`; instalacja testowa
  `tools/install_local.py` z pokwitowaniem w `backups/wild-bastards/`.

## Pełne tłumaczenie — 0.2.0

Tłumaczenie partiami przez `work/batch.py` (`show <prefiks>` wypisuje brakujące wpisy,
`put <plik.tsv>` dopisuje, pilnuje liczby nowych linii i sam przenosi spacje z początku
i końca oryginału — gra dokleja do nich liczby). Wiersz pliku to `klucz<TAB>tekst`
albo `klucz @@ tekst`. Partie leżą w `work/tsv/`.
`work/ref.py <regex> [fr,it]` pokazuje obok EN teksty innych języków — tak ustalano
płeć mówiących w dialogach (francuski i włoski; rosyjska tabela gry jest pusta).

Dialogi nie mają w kluczach mówiącego. Kto mówi, wynika z treści (zwroty „Miss”,
„Sarge”, styl) i z form francuskich. Standard: skill `lokalizacja`, biblia
`translations/biblia.yaml`, decyzje `docs/decyzje-tlumaczenia.md`, raport
`work/l10n-report.md` (bez braków, tokenów i terminów; zostają zgłoszenia długości
i spójności do obejrzenia w grze).

Plugin 0.2.0 = 0.1.1 bez zmian w kodzie, tylko nowa wersja i pełne `pl.tsv`.

## Następny krok

Test pełnej wersji: ekran banity (asy, przedmioty, cechy), mapa sektora ze
zdarzeniami (SME), mapa planety (opisy miejsc), dialogi na Drifterze.
