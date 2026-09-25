# Heat Signature — rozpoznanie techniczne

## Pełne tłumaczenie 0.2.0 — 2026-09-25

Vertical 0.1.2 potwierdzony w grze przez użytkownika (screen menu pauzy: polskie
litery, poprawne odstępy). Zlecenie: full.

**Ekstrakcja z kontekstem.** `tools/extract_strings.py` czyta tabelę
`{nazwa gml_*, adres funkcji}` z `.data` (2585 funkcji GML), wyznacza koniec
każdej funkcji (ret + wyrównanie `CC` do 16 B, bo kod runnera przeplata się
z GML) i przypisuje każdy literał do funkcji, której kod ładuje jego adres jako
stałą. Wynik: `work/strings.json` (9999 literałów), `work/strings-by-function.txt`.
Logi diagnostyczne odsiano ręcznie przy przeglądzie całej listy.

**Silnik tłumaczenia** — `plugin/Translate.h`, czysty C++, testowany
`tools/test_translate.py`. Kolejność: wpis dokładny → wersja WERSALIKAMI →
nazwa przedmiotu (rzeczownik + przymiotniki zgodne w rodzaju, `items.json`) →
szablon z lukami `{0}`..`{9}` (luki tłumaczone rekurencyjnie) → tłumaczenie
wierszy (`#`, `\r\n`) → nazwa ucięta „...” (ostatnie pełne nazwy) → fragmenty
na granicach słów. Pamięć podręczna wyników; nieprzetłumaczone trafiają do logu,
chyba że wyglądają na polski tekst (ogonki, prefiks znanego polskiego wiersza).
`pl.tsv` ma wiersze typowane: E, D (dialog), T, N, A, P. Tokeny dialogów
`<PlayerName>` build zamienia na luki szablonów.

**Dialogi przy wczytaniu.** Hook `kernel32!CreateFileW/A` rozpoznaje otwarcie
`Dialog\<nazwa>.txt` do odczytu i podaje grze kopię `NieGesi/cache/Dialog/<nazwa>.txt`
zrobioną z pliku gracza: tłumaczone są tylko wypowiedzi, zostają `[Blok]`, `#`,
`=`, `{Cel}`, `<Token>`, BOM i CRLF; odpowiedzi w całości w nawiasach
(`[Continue]`) zostają dla logiki gry. Wcześniejsze dopasowywanie prefiksów
wypisywanego tekstu usunięto — łapało też zwykłe napisy (luka „Sovereign”
jako początek kwestii dialogowej). Błąd kopii → oryginalny plik. Log:
„Dialog X.txt: n of m lines translated”. Na plikach z tej instalacji 661 z 662
linii (reszta to sam token `<ProblemDescription>`).

**Weryfikacja bez gry:** test silnika (w tym plik dialogu z BOM/CRLF/tokenami),
podgląd 189 napisów z logów sesji użytkownika i złożonych przykładów
(`work/preview-out.txt`, 20 bez zmian — imiona i nazwy własne), wszystkie
wiersze `pl.tsv` przyjęte, test zabezpieczeń fontów, raport kontrolny
(`work/l10n-report.md`: brak błędów tokenów i płci; zgłoszenia spójności to
zamierzone różnice etykieta/przymiotnik). Build ZIP 479 227 B (po poprawkach z przeglądu i decyzjach użytkownika).

**Nie sprawdzono w grze:** czy runner otwiera dialogi przez CreateFile (log
powie), czy szablony pokrywają wszystkie składane zdania (log „Untranslated”),
długość tekstów w ciasnych polach UI. Pominięto minigrę naprawy `oProblem`
(losowe zestawienia słów) i komunikaty diagnostyczne.

**Instalacja:** 0.2.0 zainstalowane 2026-09-25 przez `tools/install.py`
(manifest w `backups/`), EXE i 13 plików Dialog bez zmian. Paczka 0.1.2
wycofana do `work/`, na stronie leży 0.2.0.

