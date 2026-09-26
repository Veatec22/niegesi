# Void Bastards — decyzje tłumaczenia (0.2.1, po review)

Fakty i źródła: `translations/bible.yaml`. Raport kontrolny: `work/l10n-report.md`.

## Postacie

- **B.A.C.S. — mężczyzna** (głos Kevana Brightinga). Mówi korporacyjną nowomową HR
  i BHP: „zadania do realizacji”, „wskaźniki KPI”, „Twoja kandydatura została wybrana”,
  „interesariusze”. Uprzejmie-pasywno-agresywny, nigdy wulgarny.
- **Gracz ma losową płeć** (tytuły Mr, Mrs i Ms w danych gry). Wszystko, co mówi do gracza
  i o graczu, jest bezrodzajowe: czas teraźniejszy, strona bezosobowa („próbowano
  użyć karty”), „bystra osoba” zamiast „bystry”. **Cechy postaci są rzeczownikami**
  („Nerwowość”, „Krzepa”, „Dziurawe ręce”), bo przymiotnik zdradzałby płeć.
  Opisy osiągnięć „_past” są bezosobowe („Zbudowano…”).
- **Piraci mówią po szkocku** — twórcy dali w kontekście przekład na standardowy
  angielski. Po polsku to slang uliczny („ziomy”, „gnojek”, „kurde”). Kapitan Li Hua
  ma formy bezrodzajowe, bo płci nie da się ustalić.

## Terminy i gry słów

| EN | PL | Dlaczego |
| --- | --- | --- |
| client | klient | satyra — więźniowie nazywani „klientami” |
| brownie points | punkty lizusa | punkty za podlizywanie się szefowi (kontekst twórców) |
| Merit | zasługa | waluta; krótko |
| authorise (hakowanie) | autoryzacja | tak nazywają to twórcy |
| Gunpoint (działko) | Muszka | „at gunpoint” → „na muszce” |
| Screw (strażnik) | Klawisz | więzienny slang |
| Juve | Gówniarz | „rude adolescent” w kontekście |
| Janitor | Woźny | |
| Stapler / Staple | Zszywacz / Zszywki | strzelba na zszywki |
| Whackuum / Smackuum | Walkurzacz / Tłukurzacz | walić + odkurzacz |
| Clusterflak / Clusterfluck | Klasterflak / Klasterfuks | |
| Surgery 4 Dummies | Chirurgia dla bystrzaków | polska seria „…dla bystrzaków” |
| Operating Theatre | Teatr operacyjny | kontekst: „pół teatr, pół sala operacyjna” |
| Tombs (cele) | Kazamaty | |
| OH&S | BHP | |
| line printer / ID card | drukarka wierszowa / identyfikator | krótko w siatce części |
| Sargasso Nebula | Mgławica Sargassowa | jak Morze Sargassowe |

Bez tłumaczenia: Void Ark, S.T.E.V., P.A.L., B.A.C.S., FTL, WCG, nazwy firm (CNT,
Otori, Krell, Xon, Lux, Pac, Tydy), Regulator, Nebulator, Ion Bru, Cool Pops.

## Okazje wykorzystane

- „Client Expired” → „Klient wygasł”; „Hard Bastard” → „Twardy Drań”;
  „Easy Peasy” → „Bułka z masłem”.
- Osiągnięcia z brytyjskimi powiedzonkami: „Brown Noser” → „Lizus”,
  „Kippers for Breakfast” → „Śledzik na śniadanie”, „Cor Blimey!” → „O ja cię kręcę!”,
  „Coffin Dodger” → „Trumna poczeka”.
- „Shoplifters unite!” → „Złodzieje sklepowi wszystkich krajów, łączcie się!”.
- Imiona robozwierzaków: „plod” (policjant w slangu) → „krawężnik”.

## Świadome odstępstwa

- Liczby doklejane w kodzie zapisane jako etykiety („Spal paliwo: {[x]}”,
  „Punkty lizusa za te ustawienia: ”), żeby ominąć odmianę liczebników.
  Liczniki w profilu: „COUNT dni / COUNT dzień”, „Skoki: COUNT”.
- `_PLURAL` przedmiotów w mianowniku liczby mnogiej (etykiety).
- Nazwy klawiszy: symbole po polsku (Gwiazdka, Małpa, Ukośnik), klawisze
  specjalne jak na klawiaturze (Backspace, Home, Page Up).

## Mniej pewne (sprawdź w grze)

- **Warsztat i szafka na części** — najdłuższe nazwy (np. „Stymulator XTC”,
  „Wyściółka kaftana”, opisy ulepszeń).
- **Mapa gwiezdna** — długie tytuły zdarzeń („Namierzenie przez piratów!”,
  „Tunel czasoprzestrzenny”) i nazwy statków („Statek rekonwalescencyjny Xon”).
