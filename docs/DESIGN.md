# notgoose.cc — kierunek artystyczny

Handoff do repozytorium. Dokument jest niezależny od stacku: opisuje decyzje
wizualne i zachowania, nie implementację. Wartości liczbowe pochodzą z makiet
i są wiążące — jeśli coś ma się zmienić, lepiej zmienić to tutaj niż rozjechać
w kodzie.

---

## 1. Koncept

Nazwa jest cytatem. „A niechaj narodowie wżdy postronni znają, iż Polacy nie
gęsi, iż swój język mają" (Mikołaj Rej, 1562) to najstarszy polski manifest
w obronie własnego języka, a strona o fanowskich spolszczeniach robi dokładnie
to samo, sześć wieków później. Stąd `notgoose` i stąd gęś przekreślona czerwoną
kreską jako znak.

Z tego wynika ton: plakatowy, drukarski, trochę manifestowy. Nie gamingowy
neon, nie miękki korporacyjny interfejs. Bliżej afisza i składu typograficznego
niż launchera gier. Typografia niesie całość, kolor jest używany oszczędnie
i zawsze jako płaska plama, nigdy jako efekt.

Strona jest portfolio. Gry mają wyglądać dobrze, ale to warsztat tłumacza jest
bohaterem — dlatego cytat z gry w polskim przekładzie dostaje własną ramkę
i dominuje w panelu szczegółów nad wszystkim poza tytułem.

---

## 2. Kolor

Paleta jest zamknięta. Pięć wartości plus dwie pomocnicze do tekstu.

| Token | Hex | Rola |
|---|---|---|
| `bone` | `#E9E5DB` | Tło strony. Ciepła neutralna kość słoniowa, bez niebieskiego podbicia. |
| `paper` | `#FFFFFF` | Powierzchnie wyniesione: karty, ramki cytatów, sekcja z siatką. |
| `ink` | `#14130F` | Tekst, wszystkie ramki, wszystkie cienie, pasek statystyk. |
| `accent` | `#D6341F` | Czerwień plakatowa. Akcenty graficzne i wypełnienie głównego CTA. |
| `red-deep` | `#B02510` | Ciemniejsza czerwień. Wyłącznie jako tło pod drobnym białym tekstem. |
| `navy` | `#003670` | Status „ukończone", tła keyartów, drugi kolor kafelków. |
| `muted` | `#57534A` | Tekst drugorzędny na jasnym tle. |
| `muted-inverse` | `#B9B3A4` | Tekst drugorzędny na `ink`. |
| `hairline` | `#C9C3B4` | Cienkie linie 1 px wewnątrz ramek, np. wiersze tabeli metadanych. |

**Zasada rozdziału dwóch czerwieni jest istotna i łatwo ją zgubić.** `accent`
ma kontrast 4,4:1 z czernią, co wystarcza tylko dla tekstu od 18,66 px wzwyż
w grubym kroju. Dlatego `accent` pojawia się pod dużym napisem CTA
(Archivo Black 18–20 px) i jako czysta grafika: kwadracik przy nadnagłówku,
kreska pod nagłówkiem hero, pas przekreślający gęś, znak cudzysłowu. Nigdy nie
trafia pod drobny tekst. Wszędzie tam, gdzie na czerwieni ma stanąć biała
etykieta 10–11 px — plakietka „w trakcie", tło keyartu — używa się `red-deep`,
które daje 5,8:1.

Tła keyartów rotują między `navy`, `red-deep` i `ink`. Wszystkie trzy są
ciemne, więc etykieta `[KEYART]` w kolorze `bone` jest czytelna na każdym
z nich bez sprawdzania przypadku po przypadku.

Tryb ciemny nie jest na razie zaprojektowany. Jeśli będzie potrzebny, naturalne
odwrócenie to `ink` jako tło, `bone` jako tekst i `accent` bez zmian — ale
wtedy `navy` trzeba rozjaśnić, bo na czerni przestaje być czytelny.

---

## 3. Typografia

Trzy kroje, wszystkie z Google Fonts, wszystkie z pełnym zestawem
latin-ext — to warunek konieczny, ogonki i kreski muszą wyglądać jak część
kroju, a nie jak proteza.

| Rola | Krój | Waga |
|---|---|---|
| Display | Archivo Black | 400 |
| Treść | Space Grotesk | 400 / 500 / 700 |
| Metadane | JetBrains Mono | 400 / 700 |

Archivo Black to jedyny krój nagłówkowy i występuje wyłącznie wersalikami,
z ujemnym światłem. Space Grotesk obsługuje opisy, cytaty i zdania. JetBrains
Mono jest zarezerwowany dla wszystkiego, co jest etykietą albo danymi: rok,
platforma, gatunek, wersja, waga pliku, nazwy sekcji, nawigacja, stopka.
Ten podział niesie sporo znaczenia — użytkownik po dwóch ekranach wie, że
mono znaczy „metadane" — więc nie warto go mieszać.

Skala, desktop / mobile:

| Poziom | Desktop | Mobile | Interlinia | Światło |
|---|---|---|---|---|
| Hero | 118 px | 46 px | 0,88 / 0,90 | −0,035em |
| Nagłówek sekcji | 56 px | 30 px | 1,0 | −0,03em |
| Nagłówek stopki / panelu | 40–44 px | 28 px | 0,98 | −0,03em |
| Tytuł kafelka | 22 px | 20 px | 1,05 | 0 |
| Liczba w statystykach | 56 px | 38 px | 1,0 | 0 |
| Cytat | 21 px | 15 px | 1,45–1,5 | 0 |
| Treść | 16–17 px | 14 px | 1,55–1,6 | 0 |
| Etykieta mono | 12 px | 10 px | — | 0,14–0,18em |
| Metadane mono | 11 px | 10 px | — | 0,10em |

Etykiety mono zawsze wersalikami. Tekst treści nigdy wersalikami — dłuższe
zdanie w kapitalikach przestaje się czytać, a opisy spolszczeń bywają długie.

---

## 4. Siatka i odstępy

Skala odstępów jest wielokrotnością czwórki: 4, 8, 12, 16, 20, 24, 28, 32, 40,
48, 64, 72, 80. Poza nią nie wychodzimy.

Desktop projektowany na 1440 px, margines boczny 80 px, siatka gier
trzykolumnowa z odstępem 28 px, co daje kafelek 408 × 380 px. Mobile na 390 px,
margines 20 px, jedna kolumna z odstępem 20 px, kafelek 318 px wysokości.
Między tymi szerokościami siatka ma płynnie schodzić z trzech kolumn na dwie,
a poniżej 700 px na jedną; szerokość kafelka jest elastyczna, wysokość ustalają
proporcja keyartu i stała wysokość opisu pod nim.

Sekcje mają jasny rytm tłem, nie tylko odstępem: hero na `bone`, pas statystyk
na `ink`, siatka gier na `paper`, stopka znów na `bone`. Każdą granicę
podkreśla ramka 3 px.

---

## 5. Język formy

Tu jest cała tożsamość i trzy reguły trzymają ją w ryzach.

Ramka to zawsze 3 px pełnej linii w kolorze `ink` — na kartach, przyciskach,
polach, ilustracjach, między sekcjami. Nigdy cieńsza, nigdy w innym kolorze,
nigdy tylko z jednej strony jako ozdoba.

Cień to przesunięcie bez rozmycia: `8px 8px 0` w kolorze `ink` na desktopie,
`7px 7px 0` na mobile. To nie jest efekt głębi, tylko druga warstwa druku
z przesuniętym rejestrem. Rozmycie, przezroczystość i cień w innym kolorze niż
`ink` psują tę metaforę — jedyny wyjątek to karta aktualnie otwarta w panelu,
która dostaje cień w kolorze `accent` jako oznaczenie stanu.

Promień zaokrąglenia wynosi zero. Wszędzie. Jedyny wyjątek to uchwyt szuflady
na mobile, który jest 52 × 5 px z promieniem 3 px, bo to element gestu,
nie element kompozycji.

---

## 6. Komponenty

### Kafelek gry

Keyart na górze w proporcji 16:9, pod nim ramka 3 px oddzielająca opis,
w opisie tytuł, wiersz metadanych i przyklejony do dołu wiersz statusu.
Wysokość opisu jest stała niezależnie od długości tytułu, więc dolne krawędzie
kafelków w rzędzie się zgadzają — dwuwierszowy tytuł zjada odstęp,
nie wypycha karty.

Na keyarcie leży etykieta `[KEYART]` w lewym górnym rogu i wielka litera
inicjału tytułu w prawym dolnym, ścięta krawędzią, w `rgba(255,255,255,0.13)`.
To placeholder na czas, gdy nie ma grafiki — po wstawieniu prawdziwego keyartu
oba elementy znikają.

Cały kafelek jest linkiem, nie diva z obsługą kliknięcia. To ma znaczenie dla
nawigacji klawiaturą i dla otwierania w nowej karcie.

### Panel szczegółów

Desktop: panel o szerokości 560 px wysuwa się z prawej krawędzi, a siatka
w tym samym ruchu schodzi z trzech kolumn na dwie. Kafelki zostają widoczne,
więc można przeskakiwać między grami bez zamykania panelu — to była główna
decyzja i warto jej pilnować przy implementacji, bo najprostsze rozwiązanie
(modal z przyciemnieniem) tę właściwość zabija.

Kolejność w panelu jest celowa: pasek keyartu, tytuł, status i metadane, cytat
z gry, krótki opis, przycisk pobierania, przyciski sklepów, tabela metadanych
przyklejona do dołu. Cytat stoi przed opisem, bo to on pokazuje jakość
przekładu — czyli to, po co ktoś tu przyszedł.

Przycisk zamykania to kwadrat 44 × 44 px z krzyżykiem, z `aria-label`.

