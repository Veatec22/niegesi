# Not Geese — instrukcje dla agenta

Publiczne repo do maszynowego tworzenia spolszczeń gier indie. Użytkownik wybiera grę,
instaluje ją na swoim komputerze i przekazuje agentowi do rozpracowania. Agent prowadzi
analizę techniczną i tłumaczenie, użytkownik ocenia efekt w grze i robi korektę językową.
Rozmawiamy po polsku.

## Przebieg pracy

1. **Sprawdź istniejące spolszczenia w internecie.** Jeśli znajdziesz dostępne polskie
   tłumaczenie, podaj konkretne miejsce pobrania lub oficjalną obsługę PL i kończymy temat.
   Same zapowiedzi, forumowe deklaracje i niedostępne stare strony nie zamykają projektu.
   Brak dostępnej paczki opisuj jako brak znalezionego dostępnego spolszczenia,
   nie pewność, że żadne nigdy nie powstało.
2. **Poszukaj innych tłumaczeń fanowskich.** Mogą dostarczyć narzędzi, opisu formatów
   i sposobu instalacji. Zapisz przydatne linki i ustalenia.
3. **Zbadaj lokalne pliki gry.** Ustal silnik, format i zakres tekstów, sposób ich
   wydobycia i ponownego wgrania, obsługę polskich znaków oraz przeszkody techniczne.
   Daj krótki werdykt: czy warto ruszać, jak to zrobić i co pozostaje niepewne.
4. **Przed verticalem ustal kierunek tłumaczenia.** Po pozytywnym werdykcie użyj
   `.claude/skills/localization-direction/SKILL.md`: zbierz próbkę prawdziwych tekstów,
   zaproponuj ton, głosy postaci i ważne terminy. Z użytkownikiem rozstrzygnij istotne
   warianty na konkretnych przykładach EN/PL; zwykłe decyzje podejmuj sam.
   Zapisz ustalenia i odrzucone warianty w biblii oraz `docs/translation-decisions.md`
   gry. Nie traktuj braku odpowiedzi jako akceptacji przedstawionego wyboru.
5. **Zrób vertical według ustalonego kierunku.** Przetłumacz małą, reprezentatywną próbkę
   i przeprowadź cały proces: ekstrakcja → tłumaczenie → build → instalacja → test w grze.
   Próbka musi obejmować przynajmniej część menu (główne i ustawienia) oraz sam
   początek rozgrywki — pierwsze kwestie, samouczek, HUD — tak, żeby użytkownik po
   uruchomieniu gry zobaczył polski tekst w pierwszych minutach, bez przechodzenia dalej.
   Sprawdź widoczność tekstów, polskie znaki i układ UI. Sam poprawny build nie dowodzi,
   że spolszczenie działa; jeśli test wymaga użytkownika, podaj mu konkretne kroki.
6. **Dopiero po działającym verticalu tłumacz całość.** Zachowuj ton gry, spójną
   terminologię, placeholdery, znaczniki i formatowanie. Standard pracy opisuje
   skill `.claude/skills/localization/`: biblia gry z faktami i źródłami (postacie,
   płeć, terminy), lista pułapek i raport kontrolny, który tylko podpowiada.
   Pracuj według ustaleń sprzed verticala, rozszerzając biblię o nowy kontekst.
7. **Po fullu uruchom osobnego reviewera.** Użyj
   `.claude/skills/localization-review/SKILL.md` i subagenta w świeżym kontekście.
   Przegląd obejmuje cały tekst i ponowną ocenę początkowych decyzji w świetle całej
   gry, nie tylko próbkę lub raport automatyczny. Pewne błędy popraw, wartościowe
   warianty stylistyczne omów z użytkownikiem. Jego ustaleń nie nadpisuj samowolnie.
   Przegląd językowy nie zastępuje testu w grze.
8. **Przygotuj review i wynik do użycia.** Aktualizuj plik EN/PL, zakres tłumaczenia,
   status testów oraz instrukcję instalacji i przywrócenia oryginału. Przy oddaniu
   spisz decyzje w `docs/translation-decisions.md` gry i streść je użytkownikowi:
   co wybrano, dlaczego, skąd to wiadomo i co sprawdzić w grze. Użytkownik
   akceptuje albo odsyła poprawki.
