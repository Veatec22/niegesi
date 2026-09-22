# Skate Story — technika i stan prac

## Wersja 0.3 — przegląd skillem lokalizacji (2026-09-22)

Tłumaczenie przeszło standard `.claude/skills/lokalizacja`: biblia
(`translations/biblia.yaml`), raport (`work/l10n-report.md`), lektura całej narracji
i dialogów, spis decyzji w `docs/decyzje-tlumaczenia.md`. Zmieniono 19 wpisów.
Fonty, format i sposób dostarczania bez zmian.

Tabela I2 ma kolumny TYPE (mówiący, np. `Dialogue: Rabbie`), NOTES i 17 języków.
`work/ref-extract.py` zrzuca je do `work/ref-all.json` (poza gitem), a
`work/plec-ru.py` porównuje formy rodzajowe RU z PL — tak znalazły się Beea
i szkielet z Placu Żalu:

```powershell
.venv\Scripts\python.exe games\skate-story\work\ref-extract.py backups\skate-story\resources.assets
.venv\Scripts\python.exe games\skate-story\work\plec-ru.py
```

Wynik 0.3: SHA-256 pliku
`d4998be2e0cfca842f833577e7b86ffd092ad0288d88901e88f2fdfecea28994`, łatka 78 KB,
paczka `Skate-Story-PL-0.3-latka.zip`. Łatkę nałożoną na kopię oryginału sprawdzono
bajtowo z buildem. Aplikator aktualizuje 0.2 z odłożonego oryginału. W grze 0.3 nie
testowano — zmiany są wyłącznie tekstowe.

## Wersja 0.2

2305/2305 wpisów tekstowych ma docelową wartość PL: 2302 opracowane przez agenta
i 3 istniejące teksty polskie (nazwa języka i ostrzeżenie zdrowotne).
Nazwy własne, nazwy części trików i wielokropki pozostają bez zmiany tam, gdzie
jest to zamierzone. Przekład obejmuje całą tabelę lokalizacji, także treści demo
i debugowania. Nie obejmuje napisów wypalonych w teksturach ani modeli liter.

Użytkownik potwierdził działanie verticala przed zgodą na pełne tłumaczenie.
Pełną wersję sprawdzono w plikach; nie oznacza to testu całej kampanii.
Agent nie uruchamia gry. Następny krok to test użytkownika na istniejącym zapisie.

## Źródło i format

Lokalne wydanie GOG: `C:/Games/Skate Story/SkateStory_Data`.
Unity 6000.0.45f1, Mono, I2 Localization. `resources.assets`, MonoBehaviour 785,
2314 rekordów: 2305 tekstów i 9 odwołań do fontów. 20 kolumn, polski pod indeksem
15 (`Polish`, `pl`). Oryginalnie wyłączony; vertical włączył go w istniejącym
selektorze. Inne kolumny, w tym metadane, pozostają nienaruszone.

Oryginał SHA-256:
`3e65be29272f5879bd907a0d0c7f8134f5b5bd35902263dc65381bb0c3a7a82c`.
Potwierdzony vertical:
`ceb51c95fe43d61ad28fccce0c6834576c9c747f3bb2ad14cbd57022f7b8cd0c`.
Pełne tłumaczenie 0.2:
`a497a2f5ad82241d782df5f95a3b73acd666456eaa7253d2dba2b37f2023b340`.

## Fonty

Polski używa istniejącego dynamicznego `ru-serif-bigcaslon Regular` zamiast
BigCaslon/Cochin, istniejących IMFell dla ich stylów oraz LiberationSans zamiast
HelveticaRounded. Statyczny LiberationSans SDF 791 korzysta z istniejącego
dynamicznego fallbacku 789. Do listy zasobów I2 dopisano Font 566 i TMP 791.
Wypełniono wszystkie 9 referencji PL. Inne języki zachowują swoje fonty.
Żaden obiekt fontu ani kod wykonywalny nie jest modyfikowany.

Pełne 0.2 ma identyczne fonty, rejestr zasobów i konfigurację języków jak vertical.
Zmieniło się 2079 wartości tekstowych PL; wszystkie pozostałe obiekty zasobów
są identyczne. Znaki polskie i fonty zostały zaakceptowane w teście verticala.

## Budowanie i walidacja

Wymagania w głównym `requirements.txt`, m.in. UnityPy i TypeTreeGeneratorAPI.
Generator odczytuje metadane DLL, nie uruchamia gry.

```powershell
.venv/Scripts/python.exe games/skate-story/tools/build.py --original backups/skate-story/resources.assets --managed "C:/Games/Skate Story/SkateStory_Data/Managed" --extract
.venv/Scripts/python.exe games/skate-story/tools/review.py
.venv/Scripts/python.exe games/skate-story/tools/build.py --original backups/skate-story/resources.assets --managed "C:/Games/Skate Story/SkateStory_Data/Managed"
```

