# Boomerang X — technika i stan prac

## Stan: próbka 0.1 metodą łatania bajtów

38 z 360 wpisów przetłumaczonych. W grze działa wersja podmieniająca
`Assembly-CSharp.dll` (1,8 MB) — opis metody w docstringu `tools/build.py`.

## Metoda pluginowa — zablokowana (20 września 2026)

Plugin jest napisany i kompiluje się poprawnie (`plugin/Plugin.cs`,
`tools/build_plugin.py`). Zastępuje trzy łatki na bajtach trzema łatkami Harmony'ego:

- `localization_manager.get_translation` — podaje nasz tekst zamiast
  „LOCALIZATION ERROR"; dla wpisów nieprzetłumaczonych wraca do angielskiego.
  Uwaga: metoda bierze **cały wiersz tabeli**, nie nazwę tekstu, więc kluczem jest
  `phrase.id`.
- `font_manager.get_font` — podmienia język na rosyjski, jedyny krój z ogonkami.
- `options_screen.on_reading_save_complete` — dopisuje jedenastą pozycję do listy
  języków, przez refleksję, więc działa i z TMP_Dropdown, i ze zwykłym.

Plugin nie rusza pola `description`, które przy łataniu bajtów musiało udawać kolumnę
polską. Nie wymaga też wymieniania notatek między wierszami, żeby tekst się zmieścił.

**Blokadą jest okrojony `mscorlib`.** Gra jest zbudowana z managed strippingiem, więc
preloader BepInEksa wywraca się na `Module.GetPEKind` — dokładnie tak samo jak
Skate Story, mimo że to Unity 2020.1, a tamto Unity 6. Podstawienie kompletu pełnych
bibliotek Unity 2020.1.17 przez `dll_search_path_override` zawiesza grę przed pierwszym
ekranem, identycznie jak w Skate Story.

Wniosek wspólny dla obu gier: droga przez podstawianie bibliotek jest zamknięta.
Pozostaje własna wersja BepInEksa bez tego wywołania albo własny punkt wejścia,
który pomija wykrywanie platformy. Do decyzji.

## Własny punkt wejścia — działa, ale okrajanie sięga głębiej (21 września 2026)

`tools/loader/NieGesiLoader.cs` to nasz zamiennik punktu wejścia BepInEksa: odtwarza
jego `PreloaderRunner.PreloaderPreMain` krok po kroku, tylko platformę ustala sam,
bez `Module.GetPEKind`. Całość idzie przez refleksję, więc biblioteka nie kompiluje się
przeciw BepInEksowi i nie zawiera ani linijki jego kodu.

**Sam punkt wejścia działa bez zarzutu.** Kolejne uruchomienia przechodziły coraz dalej,
za każdym razem wywracając się na następnym elemencie wyciętym z runtime'u gry:

1. `Module.GetPEKind` w `mscorlib` — obejście: nasz punkt wejścia. **Przeszło.**
2. `System.Linq.IGrouping` w `System.Core` — obejście: podstawienie tej jednej
   biblioteki przez `dll_search_path_override`. **Przeszło**, powstał `BepInEx/config`.
3. `AmbiguousMatchException..ctor(string, Exception)` w `mscorlib` — potrzebne
   statycznemu konstruktorowi `HarmonyLib.AccessTools`. **Ściana.**

Trzeciej pozycji nie da się obejść naszą drogą: brakujący element siedzi w `mscorlib`,
a podstawienie pełnej `mscorlib` zawiesza grę przed pierwszym ekranem (sprawdzone tu
i w Skate Story, osobno i w komplecie kilkunastu bibliotek).

Wniosek: **to nie jest jeden brakujący element, tylko cały wycięty runtime.** BepInEx
i Harmony zakładają pełne środowisko .NET; gra budowana z managed strippingiem go nie ma.
Każde obejście odsłania następny brak. Dokładanie bibliotek po jednej to wyliczanka
bez końca, a podstawienie całego rdzenia gra odrzuca.

Co zostaje, gdyby ktoś chciał wrócić do tematu:

- własna wersja BepInEksa i Harmony'ego zbudowana pod okrojony profil — duży projekt,
  wymaga .NET SDK i utrzymywania forka dwóch bibliotek;
- inny mod loader, który nie wymaga pełnego runtime'u (niesprawdzone);
- zostawienie tych gier przy podmianie plików.

Boomerang X zostaje przy próbce 0.1 z łataniem bajtów. Punkt wejścia zostaje w repo,
bo jest sprawny i może się przydać przy grze okrojonej mniej agresywnie.

## Wersja 1.0 — pełne tłumaczenie i dostarczanie łatką (21 września 2026)

359 z 360 wierszy tabeli. Jednego nie da się pokryć osobno, bo **tabela gry ma
zduplikowany klucz** `difficulty_select_prompt` z dwoma różnymi tekstami; oba
dostają to samo polskie zdanie, które pasuje w obu miejscach.

Terminologia mocy: Flux → **Strumień**, Slingshot → **Zryw**, Scattershot →
**Odłamki**, Needle → **Igła**, Blaze → **Żar**, Oblivion Comet →
**Kometa Zapomnienia**.

Tepan mówi bez rodzaju gramatycznego. W oryginale jest konsekwentnie „they",
a polszczyzna wymusza wybór przy każdym czasie przeszłym — kwestie są przepisane
tak, żeby wyboru nie robić („udało mi się zobaczyć" zamiast „widziałem").
To decyzja literacka do potwierdzenia przy korekcie.

Pojemność notatek to 55 843 znaki przy potrzebie około 18 000, więc miejsca jest
z zapasem. 42 wiersze nie mieściły się we własnej notatce i pożyczyły miejsce
od innych — `lend_room` układa to sam.

### Dostarczanie

Plik po spolszczeniu **waży dokładnie tyle co oryginał**, bajt w bajt: 1 806 336 B.
Każda poprawka jest wpisywana na miejsce bajtów tej samej długości, a teksty wchodzą
do istniejących literałów, dopełniane spacjami.

Paczka z całym plikiem ważyłaby 580 KB, ale byłaby w całości cudzym kodem z naszymi
napisami w środku — czyli dokładnie tym, czego zabrania zasada z `AGENTS.md`.
Dlatego wysyłamy **łatki różnicowe: 14 KB na kod i 753 B na czcionki**.

```powershell
.venv\Scripts\python.exe games\boomerang-x\tools\build.py --source backups\boomerang-x\BOOMERANG X_Data\Managed\Assembly-CSharp.dll
.venv\Scripts\python.exe games\boomerang-x\tools\fonts.py --source backups\boomerang-x
.venv\Scripts\python.exe tools\patch.py release --original "backups\boomerang-x\BOOMERANG X_Data\Managed\Assembly-CSharp.dll" --built "games\boomerang-x\dist\BOOMERANG X_Data\Managed\Assembly-CSharp.dll" --relative "BOOMERANG X_Data/Managed/Assembly-CSharp.dll" --original "backups\boomerang-x\BOOMERANG X_Data\resources.assets" --built "games\boomerang-x\dist\BOOMERANG X_Data\resources.assets" --relative "BOOMERANG X_Data/resources.assets" --readme games\boomerang-x\docs\INSTALL-patch.txt --out-dir games\boomerang-x\dist --game-name boomerang-x --package-name Boomerang-X --version 1.0
```

`build.py` nie składa już archiwum — od paczki jest `tools/patch.py release`,
ten sam dla wszystkich gier dostarczanych łatką.

**Paczka ma dwie łatki i obie są konieczne.** Kod z `build.py` przestawia polski
na krój rosyjski, ale przyciski kategorii w opcjach zostają na `Dead Stock SDF`
i `Abys-Regular SDF`, które mają z polskich liter tylko `ł ó`. Bez fallbacku
z `fonts.py` (w `resources.assets`) są tam kwadraty. Wyszło 21.09, gdy pierwsze
wydanie z samym DLL-em trafiło na czystą grę: wcześniejsze testy szły
z `resources.assets` już przerobionym przez `fonts.py` i to maskowało brak.
