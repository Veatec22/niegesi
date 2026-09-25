# I Am Your Beast — decyzje tłumaczenia

## Przed verticalem

Data: 2026-09-25. Status: **kierunek uzgodniony z użytkownikiem**.

Odpowiedź użytkownika: tematy 1 i 2 według rekomendacji; temat 3 — „Sezon na kłólika”
i „Jestem twoją bestią”; temat 6 zmieniony: skoro pełna nazwa jest po polsku, skrót też —
**COI → ITO**. Ustalenia przeniesiono do `translations/bible.yaml`. Poniżej zachowano
próbkę z wariantami; wystąpienia „COI” w polskich propozycjach należy czytać jako „I.T.O.”.

Po teście verticala (2026-09-25) użytkownik zmienił zapis skrótu na **I.T.O.** z kropkami:
bez nich „ITO” czytało się jak słowo, nie jak skrótowiec.

Źródło próbki: `work/survey.json` (ekstrakcja z `inspect_game.py`). Klucze dialogów
to `<nazwa PhraseAsset>#<indeks odcinka>`, klucze banku Fleece to ID pasażu.
Mówiącego w scenach ustalono po kolejności wymiany i kolorystyce odcinka
(`setColorScheme`: 7231/7236 Harding, 7233 Burkin, 7234 Byron); gra nie ma etykiet
z imionami. Dalsze sceny przejrzano tylko pod kątem form zwracania się.

Ograniczenie materiału: zasoby `SCENE 1`–`SCENE 9` (dodatek Support Group) zawierają
tekst wyglądający na automatyczną transkrypcję z błędami („Birken did even a rapper”).
Poprawnie zredagowane kwestie tej samej historii są w banku Fleece (folder 44072 i inne).
Który tekst gra wyświetla, ustalimy przy pełnym zakresie; próbka ich nie dotyczy.

### 1. Głos Hardinga: sucha, ironiczna uprzejmość

Status: **uzgodnione z użytkownikiem**.

Harding mówi spokojnie, krótko albo celowo zbyt kulturalnie, a jego humor bierze się
z kontrastu z wrzeszczącym Burkinem i przeklinającymi żołnierzami. Przeklina rzadko,
więc kiedy już to robi („Ffffuck.” w `8 Helper Alpha#16`), ma to wagę. Nie robimy
z niego twardziela z filmu akcji ani nie spłaszczamy przydługich, ironicznie
grzecznych zdań.

`4_ImpoliteDispute#4`
- EN: I believe I'm making it very unpleasant for a COI agent to exist in the relatively small patch of forest I've made my home.
- Rekomendacja: Wydaje mi się, że uprzykrzam życie agentom COI na tym dość niewielkim skrawku lasu, w którym urządziłem sobie dom.

`2_Tete-A-Tete#16`
- EN: I may be out in the middle of nowhere but, I still find time to read.
- Rekomendacja: Może i siedzę na końcu świata, ale na czytanie wciąż znajduję czas.

`9 Anger#15`–`#21` (Burkin właśnie wrzasnął o wojnie z rządem)
- EN: I'm whittling a bird out of soap, Charles. / I don't know what kind of bird it is / because I'm new to whittling. / but it's... / but it's...some kind of bird. / and the only thing keeping me from my bird-shaped object / is you sending another company of motherfuckers into my home.
- Rekomendacja: Strugam ptaka z mydła, Charles. / Nie wiem, co to za ptak, / bo dopiero zaczynam strugać. / ale to... / ale to... jakiś ptak. / a jedyne, co mnie odrywa od mojego ptakopodobnego obiektu, / to kolejna kompania skurwieli, którą przysyłasz mi do domu.
- Wariant: „Rzeźbię w mydle ptaszka, Charles.”

Zdrobnienie „ptaszek” dokłada komizmu i infantylności, której w EN nie ma — Harding
mówi o ptaku całkiem serio i to jest żart. Rekomenduję „ptaka”.

### 2. Formy zwracania się

Status: **uzgodnione z użytkownikiem**.