**Przegląd językowy:** wykonany przez osobnego agenta, pewne poprawki naniesione (`docs/localization-review.md`); 6 tematów rozstrzygnął użytkownik (partia `parts/95-user.json`).

**Następny krok:**
i test w grze — rozmowa w barze, ekwipunek, tablica misji, dziennik pod B;
potem log `Untranslated` do uzupełnienia szablonów.

Budowanie (kolejność):

```powershell
.venv\Scripts\python.exe games\heat-signature\tools\gen_personal.py
.venv\Scripts\python.exe games\heat-signature\tools\assemble.py
.venv\Scripts\python.exe games\heat-signature\tools\build_plugin.py
.venv\Scripts\python.exe games\heat-signature\tools\test_translate.py --tsv --dialogs "C:\SteamLibrary\steamapps\common\Heat Signature\Dialog"
```

`assemble.py` składa `pl.json` z kluczy verticala i partii; korekty użytkownika
zapisywać w partii (np. `parts/95-user.json`), bo inne klucze znikną.

## Poprawka 0.1.2 — odstępy między literami

2026-09-25 test 0.1.1: napisy wróciły („Ekwipunek” poprawnie), ale między literami
były ogromne przerwy. Log 0.1.1 zachowano w `work/wide-spacing-0.1.1.log`.

Przyczyna z disassembly konstruktora sprite fontu (`work/disasm-font.py`): glif to
8 × int16 — `[0]` znak, `[3]` klatka, `[4]` wysokość sprite'a, `[5]` przesunięcie
pióra, `[6]` offset rysowania. W trybie proporcjonalnym `[5]` liczy się z ramki
klatki; sprite z `sprite_add` nie ma ramek per klatka (brak danych pod +0x54),
więc każda litera dostaje szerokość całej komórki atlasu.

0.1.2: `font_assets.py` zapisuje obok PNG plik `.metrics` (znak, klatka,
przesunięcie, offset, wysokość). Plugin po `font_add_sprite_ext` sprawdza całą
mapę glifów (znak, klatka, wysokość, liczba) i dopiero wtedy nadpisuje `[5]` i `[6]`
wyłącznie w fontach, które sam utworzył. Następnie mierzy przez `string_width`
każdy znak i wymaga, by „i” było węższe od „W”; inaczej zostaje oryginał i EN.

Weryfikacja: `test_font_guard.py` przechodzi (zmienne szerokości zamiast pełnej
komórki, fallback przy złym układzie). Symulacja składania tekstu z tych samych
PNG i metryk według układu z disassembly dała naturalne odstępy we wszystkich
rozmiarach. Instalacja, `dist/` i ZIP 0.1.2 są bajtowo zgodne. ZIP 0.1.1 wycofany
do `work/`, na stronie leży 0.1.2. **Test w grze 0.1.2 czeka na użytkownika.**

## Poprawka 0.1.1 — po nieudanym teście 0.1.0

2026-09-25 użytkownik uruchomił 0.1.0: dwa screeny pokazują puste pola tekstowe
w HUD i menu, przy działających sprite'ach. **Vertical 0.1.0 nie działał.**
Log zachowano w `work/failed-0.1.0.log`. Odczyt pamięci uruchomionej gry był
wyłącznie diagnostyczny, bez zapisu i bez uruchamiania gry przez agenta.

Ustalenia z pamięci: nowe fonty 19–37 miały zerowe wymiary, wysokość wiersza,
liczbę glifów i wskaźnik glifów. Oryginalne fonty 0–18 miały po 96 glifów.
Przyczyną było uznanie dodatniego identyfikatora z `font_add` za sukces.
Disassembly potwierdza, że użyta ścieżka fontów odczytuje plik, a nie rodzinę
Windows „Arial”; dodatkowo konstruktor ogranicza ostatni znak do 255.
Słownik był przechwytywany, ale wszystkie napisy rysowano pustymi fontami.