Mobile: ten sam panel wjeżdża od dołu jako szuflada, z uchwytem u góry,
przyciemnieniem tła `rgba(20,19,15,0.58)` i zamykaniem gestem w dół.
Wysokość maksymalna około 88% okna, treść w środku przewijalna.

### Przyciski

Główny: wypełnienie `accent`, tekst Archivo Black w kolorze `ink`, ramka 3 px,
cień 8 px. Na hover przesuwa się o 4 px w stronę cienia, a cień kurczy się
do 4 px — wrażenie fizycznego wciśnięcia.

Drugorzędny (sklepy, kontakt): tło `paper`, tekst i ramka `ink`. Na hover
wypełnienie i ramka zrównują się na `ink`, tekst przechodzi na `bone`. Stan
najechania jest pełny i jednolity, bez półprzezroczystości.

Wszystkie elementy klikalne mają minimum 44 × 44 px. Stan `:focus-visible` to
obrys 3 px w kolorze `accent` z odstępem 3 px — musi być widoczny także na
elementach, które same są czerwone, więc na CTA obrys przechodzi na `ink`.

### Plakietki statusu

Mono 11 px, wersaliki, wypełnienie pełne, bez ramki i bez promienia.
`Ukończone` na `navy` z białym tekstem, `w trakcie` na `red-deep` z białym
tekstem, `wstrzymane` jako sama ramka `ink` na tle karty. Obok plakietki stoi
numer wersji albo procent postępu, zwykłym mono w kolorze `muted`.

### Pasek statystyk

Cztery pola na tle `ink`, rozdzielone pionowymi liniami 3 px w kolorze `bone`.
Liczba w Archivo Black, pod nią etykieta mono. Na mobile układ 2 × 2 z liniami
w obu osiach.

---

## 7. Zachowanie i punkty łamania

| Zakres | Siatka | Panel |
|---|---|---|
| ≥ 1100 px | 3 kolumny, po otwarciu panelu 2 | Wysuwany z prawej, 560 px |
| 700–1099 px | 2 kolumny | Nakładka z prawej, ~480 px, tło przyciemnione |
| < 700 px | 1 kolumna | Szuflada od dołu |

Animacja wysuwania i zwężania siatki: 240 ms, `cubic-bezier(0.2, 0, 0, 1)`.
Obie rzeczy dzieją się w tym samym czasie, inaczej układ wygląda na zepsuty.
Przy `prefers-reduced-motion` przejścia znikają, panel po prostu się pojawia.

Escape zamyka panel. Na mobile szuflada jest modalna: pułapka na fokus,
`aria-modal`, tło pod spodem nie przewija się. Na desktopie panel nie jest
modalny, bo siatka obok zostaje aktywna.

---

## 8. Dostępność

Wszystkie kolory tekstu w makiecie przechodzą 4,5:1, z jednym świadomym
wyjątkiem opisanym w sekcji o kolorze. Struktura ma być zbudowana na prawdziwych
elementach: `a` dla nawigacji i kafelków, `button` dla filtrów i zamykania,
`h1`–`h3` w kolejności, `aria-label` na przyciskach z samą ikoną. Żadnych
`div`-ów z `onClick`, bo Tab je pomija.

Ikony są wektorami rysowanymi obrysem, dziedziczą kolor tekstu i dostają
`aria-hidden`. Emoji nie występują nigdzie.

---

## 9. Zasoby

Na grę potrzebny jest jeden keyart 1600 × 900 px, WebP z fallbackiem JPG,
kadrowany tak, żeby istotny element nie siedział przy prawej krawędzi — tam
w panelu wchodzi węższy wykrój. Wszystkie węższe warianty da się z tego
przyciąć przez `object-fit: cover`.

Trzy kroje ładowane z Google Fonts z podzbiorem `latin` i `latin-ext`,
`display=swap`. Jeśli będziesz hostować lokalnie, wystarczą cztery pliki woff2:
Archivo Black 400, Space Grotesk 400 i 700, JetBrains Mono 400 i 700.

---

## 10. Czego nie robić

Gradientów, zaokrągleń, rozmytych cieni, półprzezroczystych warstw
poza przyciemnieniem szuflady, kroju Inter, Roboto ani Arial, emoji,
ikon wypełnionych zamiast obrysowych, drobnego białego tekstu na `accent`,
kart z akcentem tylko na lewej krawędzi oraz modala zamiast wysuwanego panelu
na desktopie.

---

## 11. Treść do uzupełnienia

W makietach stoją placeholdery w nawiasach kwadratowych — liczby w pasku
statystyk, cytaty, opisy, daty i zakres spolszczenia. Tytuły gier w siatce są
przykładowe i służą wyłącznie ocenie kompozycji.

Cytaty z gier wstaw własne, ze swoich przekładów. Oryginalne kwestie dialogowe
są chronione prawem autorskim niezależnie od tego, w jakim są języku, więc
bezpiecznie cytować można tylko krótkie fragmenty i warto podpisać je sceną
albo postacią, tak jak przewiduje układ panelu.
