# Skate Story — niezależny review po fullu

Data: 2026-09-26. Przekład z paczki 0.3 (paczki nie przebudowano).
Status: **przeczytano 2305/2305 wpisów; 17 pewnych poprawek wprowadzonych; tematy
stylistyczne czekają na decyzję użytkownika. Testu pełnej kampanii w grze nadal nie było.**
Raport zawiera treść całej gry, łącznie z zakończeniem.

## Zakres i metoda

Osobny reviewer (subagent w świeżym kontekście, tylko odczyt) według
`.claude/skills/localization-review/SKILL.md`, z zasadami redakcji, pułapkami, biblią,
`docs/translation-decisions.md`, `docs/technical.md` i aktualnym `work/l10n-report.md`.
Biblia i decyzje istniały już od wersji 0.3.

SHA-256 plików przekazanych reviewerowi:

```text
en-pl-review.json:        fe12c3b00fbfc95241ea6a11a30e225234b7eeda9e8ab8ef45c6e1fd71f9b1f3
bible.yaml:               b7817792e227f53b976b7ec356fe5310e9ad99e48036a04819117541a647c160
translation-decisions.md: 8aeb6135a459434549f418c2aa78d84f83902651e2af2d2fe542bfd08a927de5
work/l10n-report.md:      bc2ed0ca4d57b1d8cd7a0cf012f0fe595a5e15c3cb083e619296096a7b15bbe7
```

Po naniesieniu poprawek `en-pl-review.json` ma SHA-256
`c71e870855f6b7f48c2a74d42f579d6cdafaf28ae70e87a80f9e530e09044577`.

Indeksy `[n]` poniżej to pozycja wpisu w `en-pl-review.json` (od zera). Pełne ustalenia
reviewera z gotowymi tekstami są w `work/review/findings.md`, manifest pokrycia
w `work/review/coverage.md`.

| Partia | Wpisów | Zakres |
| --- | ---: | --- |
| b01 UI, poziomy, rozdziały, mówcy, samouczek, triki | 376 | `UI/`, `Levels/`, `chapters/`, `Speaker/`, `tut/`, `Trick/` |
| b02 Rozdział 1 | 243 | `ch1/` |
| b03 Rozdział 2 | 153 | `ch2/` |
| b04 Rozdział 3 | 109 | `ch3/` |
| b05 Rozdział 4 | 235 | `ch4/` |
| b06 Rozdział 5 | 146 | `ch5/` |
| b07 Rozdział 6 | 137 | `ch6/` |
| b08 Rozdział 7 | 131 | `ch7/` |
| b09 Rozdział 8 | 149 | `ch8/` |
| b10 Rozdział 9 | 229 | `ch9/` |
| b11 Epilog, mroczne miejsce, bossowie, zadania, wiersze | 90 | `ch10/`, `__DARKPLACE/`, `boss/`, `quests/`, `poems/` |
| b12 Przedmioty i osiągnięcia | 307 | `Item/`, `Achievement/` |

Luk w pokryciu nie ma. Mówców nie ma w danych (kolumna TYPE tabeli I2 leży w
`work/ref-all.json` poza gitem), więc reviewer ustalał ich z treści i biblii.
Ekstrakcji z gry do porównania w tej sesji nie było.

## Ocena ogólna

Tłumaczenie jest bardzo dobre. Terminy z biblii są spójne niemal w 100%, znaczniki
(`*red*`, `*blu*`, `<color>`, `**`, `\n`) nienaruszone, typografia czysta. Głosy postaci
są wyraziste: Filozof („W istocie”, „zadumiewające”), Coney z wersalikami, gołąb-pisarz,
monolog Szczura w ch7 i wykład w ch9.

## Błędy — wprowadzone