0.1.1 korzysta z `sprite_add` i `font_add_sprite_ext`, odnajdywanych po nazwach.
Mapa UTF-8 obejmuje 120 znaków (ASCII, wszystkie polskie litery i interpunkcję).
13 wariantów rasteryzowanych z otwartego Xolonium 4.3 zastępuje 19 fontów gry.
Źródło i licencja OFL są w `fonts/README.md`; build nie czyta atlasów gry.
Kursywa jest syntetyczna. Wysokość wierszy i odstępy wymagają oceny na ekranie.

Przed aktywacją plugin sprawdza liczbę klatek sprite'a i mierzy każdy znak
przez funkcje silnika. `#` pomija w pomiarze, bo GameMaker interpretuje go jako
nową linię. Błąd zachowuje oryginalny font i angielskie teksty. Log jest teraz
otwierany ze współdzieleniem odczytu, więc nie trzeba zamykać gry, by go czytać.

Weryfikacja: test starego kodu odtworzył przyjęcie pustego fontu po samym ID
(`FAIL: empty font accepted solely by ID`). `tools/test_font_guard.py` sprawdza
rzeczywisty kod ładowania z odpowiedziami funkcji silnika: zerowe metryki,
brak polskiej litery i błędna liczba klatek przywracają oryginalny font i EN;
dodatnie metryki dopuszczają PL. To test zabezpieczenia, **nie renderowania GPU**.
Przeszły też statyczna walidacja nowych funkcji w EXE, test dopasowania tekstów,
proxy Direct3D oraz build ZIP z jawną listą 19 plików. Obejrzano podgląd glifów
z wygenerowanych PNG, lecz nie z działającej gry. Zgodnie z zasadą repo testu
wizualnego nie automatyzowano przez uruchomienie gry; musi wykonać go użytkownik.

Zainstalowano 0.1.1, zachowując manifest przywracania. EXE i wszystkie 13 plików
dialogów mają niezmienione SHA-256. ZIP 340 221 bajtów zastąpił wadliwy 0.1.0
w lokalnym `site/public/pobierz/`. Nie publikowano strony na serwerze.

**Następny krok:** użytkownik uruchamia grę, sprawdza napisy w HUD, menu pod Esc
i trzyma F8, aby wyświetlić komplet polskich liter. Potrzebny screen menu i HUD.
Angielski tekst może oznaczać zadziałanie zabezpieczenia; sprawdzić wtedy log.
Nie oznaczać verticala jako działającego przed nowym testem użytkownika.

## Historia: próbka 0.1.0 — pierwotne przekazanie do testu

2026-09-25: użytkownik wybrał wygładzenie niepoprawnej mowy terminala. Ustalenie
zapisano w biblii i `translation-decisions.md`; terminal mówi teraz poprawnie,
np. „TRENING ROZPOCZĘTY”. Pozostałe dialogi zachowują suchy humor.

Przygotowano 163 wpisy (113 literałów EXE i 50 tekstów dialogowych), EN/PL
zsynchronizowane. Zakres: menu/pauza, część ustawień, pierwsza narracja Fiasco,
instrukcje samouczka, rozmowa po samouczku i terminal treningowy. Pozostałe
elementy pozostają po angielsku. Liczba 163 nie jest liczbą tekstów pełnej gry.

Build tworzy `dist/Heat-Signature-PL-0.1.0.zip` (132 431 bajtów) z czterema
plikami: `d3d9.dll`, `NieGesi/pl.tsv`, `NieGesi/LICENSE-MINHOOK.txt`, `READ-ME.txt`.
Pakiet zawiera własny kod, teksty i MinHook na BSD; żadnych zasobów wydawcy ani
fontów Windows. Build używa jawnej listy dopuszczonych plików i sprawdza ZIP.
Kopia paczki jest w `site/public/pobierz/`; gra pozostaje w `w-trakcie`.
Wygenerowano okładkę i pięć screenów sklepowych poleceniem `tools/keyart.py`.
To ilustracje sklepu, nie dowód działania PL.

