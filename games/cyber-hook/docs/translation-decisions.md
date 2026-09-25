# Cyber Hook — decyzje tłumaczenia (0.2.0)

## Postacie
- **Dron — rodzaj męski** („nie byłem szczery”, „czułem się samotny”). Tak jest
  w wersji rosyjskiej („Уверен”), hiszpańskiej („Estoy seguro”) i portugalskiej
  („o Dron”) oraz w recenzjach. Wersja francuska (twórcy są Francuzami) robi z Drona
  kobietę („je suis sûre”, „contente”). To najmniej pewna decyzja.
- **W zakończeniu mówi Dron.** Mówiący z plików dialogu to ten sam co w samouczku,
  więc to Dron wyznaje, że stworzył poziomy, Numero („nieudany eksperyment”) i gracza.
- **Numero — rodzaj męski, imię nieodmienne** („dla Numero”, „z Numero”). W grze zawsze
  stoi w znaczniku koloru, więc odmiana rozbijałaby znacznik.
- **Gracz — formy bezosobowe, gdzie się da** („udało ci się”, „jesteś z powrotem”,
  „należy ci się wolność”). Oryginał traktuje gracza jako mężczyznę („spider boi”,
  francuskie „Tu es revenu”), więc rodzaj męski zostaje tylko tam, gdzie niesie
  nawiązanie: „Hej, w końcu się obudziłeś!” (Skyrim).
- **Dron i Numero mówią do gracza na „ty”, Numero do obu naraz — „wy”.**
- **Terminal wstępu — bezosobowy komunikat maszynowy** („Wykryto biegacza”,
  „Nie można odinstalować świadomości”).

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| runner | biegacz | tak nazywa gracza Numero i Dron; „runner” byłby żargonem | decyzja |
| hook | hak | nazwa gry i gadżetu CYBER HOOK zostaje, sam przedmiot to hak | decyzja |
| Timewarp | spowolnienie (czasu) | tak działa mechanika; „zaginanie czasu” tylko w okrzyku BEND TIME | decyzja |
| crystals | kryształy | dosłownie | decyzja |
| replay | powtórka | jak w polskich wydaniach wyścigów i platformówek | decyzja |
| leaderboard | ranking | jak w polskim Steamie | decyzja |
| personal best / PB | rekord (osobisty) | „RO” nieczytelne, „PB” obce | decyzja |
| marathon mode | tryb maratonu | dosłownie | decyzja |
| flying green probes | latające zielone sondy | jak francuskie „sondes” | fr |
| Airdash | skok w powietrzu | opis w grze: „drugi skok w powietrzu” | decyzja |
| Retract | zwolnienie haka | opis: puszcza hak | decyzja |
| world names | Początek, Trening, Wyzwanie, Mistrzostwo, Zwątpienie, Gniew, Koniec | dosłownie, bez rodzajnika | decyzja |

## Nazwy poziomów
- **Nazwy opisowe przetłumaczone** („Wieża śmierci”, „Miejska dżungla”, „Bezwładność”).
- **Nazwy własne i gry słów bez polskiego odpowiednika zostają:** Speedy Luke, Big Bank,
  Zartan, PropulZone, Koma, Klonk, Rabator, Xitra, Rotato, Tobledrone, Castle Trashers,
  cORE, Korridor, Slipgate, Skorpion, JCVD, La Grange, Metropolis X, Ring Ring, Three 6.
- **Nawiązania z utartym polskim tytułem:** Captain Hook → „Kapitan Hak” (Piotruś Pan),
  Hang'em High → „Powieś go wyżej” (western z Eastwoodem), Master AirBender →
  „Mistrz powietrza” (Awatar).
- **Portal:** „Thinking with Timers/Buttons/Hooks” → „Myśl zegarami / przyciskami /
  hakami” (od „Thinking with Portals”).

## Okazje wykorzystane
- Ucięte przekleństwa zachowują efekt: „JETTISON CARGO MOTHER F” → „ZRZUCIĆ ŁADUNEK
  SKUR”, „Sh…iii…t” → „Sz…laaa…g”, „mo#&-#!(#&&” → „sk#&-#!(#&&”.
- „spider boi” → „Ale z ciebie teraz mały pajączek, co?” (bez rodzaju gracza).
- „Red is DED!” → „Czerwone to zgon!”.

## Świadome odstępstwa od oryginału
- **Naprawione błędy CSV gry.** Parser ucinał tekst na przecinku bez cudzysłowów, więc
  angielski gracz widzi samo „Hey” zamiast „Hey, you're finally awake!”, a w dwóch
  opisach zostają zgubione cudzysłowy. Nasze teksty nie przechodzą przez CSV, więc
  jest pełne zdanie.
- **Końcówka samouczka** (`Tutorial_Line_04_00` i `04_01`) ma w grze zamiast kluczy
  angielski tekst. Plugin rozpoznaje go i podmienia (16 kwestii w `raw-keys.json`).
- **Trzy kwestie DLC bez wpisu w grze** (`dialog_dlc_boss_intro_01_00`, `01_01`,
  `02_00`): gra pokazuje w nich nazwę klucza również po angielsku. Nie znamy treści,
  więc nie dopisujemy.
- **Polski w miejscu angielskiego.** Lista języków to stała lista w kodzie gry, więc
  „English” podpisane jest „Polski”.
- Typografia: „...” zostaje tam, gdzie było w oryginale — nie każdy font gry ma „…”.

## Mniej pewne (sprawdź w grze)
- **Wybór poziomu** — najdłuższe nazwy: „Mikser powietrza” skrócony do „Młody mikser
  powietrza”, „Przetwarzanie odpadów”, „Społeczeństwo w biegu”, „Klasyczny skok wzwyż”.
- **Rozmowy między światami** — najdłuższe kwestie Drona (świat 5: sondy i spowolnienie;
  świat 7: „nie odeślę do domu nas obu…”). Pole dialogu stronicuje, ale sprawdź,
  czy nic nie wychodzi poza okno.
- **Zakończenie DLC i napisy końcowe** (`dialog_ending_credits_*`) — rodzaj Drona
  w pierwszej osobie.
- **Wstęp samouczka po powrocie z poziomu** (`Tutorial_Line_04_*`) — czy surowe klucze
  rzeczywiście zamieniają się na polski.
- **Opcje: „Autopuszczanie haka”, „Wyłączona” (V-Sync)** — skrócone pod szerokość pól.

## Raport kontrolny
`work/l10n-report.md`: brak tłumaczeń 0, tokeny 0, płeć 0, adresat 0, spójność 0.
Poprawione: 5 zbyt długich etykiet. Zostały fałszywe alarmy:
- terminy (6) — nazwy ikon `<sprite name="Hook">` i nazwa gry „Cyber Hook”;
- angielskie resztki (5) — nazwy języków i „DNA”;
- typografia (55) — proste cudzysłowy wewnątrz znaczników TMP (`<color="red">`);
- długość (3) — „Naciśnij - Dowolny klawisz -” (sprawdzone w grze, mieści się),
  „Bez synchronizacji” poszło na „Wyłączona”, dwie kwestie dialogu mieszczą się
  w stronicowanym polu.