`--extract` synchronizuje review z `pl.json` i `review-notes.json`. Domyślny build
wymaga ich zgodności oraz pełnego pokrycia kluczy. Sprawdza SHA źródła, dokładny
round-trip tabeli, znaczniki (także `(S)` i `(C)`), liczbę nowych linii, fonty,
ponowny odczyt wyjścia, zmianę wyłącznie obiektu 785 i zachowanie 19 innych kolumn.
ZIP jest otwierany ponownie, sprawdzany CRC i porównywany bajtowo z plikiem wynikowym.

Wynik: `dist/SkateStory_Data/resources.assets` oraz `dist/skate-story-pl-0.2.zip`
z `SkateStory_Data/resources.assets` i `READ-ME.txt`. Build nie instaluje gry.

## Instalacja i kopie

- Oryginał: `backups/skate-story/resources.assets` od głównego katalogu repo.
- Potwierdzony vertical: `backups/skate-story-vertical/resources.assets`.
- Nie należy mieszać tych katalogów: każdy osobno nadaje się do `--restore`.

```powershell
.venv/Scripts/python.exe tools/install.py --game "C:/Games/Skate Story/SkateStory_Data" --built games/skate-story/dist/SkateStory_Data --backup backups/skate-story
# Powrót do oryginału przy zamkniętej grze:
.venv/Scripts/python.exe tools/install.py --game "C:/Games/Skate Story/SkateStory_Data" --backup backups/skate-story --restore
```

Pełne 0.2 zainstalowano 20 września 2026. Zgodność pliku w instalacji z wynikiem
buildu sprawdzono bajtowo; zachowano obie opisane wyżej kopie. Gra nie była uruchamiana.

## Terminologia i korekta

Skater = Skejter; underworld = podziemie; Crest = pieczęć; Moon = Księżyc;
Moon Vision = Księżycowy Wzrok; combo = kombo; stomp = tupnięcie;
Thinkpiece = Myślokształt; Soulflower = duszokwiat; Moonflower = Księżycowy Kwiat;
Fuss = Zgiełk; Blood Seer = Krwawy Wieszcz; Sloucher = Garbus;
Eternal Centipede = Wieczna Stonoga; Oblivion = Zapomnienie.
Nazwy trików ollie, kickflip, heelflip, revert, manual i grind zachowano.

21 wpisów z uwagami w `translations/review-notes.json` trafia do JSON i HTML EN/PL.
Do oceny przede wszystkim poezja, rymy Philoso, gra słów przez telefon,
Myślokształt/Garbus oraz litery HOUSE/CHEESE w świecie. Dialogi i opisy podają
oryginalne słowo z liter oraz znaczenie DOM/SER. Nie zmieniamy modeli liter.

[Wcześniejsze rozpoznanie](../../../docs/research/2026-09-20-skate-story.md).

## Metoda pluginowa — dlaczego nie weszła (20 września 2026)

Próba przeniesienia spolszczenia z podmiany `resources.assets` na plugin BepInEx
zakończyła się niepowodzeniem. Zapis ustaleń, żeby nie powtarzać drogi.

Plugin sam w sobie jest gotowy i kompiluje się poprawnie: `plugin/Plugin.cs` włącza
wyłączony slot 15, wypełnia 2305 tekstów z `pl.tsv` i przestawia 9 referencji czcionek
z `fonts.tsv` (mapa importowana wprost z `tools/build.py`, jedno źródło prawdy).
Buduje to `tools/build_plugin.py`; paczka wychodzi 740 KB zamiast 161 MB.

Blokada jest po stronie loadera, nie tłumaczenia:

- Doorstop wchodzi bez zarzutu — log potwierdza przejęcie `mono_jit_init_version`,
  podmianę ścieżek i otwarcie preloadera.
- Wywraca się preloader BepInEksa, w wersji 5 i 6 tak samo:
  `MissingMethodException: System.Reflection.Module.GetPEKind`. Metoda jest wołana
  w `PlatformUtils.SetPlatform` wyłącznie po to, by wykryć procesor ARM.
- Unity 6 okraja `mscorlib` z nieużywanych metod przy budowaniu gry i `GetPEKind` wypada.
- Twórcy BepInEksa uznają to za zachowanie oczekiwane, nie błąd:
  https://github.com/BepInEx/BepInEx/issues/1312 — zalecają instalację
  „BepInEx with corlibs", czyli komplet pełnych bibliotek dla danej wersji silnika.

Podstawienie **samej** `mscorlib` przez `dll_search_path_override` nie wystarcza:
gra zawiesza się przed ekranem ostrzeżenia, bez logu i bez awarii, bo Mono dostaje
pełną `mscorlib` obok okrojonych `System.dll` i `System.Core.dll`.