Zainstalowano cztery pliki w lokalnej instalacji Steam. Porównanie SHA-256
potwierdziło, że EXE i wszystkie 13 oryginalnych plików Dialog pozostały nietknięte.
Manifest stanu sprzed instalacji: `backups/heat-signature/plugin/manifest.json`.
W tej instalacji żadnego z czterech dodawanych plików wcześniej nie było.

Weryfikacja: build MSVC x86, statyczne sprawdzenie odkrywania funkcji w EXE,
test właściwego kodu C++ z dopasowaniem liczb/nazw stacji/białych znaków/CRLF,
zachowaniem nieznanych napisów i odczytem TSV; test proxy Direct3D bez gry.
Osobny proces z niepasującym EXE poprawnie zapisuje `Builtin discovery failed:
disabled`, a Direct3D nadal działa. Raport językowy: bez błędów znaczników,
pozostają trzy ostrzeżenia długości do oceny na ekranie.

**Test w Heat Signature nie został wykonany.** Nie uruchamiano gry.
Warunki próby i trzy potrzebne screeny opisuje `docs/INSTALL.txt`: menu z F8
(pełne `ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ` zamiast Wznów), ustawienia i pierwsza narracja/instrukcje.
Arial zmienia wygląd gry; to tymczasowy krój do potwierdzenia drogi technicznej.
Sprawdzić szczególnie tekst wyświetlany stopniowo, przechwycenie wszystkich
wariantów rysowania, pozycje kliknięć po zmianie szerokości i dłuższe podpowiedzi.
W razie niepowodzenia odczytać `NieGesi/LogOutput.log` z katalogu gry.

Budowanie i instalacja:

```powershell
.venv\Scripts\python.exe games\heat-signature\tools\build_plugin.py
.venv\Scripts\python.exe games\heat-signature\tools\install.py --game "C:\SteamLibrary\steamapps\common\Heat Signature"
.venv\Scripts\python.exe games\heat-signature\tools\install.py --game "C:\SteamLibrary\steamapps\common\Heat Signature" --restore
```

`prepare_ui.py` i `prepare_opening.py` dokumentują ekstrakcję i początkowy przekład.
Build czyta wyłącznie aktualne `translations/pl.json`; po korekcie użytkownika nie
uruchamiać ponownie skryptu `prepare_opening.py`, bo odtworzyłby początkowy przekład.
Przed pełnym tłumaczeniem potrzebne jest potwierdzenie tego verticala w grze.

Poniższe sekcje to historia przygotowania; ich wpisy o oczekiwaniu na wybór
użytkownika lub braku instalacji zostały zastąpione stanem opisanym powyżej.

## Przygotowanie próby pluginowej — 2026-09-25

Powstał własny plugin `plugin/Plugin.cpp`; nie wykorzystuje kodu znalezionego
HeatSignatureModLoader. Jego źródła służyły jako materiał do rozpoznania ABI.
Własne proxy `d3d9.dll` przekazuje wywołania do systemowego D3D9; inicjalizację
wykonuje przy Direct3DCreate9/Ex, poza DllMain, na wątku wywołującym.
MinHook 1.3.4 (BSD, plik LICENSE.txt) odpowiada za trampoliny.

Odkrycie: funkcja wspólnego podziału tekstu na wiersze dostaje UTF-8, sama tworzy
bufor UTF-16 i jest wołana przez pomiar szerokości oraz rysowanie. Można więc
podmienić tekst na tej granicy bez zmieniania identyfikatorów logiki gry,
EXE na dysku ani plików Dialog. Pokrycie wszystkich ekranów pozostaje do testu.

Plugin odnajduje rejestrację `draw_set_font`, `string_width`, `font_add` po nazwach,
potem sprawdza kształt instrukcji wrapperów i rozwiązuje względne wywołania.
Nie zawiera stałych adresów ani warunku sumy kontrolnej gry. Brak jednoznacznego
dopasowania wyłącza instalację hooków i pozostawia wpis w logu.
Podczas pierwszego wyboru fontu tworzy przez `font_add` odpowiedniki wszystkich
fontów w systemowym Arialu, z zakresem 32–383, oryginalnymi rozmiarami, pogrubieniem
i kursywą. Arial jest świadomym krojem diagnostycznym; wygląd Xolonium nie jest
zachowany. Nie pakujemy fontu Windows. Polskie renderowanie wymaga testu w grze.

