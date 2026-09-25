# I Am Your Beast — rozpoznanie techniczne

Stan: 2026-09-25, analiza plików; bez uruchamiania gry, instalacji pluginu i tłumaczenia.
Na prośbę użytkownika pominięto wyszukiwanie spolszczeń. Nie przeprowadzono też
poszukiwań zagranicznych paczek; poniższy werdykt opiera się na lokalnej instalacji.

## Werdykt

Warto ruszać. Zalecana droga to BepInEx 5 x64 + Harmony, z tekstami i zmianami
w pamięci. Menu i HUD mają centralny bank Fleece. Największą trudnością jest
reżyseria animowanych dialogów, nie wydobycie tekstu. Fonty źródłowe zawierają
wszystkie polskie litery. Zgodność pluginu trzeba jeszcze potwierdzić w grze.

## Instalacja i środowisko

- Lokalnie: `C:\Games\I Am Your Beast`.
- GOG game ID `1577997347`, build ID `59479796167928060` z pliku goggame INFO.
- Unity `2022.3.5f1`, Mono, aplikacja 64-bitowa.
- `PlayerSettings.bundleVersion`: `0.1.0`; to wartość wewnętrzna, nie potwierdzona
  wersja widoczna w GOG Galaxy lub menu.
- `mscorlib.dll` ma `Module.GetPEKind` i wszystkie cztery konstruktory
  `AmbiguousMatchException`. Nie występuje znana blokada okrojonego runtime.
- `Assembly-CSharp.dll` i `AudioTextSynchronizer.dll` dają się odczytać przez Cecil.

## Gdzie są teksty

Przegląd wszystkich głównych plików `.assets` i `level*` zakończył się bez błędów
odczytu interesujących nas obiektów:

- `resources.assets`: `Fleece.Story` o nazwie `Sample`, 687 referencji do
  `Fleece.Passage`, 687 unikatowych ID; 684 wpisy mają niepusty tekst. Łącznie
  około 2663 słów. Nazwa „Sample” jest myląca: bank obejmuje prawdziwy interfejs,
  HUD, tutorial, kwestie przeciwników, nazwy i inne teksty gry.
- 44 `AudioTextSynchronizer.Core.PhraseAsset`, łącznie 870 elementów `Timings`
  i około 3797 słów w tych elementach. Są sceny fabularne, tutorialowe,
  `CATCH`, `RELEASE`, `ENDING`, ale też `Example Cutscene No Text`.
- 1679 niepustych pól TMP w scenach/prefabach, 327 różnych ciągów. To nie
  1679 dodatkowych tłumaczeń: wiele pól powtarza bank, ma placeholder albo jest
  starym ekranem demonstracyjnym. Pozostaje porównanie z Fleece i użyciami w kodzie.
- Są stare eksporty Fleece jako TextAsset CSV/JSON, lecz właściwym źródłem do
  ekstrakcji są bieżące obiekty `Passage`, a nie te eksporty.

Podane liczby to inwentaryzacja zasobów, nie ostateczny zakres żywego tekstu.
Nie skatalogowano jeszcze wszystkich literałów w kodzie ani tekstów w grafikach.
Pliki EN/PL są szkieletem do pracy: puste polskie wartości oznaczają brak tłumaczenia.

## Punkty zaczepienia pluginu

`Fleece.Jumper.get_passage` rozwiązuje ID przez aktywną historię i `Story.Find(int)`.
`Passage.get_parsedText` przepuszcza `Passage.text` przez `Fleece.Parser.Parse`.
Tłumaczenie należy podać przed parsowaniem, zachowując komendy i znaczniki;
identyfikatorem jest ID wpisu, nie tekst angielski. Do sprawdzenia pozostają
bezpośrednie odczyty pola `text` i napisy poza bankiem.

