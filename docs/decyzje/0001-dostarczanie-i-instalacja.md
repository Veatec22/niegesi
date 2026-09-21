# 1. Jak gracz dostaje spolszczenie

**Stan: zrealizowane 21 września 2026 — wszystkie trzy kroki.** Wynik na końcu
dokumentu, w sekcji „Co zrobiliśmy". Reszta to zapis rozważań sprzed decyzji.
Rozstrzygnięte wcześniej reguły (plugin przed podmianą pliku, łatka przed plikiem)
są już w `AGENTS.md` i nie są przedmiotem tego dokumentu.

## Skąd się wziął temat

Osiem gier dzieli się dziś na dwie grupy i każda dostarcza spolszczenie inaczej.
Pytanie brzmi, czy da się doprowadzić do jednego, wspólnego doświadczenia gracza:
pobierasz, wypakowujesz, grasz.

## Co działa dzisiaj

| | Pobierz | Zainstaluj w przeglądarce |
| --- | --- | --- |
| Sześć gier na pluginach | **działa** — zip, wypakuj do katalogu gry, koniec | nie istnieje |
| Dwie gry na łatce | **działa** — zip z łatką, instrukcją i `patch.py` | nie istnieje |

Guzik „zainstaluj" nie istnieje dla żadnej gry. To pomysł z File System Access API,
omówiony i nigdy nie zbudowany.

Paczki pluginowe są samowystarczalne: wypakowanie i tyle, zero skryptów.
**Jedyna realna dziura to paczki deltowe — do nałożenia łatki potrzebny jest Python.**

Rozmiary, dla porządku:

| Gra | Plik gry | Łatka | Paczka |
| --- | --- | --- | --- |
| Boomerang X | 1,72 MB | 18,4 KB | 22,3 KB |
| Skate Story | 275 MB | 2,4 MB | 2,15 MB |

## Rozważone drogi

**Klasyczny instalator (NSIS, Inno Setup) — odrzucone.** Nasze instrukcje chwalą się
„żadnych skryptów, instalatora ani mod loadera", bo scena moderska tego nie lubi:
instalator to nieprzejrzysty plik wykonywalny grzebiący w katalogu gry. Do tego
wymagałby kolejnego narzędzia w repo.

**Mały własny aplikator `.exe` — rekomendowane.** Jeden plik obok łatki, dwuklik albo
`.bat`, żadnej instalacji, rząd kilkudziesięciu kilobajtów. Mamy czym go zbudować:
kompilator C# już wykorzystujemy do pluginów, a .NET Framework jest na każdym
Windowsie od dekady.

**Guzik „zainstaluj" w przeglądarce.** Przy grach pluginowych zapisuje pliki do katalogu
gry, przy deltowych czyta plik gracza, nakłada łatkę i zapisuje wynik. Ten sam kod,
różny ostatni krok. Działa tylko na przeglądarkach na Chromium — Firefox i Safari nie
mają wyboru katalogu z prawem zapisu.

## Przeszkoda wspólna dla obu: format łatki

Dzisiejsza łatka używa **zstd ze słownikiem**. Ani .NET Framework, ani przeglądarka nie
mają tego wbudowanego, więc aplikator musiałby nieść własną implementację — koniec
z „kilkadziesiąt kilobajtów, zero zależności".

Rozwiązaniem jest format przenośny: lista operacji „skopiuj od bajtu X" i „wstaw te
bajty", a do skompresowania literałów zwykły **DEFLATE**, który mają oba środowiska
(`System.IO.Compression` w .NET, `DecompressionStream` w przeglądarce).

**To jedna zmiana odblokowująca oba guziki naraz** i dlatego jest pierwszym krokiem,
choć sama w sobie nie daje graczowi nic.

### Czego nie wiemy

**O ile urośnie łatka po zmianie formatu.** Zstd ze słownikiem jest w tym zadaniu bardzo
dobry. Przy Boomerang X własny format powinien wypaść podobnie albo lepiej, bo plik nie
zmienia rozmiaru, a różnice są punktowe. Przy Skate Story układ pliku się przesuwa, więc
potrzebny jest prawdziwy algorytm dopasowania (rolling hash) i tam może być gorzej.

To pomiar na godzinę, nie spekulacja — i należy go zrobić **przed** decyzją, a nie po.

## Proponowana kolejność