Weryfikacja wykonana:
- `verify_hooks.py` potwierdził dopasowania ABI i odkrycie adresów w lokalnym EXE.
- Build DLL x86 przez MSVC zakończył się powodzeniem.
- Osobny program `work/build/ProxySmoke.exe` załadował proxy, wywołał
  D3DPERF_GetStatus i Direct3DCreate9, odczytał jeden adapter i zwolnił obiekt.
  To test przekazywania wywołań, **bez uruchamiania Heat Signature**.
- `prepare_ui.py` zweryfikował obecność 74 oryginałów EN w EXE i zapisał PL
  oraz zsynchronizowany plik review. To niezależna część UI/instrukcji.

Polecenia:

```powershell
.venv\Scripts\python.exe games\heat-signature\tools\verify_hooks.py "C:\SteamLibrary\steamapps\common\Heat Signature\Heat_Signature.exe"
.venv\Scripts\python.exe games\heat-signature\tools\build_plugin.py --binary-only
```

Budowanie wymaga MSVC x86 i źródeł MinHook z
https://github.com/TsudaKageyu/minhook/archive/refs/tags/v1.3.4.zip
rozpakowanych do `work/minhook-1.3.4/`. Wersja i LICENSE.txt muszą towarzyszyć
ewentualnej dystrybucji. Build pełnej paczki jest przygotowany, ale wymaga jeszcze
domknięcia narracyjnej części próbki oraz `docs/INSTALL.txt`.

**Następny krok:** odpowiedź na przedstawiony wybór języka terminala/suchego humoru;
następnie dopisać początek narracji, wykonać ZIP i instalację, podać użytkownikowi
kroki testu. Nie traktować przygotowanych 74 wpisów jako pełnego verticala.
Nie ma jeszcze paczki dla gracza ani instalacji. Lokalna gra pozostaje nietknięta.
Log docelowy: `NieGesi/LogOutput.log`; zawiera wersję pluginu, wersję PE gry,
silnik, wynik odkrywania, tworzenie fontów i liczbę zaobserwowanych nieprzetłumaczonych napisów.

Poniżej zachowano pierwotny raport analizy; jego uwagi o pustym zbiorze PL
i braku kodu buildu opisują etap sprzed powyższych prac.

Stan: 2026-09-25. Werdykt: warto podjąć próbę pluginową, trudność podwyższona.
To analiza plików, nie działające spolszczenie. Gry nie uruchamiano, niczego do niej
nie instalowano. Poszukiwanie PL pominięto na wyraźną prośbę użytkownika.

## Lokalna instalacja i dowody

- Steam: `C:\SteamLibrary\steamapps\common\Heat Signature`, appid 268130,
  buildid 6124596 z `appmanifest_268130.acf`.
- W EXE występuje wersja `2021.1.20.1`; nie potwierdzono jej w menu gry.
- `Heat_Signature.exe`: 73 653 760 bajtów, PE x86, GameMaker Studio / YYC.
  SHA-256: `a5f8befe28786206ed1e2a52385051049524fea51e9e80660e3115e7126274d2`.
  Suma dokumentuje wejście analizy, nie jest proponowanym warunkiem startu pluginu.
- W EXE, pod offsetem 17 597 096, znajduje się kontener FORM długości
  54 608 170 bajtów. CODE, VARI i FUNC są puste: kod gry jest natywny,
  nie ma bytecode'u do standardowej edycji GML.
- Przed FORM znaleziono 2566 różnych nazw funkcji `gml_*`.

## Teksty i ich wydobycie

1. `Dialog/*.txt`: 13 plików, 672 niepuste wiersze poza samymi etykietami
   bloków. To liczba surowych wierszy parsera, nie zatwierdzona liczba wpisów
   pełnego tłumaczenia. Obejmuje rozmowy barmanów czterech frakcji, Fiasco,
   terminal treningowy i zakończenie samouczka.
