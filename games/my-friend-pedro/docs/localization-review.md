# My Friend Pedro — niezależny review po fullu

Data: 2026-09-24. Przekład do wydania 0.3.1.
Status: **przeczytano 721/721 wpisów; dwie pewne poprawki wdrożone, trzy tematy redakcyjne otwarte**.
Raport zawiera informacje z późniejszych scen i zakończenia (spoilery).

## Zakres i metoda

Osobny reviewer `pedro_full_review`, świeży kontekst, tylko odczyt. Po przerwaniu
przez limit użycia wznowiono zadanie na polecenie użytkownika. Poniższe pokrycie
pochodzi z zakończonego odczytu, nie z samego raportu regexowego.

| Pozycje w JSON (od 1) | Liczba | Pierwszy — ostatni klucz |
| --- | ---: | --- |
| 1–100 | 100 | w101-1 — w4101-5 |
| 101–200 | 100 | w4101-6 — in18 |
| 201–350 | 150 | in19 — mOff |
| 351–500 | 150 | mProceed — achN28 |
| 501–650 | 150 | achD28 — Home |
| 651–721 | 71 | Page Up — iGameModNot |

Wszystkie partie przeczytano bez obcięcia. Następnie reviewer ponownie przeczytał
same polskie dialogi (pozycje 1–127, partie 1–80 i 81–127), a propozycje porównał z EN.
Nie stwierdził luk w czytaniu. Niektóre konteksty ekranowe pozostają nieznane.
Manifest kluczy i kopie robocze: `work/review-2026-09-24/`.

SHA-256 plików przeczytanych przez reviewera:

```text
pl.json: e02115e0cf144dfdcb0510cac4ac68311c093d25379969b64b5d61d339cf7dca
en-pl-review.json: 518efee61a453bdc4de797320075471bb69d20b5ce0cc1bd04e91cffed47c1a3
bible.yaml: b8066521d77f7a2ffd545cdcddb30dc6a30fa3a3931a3a949ba42061edd8ae9b
translation-decisions.md: 99d7794e6ff646614065f4051ecabfb75c74a82e991118de843e71cd3e50a777
```

Reviewer potwierdził 721 unikalnych kluczy, zgodność zbiorów kluczy i wszystkich
wartości PL w obu JSON-ach. Agent prowadzący dodatkowo porównał EN z oryginalnym
zasobem gry (SHA-256 4a81ed99cd1e8e5e4665bde87b80d4bd551bf95c088c1b3a80ed2ecfbb9764fd):
wszystkie wpisy zgodne, parser odtwarza oryginał bajtowo, tokeny i segmenty zachowane.
To kontrola plików, nie test w uruchomionej grze.

## Wprowadzone poprawki

Przed niezależnym review wdrożono zaakceptowane w102-18, w410-1, achN4 i poprawiono
odwrócony sens w102-14. Po review agent prowadzący zweryfikował poniższe dwa błędy
w pełnych EN/PL i kontekście, po czym poprawił oba polskie pliki.


### w54-1 — wprowadzono

Termin alarmów: circuit oznacza obwód, nie obieg. Minimalna zmiana bez dopisania sposobu działania.

EN:
```text
[OpheliaScreenCheckScreen]Ah crap. The wifi is really spotty around here.|[PresentingLeft]Activate the closed circuit laser alarms!
```

PL przed:
```text
[OpheliaScreenCheckScreen]Cholera. To Wi-Fi ciągle przerywa.|[PresentingLeft]Włączyć alarmy laserowe w obiegu zamkniętym!
```

PL po:
```text
[OpheliaScreenCheckScreen]Cholera. To Wi-Fi ciągle przerywa.|[PresentingLeft]Włączyć alarmy laserowe w obwodzie zamkniętym!
```


### w57-4 — wprowadzono

EN nie podaje lat. Także w511-1 i w512-2 nie ustalają jednostki czasu. Usunięto niepotwierdzony fakt chronologiczny, zachowując powtórzenie źródła.

EN:
```text
[ScreenTalk1]It really is you, isn't it??|[ScreenTalk3]After all this time...|[ScreenTalk2]It's been so long...|[ScreenTalk1]But why?|[ScreenTalk3]Why this?|[ScreenTalk1]Why now?
```

