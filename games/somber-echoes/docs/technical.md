# Somber Echoes — rozpoznanie i vertical

## Stan 2026-09-22

Instalacja: `C:\Games\Somber Echoes`, GOG gameId 1448685189,
buildId **59160173690323092** z `goggame-1448685189.info`.
Brak testu w uruchomionej grze. Agent gry nie uruchamia.

Nie znaleziono dostępnego spolszczenia. [GOG](https://www.gog.com/en/game/somber_echoes)
nie wymienia języka polskiego. Znalezione tłumaczenia fanowskie:

- [Czeskie, DickzillaTranslator](https://lokalizace.net/localizations/somber-echoes): publiczna paczka ZIP 92,1 KB, strona deklaruje komplet tłumaczenia i testów. Nie pobierano ani nie używano jej tekstów.
- [Tureckie, SinnerClown](https://sinnerclownceviri.net/konu/somber-echoes-tuerkce-yama-yayinlandi.11086/): odnaleziony wpis, odczyt strony nie powiódł się; metoda instalacji niepotwierdzona.
- [Rosyjskie, Wulf84](https://boosty.to/wulf84/posts/c109b9ea-7d82-4e81-b093-09ce22594f97): odnaleziony wpis; rosyjski jest też obecnie oficjalnym językiem gry.

## Format i zakres

Unreal Engine, gałąź 5.4 wskazana przez dołączony plugin XeSS. Paki v11,
bez szyfrowania indeksów, bez kompresji i bez towarzyszących plików IoStore.
Teksty w `pakchunk0-Windows.pak`, `SomberEchoes/Content/Localization`:

| Tabela | Wpisy EN |
| --- | ---: |
| Challenges | 80 |
| Dialog | 326 |
| Journal | 101 |
| StringTables | 798 |
| Updated1 | 28 |
| Updated2 | 36 |
| Updated3 | 18 |
| Updated4 | 120 |
| Razem | 1507 |

Liczba obejmuje wszystkie wpisy tabel, także sklep i osiągnięcia; nie oznacza
1507 unikatowych kwestii widocznych w rozgrywce. Część angielskich źródeł ma
już znaki zastępcze U+FFFD — przy całości porównywać z innymi językami/kontekstem.

W DefaultGame.ini jest lista SupportedCultures oraz wszystkie osiem LocalizationPaths.
Kultury angielskie to en i en-001. Próbka podmienia wyłącznie wybrane wpisy
w Dialog i StringTables w obu kulturach. Wpisy poza próbką mają korzystać
z angielskich źródeł zasobów; fallback wymaga potwierdzenia w grze.

## Fonty

Sprawdzono cmap fontów wyciągniętych z lokalnych paków narzędziem fontTools.
Cinzel Regular/Medium, Maitree-Cinzel (podstawowy), Minion Pro, Montserrat i
Yanone Kaffeesatz zawierają polski alfabet. Maitree-Cinzel Medium nie ma dużego Ą (U+0104);
Merienda i Paestum mają wiele braków, numeryczny Maitree nie ma polskich liter.
Istnienie glifów nie dowodzi wyboru właściwego fontu/fallbacku w UI.
Nie dokładamy ani nie podmieniamy fontów przed testem próbki.

## Budowanie

Z katalogu repo:

```powershell
.venv\Scripts\python.exe games\somber-echoes\tools\extract.py
.venv\Scripts\python.exe games\somber-echoes\tools\build.py
```

Wykorzystujemy istniejący czytnik paka i locres z BPM oraz writer paka ze SPRAWL-a.
Ekstrakcja zapisuje zasoby i pełne EN wyłącznie w ignorowanym `work/`.
Klucze tłumaczenia: `tabela/namespace/key`, czyli identyfikatory Unreala
z nazwą tabeli zapobiegającą kolizjom. Review EN/PL obejmuje 111 tłumaczonych wpisów.

Build filtruje tabelę do naszych tłumaczeń, przenosi oryginalne hashe kluczy i źródeł,
sprawdza znaczniki, zgodność EN/PL, odczyt zwrotny locres i każdego pliku paka.
ZIP ma ścisłą listę zawartości: pak z czterema wygenerowanymi locres i READ-ME.txt.
Nie publikuje oryginalnych tabel EN, fontów, konfiguracji ani zasobów gry.
Pak nie blokuje uruchomienia na podstawie numeru wersji gry.

## Test i następny krok

Werdykt: warto kontynuować przez mały pak nakładkowy. Przygotowano próbkę 111 wpisów.
ZIP 6568 bajtów trafił do `dist/` oraz `site/public/pobierz/`; okładka i pięć
zrzutów sklepowych są w `site/public/keyart/somber-echoes/`.
Próbkę zainstalowano jako nowy `SomberEchoes/Content/Paks/pakchunk99-notgeese-PL_P.pak`.
Nie istniał wcześniej, więc nie podmieniono żadnego pliku i nie była potrzebna
kopia oryginału. SHA-256 źródła i zainstalowanego paka są zgodne:
`410a7f92324492fd38a8d1a2fc859e3baadee44dba982c4b14edcc43aba9b66b`.
Weryfikacja plików nie zastępuje testu w grze. Użytkownik uruchamia grę z językiem
English i napisami, sprawdza menu/opcje, intro oraz pierwsze samouczki na wolnym
slocie zapisu. Oczekujemy screenów menu, opcji dźwięku i napisów/samouczka.
Po działającym verticalu można opracować oddzielny wybór Polski i pełne tłumaczenie.

## Pełne tłumaczenie 0.2.0

Komplet 1507/1507 wpisów w ośmiu tabelach, wyłącznie w kulturze `pl`. Tabele en i en-001
nie są już nadpisywane. Lista języków w menu jest zaszyta w blueprintach (`Settings_BP`
„Get Languages”, `UI_Settings-Text_BP` „LanguageHack”). Skrypt `plugin/main.lua` (UE4SS
v3.0.1-1140-gf58e8f84, jak w Holy Shoot) dopisuje `pl` do zwracanej listy, a etykietę
ustawia na „Polski”. Nie usuwa ani nie przestawia pozostałych kultur i nie sprawdza wersji gry.
`tools/test_selector.py` testuje hooki na modelu parametrów UE4SS i nie zastępuje testu w grze.

ZIP (9 plików): pak z ośmioma locres `pl`, loader `dwmapi.dll`, UE4SS z licencją, `mods.txt`/`mods.json`,
skrypt i READ-ME. Build sprawdza SHA-256 archiwum UE4SS i odrzuca zasoby gry (`.uasset`, `.uexp`,
`.ufont`, `.ubulk`). Otwarte pytanie: czy silnik wczyta tabele `pl` spoza SupportedCultures
z DefaultGame.ini. Próbka pod `en` działała, ale `pl` nie było jeszcze sprawdzane w grze.

## Review 2026-09-25

Niezależny przegląd 1507/1507 wpisów: `docs/localization-review.md`. Naniesiono 8 pewnych poprawek
w `en-pl-review.json`; paczki nie przebudowano, więc 0.2.0 w `dist/` ich nie zawiera. Następny krok:
decyzje użytkownika w sprawie wariantów z raportu, potem build i pełne przejście w grze.

## Pracownia korekty

`translations/structure.yaml` dzieli teksty na 9 grup po tabeli locres (menu, samouczki, mapa, przedmioty, zadania, dziennik, dialogi, wyzwania, aktualizacje). Bez sekwencji — dialog to głównie narracja.