2. Składnia dialogów: `[Start]` i inne identyfikatory bloków; `#` odpowiedzi;
   `{EngageFiasco}` cele przejść; `<PersonalMissionCost>` i `<ProblemDescription>`
   podstawienia. Występuje też `=` na początku kolejnej kwestii. Znaczniki i
   odwołania zachować; pełną semantykę sprawdzić w parserze przed budowaniem.
3. Menu, tutorial, sprzęt, cele misji i komunikaty mają czytelne literały w EXE,
   poza FORM. Przykłady: `Restart tutorial`, `Needs Armour-Piercing Rounds`,
   `Armour-Piercing Shortblade`, `, kill no-one`.
4. Heurystyka znalazła 4468 wielowyrazowych kandydatów przed FORM; obejmuje
   diagnostykę, duplikaty i fragmenty. **Nie oznacza to 4468 tekstów do tłumaczenia.**
   Zwykły eksport STRG nie daje tekstów całej gry: STRG ma 2783 rekordy,
   w tym nazwy zasobów i kod shaderów.
5. `Forenames.txt` i `Surnames.txt` są dodatkowymi listami nazw. Ich zakres
   lokalizacyjny pozostaje do decyzji. Napisy zapisane w grafice wymagają osobnego
   przeglądu atlasów; raport fanowski wskazuje m.in. wskaźniki HUD.

Odtworzenie analizy (odczytuje grę, zapisuje tylko do `work/` w repo):

```powershell
.venv\Scripts\python.exe games\heat-signature\tools\inspect_game.py --game "C:\SteamLibrary\steamapps\common\Heat Signature"
```

Wyniki: `work/inspection.json`, `work/dialog-review.json`,
`work/native-candidates.json`. Wygenerowane dane gry są ignorowane przez Git.
`translations/en-pl-review.json` jest na razie pusty, tak samo jak zbiór PL:
surowych kandydatów nie przedstawiamy jako zatwierdzonego zakresu tłumaczenia.

## Polskie znaki

Odczytano FONT i rzeczywiste identyfikatory glifów: **wszystkie 19 fontów ma
96 glifów o kodach 32–127, bez ani jednej polskiej litery, również bez ó**.
18 fontów używa `XoloniumCustom`, debugowy `fDebugLarge` używa Arial.
Warianty mają rozmiary 8–64, różne pogrubienie, kursywę i antyaliasing.
Wśród nich są `fMenus`, `fMenuHeader`, `fInventory`, `fHelpText`, `fControlList`.

Sam UTF-8 w dialogach nie rozwiąże renderowania. Potrzebne są nowe glify i mapa
znaków albo fonty podmieniane w pamięci. W EXE są nazwy funkcji silnika `font_add`
i `font_add_sprite_ext`, lecz ich obecność nie dowodzi, że ich wywołanie z pluginu
oraz zastąpienie wszystkich używanych fontów jest już rozwiązane.
Najpierw sprawdzić font ładowany podczas działania i pomiar tekstu, potem dopiero
rozstrzygać, czy uzupełniać atlasy gry. Trzeba zachować czytelność małych rozmiarów.

## Plugin i ponowne wgranie