PL przed:
```text
[ScreenTalk1]To naprawdę ty, prawda??|[ScreenTalk3]Po takim czasie...|[ScreenTalk2]Tyle lat...|[ScreenTalk1]Ale dlaczego?|[ScreenTalk3]Dlaczego to robisz?|[ScreenTalk1]Dlaczego teraz?
```

PL po:
```text
[ScreenTalk1]To naprawdę ty, prawda??|[ScreenTalk3]Po takim czasie...|[ScreenTalk2]Minęło tyle czasu...|[ScreenTalk1]Ale dlaczego?|[ScreenTalk3]Dlaczego to robisz?|[ScreenTalk1]Dlaczego teraz?
```


## Trzy tematy do rozmowy — niewdrożone

### 1. Mikołaj i ojcowskie autorytety — w20-3

EN łączy „Father Christmas” z „fathers”. Po polsku nazwa „Święty Mikołaj” gubi
przygotowanie żartu. Pełna gra pokazuje też znaczenie motywu ojca (w29-1, w511-1).
Reviewer proponuje dopisać „Taki dobrotliwy ojczulek...” przy zdaniu o ojcowskich
autorytetach. Prowadzący nie przyjmuje automatycznie tej wersji: po „To ja, Denny”
może nie być jasne, do kogo odnosi się „ojczulek”.

Rekomendacja prowadzącego do rozmowy: przygotować skojarzenie wcześniej,
w segmencie przedstawienia Mikołaja: **„To ja, wasz świąteczny ojczulek — Mikołaj!”**.
Dalej pozostaje „Żartuję. To ja, Denny” i zdanie o ojcowskich autorytetach.
Zysk: czytelny związek obu części; koszt: nietypowe określenie Mikołaja i dłuższy segment.
To świadoma adaptacja, nie jednoznaczny błąd. Można zachować obecną wersję.

### 2. Początkowe zamroczenie — w101-6

Obecnie: „Nieźle cię tam załatwili”. EN „You got knocked out pretty bad there” nie
określa sprawcy. Reviewer proponuje **„Nieźle cię zamroczyło”**. Rekomenduję ten wariant:
zachowuje niedopowiedzenie, choć jest mniej precyzyjny niż utrata przytomności.
Nowy kontekst z zakończenia (w512-2): bohater sam pozbawił się przytomności.
Reviewer nie uznaje obecnego zdania za pewny błąd, bo Pedro zwodzi bohatera;
zmiana wymaga decyzji o sposobie prowadzenia tego niedopowiedzenia.

### 3. Natężenie „shit” — w28-2, eAlerted1

Obecnie „Shit!” → „Kurwa!”, a „Oh crap! Shit, shit, shit...” →
„O cholera! Kurwa, kurwa, kurwa...”. Naturalne, ale mocniejsze w PL.
Reviewer proponuje „Cholera”, zauważając utratę eskalacji po już użytym „O cholera”.

Rekomendacja prowadzącego do rozmowy:
- eAlerted1: **„Cholera!”**;
- w28-2: **„[Aargh]N-nie! O kurczę! Cholera, cholera, cholera...”**.

Zysk: mniejsza siła i zachowany wzrost od łagodniejszego okrzyku do powtarzanego
przekleństwa. Koszt: łagodniejsze również „Oh crap”; scena może wymagać większej
intensywności. Nie jest to globalna zamiana wulgaryzmów. W401-1 z „FFFFUUUU...”
pozostaje mocnym „KUUUURWAAAAAA...!”, zgodnie z formą źródła.

### Pełne źródła otwartych tematów


#### w20-3

EN:
```text
[WelcomeWave]Ho ho ho! Welcome and merry Christmas, everybody.|[ItsMe]It's me, Father Christmas!|[JustKidding]Just kidding. It's me, Denny.|[Talking_1]We all know fathers are just disappointing authority figures anyways...|[Talking_1]I'm glad to see so many faces out there.|[Talking_1]But let's cut to the chase. I know why you all bothered following the dress code and show up tonight.|[Dazzle]The Mega Christmas Bounty!
```

