# Kandydaci do spolszczenia — analiza lokalna, 2026-09-20

Zakres: rozpoznanie według AGENTS.md, bez uruchamiania gier, modyfikacji instalacji
ani tworzenia tłumaczeń. [Źródła internetowe](2026-09-20-kandydaci-zrodla.md).
Wszystkie trzy gry znaleziono lokalnie w C:/Games.

## Boomerang X — TAK, pierwszy kandydat

Instalacja: `C:/Games/Boomerang X/BOOMERANG X_Data`.
Unity, backend Mono; kod dostępny w `Managed/Assembly-CSharp.dll`.
Odczyt metadanych dnfile i zasobów UnityPy, bez wykonywania kodu gry.

`localization_table` tworzy `SheetData` i wywołuje `Init`.
Metoda `SheetData.Init` (RVA 0x74d60 w tej instalacji) buduje 360 obiektów `Data`.
Każdy ma id, description, max_char_limit, asian_char_limit oraz kolumny językowe:
angielski, dodatkowe angielskie źródło dla Azji i 9 pozostałych języków.
Teksty są literałami w zarządzanej DLL, nie luźnym plikiem JSON/CSV.
To 360 wierszy tabeli, nie gwarancja pokrycia każdego tekstu zaszytego w grze.

Enum `language` ma 10 języków i LENGTH, brak polskiego. Są metody
`localization_manager.set_language`, `get_translation` i `GetPlatformDefaultLanguage`.
`font_manager` ma osobne zestawy fontów dla alfabetów/kategorii tekstu.

Droga: wydobycie tabeli do EN/PL, modyfikacja tabeli i logiki językowej w DLL,
dodanie polskiego do wyboru języków, sprawdzenie zapisu wyboru i glifów we wszystkich
używanych fontach. Nie zweryfikowano jeszcze kompletności glifów fontów ekranowych.
W resources.assets znaleziono LiberationSans, ale sama jego obecność nie dowodzi,
że każdy tekst korzysta z niego ani że działa fallback.

Trudność wstępna: średnia. Mała tabela i dostępny kod przemawiają za tym tytułem
jako pierwszym. Osobny język wymaga pracy, ale kod da się analizować jako .NET.
Vertical: własny wybór Polski, zapis wyboru, menu, samouczek i rozmowa, test znaków
ąćęłńóśźż oraz limitów. Dopiero po potwierdzeniu użytkownika pełne tłumaczenie.

## My Friend Pedro — TAK, najlepszy kandydat po analizie lokalnej

Po doprecyzowaniu użytkownika same deklaracje wydania NelsonPL nie zamykają gry.
Nie znaleziono dostępnej paczki PL. Wcześniejszy STOP wycofany.

Instalacja GOG: `C:/Games/My Friend Pedro/My Friend Pedro - Blood Bullets Bananas_Data`.
Unity 2017.4.19f1, backend Mono, I2 Localization w Assembly-CSharp-firstpass.dll.
Kod menu jest w Assembly-UnityScript.dll (również zarządzany .NET).

Tabela: `resources.assets`, MonoBehaviour path ID 2279, 366496 bajtów.
SHA-256 całego resources.assets:
`4a81ed99cd1e8e5e4665bde87b80d4bd551bf95c088c1b3a80ed2ecfbb9764fd`.
Odczytano 10 języków i 721 unikalnych kluczy, wszystkie typu tekstowego (0),
24370 znaków w kolumnie angielskiej. Obejmuje dialogi (np. w101-1), menu,
komunikaty i modyfikatory gry. Nie jest to dowód pokrycia napisów w grafikach
ani każdego hardcodowanego komunikatu/integracji platformy.

Format starszego I2 różni się od Shotgun Cop Man: metadane i lista języków są
przed terminami. Licznik języków na offsecie 284, lista kończy się na 608;
licznik terminów na 616, dane od 620, końcowe 12 bajtów po tabeli.
Rekord: klucz, typ, opis, lista językowych stringów, flagi, dodatkowy pusty element.
Parser odczytał komplet tabeli i odtworzył oryginalny obiekt identycznie bajt w bajt.
To próba odczytu/zapisu w pamięci; nie powstała zainstalowana paczka ani vertical.

Analiza IL OptionsMenuScript.buildLanguageMenu: wywołuje GetAllLanguages,
get_Count, get_CurrentLanguage i GetTranslation. executeOption pobiera listę
języków oraz wywołuje set_CurrentLanguage i get_CurrentLanguageCode.
To mocna przesłanka, że dopisany jedenasty język pojawi się automatycznie.
Nie potwierdzono jeszcze w grze zapisu wyboru po restarcie ani wyglądu nowej pozycji.