Istnieje natywny [HeatSignatureModLoader](https://github.com/piepieonline/HeatSignatureModLoader)
autorstwa piepieonline. To ważny dowód, że wpinanie DLL w tę grę jest praktyczną
drogą; nie dowodzi gotowej obsługi lokalizacji. Loader używa proxy D3D9,
MinHook i przechwyceń skryptów GML. Starszy opis na Nexus podaje jeszcze DXGI;
changelog wskazuje zamianę na D3D9.

W lokalnym EXE istnieją nazwy `LoadDialogFile`, `GetDialogTextBlock`,
`GetDialogResponseText`, `DrawTextInABox`, `DrawDescriptionText`,
`SetDescriptionTargetNameAndClausesForMission` i `SetProblemDescriptionForPersonalMission`.
Są też w tabeli skryptów loadera. To kandydaci do przechwycenia dialogów,
opisów i składania misji przed podziałem tekstu na wiersze. Ich sygnatury,
argumenty i pokrycie wymagają dalszego sprawdzenia.

**Loader nie jest jeszcze rozwiązaniem zgodnym z naszym standardem aktualizacji.**
`UniversalHooks.cpp` korzysta z tabeli stałych offsetów, a `ModLoader.cpp`
ma m.in. stałe adresy tablic funkcji silnika i dispatchera. Nazwa hooka w API
nie oznacza automatycznego wyszukania funkcji po nazwie w nowym EXE.
Docelowo trzeba oprzeć lokalizację na odkrywaniu i walidacji funkcji podczas
działania, z pominięciem instalacji hooków przy niejednoznacznym wyniku oraz logiem.
Nie wykazano, że pluginu się nie da, więc nie ma podstaw do wyboru podmiany EXE.

Proponowany pakiet: własny plugin + słownik PL + font z odpowiednią licencją
lub własne rozszerzenia glifów. Dialogi najlepiej podmieniać po odczycie w pamięci
albo przekierować odczyt do plików moda. Dla zdań proceduralnych tłumaczyć
szablony lub składniki ze znajomością kontekstu, nie tylko końcowy `draw_text`.
Pomiar szerokości i łamanie wierszy muszą operować już na wersji polskiej.
Jeśli dalsza próba wykluczy plugin, alternatywą będzie łatka różnicowa zgodna
z zasadami repo; nigdy dystrybucja całego EXE z zasobami gry.

Repo loadera zawiera `LICENSE.md` oznaczony CC BY-NC 4.0; strona Nexus ma osobne
restrykcyjne ustawienia uprawnień. Przed pakowaniem ustalić konkretny artefakt,
jego warunki i licencje zależności. W tej analizie niczego nie redystrybuowano.

## Inne tłumaczenia i źródła

- [Rosyjski projekt — relacja autora, 2021/2023](https://steamcommunity.com/app/268130/discussions/0/5625537320589891356/):
  dialogi i nazwy zapisywano transliteracją łacińską. Próby podmiany grafiki fontu
  nie dały prawidłowej cyrylicy. Autor później opublikował wariant z rosyjskimi
  sprite'ami i transliteracją dialogów; brak dowodu kompletnej lokalizacji menu.
  Nie pobierano paczki ani nie potwierdzano dostępności linków Google Drive.
- [Chińska łatka LMAO 2.0](https://patch.ali213.net/showpatch/90869.html):
  strona zespołu opisuje łatkę dla builda 20180323. To historyczny precedens,
  nie potwierdzenie zgodności z lokalną wersją 2021. Nie pobierano instalatora.
- [Loader na Nexus](https://www.nexusmods.com/heatsignature/mods/1).
- [Kod loadera](https://github.com/piepieonline/HeatSignatureModLoader/blob/main/ModLoader/ModLoader.cpp),
  [hooki](https://github.com/piepieonline/HeatSignatureModLoader/blob/main/ModLoader/UniversalHooks.cpp),
  [tabela skryptów](https://github.com/piepieonline/HeatSignatureModLoader/blob/main/docs/ScriptFunctions.txt).

## Następny krok i granice werdyktu

Rozpoznanie pozytywne warunkowo: teksty są dostępne, istnieje infrastruktura modów,
ale nie wykonano jeszcze ekstrakcji z kontekstem całego EXE ani próby fontów.
Najpierw ustalić kierunek językowy skillem localization-direction; następnie mały
vertical: menu główne, ustawienia, pierwszy tutorial i dialog, pełny zestaw
`ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ`, teksty o różnej długości i z liczbami.
Użytkownik uruchamia grę i ocenia screeny. Dopiero udany test uzasadnia pełne tłumaczenie.

Nie ma buildu, instalacji, paczki ZIP ani testu w uruchomionej grze.
Dokument i skrypt są wynikiem rozpoznania, nie deklaracją ukończenia projektu.
