# Somber Echoes — decyzje tłumaczenia (0.2.0)

Zakres: 1507/1507 wpisów wszystkich ośmiu tabel. Zaakceptowane 111 wpisów próbki 0.1 zostało bez zmian.
Polski jest osobnym językiem `pl` z pozycją „Polski” w selektorze. English pozostaje oryginalny (decyzja użytkownika).

## Postacie
- **Adrestia i Harmonia — kobiety, bliźniaczki.** Teksty gry (TheFracture1.1–1.2) i opis GOG. Zgodnie z tym Adrestia ma żeńskie formy we wszystkich opisach i osiągnięciach: „Łuczniczka”, „Miłośniczka sztuki”, „Wojowniczka przestworzy”, „Całkiem niezła inżynierka”, „Godna dźwięcznego ostrza”.
- **Dziennik w pierwszej osobie żeńskiej** (Adrestia), narrator dialogów w trzeciej osobie. W dialogach rozróżniam wypowiedzi Adrestii od głosu narratora.
- **Eter i Nyks jako para**: czasowniki w liczbie mnogiej męskoosobowej („wyjaśnili”, „ryknęli”), bo Eter jest mężczyzną.

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| Aether / Nyx | Eter / Nyks | polskie formy mitologiczne, spójne z nazwami mocy | decyzja (próbka zaakceptowana) |
| Fracture | Rozłam | wydarzenie fabularne, dobrze się odmienia | decyzja |
| Radiance / Nocturne | Blask / Nokturn | para jasność–noc; Nokturn zachowuje muzyczny, nocny wydźwięk | decyzja |
| Ashfall / Cesspit / The Grove | Popielisko / Ściekowisko / Gaj | nazwy stref mapy jako polskie rzeczowniki miejsca | decyzja |
| Centimanes | Sturęcy | polska nazwa hekatonchejrów | mitologia |
| Circe (komora) | Kirke | polska forma imienia; system C.I.R.C.E. zostaje jako skrót | decyzja |
| Pythia | Pytia | polska forma | mitologia |
| Gladius, Arbiter | bez zmian | nazwy własne broni | decyzja |
| Via Regia, Via Pelagus, Opera Publica | bez zmian | łacińskie nazwy ulic statku, tak jak w oryginale | decyzja |
| The Maiden (wspomnienie/posąg) | Panna | seria archetypów (Wojownik, Żeglarz, Łowczyni), wiąże się z Demeter i Korą | decyzja |

## Świadome odstępstwa od oryginału
- Szyk narratora („his gratitude he extended”) nie jest kopiowany. Podniosły ton oddaje słownictwo, nie inwersja ani rymy.
- Literówki oryginału (Ather, vulnurable, deaccelarate) poprawione w tłumaczeniu.
- Osiągnięcia bossów jako rzeczowniki odczasownikowe („Oślepienie Cyklopa”, „Uciszenie Harmonii”), a nie imiesłowy przepisane z angielskiego.
- „No stone left unturned” → „Pod każdym kamieniem”.

## Mniej pewne (sprawdź w grze)
1. **Wybór języka**: czy „Polski” pojawia się na końcu listy, przełącza teksty od razu i zostaje po restarcie. Hooki Lua przeszły tylko test na modelu, nie w grze.
2. **Długie nazwy na mapie**: „System podtrzymywania życia (1)”, „Sklepy z egzotycznymi roślinami”, „Przeprawa przez nieczystości”.
3. **Wyzwania i ulepszenia**: „Strącenie Ptaka stymfalijskiego”, „Celowanie łukiem i włócznią”, „Gracz w rankingu światowym” — ryzyko ucięcia.
4. **Fonty**: Maitree-Cinzel Medium nie ma wielkiego Ą; sprawdź nagłówki pisane wersalikami.
5. **Wielowierszowe napisy narratora** (NyxOverflow, SpecimentGrowth, StrandedInTheVoid): czytelność i czas wyświetlania.

## Raport kontrolny
`work/l10n-report.md`: brak=0, tokeny=0, spójność=0, liczebniki=0. Pozostałe zgłoszenia to fałszywe alarmy:
- terminy (9): token `[ICON:Aether]` oraz „Fracture” w znaczeniu pęknięcia;
- angielskie resztki (22): tokeny ikon i słowa takie same po polsku (Narrator, Teleporter, Demo);
- typografia (27): spacja na końcu kwestii w oryginale. Zostawiona tylko przy `Poziom {num} `, bo tam może służyć do doklejania tekstu;
- wielkie litery (6): etykiety przy ikonach.
Długość (9): patrz „Mniej pewne”.

## Po niezależnym review (2026-09-25)
Pełny raport: `docs/localization-review.md`. Wszystkie decyzje z tabeli terminów utrzymane.
- **Kirke vs C.I.R.C.E.**: komora konsekwentnie „Kirke”, także w komunikacie zabezpieczeń (CirceAutoSecurity1.2 poprawione z „komory C.I.R.C.E.”). Nazwa interfejsu zostaje „Interfejs C.I.R.C.E.”. Czy dodać graczowi mostek między nazwami — otwarte, czeka na decyzję użytkownika.
- **Gladius**: samodzielna nazwa przedmiotu wielką literą, w nazwach ulepszeń małą („Wzmocniony gladius 1”); Arbiter jako imię własne. Zapis w biblii doprecyzowany, tekst bez zmian.
- **Exit na mapie** (STRING_MapElements/Transition_*): „Wyjście”, rzeczownik jak pozostałe elementy legendy, a nie „Wyjdź”. Podpowiedzi przycisków „[ikona] — Wyjdź” zostają w trybie rozkazującym.
- Dopisane do biblii bez zmiany tekstu: Spopieleni, Feniks, Legion Helikonu, Mojry, boska dwójca.
- Otwarte warianty stylistyczne (Udręka Posejdona, osiągnięcia z kalkami, „czysta Nyks” itd.) czekają na użytkownika; do czasu decyzji tekst bez zmian.