9. **Domknij grę paczką i metadanymi.** Spolszczenie jest gotowe dopiero wtedy, gdy build
   zostawia w `dist/` spakowany ZIP — wszystko do wypakowania w katalogu gry plus
   `READ-ME.txt` z instrukcją — a `games/<gra>/game.yaml` opisuje aktualny stan: wersję,
   liczbę wpisów, status testu w grze i rodzaj paczki. Luźne pliki w `dist/` bez archiwum
   to niedokończona robota. Do domknięcia należy też okładka i galeria na stronę:
   `tools/keyart.py --game <gra>` (szczegóły w `docs/adding-a-game.md`) — gra bez nich
   stoi na stronie jako zastępczy kafelek. Status spolszczenia (gotowe, wersja testowa, w trakcie)
   ustawia się w jednym miejscu, `games/catalog.yaml`: nowa gra trafia tam od razu
   na listę `w-trakcie`, a na `gotowe` przenosi ją dopiero użytkownik po pełnym ograniu. Zasady dotyczące zawartości paczki opisuje sekcja poniżej.
10. **Korekty z pracowni.** Użytkownik czyta i poprawia teksty w pracowni
    (`notgeese.cc/admin/`), pobiera eksport gry i daje go sesji na swoim komputerze.
    Naniesienie, build i wydanie na main opisuje
    `.claude/skills/workspace-corrections/SKILL.md`. Gra trafia do pracowni po kroku 7:
    z biblią, decyzjami i niezależnym review, żeby użytkownikowi zostało jak najmniej.

## Jak dostarczamy spolszczenie

Domyślną metodą jest **plugin dokładający tłumaczenie w czasie działania gry**, a nie
podmiana plików gry. Przy silniku Unity to BepInEx z łatką Harmony, przy Unrealu
nakładkowy pak. Podmiana pliku jest ostatecznością, po wykazaniu, że pluginu się nie da.

Wynika z tego kilka reguł, których trzymamy się bez wyjątku:

- **Paczka nie niesie zawartości gry.** Nie publikujemy przepisanych zasobów wydawcy —
  plików, w których nasze tłumaczenie jest drobnym dopiskiem, a resztę stanowią cudze
  tekstury, dźwięki i dane scen. Build sprawdza to sam i odmawia złożenia archiwum,
  jeśli wpadł do niego zasób gry.

  Wyjątkiem są **minimalne struktury nośne**, bez których silnik nie przyjmie nowego
  języka i których nie da się rozsądnie wytworzyć od zera: tabela języków, kontener
  tekstury flagi, nagłówek zasobu. Warunek jest podwójny: mają być małe wobec naszej
  treści i w całości związane z lokalizacją, nigdy „przy okazji" niosące resztę gry.
  Każdy taki plik wymieniamy w instrukcji, żeby gracz wiedział, co dostaje.

  Wzorzec granicy: pak SPRAWL-a to 240 KB, z czego 182 KB to nasz plik tekstów,
  a 62 KB to tabela języków i pojemnik tekstury flagi z przemalowanymi pikselami —
  mieści się w wyjątku. `resources.assets` z My Friend Pedro to 205 MB, z czego nasze
  jest kilkadziesiąt kilobajtów — nie mieści się i nigdy nie będzie.