Obecne PL (bez zmian):
```text
[WelcomeWave]Ho, ho, ho! Witajcie i wesołych świąt!|[ItsMe]To ja, Święty Mikołaj!|[JustKidding]Żartuję. To ja, Denny.|[Talking_1]Wszyscy wiemy, że te ojcowskie autorytety i tak tylko rozczarowują...|[Talking_1]Miło widzieć tyle znajomych twarzy.|[Talking_1]Ale do rzeczy. Wiem, dlaczego zechcieliście się przebrać i przyjść tu dziś wieczorem.|[Dazzle]Wielka Gwiazdkowa Nagroda!
```


#### w101-6

EN:
```text
It's me. <color=#FFF49F>Pedro</color>. <i>Your friend</i>...|You got knocked out pretty bad there.|Are you okay?|How many fingers am I holding up?|Never mind.|Let's just get out of here... Wherever we are.
```

Obecne PL (bez zmian):
```text
To ja. <color=#FFF49F>Pedro</color>. <i>Twój przyjaciel</i>...|Nieźle cię tam załatwili.|Wszystko gra?|Ile palców pokazuję?|Nieważne.|Po prostu się stąd wynośmy... Gdziekolwiek jesteśmy.
```


#### w28-2

EN:
```text
[Aargh]N-no! Oh crap! Shit, shit, shit...
```

Obecne PL (bez zmian):
```text
[Aargh]N-nie! O cholera! Kurwa, kurwa, kurwa...
```


#### eAlerted1

EN:
```text
Shit!
```

Obecne PL (bez zmian):
```text
Kurwa!
```


## Ponowna ocena początkowych decyzji

| Decyzja | Werdykt na całości i przesłanki |
| --- | --- |
| Potoczny, pozornie troskliwy Pedro | Utrzymać: w102-12, w24-1, w32-1, w55-1; finał w512-2–w513-1 zachowuje także powagę, nie dopisujemy żartów. |
| Zaakceptowane w102-18 | Utrzymać bez zmian: lekka forma makabrycznej rady pasuje do późniejszych scen. |
| Adaptacja istniejących sucharów | Utrzymać: w24-1 pozostaje celowo nieudanym wierszem, w52-2 zachowuje samozaprzeczenie Ofelii. |
| Zaakceptowane w410-1 | Utrzymać bez zmian: w4101-1–w4101-2 potwierdzają rzeczywisty kontekst kolejowy. |
| Czary-combary, Combo na zaczes, słowo combo | Utrzymać bez zmian: opisy x10/x20 jednoznaczne; nie wracać do odrzuconego opisowego wariantu. |
| Pozostałe nazwy osiągnięć | Utrzymać: Mięsko mi cię poznać, Lotna patelnia, Beczka niespodzianek i Pociąg do myślenia pozostają związane z opisami. |
| Focus → skupienie | Utrzymać: w102-2, in9, mFocus, mInfFocus, mSlowScale. |
| Split aim → rozdzielanie celowania | Utrzymać: w102-9 objaśnia pHint3; „Dwa cele” w bul8 to skrót punktowy, nie błąd terminu. |
| Mitch Rzeźnik, szorstki ton | Utrzymać: w102-19, w102-21, w175-2 i pościg; nie dodawać wulgaryzmów. |
| Ofelia, rodzaj żeński | Utrzymać: autoprezentacja, w29-1 i finał. |
| Pedro, Denny, pozostałe imiona i kody ISP | Utrzymać: odmiana spójna, oznaczenia nie wymagają tłumaczenia. |
| Stare Miasto, Dzielnica Null, Świat Pedra, Kanały, Internet | Utrzymać: zgodne dialogi, wybór rozdziału i osiągnięcia. |
| Internetowa Straż Porządkowa (ISP) | Utrzymać: w45-1, w46-1 i zachowane inicjały. |
| Hejterzy i slang growy | Utrzymać: w32-1, w34-1, odzywki; nie trzeba zostawiać każdego skrótu po angielsku. |
| Jednoznaczne UI | Utrzymać: hChW/mChgWep i mKick/bul28 mają różne funkcje, nie ujednolicać mechanicznie. |
| Dopowiedzenia A/B/C/S | Utrzymać: wszystkie zaczynają się od właściwych liter; szerokość pola do testu. |
| Nazwy klawiszy, tytuł gry | Utrzymać; Home/Page Down są czytelnymi oznaczeniami klawiszy. |
| Historyczna integracja Twittera | Utrzymać przekład źródła; działanie integracji niezweryfikowane. |
| Tagi, animacje, segmenty | Utrzymać; [Nieprzypisane] to etykieta, nie komenda. |