| [n] klucz | EN | Było PL | Jest PL | Przesłanka |
| --- | --- | --- | --- | --- |
| [772] `ch1/09-lyceum/2rabbit2lookthinkpiece-1-seq-02` | Look through your arm, the Moon Vision will guide your way. | Spójrz przez swoje ramię — … | Spójrz przez swoją rękę — … | „Spojrzeć przez ramię” = obejrzeć się za siebie; chodzi o patrzenie przez szklaną rękę ([767]). |
| [1106] `ch3/01-bedhail/01wakeupintro-1-seq-04` | The Rabbit read dimly from a letter burned bedside. | Królik czytał sennie z listu spalonego przy łóżku. | Królik czytał w półmroku list, który wypalił się przy łóżku. | Spalonego listu nie da się czytać; listy w tym świecie wypalają się na miejscu ([1038]). „Dimly” ≠ sennie, a zdanie wcześniej Królik jest bezsenny. |
| [2244] `poems/ch03-poem-body` (wers 3) | the Rabbit read dimly from a letter burned bedside. | czytał Królik sennie z listu spalonego przy łóżku. | czytał Królik sennie list, co wypalił się przy łóżku. | Jak wyżej; w wierszu Królik „leżał we śnie”, więc „sennie” zostaje. |
| [1170] `ch3/06-flowershop/10talkbea-1-seq-01` | the Moonflower festival | święto księżycowych kwiatów | święto Księżycowych Kwiatów | Termin z biblii; to kwiat, o który Beea zaraz prosi. |
| [744] `ch1/08-captureskater/1kneeldemon-1-seq-03` | It has come to my attention that… | „Doszło mnie, że… | „Doszło do mojej wiadomości, że… | „Doszło mnie” bez podmiotu („słuchy”, „wieść”) jest błędne; urzędowa formuła pasuje do Filozofa-sędziego. |
| [1026] `ch2/07-worldmap/103amb-1-seq-01` | The subway wouldn't go backwards further. | Metro nie chciało już dalej cofać. | Metro nie chciało się już dalej cofać. | O pojeździe: „cofać się”. |
| [1846] `ch7/waitstage/89end-1-seq-03` | A distant screech was imminent. | Daleki skrzek był nieunikniony. | Zaraz miał się rozlec daleki skrzek. | „Imminent” = nadciągający, nie „nieunikniony”. |
| [733] `ch1/06-mooncore/6firstkickflipdone-1-seq-01` | …but gets stale quickly. | …ale szybko się nudzi. | …ale szybko staje się oklepany. | Mechanika wprowadzona w [729] na czerwono jako „oklepany”; jedno słowo dla jednego stanu. |
| [786] `ch1/09-lyceum/HEELFLIPTEXT-1-seq-06` | However, it gets stale more quickly… | Jednak szybciej traci skuteczność przy powtarzaniu i… | Jednak szybciej staje się oklepany i… | Jak wyżej. |
| [734] `ch1/06-mooncore/ranout-1-seq-01` | The Skater's soul expired… | Dusza Skejtera się wyczerpała… | Dusza Skejtera wygasła… | Ten sam komunikat w [1085] ma „wygasła”. |
| [706], [707], [709] `ch1/05-L0/1ollieobelisk-1-seq-02/03/05` | the Skater | skejter / skejtera | Skejter / Skejtera | Identyczne opisy trików w Liceum ([776]–[784]) i biblia piszą wielką literą. |
| [2246] `poems/ch05-poem-body` | grey cliffs | szare skały | szare klify | W ch5 „grey cliffs” to zawsze „szare klify” ([1476], [1581]). |
| [2250] `poems/ch09-poem-body` (wers 1) | The entire Underworld | Całe podziemie | Całe Podziemie | Identyczne zdanie w [2184]; EN wielką literą. |
| [2065] `ch9/06-setitonfire-area/89win-1-seq-03` | The Moons thawed from the ice. | Księżyce odmarzły z lodu. | Księżyce wytopiły się z lodu. | „Odmarznąć z czegoś” to nienaturalna kolokacja. |
| [2077] `ch9/06-setitonfire-area/ambburning-1-seq-12` | Specks of souls thawed from the saliva. | Drobiny dusz odmarzały ze śliny. | Drobiny dusz wytapiały się ze śliny. | Jak wyżej. |

W [772] reviewer proponował „przez swoją szklaną rękę”; wprowadzono krótsze „przez swoją
rękę”, bez dopisku. W [1846] zostawiono „skrzek” (reviewer proponował „zgrzyt”, to już gust).

## Decyzje sprzed verticala — ponowna ocena