- **Żadnego przypinania wersji w metodzie pluginowej.** Plugin wiąże się po nazwach klas,
  nie po sumach kontrolnych. Wersja gry jest informacją w instrukcji („sprawdzone na…"),
  nigdy warunkiem uruchomienia. Po aktualizacji gry spolszczenie ma działać dalej albo
  wyłączyć się po cichu z wpisem w logu — nigdy nie wywracać gry ani jej nie blokować.
- **Brakujące teksty to nie błąd.** Nowe kwestie po aktualizacji zostają po angielsku,
  a plugin zapisuje w logu, ile ich było. To wystarcza za zgłoszenie do dotłumaczenia.
- **Plugin loguje wersję gry i Unity przy starcie**, żeby zgłoszenie od gracza od razu
  mówiło, z czym ma się do czynienia.
- **Dołączane cudze oprogramowanie musi być zgodne licencyjnie.** BepInEx jest na LGPL-2.1:
  pakujemy go w całości, razem z jego plikiem LICENSE, a obok paczki kładziemy archiwum
  źródeł tej konkretnej wersji. Nie modyfikujemy jego kodu i nie scalamy go z naszym.

Wzorcem jest `games/my-friend-pedro`: plugin w `plugin/Plugin.cs`, budowanie przez
`tools/build_plugin.py`, teksty dalej w `translations/`. Ta droga zbiła paczkę
z 142 MB przepisanego zasobu Unity do 660 KB, z czego nasze jest 43 KB.

**Gdy pluginu się nie da, dostarczamy łatkę różnicową, nie plik.** Paczka niesie wtedy
wyłącznie to, czym spolszczony plik różni się od oryginału; resztę gracz ma na dysku.
Wynik jest bajt w bajt taki sam jak pełny build, a my nie rozpowszechniamy cudzego pliku.
Służy do tego wspólne `tools/patch.py`, jedno polecenie na grę:

```powershell
.venv\Scripts\python.exe tools\patch.py release --original <oryginał> --built <wynik builda> --readme <docs/INSTALL-patch.txt> --out-dir <dist> --game-name <slug> --relative "<ścieżka w katalogu gry>" --package-name <Nazwa> --version <wersja>
```

Nagłówek łatki jest tekstowy i niesie sumy kontrolne obu stron, więc nakładanie odmawia
pracy na innej wersji gry albo na pliku już spolszczonym. Błędny plik nigdy nie powstaje.
Skala: Skate Story 275 MB → 78 KB, Boomerang X 1,8 MB → 14 KB.

Format łatki jest przenośny (operacje kopiuj/wstaw spakowane DEFLATE, po jednej łatce na plik), więc gracz nie
potrzebuje Pythona: paczka niesie aplikator nazwany jak paczka, `<Nazwa>-PL-<wersja>.exe`
(`tools/applier/`, ~85 KB z ikoną logo, .NET Framework z Windowsa). Format ma dwie implementacje — `patch.py` i aplikator; zmieniasz
jedną, zmieniasz obie. `release` sam buduje aplikator i wkłada go do paczki.

Format 3 pozwala łatce **utworzyć nowy plik** z wycinków plików gry (`sources`,
`mode create`) — tak BPM składa dodatkowy pak z fontów leżących wewnątrz 3 GB paka
gracza. Wzór: `games/bpm/tools/release.py`.

**Paczka musi trafić na stronę.** Gotowy ZIP kopiujesz do `site/public/pobierz/`
i wpisujesz w `game.yaml` (`download`). Strona pokazuje tylko paczki, które tam naprawdę leżą.

**Znany wyjątek: gry z okrajanym kodem zarządzanym.** Jeśli twórca włączył w Unity
„managed stripping", z `mscorlib` znikają metody, których gra sama nie używa — między
innymi `Module.GetPEKind`. Preloader BepInEksa woła ją w `PlatformUtils.SetPlatform`
wyłącznie po to, żeby wykryć procesor ARM, i wywraca się na starcie. Doorstop wchodzi
poprawnie, więc objawem jest brak `BepInEx/LogOutput.log` i plik `preloader_*.log`
w katalogu gry.

**To nie zależy od wersji silnika.** Potwierdzone w Skate Story (Unity 6000.0.45)
i w Boomerang X (Unity 2020.1.17). Twórcy BepInEksa uznają to za zachowanie oczekiwane
i odsyłają do instalacji z kompletem pełnych bibliotek silnika
([issue #1312](https://github.com/BepInEx/BepInEx/issues/1312)).

**Podstawianie bibliotek przez `dll_search_path_override` nie działa** — sprawdzone
w obu grach, i z samą `mscorlib`, i z kompletem kilkunastu bibliotek: gra staje przed
pierwszym ekranem, bez logu i bez awarii. Prawdziwe odchudzanie na odwrót wymaga
podmiany plików w katalogu `Managed` gry, czyli łamie zasadę powyżej.

**Próba obejścia wyczerpana.** `tools/loader/notgeeseLoader.cs` zastępuje punkt wejścia
BepInEksa i pomija to wywołanie — działa, ale odsłania kolejne braki: najpierw
`System.Linq.IGrouping` w `System.Core` (to akurat da się podstawić), potem konstruktor
`AmbiguousMatchException` w `mscorlib`, którego wymaga Harmony. To nie jeden brakujący
element, tylko cały wycięty runtime. Szczegóły w `games/boomerang-x/docs/technical.md`.

Zanim zaczniesz robić plugin, sprawdź dwie rzeczy w `<gra>_Data/Managed` — bez
uruchamiania gry i bez pisania linijki kodu:

1. czy `mscorlib.dll` zawiera ciąg `GetPEKind`;
2. czy `AmbiguousMatchException` ma w niej cztery konstruktory, czy trzy.

Brak pierwszego znaczy, że gra jest okrojona i preloader nie wstanie — to obchodzi nasz
punkt wejścia. Trzy konstruktory zamiast czterech znaczą, że nie wstanie też Harmony,
a tego nie obchodzi już nic: sprawdzone we wszystkich wydaniach BepInEksa od 5.4.17
do 6.0.0-be.788. Wtedy zostaje podmiana plików.

## Pliki i praktyka

- Każda gra ma katalog `games/<gra>/`. Przy kontynuacji najpierw przeczytaj jego
  `docs/technical.md` i sprawdź istniejące teksty oraz narzędzia, żeby podjąć pracę
  od aktualnego etapu.
- Każda gra ma jeden plik tłumaczenia, `translations/en-pl-review.json`
  (decyzje 0013 i 0021): lista wpisów z `key`, opcjonalnym `namespace`, `english`,
  `polish` i opcjonalnie `context`, `note`, `max_length`. Wzór:
  `games/shotgun-cop-man/translations/en-pl-review.json`. Z tego pliku czytają buildy
  (`tools/translations.py`) i pracownia korekty; innej kopii polskich tekstów w repo nie ma.
  Pusty `polish` przy niepustym `english` znaczy „jeszcze nieprzetłumaczone” — build
  zostawia wtedy oryginał. `tools/check_games.ts` pilnuje formatu wszystkich gier.
- Podział treści w katalogu gry jest sztywny, bo zasila też stronę w `site/`:
  `README.md` to wyłącznie instrukcja dla gracza, po polsku, wyświetlana w panelu gry
  na stronie: nagłówek `# <Gra> PL`, sekcja `## Instalacja` z ponumerowanymi krokami
  i jeden akapit o usunięciu lub przywróceniu. Nic dla dewelopera — wzór:
  `games/shotgun-cop-man/README.md`. Treść bierze się z instrukcji w aktualnej paczce.
  `docs/technical.md` na ustalenia techniczne, budowanie, stan testów i notę o materiale
  gry, `game.yaml` na liczby, status testu, linki do sklepów (`stores`) i przetestowaną
  wersję gry (`tested_on`: sklep i wersja z GOG Galaxy lub z menu gry),
  `games/catalog.yaml` na status spolszczenia i datę dodania. Główny `README.md` repozytorium jest
  po angielsku, dla przypadkowego czytelnika z GitHuba.
- Decyzje otwarte i rozważane warianty trzymamy w `docs/decisions/`, po jednym pliku
  na temat. Zanim zaproponujesz zmianę sposobu dostarczania spolszczeń, przeczytaj,
  co już zostało tam rozważone i odrzucone.
- Korzystaj z istniejących narzędzi i układu katalogów, gdy pasują. Szczegóły techniczne
  są w `docs/adding-a-game.md`; nie rozbudowuj konwencji ani infrastruktury bez potrzeby.
- Zachowuj oryginały przed podmianą plików gry. Buduj do osobnego katalogu (`dist/`),
  a instalację do testów wykonuj z kopią zapasową umożliwiającą powrót do oryginału.
- Zapisuj istotne ustalenia i następny krok w `docs/technical.md` gry. Rozróżniaj weryfikację plików
  od faktycznego testu w uruchomionej grze.
- Nie uruchamiaj gry za użytkownika. Jeśli potrzebujesz feedbacku wizualnego, podaj
  konkretne kroki testu i wskaż, co ma być widoczne na screenach. Użytkownik sam
  uruchomi grę i prześle screeny; poczekaj na nie przed oceną wyniku testu.
- Pracujemy bezpośrednio w tym repo. Nie organizuj pracy wokół branchy,
  worktree, PR-ów ani konwencji commitów, chyba że użytkownik o to poprosi.
