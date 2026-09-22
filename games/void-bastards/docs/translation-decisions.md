# Void Bastards — decyzje tłumaczenia (0.2.0)

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