Fonty w resources.assets obejmują rodziny NotoSans/NotoSansDisplay i Arial.
Sprawdzono rzeczywiste niezerowe mapowania cmap dla wszystkich 18 polskich
małych/wielkich liter w NotoSans (path ID 661) i NotoSansDisplay-Bold (638).
Przypisania fontów ekranowych, TMP atlas/fallback i faktyczne renderowanie wymagają
verticala; obecność TTF nie gwarantuje poprawności każdego ekranu.

Plan techniczny: przypiąć oryginał hashem, dodać rekord Polish/pl i jedenastą
kolumnę każdego terminu z flagami, zachować wszystkie oryginalne języki/metadane.
Dla nieprzetłumaczonej części verticala można skopiować tekst angielski.
Zachować separator dialogowy | oraz znaczniki/placeholdery. Zweryfikować cały
resources.assets po zapisie, w tym niezmienione inne obiekty. Narzędzie ze Shotgun
Cop Man jest punktem wyjścia, ale jego parser nie pasuje bez dostosowania.

Trudność wstępna: niska do średniej, najmniej ryzyka z trzech badanych gier.
Przewidywany zakres łatki: resources.assets; konieczność zmiany kodu nie wynika
z dotychczasowej analizy. Nie obiecywać tego przed działającym verticalem.

Vertical do następnego etapu: osobne Polski w menu, powrót do English, restart
z zachowanym wyborem, kilka pierwszych kwestii Pedro, samouczek z ikonami,
polskie znaki i dłuższy komunikat. Bez uruchamiania gry przez agenta.
Inne tłumaczenia i ich linki zapisano w notatce źródłowej.

## OTXO — TAK warunkowo, drugi kandydat przy wymaganiu własnego języka

Instalacja: `C:/Games/OTXO`.
GameMaker: archiwum `data.win` ma nagłówek FORM i typowe chunki GEN8/STRG/FONT itd.
Brak chunków CODE/VARI/FUNC z bytecode; OTXO_Release.exe zawiera natywne symbole
skryptów i nazwy plików językowych. Jest to wydanie z kodem natywnym (YYC),
więc zwykła edycja skryptów GameMakera w data.win nie jest dostępną drogą.

`script_english.ini`: sekcja [english], 1476 unikalnych liczbowych kluczy.
`scriptcatchups.ini`: 52 klucze, wszystkie już obecne w angielskim INI;
nie doliczać ich jako 52 nowych tekstów. Rola pliku w runtime nieustalona.
Zewnętrzne tłumaczenia: francuski, niemiecki, portugalski brazylijski, rosyjski,
hiszpański, chiński. Nie wszystkie pliki mają identyczną liczbę kluczy;
francuski zawiera powtórzenia. Ekstraktor powinien kontrolować duplikaty i fallback.

Dołączony `notosans.ttf` ma w cmap wszystkie 18 polskich małych i wielkich znaków.
To potwierdzenie fontu na dysku, nie test sposobu jego użycia przez każdy ekran.
`data.win` ma również zasoby FONT; obsługa glifów w grze wymaga testu.

Sama podmiana tekstów jest obiecująco prosta: zewnętrzne INI, potwierdzona przez
instrukcję autora japońskiego moda (link w źródłach). Ten mod podmienia chiński slot.
Osobny polski język i flaga nie są potwierdzone. Lista plików/wybór języka występują
w natywnym EXE; może być potrzebna analiza i łatka natywna zamiast edycji danych.
Nie należy zakładać, że dopisanie pliku script_polish.ini zostanie wykryte.

Trudność: niska dla tekstów w istniejącym slocie; podwyższona i obecnie nieustalona
przy wymaganiu osobnego PL jak w SPRAWL. Najpierw techniczny vertical selektora,
zapisu języka i tekstu dialogu/opisu trunku ze znakami PL. Nie zaczynać tłumaczenia
1476 wpisów przed wyjaśnieniem tej przeszkody.

## Kolejność do planowania

1. My Friend Pedro — 721 wpisów, I2 i dynamiczna lista języków, najmniej ryzyka.
2. Boomerang X — 360 wierszy, zarządzany kod, umiarkowany koszt techniczny.
3. OTXO — 1476 wpisów, łatwe teksty, ryzyko natywnego selektora.

Kolejność zakłada model osobnego języka znany ze SPRAWL. Żaden nowy vertical
nie został jeszcze zbudowany ani zainstalowany. Werdykt techniczny jest wstępny.