Nie stwierdzono odwróconych warunków lub utraconych liczb w osiągnięciach,
trudnościach i modyfikatorach. Zachowano różnice naciśnij/przytrzymaj, efekty jednego
trafienia dla gracza/wroga oraz brak zapisu i wysyłania wyników przy modyfikatorach.
`mExpNotice` zalecające angielski w eksperymentalnej wersji oddaje treść źródła.

## Raport automatyczny i granice oceny

Wejście: brak=0, tokeny=0, płeć=0, adresat=0, terminy=0, spójność=6,
angielski=30, długość=18, wielkie_litery=1. Wszystkie sekcje oceniono.
Nazwy, klawisze i slang uznano za zamierzone, warianty Splendid za dopuszczalne.
`in23` zawiera dwa polecenia po separatorze, nie angielski Title Case.
Ostrzeżenia długości pozostają wskazówkami do testu, nie potwierdzeniem ucięć.
Brak regexów mówiących w biblii oznacza, że zero automatycznych zgłoszeń płci
nie dowodzi jej poprawności; ten aspekt czytał reviewer w kontekście tekstu.

## Do testu użytkownika w grze

- Początek: w102-18 — rytm rady Pedra; polskie znaki i segmenty dialogu.
- Kolej: w410-1 — tok/tor myślenia; osiągnięcie combo x20 — „Combo na zaczes”.
- Internet, w54-1 — alarm i czytelność poprawionej kwestii; w57-4 i długie kwestie
  w511-1/w512-2 — czas na odczyt, podział i ucięcia.
- HUD hSec („DRUGA BROŃ”) oraz wyzwalacz interact6 („Przewróć”): znaczenie etykiet
  nie jest rozstrzygnięte na podstawie samych tabel, brak dowodu błędu.
- pHint3, pHint4, in36 — długość tekstu oraz ikony rozdzielania celowania i lunety.
- Wyniki A/C/S, etykiety modyfikatorów, „Prędkość czasu w skupieniu”.
- Po ewentualnej akceptacji dodatkowej redakcji: w20-3 — rytm przygotowania żartu.

Gra nie została uruchomiona przez agenta. Potwierdzony vertical pozostaje
potwierdzony; pełnej kampanii ani nowej korekty 0.3.1 nie uznajemy za ograne.

## Kontrola po integracji i paczka

Prowadzący ponownie sprawdził dwie poprawki review i ich kontekst. Klucze oraz EN
pozostały identyczne, 721/721 wartości PL jest zgodnych w JSON-ach i TSV w archiwum.
Zachowana kolejność znaczników, komend animacji i granic segmentów.
Łącznie sześć zmienionych wpisów względem 0.3; propozycje do rozmowy nietknięte.

Raport po uzasadnionym oznaczeniu wyjątków w biblii: wszystkie sekcje 0 poza
18 ostrzeżeniami długości do sprawdzenia w grze. Nie jest to wynik jakości ani
dowód braku błędów językowych.

Zbudowano `My-Friend-Pedro-PL-0.3.1.zip` (661725 B)
i identyczną kopię w `site/public/pobierz/`. Archiwum zawiera wyłącznie pliki
oficjalnego BepInEx (wszystkie, niezmienione), nasz plugin/teksty/licencję oraz READ-ME
i licencję BepInEx. Źródła BepInEx 5.4.23.5 leżą obok obu kopii paczki.
Nie instalowano 0.3.1 do gry ani nie uruchamiano gry.

SHA-256 po poprawkach:
```text
pl.json: 5340e4b88861d4ca3e9a7336f4e9c1f93f3caf36fe2e8c16dc3207cf76de73c0
en-pl-review.json: 5327df6f7abbf47456e2021745adc9b0feb091bf12ae6385088a740f5cb5b046
ZIP: 11ea358c2cc4b2a374f1aaf86a1956074dd585b03c7b5c0e4d20f7afd6da9353
```