Następna próba, gdy wrócimy do tematu: **komplet corlibs**, nie pojedynczy plik.
Pełny zestaw dla 6000.0.45 jest w `vendor/unity-corlibs/6000.0.45.zip`
(15 MB po rozpakowaniu, z serwera BepInEksa). Do rozstrzygnięcia zostaje wtedy,
czy rozprowadzanie kompletu bibliotek wykonawczych Unity mieści się w naszych zasadach
— biblioteki są zbudowane z klas Mono na licencji MIT, ale to i tak trzeci podmiot w paczce.
Alternatywa bez corlibs: własna wersja BepInEksa z usuniętą tą jedną linijką.

Do tego czasu obowiązuje metoda z podmianą `resources.assets` opisana wyżej.

### Próba z kompletem corlibs — również nieudana

Podstawienie **wszystkich 15 bibliotek** z `vendor/unity-corlibs/6000.0.45.zip`
przez `dll_search_path_override` daje ten sam skutek co sama `mscorlib`: gra staje
przed ekranem ostrzeżenia, bez logu i bez awarii. Hipoteza o niezgodności między
pełną `mscorlib` a okrojoną resztą była więc błędna — problem leży głębiej.

Tym samym droga „bez dotykania plików gry" jest dla tej gry wyczerpana. Pozostają
dwie opcje, obie do świadomej decyzji, nie do przypadkowego wyboru przez agenta:
podmiana bibliotek wprost w `SkateStory_Data/Managed` (łamie zasadę z AGENTS.md)
albo własna wersja BepInEksa bez wywołania `GetPEKind`.

### Własny punkt wejścia też nie pomoże — sprawdzone statycznie (21 września 2026)

Po tym, jak `tools/loader/NieGesiLoader.cs` przeszedł dalej w Boomerang X, sprawdziliśmy,
czy Skate Story nie jest okrojone łagodniej. Test statyczny, bez uruchamiania gry:

| element | Boomerang X | Skate Story | Anger Foot (działa) |
| --- | --- | --- | --- |
| `Module.GetPEKind` w `mscorlib` | brak | brak | jest |
| `System.Linq.IGrouping` w `System.Core` | brak | **jest** | jest |
| `AmbiguousMatchException..ctor(string, Exception)` | **brak** | **brak** | jest |

Skate Story jest okrojone łagodniej niż Boomerang X — ma `IGrouping`, więc drugi
problem go nie dotyczy. Ale trzeciego, decydującego, brakuje tak samo: pełny .NET
ma cztery konstruktory `AmbiguousMatchException`, obie gry mają trzy, i za każdym
razem wypada ten sam — `(string, Exception)`.

Tego konstruktora wymaga statyczny konstruktor `HarmonyLib.AccessTools`, a bez
`AccessTools` nie działa nic w Harmonym. Sprawdziliśmy **wszystkie wydania BepInEksa
od 5.4.17 (2021) do 6.0.0-be.788**: każde niesie Harmony odwołujące się do tego
konstruktora, i każde woła `GetPEKind` w preloaderze. Starsza wersja nie jest wyjściem.

Zostaje jedno: **przebudowa Harmony'ego bez tego odwołania.** Harmony jest na licencji
MIT, więc prawnie to żaden problem, ale wymaga .NET SDK i utrzymywania forka biblioteki,
od której zależy całe BepInEx. To już nie jest obejście, tylko własna gałąź cudzego
projektu — decyzja na osobną rozmowę, nie do podjęcia mimochodem.

Do tego czasu Skate Story zostaje przy podmianie `resources.assets`. Zmierzona łatka
różnicowa wobec oryginału to **2,4 MB** przy 275 MB pliku (format 1, zstd; od formatu 2 — **78 KB**), więc gdyby wracać do tematu
publikacji tej gry, to właśnie tamtędy.

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „Skate Story — spolszczenie”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

Pełne spolszczenie tekstów Skate Story: dialogi wszystkich rozdziałów i epilogu,
samouczki, menu, ekwipunek, cele, osiągnięcia oraz poetyckie podsumowania.
Polski jest osobnym językiem w ustawieniach gry.

Przy zamkniętej grze zachowaj oryginalny `SkateStory_Data/resources.assets`,
a następnie wypakuj [paczkę ZIP](../dist/skate-story-pl-0.2.zip) do katalogu gry.
Uruchom grę samodzielnie i wybierz **Polski** w ustawieniach.
Pełna [instrukcja instalacji i przywrócenia](../docs/INSTALL.txt).

Vertical został potwierdzony przez użytkownika. Pełna tabela ma 2305/2305 wpisów;
cała kampania czeka na sprawdzenie w rozgrywce. Następny krok: kontynuacja zapisu,
kontrola dłuższych dialogów, sklepu i celów. Tekstury z napisami nie są zmieniane.

[Korekta EN/PL w przeglądarce](../translations/en-pl-review.html) ·
[JSON EN/PL](../translations/en-pl-review.json) · [Polskie teksty](../translations/pl.json).
21 wpisów ma uwagi do korekty, przede wszystkim literackiej.

[Szczegóły techniczne, build i kopie zapasowe](../docs/technika.md) ·
[Metadane](../game.yaml).