`PhraseAsset` zawiera `Text`, `Clip` oraz listę `Timings`. Każdy odcinek ma własny
`Text`, początek i koniec, wyrównanie, animację i zmianę kolorystyki.
`TimingsTextSplitConfig.DivideTextForParts` szuka tekstu odcinka w pełnym tekście
przez `IndexOf`, zaczynając po poprzednim fragmencie. Są też zdania narastające:
krótki początek, a potem powtórzenie z dalszą częścią. Nie wolno ich usuwać jako duplikatów.

Plan: klonować PhraseAsset w pamięci, podmieniać tekst wszystkich odcinków i
spójnie odtwarzać pełny `Text`, zachowując audio i parametry sceny.
`TextSynchronizer.set_Timings` wywołuje `Stop`, `SplitWords` i `InitEffect`, więc
to kandydat do podania przygotowanej kopii. Sprawdzić także ścieżkę startową
z obiektem przypisanym bezpośrednio w scenie. Przed buildem walidować, że wszystkie
fragmenty dają się odnaleźć w prawidłowej kolejności. Synchronizacja wymaga testu
wizualnego: polska składnia i długość słów mogą wymusić zmianę podziału/timingu.

## Polskie znaki

W `sharedassets0.assets` są źródłowe fonty `octin college rg` (19092 B) i
`LiberationSans` (350200 B). Odczyt tablic cmap przez fontTools potwierdził komplet
`ąćęłńóśźżĄĆĘŁŃÓŚŹŻ` w obu.

Trzy warianty TMP Octin mają tryb dynamiczny (AtlasPopulationMode=1), referencję
do źródłowego fontu i pustą listę fallbacków. Ich obecne atlasy nie zawierają
polskich znaków, ale istnieją dane do wygenerowania ich w czasie działania.
LiberationSans ma atlas statyczny i dynamiczny fallback ze źródłem.
Na verticalu sprawdzić generowanie znaków, wariant gruby/cień, clipping i wielkie
litery. Nie ma obecnie przesłanki do podmiany kroju lub dystrybucji fontów gry.

## Odtworzenie analizy

```powershell
.venv\Scripts\python.exe games/i-am-your-beast/tools/inspect_game.py --game "C:\Games\I Am Your Beast"
```

Wynik: ignorowany `work/survey.json`. Narzędzie nie zapisuje niczego w katalogu gry.
Używa UnityPy i TypeTreeGeneratorAPI z repo. MonoScript należy rozwiązywać ze
standardowego nagłówka MonoBehaviour i jawnie załadowanego `globalgamemanagers.assets`;
następnie czytać dane przez wygenerowane drzewo właściwej klasy. W generowanym
drzewie pole nagłówka `m_Script` ma błędną interpretację endian — nie używać go
do rozwiązywania referencji ani zapisu zasobów. Właściwe dane tekstowe czytają się
w całości; narzędzie służy wyłącznie do odczytu.

## Plugin (0.2.0)

`plugin/Plugin.cs`, budowanie przez `tools/build_plugin.py`, teksty w `translations/en-pl-review.json` (jedyny plik tłumaczenia, 0021).
Kod gry przejrzano przez Cecil (zrzut IL w scratchpadzie, nie w repo). Trzy warstwy:

- **Fleece.** Wszystkie odczyty tekstu idą przez `Passage.text` (`parsedText`,
  `Drawstring.Begin`, `Parser.InsertPassage`). Plugin podmienia pole raz na obiekt:
  prefiks `get_parsedText` i `Drawstring.Begin`, postfiks obu `Story.Find`, plus
  przegląd `Resources.FindObjectsOfTypeAll<Passage>()` po wczytaniu sceny. Tytułów
  nie ruszamy — `Story.Find(string)` szuka po tytule.
- **Sceny dialogowe.** `CutsceneTextEffect` wyświetla wyłącznie `TextPart.Text`,
  czyli tekst odcinka (`Timing.Text`); pełny `PhraseAsset.Text` służy tylko do
  `IndexOf` w `TimingsTextSplitConfig` i podziału na słowa. Plugin podmienia teksty
  odcinków i składa `Text` z odcinków połączonych `
`, żeby każdy dał się odnaleźć
  po kolei. Wpięcia: `TextSynchronizer.set_Timings`, `SplitWords`,
  `TextSplitConfigBase.Init`, `TextEffectBase.Init`. Zdania narastające to po prostu
  kolejne slajdy, więc nie wymagają wspólnego przedrostka technicznie — trzymamy go
  redakcyjnie. Już oryginał ma odcinki, których `IndexOf` nie znajduje (np. „Dear diary”
  przy „Dear Diary...”), i gra to znosi.