- **Harding ↔ Burkin: „ty” w obie strony.** Znają się od lat (wspólna przeszłość
  wraca w późniejszych scenach). Dystans niesie tytuł i imię, nie forma czasownika:
  Harding mówi „generale”, a przy drwinie „Charles”; Burkin mówi „Harding”, „synu”.
  W jednej z późnych scen zmiana „generał/Charles” ma znaczenie fabularne i „ty”
  ją zachowuje. Wariant „pan generał” z formą pańską po stronie Hardinga odrzucam:
  brzmi jak regulamin, a Harding od pierwszej kwestii ostentacyjnie go łamie.
- **Byron → Harding: „pan” przy pierwszym kontakcie, „ty” od następnego.**
  W `6 Help Wanted` Byron zaczyna od „Mister, uh... Mister Alphonse Harding?”,
  jąka się i przeprasza. W `8 Helper Alpha` wita się już „Alphonse? You there?”.
  Polskie „pan” oddaje tremę przed legendą, a przejście na imię i „ty” pokazuje,
  że układ się zadomowił. Harding do Byrona od początku mówi „ty”.
- Wariant: Byron cały czas na „ty” (prościej, bez przeskoku, ale bez tremy
  z pierwszej rozmowy). Byron cały czas na „pan” odpada, bo gryzie się z „Alphonse”.

`6 Help Wanted#0`–`#14` w rekomendacji:
- EN: Uh, hello? / Mister, uh... / Mister Alphonse Harding? / You're...lost. / heh / In case you didn't know. / Using an old frequency. / Rest of the force changed over a couple days ago. / Uh, yeah. / I know. / I know. / I just... / \*sigh\* / figured you might still be monitoring it? / Just in case?
- PL: Eee, halo? / Panie, eee... / Pan Alphonse Harding? / Zabłądziłeś. / heh / Gdybyś nie wiedział. / Nadajesz na starej częstotliwości. / Reszta sił przeszła na nową parę dni temu. / Eee, no tak. / Wiem. / Wiem. / Ja tylko... / \*westchnienie\* / pomyślałem, że może pan jej wciąż nasłuchuje? / Tak na wszelki wypadek?

Nazwiska odmieniamy (Hardinga, Burkinowi, Byrona), w wołaczu zostaje mianownik
(„Harding!”, „Alphonse?”) — tak brzmi to w mowie. **Decyzja agenta.**

### 3. Nazwy poziomów i scen

Status: **uzgodnione z użytkownikiem**.

Tłumaczymy z adaptacją, zachowując nawiązania czytelne po polsku. Tytuł gry na logo
zostaje angielski.

| Klucz | EN | Rekomendacja | Uwagi |
|---|---|---|---|
| 51597 | Walkout | Odejście | |
| 95252 / 78486 | Tete-a-Tete | Tête-à-tête | polszczyzna ma ten zwrot |
| 29327 | Starting Gun | Strzał startowy | |
| 62995 | Mind the Gap | Uwaga na przepaść | gra słów z metrem londyńskim tylko częściowo |
| 33876 | On Your Six | Na szóstej | |
| 53057 | Javert and Valjean | Javert i Valjean | „Nędznicy” są u nas znani |
| 45110 | Wabbit Season | Sezon na kłólika | wariant: „Sezon polowań” |
| 61392 | I Am Your Beast | Jestem twoją bestią | wariant: zostawić po angielsku |
| 90608 | I Am Your Fears | Jestem twoim strachem | idzie za wyborem powyżej |

„Wabbit Season” to Elmer Fudd polujący na Królika Bugsa; w scenie żołnierz woła
„kici, kici” i drwi z ukrywającego się Hardinga. „Kłólik” zachowuje wadę wymowy
i myśliwski żart, „Sezon polowań” jest bezpieczny, ale bez żartu.

Ostatni poziom nosi tytuł gry. Po polsku „Jestem twoją bestią” nadal czyta się
jako nawiązanie do tytułu, a gracz rozumie sens; angielski tytuł wyglądałby
na nieprzetłumaczony wpis wśród polskich nazw.

### 4. Wulgaryzmy tej samej siły