| Decyzja | Werdykt | Przykłady / uzasadnienie |
| --- | --- | --- |
| Skejter w rodzaju męskim | utrzymać | cała gra spójna, także ch8 i epilog |
| Pisownia „Skejter” wielką literą | utrzymać | 321/331 wystąpień, reszta to zaimki; [706]/[707]/[709] poprawione |
| Beea w rodzaju żeńskim | utrzymać | [1170], [1173], [1736] |
| Szkielet z Placu Żalu męski | utrzymać | [1368] |
| Kamień młyński (ch9) męski | utrzymać | [2052]–[2055] |
| Frotue męski o sobie, „Żaba” żeńska w narracji | utrzymać | [978], [1346], [1722], [1827], [2243] |
| Licha żeńska, per „pan” | utrzymać | [1033]–[1044] |
| Fałszywe Słońce nijakie | utrzymać | [1695]–[1709], [2157]–[2159] |
| Echo „Ten demon…” (ch1 ↔ ch8) | utrzymać | [683]/[684] ↔ [1919]/[1920] |
| Wielkie litery nazw bytów świata | utrzymać | małe tam, gdzie EN małe ([1663], [2168]) |
| podziemie, Głębia, Zapomnienie, Zgiełk, Wieczna Stonoga, Krwawy Wieszcz, Myślokształt, blat, pieczęć, kombo, tupnięcie | utrzymać | 100% spójności w całym pliku |
| Garbus (Sloucher) | utrzymać, brak kontekstu wizualnego | notka twórców w [384] — sprawdzić sylwetkę w grze |
| umowa / kontrakt tylko w ch1 | utrzymać | 25× umowa, 1× kontrakt [687] |
| Księżycowy Kwiat | utrzymać | jedna poprawka [1170] |
| Rymy Philoso | utrzymać, jeden wers do rozmowy | [795] |
| Hamlet [652], „W KROPCE”, „Demon Dom Ser” | utrzymać | |
| HOUSE/CHEESE: słowo angielskie + polskie znaczenie | utrzymać warunkowo | [155], [157], [1336], [1378]; rozstrzyga test |
| „stale” = oklepany (dotąd niezapisane) | wprowadzono ujednolicenie | [729], [733], [786]; dopisane do biblii |
| „soul expired” = wygasła (dotąd niezapisane) | wprowadzono ujednolicenie | [734], [1085]; HUD [620]/[621] do testu |
| Lyceum = Liceum (niezapisane) | brak kontekstu, do rozmowy | 11 wpisów w ch1 |
| „Ten Bolgias” = Dziesięć Jarów | proponowana zmiana (wariant) | [1754] sam mówi o „rowach” |
| Penin „skarbie” | proponowana zmiana (wariant) | pokrywa się z Beeą na Bankiecie |
| pain/pane oddane zawahaniem | proponowana zmiana (wariant) | [1034] |

## Do rozmowy

Stan: **czeka na użytkownika**, obecny tekst zostaje do decyzji.

1. **Telefon Lichy, gra słów pain/pane [1034].** EN: "Made of... glass and pane?"
   Obecne: „Ze... szkła i... bólu?”. Rekomendacja: „Ze... szkła i... szyby?” — wraca
   przekręcenie taglinu „ze szkła i bólu” ([2240]). Koszt: działa, gdy gracz pamięta tagline.
2. **Lyceum → „Liceum” (ch1, 11 wpisów).** Wariant: „Likejon” (szkoła Arystotelesa).
   Rekomendacja: zostawić „Liceum” — czytelne, a skojarzenie ze szkołą pasuje do
   „OCENY” i egzaminu. Zapisać wybór w biblii.
3. **„Ten Bolgias” → „Dziesięć Jarów” [339], [342].** Rekomendacja: „Dziesięć Rowów” —
   aluzja do Malebolge i zgodność z [1754] „Przepłyniemy przez rowy ósmej…”.
   Koszt: „Jary” brzmią ładniej.
4. **Rymy: Philoso [795] i Larry [990].** [795] ostatni wers „Za trud twój Myślokształt
   niech będzie zapłatą.” → „Masz więc Myślokształt — nie trudziłeś się marno.” (rym
   darmo/marno). [990] „KARMIĄ MNIE WIBRACJE. / JEDŹ DLA MNIE, BESTIO.” →
   „WIBRACJE — MOJA STRAWA. / JEDŹ DLA MNIE, BESTIO KRWAWA.”
5. **Motyw drutu w wierszach [2245], [2251] („wiry”).** „żylaste sługi Zgiełku” →
   „druciani funkcjonariusze Zgiełku”; „Szorstka sierść Diabła” → „Druciana sierść
   Diabła”. Świat gry jest z drutu ([1306], [1507], [1793], [1938]), a „funkcjonariusze
   Zgiełku” to termin z całej gry ([1294]).
6. **Targ Przybyszów jako giełda [1388].** „Patrzy, jak spisują każdą nową duszę
   podziemia.” → „Patrzy, jak na giełdę trafia każda nowa dusza podziemia.” (ostrożniej:
   „…jak notuje się każdą nową duszę…”). Domyka satyrę rynkową rozdziału.
7. **Penin „skarbie” → „złotko” [1522].** Jubilerski, protekcjonalny zwrot; odróżnia go
   od Beei, która na Bankiecie mówi „skarbie” tuż obok. Zmienia rejestr w biblii.
8. **Blat „Let's Chug Bile Tea” [66].** „Chluśnij Żółciową Herbatą” czyta się jak
   „oblej herbatą”. Rekomendacja: „Obalmy Żółciową Herbatę”; wariant „Chlapnijmy
   Żółciowej Herbaty”.
