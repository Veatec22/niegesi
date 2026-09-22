# SPRAWL — technika i stan prac

## Wersja 0.2

717/717 wpisów angielskiego zasobu `Game.locres`: menu, HUD, samouczki, dialogi,
kodeks, interakcje, nazwy i opisy poziomów, przeciwników i broni. Poza zakresem
zostaje dubbing i teksty wypalone w grafikach.

Użytkownik potwierdził w grze selektor języka, powrót do angielskiego, zapis wyboru
po restarcie oraz próbkę dialogów, samouczków i interakcji. Pełna kampania i układ
wszystkich długich tekstów czekają na przejście. Agent nigdy nie uruchamia gry.

Następny test użytkownika: długie strony kodeksu, późniejsze dialogi, opisy poziomów
oraz ustawienia. Sprawdzić obcięcia tekstu, znaki PL i ikony przycisków.

## Silnik i sposób wejścia

Unreal Engine 4.27, wydanie GOG, ekran tytułowy 2024.12.09 (v1.6).

Menu `Marketplace/UltimateMenu/UserInterface/Examples/WB_MainMenuPanel` wylicza języki
z mapy `LocaleInfo_PC`; wystarczy rozszerzyć mapę i dodać teksturę flagi. Bytecode
Blueprintu pozostaje nietknięty.

Spolszczenie to **nakładkowy pak** — Unreal sam przewiduje taką drogę. Oryginalny
`Sprawl-WindowsNoEditor.pak` nie jest ani zmieniany, ani usuwany, a odinstalowanie
polega na skasowaniu jednego pliku. To jedyna gra w repo, w której nie podmieniamy
niczego, i wzorzec, do którego dociągamy pozostałe.

Archiwum w wersji 11 wymaga stopki 221 bajtów (z 16-bajtowym GUID-em) oraz katalogów
nadrzędnych w indeksie, inaczej gra nie wykryje kultur. Wcześniejsza podmiana slotu
angielskiego służyła wyłącznie diagnozie i została usunięta.

## Co jest w paku

Pięć plików, 240 KB łącznie:

| Plik | Pochodzenie | Waga |
| --- | --- | --- |
| `Content/Localization/Game/pl/Game.locres` | w całości nasz, 717 wpisów | 182 KB |
| `Content/StringTables/LocaleInfo_PC.uasset` + `.uexp` | tabela języków gry z dopisanym wierszem | 3,7 KB |
| `Content/Textures/UI/Flags/polska_.uasset` + `.uexp` | pojemnik tekstury flagi z przemalowanymi pikselami | 59 KB |

Flaga powstaje z istniejącej w grze flagi ukraińskiej: zachowujemy jej maskę
przezroczystości i natywną warstwę 120×120 BGRA, a piksele malujemy na biało-czerwone.
Piksele są nasze, pojemnik pochodzi z gry.

Te 62 KB to minimalne struktury nośne w rozumieniu zasady z `AGENTS.md`: bez tabeli
języków i bez tekstury flagi Unreal nie przyjmie nowego języka, a zbudowanie pojemnika
tekstury od zera nie dałoby graczowi żadnej różnicy.

## Odtwarzalność

Build wymaga plików wyciągniętych z własnej kopii gry: `translations/en.locres`
oraz czterech zasobów w `work/assets`. Żaden z nich nie jest i nie będzie w repo,
więc **paczki nie da się złożyć z czystego klona** — to jedyna taka gra w repo
i trzeba o tym pamiętać, gdy budowanie paczek się zautomatyzuje.

Zasoby selektora wyciąga się z własnej instalacji:

```powershell
.venv\Scripts\python.exe games\sprawl\tools\prepare_selector_assets.py --game-pak "<gra>\Sprawl\Content\Paks\Sprawl-WindowsNoEditor.pak" --oodle "<FModel>\Output\.data\oodle-data-shared.dll"
```

Wszystkie cztery źródła mają przypięte sumy SHA-256; ekstraktor odmawia pracy na innych.

## Budowanie i walidacja

```powershell
.venv\Scripts\python.exe games\sprawl\tools\validate_translations.py
.venv\Scripts\python.exe games\sprawl\tools\review.py
.venv\Scripts\python.exe games\sprawl\tools\build.py
.venv\Scripts\python.exe -m unittest discover -s games/sprawl/tools -p "test_*.py"
```

Walidacja sprawdza kompletność, zgodność EN/PL, znaczniki, ikony, placeholdery, encje
i brak znaczników testowych. Dalej: odczyt locres po zapisie, hashe kluczy i źródeł,
odczyt paka, zachowanie oryginalnych wierszy selektora oraz kanał alfa flagi.

Build pisze wyłącznie do `dist/`. Wynik: `dist/Sprawl-WindowsNoEditor_pl_P.pak`
oraz `dist/SPRAWL-PL-0.2.zip` (57 KB) z pakiem i `READ-ME.txt`.

Działający vertical sprzed pełnej wersji zachowany w
`backups/sprawl/gameplay-vertical-before-full.pak`.

## Korekta

- [Wyszukiwalny podgląd EN/PL](../translations/en-pl-review.html) — otwórz w przeglądarce.
- [EN/PL JSON](../translations/en-pl-review.json) — oryginał i tłumaczenie każdego wpisu.
- [Terminologia i miejsca do korekty](../translations/REVIEW.md).
- [Polskie teksty źródłowe](../translations/pl.json).

Po korekcie utrzymuj oba JSON-y w zgodzie, uruchom walidację, odtwórz HTML i build.
Podgląd HTML nie zapisuje zmian. Do zgłoszenia poprawki wystarczy namespace, key i tekst.

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „SPRAWL po polsku”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

Pełne spolszczenie SPRAWL-a: 717 z 717 wpisów tekstowych — menu, HUD, dialogi, kodeks,
samouczki, interakcje oraz nazwy i opisy poziomów, przeciwników i broni. Polski jest
osobnym językiem z biało-czerwoną flagą, a wszystkie jedenaście oryginalnych języków
zostaje na swoim miejscu. Dubbing i napisy wypalone w grafikach pozostają angielskie.

Spolszczenie **nie podmienia żadnego pliku gry**. To osobny pak, który Unreal dokłada
obok oryginalnego — odinstalowanie polega na skasowaniu jednego pliku.

### Instalacja

1. Zamknij grę.
2. Wypakuj [paczkę ZIP](../dist/SPRAWL-PL-0.2.zip) do katalogu gry, tak aby
   `Sprawl-WindowsNoEditor_pl_P.pak` trafił do `Sprawl/Content/Paks` obok
   oryginalnego `Sprawl-WindowsNoEditor.pak`.
3. Uruchom grę normalnie, bez dodatkowych parametrów.
4. Strzałkami przy fladze wybierz biało-czerwoną flagę Polski.

Jeśli instalujesz nowszą wersję spolszczenia, zachowaj kopię poprzedniego paka poza
katalogiem `Paks`. Pełna [instrukcja instalacji i usunięcia](../docs/INSTALL.txt).

### Usunięcie

Przy zamkniętej grze usuń `Sprawl-WindowsNoEditor_pl_P.pak`. Oryginalnego paka gry
nie ruszamy, więc nie ma czego przywracać.

### Stan

Sprawdzone w grze: selektor języka, powrót do angielskiego, zapis wyboru po restarcie
oraz próbka dialogów, samouczków i interakcji. Pełna kampania czeka na przejście.

Wersja źródłowa: GOG, ekran tytułowy 2024.12.09 (v1.6).

[Szczegóły techniczne, budowanie i materiały do korekty](../docs/technical.md) ·
[Metadane](../game.yaml)