- **Stałe napisy TMP** (klucze `tmp/<angielski>`): dokładne dopasowanie w prefiksie
  `TMP_Text.set_text`, w `Awake` obu klas TMP (pole `m_text`) i w przeglądzie po scenie.

Każdy wpis Fleece i odcinek ma w `pl.tsv` odcisk FNV-1a liter i cyfr ASCII angielskiego
oryginału. Niezgodność po aktualizacji gry zostawia tekst po angielsku i trafia do
licznika w logu. Plugin loguje wersję gry i Unity oraz stan polskich liter w każdym
`TMP_FontAsset` (`HasCharacters(..., tryAddCharacter: true)` od razu dokłada je do atlasu).

Wstawki do zachowania: `[KEY]`, `[WEAPON]`, `VALUE`, `[Quick Turn]` (HintManager
zamienia treść nawiasu na nazwę klawisza akcji, więc angielska nazwa akcji zostaje),
znaczniki TMP. Build je sprawdza.

Oba fonty źródłowe mają też „ ” — – … ’, więc polska typografia jest bezpieczna.

```powershell
.venv\Scripts\python.exe games\i-am-your-beast	oolsuild_plugin.py --game "C:\Games\I Am Your Beast"
.venv\Scripts\python.exe games\i-am-your-beast	ools\install_local.py --game "C:\Games\I Am Your Beast"
.venv\Scripts\python.exe games\i-am-your-beast	ools\install_local.py --game "C:\Games\I Am Your Beast" --restore
```

Paczka 0.2.0: 683 KB, 1581 wpisów (684 Fleece, 853 odcinki scen, 44 napisy TMP) — całość.

## Stan testów

- 2026-09-25: vertical 0.1.0 **potwierdzony w grze przez użytkownika** („świetny efekt”);
  jedyna uwaga — skrót I.T.O. z kropkami (0.1.1). Nie przesłano logu ani zrzutów.
- 2026-09-25: full 0.2.0 — wszystkie teksty, niezależny przegląd językowy
  (`docs/localization-review.md`), poprawki naniesione, build i instalacja lokalna.
  Test pełnej gry w uruchomionej grze — **jeszcze nie**.
- Do sprawdzenia: lista w `docs/localization-review.md`, sekcja 5.

## Grupa wsparcia: skąd teksty

Przerywniki dodatku to `CutsceneInformation` `PLP_Cutscene_1`–`9` i `_FINAL`, które
wskazują `PhraseAsset` `SCENE 1`–`9` i `FINAL CUTSCENE`. Ich pełne pole `Text` wygląda
na automatyczną transkrypcję z błędami, ale gra go nie wyświetla — odcinki (`Timings`)
mają poprawnie zredagowany tekst i to je tłumaczymy. Narracja z banku Fleece (folder
44072 i pokrewne) to osobne teksty, prawdopodobnie z poziomów dodatku; też przetłumaczone.
Mówiących w dodatku wskazują profile kolorów BOB, IRIS, JODIE, KYLE, MARKUS, NATHAN, STEPHEN.

## Następny krok

Użytkownik testuje całość. Po akceptacji: przeniesienie w `games/catalog.yaml` należy
do użytkownika.

## Materiał gry

Paczka zawiera wyłącznie plugin, `pl.tsv` z polskimi tekstami i odciskami angielskich,
instrukcję oraz BepInEx z licencją (źródła tej wersji obok paczki). Build odmawia
złożenia archiwum z plikami gry. Zrzuty zasobów i fonty zostają lokalnie w ignorowanym `work/`.