9. **„NIE! MA NAS!” [2207]** (EN "NO! IT'S GOT US!"). Wersalikami łatwo czytać jako
   „nie ma nas”, a scena mówi o przestaniu istnienia. Rekomendacja: „NIE! ZŁAPAŁO NAS!”
   (albo „DORWAŁA NAS!”, jeśli podmiotem jest Stonoga).
10. **Róg Grzechu [1879].** „grzechu wartym ponad 10 000 punktów… Nie waż się go obudzić.”
    → „nagromadzonym grzechu powyżej 10 000 punktów… Nie waż się sprawić, żeby
    zatrąbił.” „Accumulated” mówi graczowi, że liczy się suma kombo.

Pozostałe warianty reviewera (niższy priorytet, pełne teksty w `work/review/findings.md`):
[484]/[576] „Interfejs scen” → „Pokaż interfejs w scenach”; [798] „Otóż” → „No więc”;
[788] szyk „Pojawiły się tylko wokół mnie”; [906] „Filozof zadrżał” → „Filozofem
wstrząsnęło” (powtórzone w [911]); [1061] „bezimienny” → „bez twarzy”; [1089] „opadał
z sił” → „flaczał” (deflated); [956] „dobrze trafiłeś” → „jestem twoim szczęśliwym
znakiem”; [1153] „przykujemy” → „przyszpilimy” (pin up/pin down); [1105] rym
weeping/sleeping; [1189]/[1309] „w tej gospodarce”; [1236] „My tylko prześpimy tędy” →
„My tu tylko przesypiamy przejazdem”; [1402] „nagłówek pożerał własny ogon”; [1491]
„To byli moi byli…” → „To moi byli…”; [1476] „ostatnia rzecz na łańcuszku” → „ostatnia
rzecz, do której była przykuta”; [1572] „krzyczał, pozbawiony właściciela”; [1811]
„Tęsknisz czasem?”; [1966] „bez jednego obłoczka”; [2250] „wypluł” → „zwymiotował”
(domyka „Wymiotuj!”); [186] naklejka „Try Hard”; [33]/[35]/[37] długość opisów osiągnięć.

## Brak kontekstu

[620]/[621] HUD „DUSZA / WAŻNOŚĆ” (może „DUSZA … WYGASA”), [496] „ZAKOŃCZENIE” (ender =
trik kończący?), [388]–[404] składanie modyfikatorów trików z nazwą, [893] długość celu,
[1478] thinkpiece jako tekst publicystyczny, [1574] rym „later, skater”, [1711] „along”
w EN (literówka?), [2256] „Pudełko z upominkiem”, [115] blat „Oneway Stop” (znak drogowy,
nie przystanek? — wtedy „Jednokierunkowy stop”).

## Do sprawdzenia w grze

1. Ustawienia → Rozgrywka/Grafika/Dostępność: długie opcje obok przełączników
   ([477], [487], [572], [573], [599], [603], [611]) i czy „Interfejs scen” jest zrozumiały.
2. HUD licznika duszy w ch1: układ „DUSZA … WAŻNOŚĆ” wokół licznika.
3. Ekran kombo i boss Filozofa: modyfikatory trików, „ZAKOŃCZENIE”, cel fazy 3 [893].
4. Liceum, rozmowa z Królikiem [772]: jak wygląda Księżycowy Wzrok (patrzenie przez rękę).
5. ch4, Plac Żalu: czytelność liter HOUSE/CHEESE z dialogiem [1378].
6. ch2, telefon na stacji [1034]: odbiór „szkła i… bólu?”.
7. ch8: nazwa „Ulica Minus Sześćset Sześćdziesiąta Szósta” (42 znaki).
8. Menu Księżycowego Wzroku: „Pudełko z upominkiem” [2256].
9. Ekwipunek → Blaty: grafika „Oneway Stop” [115], naklejka „Try Hard” [186].
10. ch7, „Czy odczuwasz czasem tęsknotę?” [1811] — długość w dymku.
11. ch4: sylwetka Garbusów.
12. Ekran osiągnięć: opisy 17–19.

## Kontrola po poprawkach

Zmieniono 17 wpisów, tylko pole `polish`. Znaczniki i `\n` w zmienionych wpisach
sprawdzone. `l10n_report.py`: brak 0, tokeny 0, płeć 0, adresat 0, spójność 0,
typografia 0 — bez zmian wobec stanu sprzed review. `tools/check_games.ts` przechodzi.
`translations/en-pl-review.html` przegenerowany (`tools/review.py`).
Paczka 0.3 w `dist/` i na stronie **nie zawiera** tych poprawek — wejdą w następny build.
