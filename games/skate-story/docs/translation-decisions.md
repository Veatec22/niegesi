# Skate Story — decyzje tłumaczenia (0.3)

Przegląd istniejącego tłumaczenia 0.2 według skilla lokalizacji: biblia, raport
i lektura całej narracji, dialogów, poezji, przedmiotów i UI. Tłumaczenie było
bardzo dobre; zmieniono 19 wpisów, głównie płeć postaci i kilka niezręczności.

## Postacie
- **Skejter — rodzaj męski.** W oryginale bez płci („the Skater”, „it”); po polsku
  za rzeczownikami „skejter” i „demon”. Rosyjska wersja gry robi tak samo.
- **Beea (kwiaciarka) — rodzaj żeński.** Było „gdybym miał kwiaty”, „Już
  sprzedałem”, „Przywykłem”; RU „я обменяла”. Oscar mówił o niej „ten słodziak
  z kwiaciarni” — teraz „ta ślicznotka”.
- **Szkielet z Placu Żalu — rodzaj męski.** Było „Myślałam”; RU „я понадеялся”
  i FR „il m'a vu” zgodnie męskie.
- **Kamień młyński (ch9) — męski, bez zmian.** RU daje formy żeńskie, ale ES i FR
  męskie, a po polsku „kamień” jest męski.
- **Frotue — męski o sobie, „Żaba” w narracji.** „Wcale tam nie spałem”, ale
  „spytała Żaba” — zgoda z rzeczownikiem. Zostawione z 0.2.
- **Licha z Departamentu Śmierci — żeńska, do Skejtera per „pan”.** Decyzja z 0.2,
  RU nie rozstrzyga.

## Terminy
Bez zmian wobec 0.2; teraz spisane w `translations/bible.yaml` (Skejter, podziemie,
Księżyc, Myślokształt, Zgiełk, Garbus, Wieczna Stonoga, Zapomnienie, blat).

## Poprawki
- **Echo otwarcia gry.** Rozdział 8 powtarza pierwsze zdania gry („This Demon was
  hungry and tired. This Demon was going to eat…”). Było „Demon ten był głodny”
  na początku i „Ten Demon był głodny” w ch8 — teraz oba „Ten demon…”, żeby echo
  było słychać.
- „Ty chwiejący się draniu” → „Ty chybotliwy draniu” (Wobbly bastard, do Pingwina).
- „40 000 dusz wykrzyczało się w powietrze” → „Powietrze rozdarł krzyk 40 000 dusz”.
- „wciągnął Fioletowy Księżyc z oddechem” → „jednym wdechem”.
- „możesz spróbować zjeść Księżyc pierwszy” → „przed nią” (przed Stonogą).
- Blat „Literature”: „Pierwszy list Frankensteina” → „Pierwszy list z „Frankensteina””
  — powieść zaczyna się od listu Waltona, nie Frankensteina.
- Blat „Dead Typographer”: „zanim ledwie zaczął widzieć” → „zanim niemal oślepł”.
- Rym Philoso: „by się Księżyc zajadało” → „a Księżyca zjesz niemało”.
- Typografia: „1400 °C”, „0 °C” ze spacją.

## Okazje wykorzystane
- **Hamlet** („to die, to skate, perchance to repeat”): „Sposób, by umrzeć, jeździć —
  powtarzać może”, echem polskiego „śnić może”.
- Zostawione z 0.2, bo dobre: rymy Philoso, „jestem zajęty byciem W KROPCE”,
  „Demon Dom Ser”, „Skejter poczuł wszystkość”.

## Świadome odstępstwa od oryginału
- Wielkie litery w nazwach bytów świata („Pranie Diabła”, „Łańcuch Deskorolki”)
  zostają — oryginał pisze je tak samo i tłumaczenie trzyma to konsekwentnie.

## Mniej pewne (sprawdź w grze)
- **Kwiaciarnia (ch3) i Bankiet (ch7):** rozmowy z Beeą w rodzaju żeńskim.
- **Plac Udręki, ogon w tyłku Oscara:** „Oby ta ślicznotka z kwiaciarni mnie tak
  nie zobaczyła”.
- **Ustawienia → Rozgrywka:** najdłuższe opcje, np. „Wyłącz spowolnienie przy
  tupnięciu” (34 znaki), „Automatyczne centrowanie kamery” — czy mieszczą się
  obok przełącznika.
- **Ch8, Ulica Minus Sześćset Sześćdziesiąta Szósta:** 42 znaki w nazwie poziomu.

## Raport kontrolny
`work/l10n-report.md`: brak 0, tokeny 0, płeć 0, adresat 0, spójność 0, liczebniki 0,
wielkie litery 0 (styl oryginału, wyciszone w biblii), typografia 0.
Terminy 12 — wszystkie to polskie zaimki zamiast powtarzania „Skejter”
(„mógł”, „go”). Angielskie 1 („II. GRIND”, termin). Długość 19 — opcje
ustawień i nazwy poziomów, wyżej w „sprawdź w grze”.
Płeć porównana dodatkowo z rosyjską kolumną gry (`work/gender-ru.py`): zostaje
tylko kamień młyński, opisany wyżej.

## Niezależny review (2026-09-26)
Osobny reviewer przeczytał całość (2305 wpisów); raport w `docs/localization-review.md`.
Wszystkie decyzje o płci, terminach i echach utrzymane. Wprowadzono 17 pewnych poprawek
w polu `polish`, m.in.:
- **„stale” = „oklepany”** we wszystkich trzech samouczkach (było też „się nudzi”,
  „traci skuteczność”) — dopisane do biblii.
- **„soul expired” = „dusza wygasła”** w obu komunikatach porażki — dopisane do biblii.
- List Diabła „wypalił się” przy łóżku, nie „spalony” (ch3 i wiersz ch3).
- „Spójrz przez swoją rękę” zamiast „przez ramię” (Księżycowy Wzrok, ch1).
- „Skejter” wielką literą także na obelisku ollie.

Czeka na decyzję użytkownika (obecny tekst zostaje): pain/pane w telefonie Lichy,
Liceum czy Likejon, Dziesięć Jarów czy Rowów, rymy Philoso [795] i Larry'ego [990],
„druciani funkcjonariusze Zgiełku” w wierszach, giełda na Targu Przybyszów,
Penin „złotko”, blat „Chluśnij Żółciową Herbatą”, „NIE! MA NAS!”, Róg Grzechu.