Status: **decyzja agenta**, zgodnie z przyjętą praktyką w Wild Bastards, Katana ZERO
i Laika. Nie łagodzimy i nie dokładamy. Humor żołnierzy i wściekłość Burkina opierają
się na przekleństwach, a spokój Hardinga działa właśnie na ich tle. Bez obelg
homofobicznych (w Laice odrzucono „cioto”).

| Klucz | EN | PL |
|---|---|---|
| `9 Anger#3` | FUCK your access code! | PIERDOLĘ twój kod dostępu! |
| `8 Helper Alpha#16` | Ffffuck. | Kuuurwa. |
| 46685 | Employee of the motherfucking month! | Pracownik, kurwa, miesiąca! |
| `3_WabbitSeason#8` | Come on out, ya big bitch! | No wyłaź, ty cipo! |
| 14641 | The fuck. Do you watch me piss? | Co, kurwa? Patrzysz, jak sikam? |

### 5. Pocięte kwestie i zdania narastające

Status: **decyzja agenta** (wymóg techniczny i redakcyjny).

Odcinki pojawiają się w rytmie głosu. Tłumaczymy każdy odcinek osobno i tak, żeby
polski szyk dał się pociąć w tych samych miejscach. Zdania narastające zachowują
początek dosłownie, bo gra wyświetla najpierw krótszy wariant, a potem pełny:

`2_Tete-A-Tete#26`–`#29`
- EN: See, / See, I don't think that's true. / I think as of 5 one-last-jobs ago, / I think as of 5 one-last-jobs ago, you owe me.
- PL: Widzisz, / Widzisz, ja tak nie uważam. / Według mnie od pięciu „ostatnich robót” / Według mnie od pięciu „ostatnich robót” to ty jesteś winien mnie.

Gdy polski szyk wymusza inny podział, przesuwamy granicę odcinka i odnotowujemy to
do sprawdzenia w grze. Jąkanie, urwania („--”) i didaskalia (`*sigh*` → `*westchnienie*`,
`*click*` → `*klik*`) zostają.

### 6. Terminy

Status: **decyzja agenta**.

- **COI → I.T.O.** (uzgodnione z użytkownikiem; pierwotna propozycja zostawienia „COI”
  odrzucona). Covert Operations Initiative → Inicjatywa Tajnych Operacji. Skrót
  nieodmienny, rodzaj żeński według wyrazu głównego: „I.T.O. zrobiła ze mnie…”
  (decyzja agenta). Napisy na teksturach, jeśli są, zostają.
- **one last job → ostatnia robota**. Motyw wraca w dialogach („5 one-last-jobs ago”),
  więc jedno sformułowanie wszędzie. „Zlecenie” jest zbyt urzędowe, „misja” zbyt wojskowa
  jak na cynizm Hardinga.
- Alfabet NATO w kodach dostępu zostaje: „Osiem, Hotel, Alfa, Delta, Echo, Sierra”.
- „Dear diary” → „Drogi pamiętniku”.
- Mechanika: Stomp → zdeptanie (Stomp Kill → zabójstwo z wyskoku / zdeptanie — do
  sprawdzenia w HUD-zie), Kick → kopnięcie, Quick Turn → szybki obrót, Perch → „Przyczaj się”
  (polecenie na drzewie; po review poprawiony zapis — wcześniej „przyczajka”), Kill Confirms → potwierdzenia zabójstw, poultice bushes → ziołowe krzaki.
  Oceny S–D zostają literami.
- Napisy końcowe: tłumaczymy funkcje, nazwiska i nazwy studiów bez zmian.

## Próbka EN/PL — pozostałe wpisy

Wpisy z UI i samouczka, bez wariantów. Rekomendacja idzie do verticala.