- **Opcje** — „Synchronizacja pionowa”.
- **Profil postaci** — długie wykroczenia („Przechodzenie przez jezdnię w niedozwolonym miejscu.”).

## Raport kontrolny

Po pełnym tłumaczeniu: 0 zgłoszeń poza 18 dotyczącymi długości. Poprawiono po
raporcie: skrócone nazwy części i cech, ujednolicony „identyfikator”. Fałszywe alarmy
(nazwy klawiszy, nazwy języków, skróty na mapie, oboczności „turyści”, „śmieci”)
opisane w biblii jako wyjątki albo rdzenie.

## Poprawki po teście 0.2.0

- **Log akcji (prawy górny róg)** — tytuł wpisu ma miejsce na jedną linię, pod nim
  gra rysuje podpis (np. rodzaj ładunku). Dłuższy tytuł zawijał się na podpis.
  Budżet: długość angielskiego (do ~20 znaków). „Wezwano statek zaopatrzenia” →
  „Wezwano dostawę” (spójne z „wezwij dostawę” przy terminalu), „Wypłata
  z ubezpieczenia” → „Odszkodowanie”.

## Review po fullu (2026-09-26)

Niezależny przegląd całości (2480/2480 wpisów, trzech reviewerów w świeżym kontekście):
`docs/localization-review.md`. Kierunek sprzed verticala utrzymany w całości. Wprowadzono
31 pewnych poprawek, m.in.:

- **Blokada drzwi:** „lock/unlock” to „blokować/odblokować” także w opisach ulepszenia
  HackDoor i podpowiedziach (`Hint/Lock`, `Hint/Robots`) — wcześniej „zamykać/otwierać”
  zmieniało sens mechaniki.
- **Moduły w opisach amunicji** jak na mapie: „w kwaterach” (hab), „w modułach min
  atomowych Pac” (nuc bays) — „wyrzutnie” to moduł torped.
- **rehydrate = nawodnić** także w opisie Void Ark na mapie gwiezdnej.
- Spacja przed liczbą doklejaną do „Punkty lizusa za te ustawienia:”, jeden wyciek
  formy męskiej („Bądź gotowy” → „Przygotuj się”), wielka litera po kropce w opisach broni.
- Biblia: „action items” w praktyce oddawane jako „zadanie/zadania”; spacje końcowe EN
  bez doklejanej treści oznaczone jako wyjątek raportu.

Przegląd językowy nie zastępuje testu w grze — pełne przejście nadal czeka.

## Rozstrzygnięte z użytkownikiem po review (2026-09-26)

Wprowadzone (31 wpisów):

1. **Samouczek B.A.C.S.-a** bez sztywnych obejść rodzaju: „Czy wiesz, że na tym statku jest
   brzęczek?”, „Nie wiesz, dokąd iść?”, „…zanim ktoś cię zabije albo się udusisz.”,
   „Zamiast budować w warsztacie lokalizator części.” — zwrot „ty” zamiast strony bezosobowej
   tam, gdzie nie wymaga form rodzajowych.
2. **Osiągnięcia `_past`:** „Udana ucieczka z mgławicy [na poziomie X] […].”, „Doprowadzono
   S.T.E.V. …”, „Przeżyto spotkanie z piratami.”
3. **Piraci:** „Jakiś frajer puścił…” (dobber = idiota, nie donosiciel), Li Hua: „mam tam wyleźć
   i zrobić to za was??”, „Luli ciągle gada…” (płeć Luli nieznana).
4. **Akcje w sterowaniu w trybie rozkazującym:** „Strzelaj”, „Skacz”, „Biegnij”.
5. **Stopnie wrogów:** Veteran → „weteran” po nazwie („Woźny weteran”, „Skryba weteran”),
   Senior → „Starszy”.
6. **upscale → przerób:** „przerób”, „złom do przeróbki”, „Przerobiono”, na mapie „Przerabia złom”.
   Odrzucone: „ulepsz” (myli się z warsztatem), „uszlachetnij”.
7. **Kalambury:** „Proszę czekać dalej — i przy okazji szukać identyfikatora.”,
   „Zarządzanie pieczarkowe” (odrzucone: „Metoda pieczarki”), „Sknera”.

## Do rozmowy (pozostałe propozycje z review)

Nie wprowadzone, obecny tekst zostaje. Szczegóły w `docs/localization-review.md`:
„Pirat mat” → „Pirat bosman”; „Autorytet” (wyzwanie) → „Figura autorytetu”; „Zadanie!”
(Action Item!) → „Do realizacji!”; kalambur „stacja… papiernicza”; drobne luki wierności
(punkt 8) i wygładzenia komiksu (punkt 9); skróty zależne od testu długości (punkt 10).
