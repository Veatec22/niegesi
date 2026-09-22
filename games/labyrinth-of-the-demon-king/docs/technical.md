# Labyrinth of the Demon King — analiza techniczna

## Aktualny stan: pełny przekład 0.2, 21 września 2026

Użytkownik potwierdził działanie verticala („poszło gładko”) i zlecił pełny
przekład. Dodano 798 wpisów, zachowując 322 wpisy verticala bez zmian:
**1120/1120**. Pliki `pl.json` i `en-pl-review.json` są zsynchronizowane;
`tools/review.py` tworzy przeszukiwalne HTML z uwagami do korekty.

Paczka `dist/Labyrinth-of-the-Demon-King-PL-0.2.zip`: **83 553 bajty**,
locres PL: **169 626 bajtów**. Pliki selektora `.utoc` i `.ucas` są identyczne
bajtowo z potwierdzonym verticalem. Zmienił się PAK z tekstami i READ-ME.
Nie dodano żadnych nowych nośników ani zależności gry.

Build sprawdza kompletność przekładu znanego zbioru review. Nowe wpisy dodane
w przyszłej wersji gry mogą pozostać w języku źródłowym. Dla obecnej kopii
znany zbiór i zbiór gry są identyczne. Zachowano placeholdery, znaczniki,
liczbę podziałów CRLF i spójność tłumaczeń identycznych oryginałów.
W ośmiu źródłach z podwojonym zdaniem o zamkniętych drzwiach usunięto
powtórzenie; opisano to w uwagach review.

Kontrole buildu i `tools/test_overlay.py` przeszły. Porównanie 0.1/0.2
potwierdziło zachowanie całego verticala oraz identyczność selektora.
Pełna wersja została zainstalowana przy zamkniętej grze. Kopia trzech plików
verticala: `backups/labyrinth-of-the-demon-king-vertical/`. SHA-256 pięciu
oryginalnych kontenerów gry są identyczne przed i po instalacji.
Potwierdzenie instalacji: `backups/labyrinth-of-the-demon-king/install-receipt.json`.

**Potwierdzony w grze jest vertical, nie pełne przejście kampanii.** Następny
krok użytkownika to kontrola długich dialogów, notatek, zagadek i składu UI.
Terminologia, niepewne przypisania mówców i adaptacje dowcipów są opisane w
`translations/REVIEW.md` oraz uwagach poszczególnych wpisów.

## Historia: vertical 0.1, 21 września 2026

Zbudowano i zainstalowano nakładkę, **bez uruchamiania gry**. 322/1120 wpisów:
menu i ustawienia oraz próbki samouczka walki, dialogów, notatek i przedmiotów.
`dist/Labyrinth-of-the-Demon-King-PL-0.1.zip` ma około 29 KB. Szczegółowe rozmiary
i sumy są w `dist/build-report.json`; metadane w `game.yaml`.

- Dodatkowy PAK v11 zawiera wyłącznie `pl/Game.locres` (32 654 bajty).
- Dodatkowy IoStore v3 zawiera tylko `UI_LanguageSlot` (24 355 bajtów) oraz
  jego mały nagłówek kontenera. To minimalny, istniejący nośnik selektora,
  w całości dotyczący lokalizacji. Jest jawnie wymieniony w instrukcji.
- Nie dołączono fontów, innych blueprintów, tekstur ani danych poziomów.
- W mapie `LanguageStrings` dopisano `pl -> Polski`. Zachowano 12 starych
  etykiet, w tym angielską i nieaktywną wietnamską. Zmiana nie podmienia English.
- Nie zmieniano kodu wykonywalnego blueprintu ani enum języków. To, czy
  `GetLocalizedCultures` odkryje nowy locres, rozstrzygnie test w grze.

`tools/language_slot.py` odczytuje mapę nazw i eksporty pakietu, odnajduje CDO
po nazwie i dopisuje wpis do mapy właściwości. Aktualizuje jej rozmiar/liczbę
elementów oraz rozmiar i przesunięcia eksportów. Nie opiera się na stałych
offsetach właściwości. Oryginalna zawartość mapy pozostaje identyczna bajtowo.