| Klucz | EN | PL |
|---|---|---|
| 324 | Start | Start |
| 25268 | Settings | Ustawienia |
| 38771 | Quit | Wyjdź |
| 89364 | Assists | Ułatwienia |
| 75738 | Press [KEY] to jump. | Naciśnij [KEY], aby skoczyć. |
| 69814 | Press [KEY] to jump on enemies' heads. | Naciśnij [KEY], aby wskoczyć wrogom na głowy. |
| 28980 | Catch the shotgun with [KEY]. | Naciśnij [KEY], aby złapać strzelbę. |
| 89426 | Use poultice bushes to heal yourself. | Ulecz się przy ziołowych krzakach. |
| 15082 | Scopes are for cowards. Alphonse isn't a coward. | Celowniki optyczne są dla tchórzy. Alphonse nie jest tchórzem. |
| 44082 | Holding guns sideways makes them more accurate. | Broń trzymana bokiem strzela celniej. |
| `TUT_DearDiary#2`–`#3` | Did I tell you that I saw a bird? / It had brown feathers and a red chest - it gleamed against the sky. | Mówiłem ci, że widziałem ptaka? / Miał brązowe pióra i czerwoną pierś — lśnił na tle nieba. |
| `TUT_IDidntFeelAThing` | I didn't feel a thing. / I am what the COI made me. / And I'm not going back. | Nic nie poczułem. / Jestem tym, co zrobiła ze mnie I.T.O. / I nie zamierzam wracać. |
| `2_Tete-A-Tete#17`–`#19` | It's one last job, Harding. / One last job. / And you're out. | To ostatnia robota, Harding. / Jedna ostatnia robota. / I jesteś wolny. |

## Po fullu — niezależny przegląd (2026-09-25)

Osobny reviewer w świeżym kontekście przeczytał wszystkie 1581 wpisów scenami i grupami
(szczegóły: `docs/localization-review.md`). Wszystkie decyzje sprzed verticala: **utrzymać**.

Naniesione od razu (pewne błędy):
- `6 Help Wanted/54` „Puści go pan.” → „Puści mnie pan.” — błąd sensu: agentem
  w różowej rękawiczce jest sam Byron.
- `4_ImpoliteDispute/22` „rozerwaną na pół z broni” → „przez broń” (składnia).
- `FINAL CUTSCENE/25` kalka „To powiedziawszy...” → „No dobrze...”.
- `12 Helper Gamma/13–16` „za mgliście” → „za mglisto” (pogoda), z zachowaniem przedrostka.
- `fleece/2306` „Nie zabij nikogo” → „Nie zabijaj nikogo”; `fleece/48222` „Okno” → „W oknie”.
- Ustawienia ułatwień: „rangę S” → „ocenę S”, jak wszędzie indziej.
- `SCENE 1/4` bez „stary” — Bob mówi do Jodie (kobieta według biblii).
- Decyzja agenta w ramach tematu 4: „pieprzony” → „pierdolony” w `fleece/29393`
  i `SCENE 1/14`, jak pozostałe „fucking”.
- Nathan mówił do Burkina raz „ty”, raz „pan”: `SCENE 9/26–27` → „O tak, szefie. /
  Świetnie pan wygląda.”
- Ekran odblokowań: gra skleja „Complete” + nazwa kampanii + „bonus objectives x5”.
  „Ukończ Fabuła cele dodatkowe” → „Ukończ: Fabuła – cele dodatkowe x5”
  (`fleece/99330`, `fleece/84896`). Do sprawdzenia w grze.

Warianty do rozmowy z użytkownikiem: w `docs/localization-review.md`, sekcja 3.

### Rozmowa o wariantach z przeglądu

Użytkownik (2026-09-25) przyjął cztery z pięciu przedstawionych wariantów:
- kalki: `SCENE 3/1` „Nie bez powodu nie daje się księgowym wyrzutni rakiet.”,
  `20 Helper Delta/28` „wyjdziesz z tego cało”, `SCENE 7/6` i `RELEASE/24` „czy coś”;
- `fleece/36027` „Złap i wypuść” → „Złów i wypuść”;
- `SCENE 9/19`, `/22` „GENERALE BURKIN!” → „GENERAŁ BURKIN!”;
- `fleece/34877` „Nie patrz w dół” → „Spójrz w dół”.

Odrzucony: `SCENE 9/1` „Weź się ogar-” zostaje (nie „Nie przesadzaj-”).
Nie przedstawione użytkownikowi i nie wdrożone: `17 Acceptance/8–9`, `SCENE 8/14`,
`RELEASE/42–43`, `24 Goodbye/13`, drobne z sekcji 3.8 raportu review.