Trzy kroki, każdy osobno sensowny, każdy może być ostatni:

1. **Zmiana formatu łatki na przenośny.** Warunek konieczny obu guzików. Zacząć od
   pomiaru rozmiaru na obu grach i dopiero wtedy decydować.
2. **Aplikator `.exe` w paczce deltowej.** Po tym kroku wszystkie osiem gier ma
   pobieranie działające bez niczego dodatkowego — jeden model wszędzie, bez wyjątków.
3. **Guzik „zainstaluj" w przeglądarce**, dla obu rodzajów gier.

Rekomendacja: zrobić 1 i 2, a 3 zostawić na moment, gdy strona będzie stała.
**Jeden działający guzik na wszystkich ośmiu grach jest ważniejszy niż dwa guziki
na części z nich.**

## Do rozstrzygnięcia jutro

- Czy w ogóle wchodzimy w zmianę formatu łatki, czy zostawiamy Pythona w paczce
  deltowej jako świadomy kompromis na dwie gry z ośmiu.
- Jeśli wchodzimy: jaki wzrost rozmiaru łatki jest akceptowalny. Dwukrotny przy
  Skate Story to nadal 5 MB wobec 275 MB pliku, więc prawdopodobnie tak.
- Czy aplikator ma być `.exe` z dwuklikiem, czy `.bat` wołający `.exe` z parametrami.
  Pierwsze jest przyjaźniejsze, drugie łatwiejsze do obejrzenia przed uruchomieniem.

## Powiązane

- `AGENTS.md`, sekcja „Jak dostarczamy spolszczenie" — reguły już obowiązujące.
- `tools/patch.py` — obecny format i polecenie `release`.
- `games/skate-story/docs/technika.md`, `games/boomerang-x/docs/technika.md` —
  dlaczego te dwie gry nie mogą mieć pluginu.

## Co zrobiliśmy

Weszliśmy we wszystkie trzy kroki naraz.

**1. Format 2 łatki** (`tools/patch.py`): lista operacji „skopiuj z oryginału" /
„wstaw bajty" spakowana surowym DEFLATE. Obawa o wzrost rozmiaru okazała się odwrotna —
łatki zmalały, bo dopasowanie z zapamiętanym przesunięciem łapie przesunięty plik
w całości, a zstd nie sięgał dopasowaniami przez całe 275 MB:

| Gra | Format 1 (zstd) | Format 2 (DEFLATE) | Paczka |
| --- | --- | --- | --- |
| Boomerang X | 18,4 KB | 14,3 KB | 21 KB |
| Skate Story | 2,4 MB | 78 KB | 85 KB |

Format 1 został usunięty razem z zależnością od `zstandard`.

**2. `NieGesiPatch.exe`** (`tools/applier/`, 11 KB, C# 5, .NET Framework 4): wypakuj
paczkę do katalogu gry, dwuklik. Sprawdza sumę, odkłada oryginał jako
`<plik>.przed-spolszczeniem`, zapisuje przez plik tymczasowy. Uruchomiony ponownie
na spolszczonej grze pyta o przywrócenie oryginału. Wybrano `.exe` z dwuklikiem;
parametry (`<katalog gry> [łatka]`, `--przywroc`) działają też z wiersza poleceń.

**3. Guzik „Zainstaluj"** na stronie (`site/src/lib/install.ts`), dla obu rodzajów gier.
Katalog gry rozpoznaje po pliku `install.marker` z `game.yaml`. Przy pluginowych
zapisuje pliki z zipa (pomija `READ-ME.txt`; plik już istniejący i różny odkłada obok
z tym samym dopiskiem), przy deltowych nakłada łatkę jak aplikator.

### Ograniczenia, które wyszły przy budowie

- **Chrome i Edge nie udostępniają stronom niczego w `Program Files`**, także
  podkatalogów (lista blokad Chromium, `kBlockAllChildren`). Domyślne biblioteki
  Steama i GOG Galaxy tam leżą, więc dla sporej części graczy guzik nie zadziała
  i zostaje pobranie. Strona mówi o tym wprost pod guzikiem.
- Nieprzetestowane: czy Chrome przy zapisie `winhttp.dll` i pluginu `.dll` przez
  File System Access nie wstrzyma pliku kontrolą Safe Browsing. Do sprawdzenia
  przy pierwszym teście gry pluginowej.