`tools/iostore.py` tworzy nowy kontener z jednym pakietem, jego identyfikatorem,
minimalnym wpisem package store i listą zależności odnoszącą się do oryginałów.
Nie kopiuje zależnych pakietów. Aktualizuje ExportBundlesSize, indeks katalogów,
bloki, pozycje chunków i SHA-1 zapisane w 32-bajtowym polu hash UE4.
Układ oparto na źródłach CUE4Parse:
[FIoContainerHeader](https://github.com/FabianFG/CUE4Parse/blob/master/CUE4Parse/UE4/IO/Objects/FIoContainerHeader.cs),
[FFilePackageStoreEntry](https://github.com/FabianFG/CUE4Parse/blob/master/CUE4Parse/UE4/IO/Objects/FFilePackageStoreEntry.cs),
[FIoChunkId](https://github.com/FabianFG/CUE4Parse/blob/master/CUE4Parse/UE4/IO/Objects/FIoChunkId.cs).

```powershell
.venv/Scripts/python.exe games/labyrinth-of-the-demon-king/tools/build.py --game "C:/Games/Labyrinth Of The Demon King"
.venv/Scripts/python.exe games/labyrinth-of-the-demon-king/tools/test_overlay.py
```

Build sprawdza synchronizację review, oryginały przetłumaczonych wpisów,
placeholdery, znaczniki, liczbę CRLF, round-trip locres oraz zawartość obu
kontenerów i ZIP. Dopuszcza tylko locres PL, wskazany widżet i minimalny nagłówek;
ogranicza też rozmiar nośnika. Negatywne próby potwierdziły odrzucenie obcego
zasobu wewnątrz PAK, luźnego resources.assets i uszkodzonego chunka.
Nie ma warunku SHA wersji gry w builderze wydania ani w instalowanej nakładce.

Instalacja dopisała wyłącznie trzy pliki `pakchunk99-NieGesiPL_P` do Paks.
Oryginały PAK/IoStore/global porównano SHA-256 przed i po instalacji: identyczne.
Potwierdzenie: `backups/labyrinth-of-the-demon-king/install-receipt.json` w repo.
Nie było wcześniejszych plików tej nakładki do zastąpienia.

**Pozostaje test użytkownika:** uruchomienie/montowanie małego IoStore,
odkrywanie `pl`, etykieta selektora, przełączanie, zapis ustawienia i fallback
fontów w menu oraz rozgrywce. Sam odczyt naszym parserem nie dowodzi, że silnik
zaakceptuje nowy kontener. Zgodność widżetu z przyszłymi aktualizacjami pozostaje
niepotwierdzona. PAK nie implementuje logowania brakujących tekstów jak BepInEx;
brakujące wpisy pozostają w źródle. Nie zaczynać pełnego przekładu przed testem.

Poniżej zachowano wcześniejsze rozpoznanie i plan; opis pustego pl.json odnosi
się do stanu sprzed przygotowania verticala.

Stan: 20 września 2026. **Werdykt: warto robić vertical.** Teksty są proste do
wydobycia i zapisania. Główna niewiadoma dotyczy etykiety własnego języka i
wyboru odpowiednich fontów, a nie samego formatu tłumaczenia.

## Lokalna wersja i archiwa

- Instalacja: `C:/Games/Labyrinth Of The Demon King`.
- GOG buildId: `59111742023178281`. `ProjectVersion=1.0.0.0` w konfiguracji
  jest wartością projektu, nie dowodem numeru aktualizacji sklepowej.
- Unreal Engine 4.27: ciąg `++UE4+Release-4.27-CL-0`, data kompilacji Apr 24 2025
  w pliku Shipping.exe, odczytanym jako dane. Nie uruchamiano pliku wykonywalnego.
- `Shinigami/Content/Paks/pakchunk0-WindowsNoEditor.pak`: 187 028 772 bajty,
  wersja PAK 11, indeks nieszyfrowany, mount point `../../../`, 3970 nazw plików.
- Obok `.pak` są `.utoc` i `.ucas` oraz kontener `global`. Główny IoStore ma
  wersję 3, flagę Indexed (8), jedną partycję, brak szyfrowania i kompresji.
  Odczyt indeksu i wybranych chunków pozwolił znaleźć blueprinty UI.

SHA-256 głównego PAK:
`e2be58acee1ecdbe04b3147612b298a2112791b98a2fc2d80658433bc91f3d48`.

## Teksty

Główny plik `Shinigami/Content/Localization/Game/en/Game.locres` znajduje się
w zwykłym PAK, jako wpis nieskompresowany. Nie wymaga odpakowania całego IoStore.
To locres v3, 126 521 bajtów, **1120 wpisów / 59 899 znaków angielskiego tekstu**.
Wszystkie wpisy mają pusty namespace i unikalne klucze. Format jest zgodny
z parserem użytym w SPRAWL. Odczyt i ponowny zapis EN dają identyczne bajty.

SHA-256 EN locres:
`a21b8c409d78fd066ef0a5cd9f4e41efc11dccf6bea74a321ec7d35387cad846`.

Zakres w tabeli: menu, ustawienia, sterowanie, opisy przedmiotów, notatki,
teksty fabularne i dialogi. Nie jest to dowód, że każdy napis w grze jest
lokalizowany; tekstury i ewentualne pominięte FText trzeba sprawdzić w verticalu.
Notatki zawierają istotne wskazówki zagadek, nazwy japońskie i formatowanie CRLF.
Trzeba zachować placeholdery i znaczniki, nie zastępować ich na podstawie domysłów.

W archiwum jest 11 języków gry: en (1120), ar-AE (1117), de-DE (1076),
es-ES (1093), fr-FR (1074), it-IT (1081), ja-JP (1113), pt-BR (1084),
ru-RU (1112), zh-Hans-CN (1115), zh-Hant (1114). Nie ma polskiego locres.
Konfiguracja wymienia również vi-VN, ale nie znaleziono zasobu Game.locres dla niego.
`InternationalizationPreset=All` jest korzystne dla dodania kodu `pl`.

## Osobny język i UI — do potwierdzenia

Odczytane chunki:

- `Blueprints/Widgets/LanguageSelectScreen/UI_LanguageSelectScreen`
- `.../UI_LanguageSelectScreen_OptionsMenu`
- `.../UI_LanguageSlot`
- `Blueprints/StructsAndEnums/E_SupportedLanguages`
- `Blueprints/Core/BP_LotDK_GameInstance`

W obu ekranach wyboru są odwołania do `GetLocalizedCultures` i `SetCurrentCulture`
oraz iteracji po tablicy. To **wskazówka**, że lista może wykryć dodane `pl`.
Slot zawiera też `LanguageStrings`, a gra ma enum obsługiwanych języków.
Sam odczyt nazw nie dowodzi przepływu blueprintu ani poprawnej etykiety PL.
Nie zakładamy, że dopisanie locres wystarczy: vertical ma sprawdzić osobną pozycję
„Polski”, przełączenie na EN i z powrotem oraz zapis po restarcie.
Jeśli trzeba edytować slot/font, ich cooked assets są w IoStore, więc łatka
może wymagać formatu IoStore zamiast samego dodatkowego PAK.

## Fonty

Sprawdzono rzeczywiste tablice cmap plików `.ufont`, z niezerowymi glyph ID dla
18 liter `ąćęłńóśźżĄĆĘŁŃÓŚŹŻ`:

- Lora, NotoSerif (normalny i italic), NotoSansArabic oraz trzy EB Garamond: 18/18.
- DotGothic16: brakuje 14 znaków; NotoSerif JP/SC/TC: brakuje 14;
  ShipporiMincho Bold/B1: brakuje 16.

UI odwołuje się do `ShipporiMinchoB1-Regular_Font`. To jednak **font złożony**:
chunk zawiera również referencje do Lora/NotoSerif, `FallbackTypeface`,
`SubTypefaces`, `Cultures` i `CharacterRanges`. Sam brak PL w japońskim pliku
źródłowym nie dowodzi błędnego renderowania. Trzeba sprawdzić faktyczną regułę
wyboru dla `pl`; w grze są już fonty, które potrafią wyświetlić wszystkie litery.

## Narzędzia i potwierdzone próby

```powershell
.venv/Scripts/python.exe games/labyrinth-of-the-demon-king/tools/analyze.py --game "C:/Games/Labyrinth Of The Demon King"
```

Skrypt sprawdza źródłowy PAK po SHA, wyciąga teksty, aktualizuje JSON EN/PL,
liczy języki i bada fonty. W `work/analysis.json` zapisuje wyniki. `pl.json` jest
obecnie pusty, a review ma 1120 angielskich oryginałów z pustą kolumną polską.

Przeprowadzono też próby w samym repo:

1. Dokładny round-trip angielskiego locres.
2. Zapis i odczyt locres z `Język — zażółć gęślą jaźń`, zachowując oryginalne hashe.
3. Zapakowanie próbki jako `Shinigami/Content/Localization/Game/pl/Game.locres`
   do PAK v11 z katalogami nadrzędnymi i ponowne wydobycie identycznych bajtów.

Próbki są w `work/codec-probe*`. **Nie są verticalem ani paczką do instalacji.**
Nie kopiowano niczego do gry. Nie tworzono finalnego `dist/`, ZIP ani buildera
wydania przed rozpoczęciem verticala. Czy gra montuje taką paczkę, pozostaje do testu.

Pomocniczy `work/inspect_iostore.py` wyciąga wybrane chunki i ich czytelne ciągi.
Interpretacja nagłówka i indeksu opiera się na
[źródle UEcastoc](https://github.com/gitMenv/UEcastoc/blob/master/utoc.go);
do pełnego odczytu blueprintów można wykorzystać
[CUE4Parse](https://github.com/FabianFG/CUE4Parse).

## Plan verticala

### Zasady dostarczania — aktualizacja 21 września 2026

Przejrzano nowe AGENTS.md oraz `plugin/Plugin.cs`, `tools/build_plugin.py`
i instrukcje pluginowe My Friend Pedro i Anger Foot. Pedro dodaje język do I2
po wczytaniu źródła, Anger Foot przechwytuje getter tekstu po GUID i udostępnia
pusty slot językowy. Wspólny wzorzec: własne teksty i mała nakładka, bez
dystrybucji przepisanych zasobów gry. Ich główne README opisują jeszcze starą
metodę; nie są wzorcem aktualnego sposobu pakowania.

Dla tej gry podstawą jest dodatkowy PAK z polskim locres. Jeśli selektor wymaga
IoStore, trzeba przygotować mały kontener nakładkowy zawierający wyłącznie
niezbędną strukturę lokalizacyjną. Przepakowanie całego oryginalnego UCAS/UTOC
do paczki jest wykluczone. Ewentualny nośnik selektora lub reguł fontu musi być
minimalny, uzasadniony, mały względem tłumaczenia i wymieniony w READ-ME.
Najpierw należy sprawdzić możliwość wykorzystania istniejących fontów bez ich
dołączania. Skuteczność montowania nakładki pozostaje do potwierdzenia.

Build ma sprawdzać dokładną listę plików wewnątrz kontenerów, ich przeznaczenie
i rozmiary, a nie tylko rozszerzenia zewnętrznego ZIP. Niedozwolona zawartość
ma przerwać budowanie. Nowe/brakujące wpisy zostają po angielsku; suma kontrolna
lokalnej kopii służy dokumentacji analizy, nie blokadzie działania spolszczenia.
Nie zakładamy odporności zmodyfikowanego blueprintu na aktualizacje bez dowodu.
Wycofanie łatki ma polegać na usunięciu jej własnych plików.

Próbka: menu, wybór „Polski”, początkowa rozmowa, notatka ze wskazówką zagadki,
przedmiot i podpowiedź sterowania. Dodać `pl/Game.locres` jako osobną kulturę,
sprawdzić nazwy na ekranie wyboru i fonty. Zachować oryginały każdej podmienianej
rzeczy; build ma zostawić ZIP z układem katalogów gry i READ-ME.
Test uruchamia użytkownik. Pełny przekład dopiero po jego potwierdzeniu.

[Rozpoznanie istniejących tłumaczeń](../../../temp/research/2026-09-20-labyrinth-of-the-demon-king.md).

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „Labyrinth of the Demon King — pełny przekład PL 0.2”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

Spolszczenie Labyrinth of the Demon King obejmuje wszystkie 1120 wpisów
lokalizacji: menu, dialogi, sterowanie, samouczki, opisy przedmiotów, notatki,
mapy i osiągnięcia. Osobny język „Polski” działa przez małą nakładkę;
vertical potwierdzono w grze, pełna kampania czeka na przegląd.

Nie znaleziono dostępnego spolszczenia. Steam nie obsługuje PL; znaleziono
fanowski przekład koreański jako dodatkowy trop. [Źródła i linki](../../../temp/research/2026-09-20-labyrinth-of-the-demon-king.md).

### Instalacja

Wypakuj [ZIP 0.2](../dist/Labyrinth-of-the-Demon-King-PL-0.2.zip) do katalogu
z `Shinigami.exe`, przy zamkniętej grze. Uruchom ją i wybierz „Polski”.
Są potrzebne wszystkie trzy pliki `pakchunk99-NieGesiPL_P` (`pak`, `utoc`, `ucas`).
Usunięcie tych trzech plików wycofuje łatkę. Oryginały gry pozostają nietknięte.
[Pełna instrukcja i zawartość paczki](../docs/INSTALL.txt).
Przy aktualizacji z 0.1 zastąp te same trzy pliki. Paczka ma około 84 KB.

### Stan testu i następny krok

Pełny przekład jest zainstalowany lokalnie. Użytkownik potwierdził działanie
verticala i zlecił pełne tłumaczenie. Nakładka selektora pozostała identyczna
bajtowo, zachowano wszystkie 322 teksty verticala i dodano 798 pozostałych.
Sprawdzono zgodność review, znaczniki, podziały akapitów, locres i zawartość ZIP.
Oryginalne kontenery gry pozostały identyczne; kopia verticala jest w
`backups/labyrinth-of-the-demon-king-vertical/` w repo.

Pozostaje ocena całej kampanii: dłuższych rozmów i notatek, wskazówek zagadek,
układu UI i komunikatów łączonych z nazwami przedmiotów. Uwagi do korekty są
w review. Gra nie była uruchamiana przez agenta. Nagrania, teksty w obrazach
i opisy w klientach sklepów są poza zakresem.

[Przeszukiwalne review EN/PL](../translations/en-pl-review.html) ·
[JSON EN/PL](../translations/en-pl-review.json) ·
[Terminologia i uwagi](../translations/REVIEW.md) ·
[Technika i ryzyka](../docs/technical.md) · [Metadane](../game.yaml).
