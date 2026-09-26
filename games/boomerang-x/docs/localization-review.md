# Boomerang X — niezależny review po fullu

Data: 2026-09-26. Przekład z paczki 1.1 (paczki nie przebudowano).
Status: **przeczytano 359/359 wpisów; 10 pewnych poprawek wprowadzonych w pliku
tłumaczenia, jedna decyzja do rozstrzygnięcia (rodzaj Tepana) i tematy redakcyjne otwarte.
Testu pełnego tłumaczenia w grze nadal nie było.**
Raport zawiera treść późniejszych scen z Tepanem.

## Zakres i metoda

Osobny reviewer (subagent w świeżym kontekście, tylko odczyt) według
`.claude/skills/localization-review/SKILL.md`. Przed przeglądem agent prowadzący spisał
wstecznie `translations/bible.yaml` i `docs/translation-decisions.md` (gra ich nie miała)
oraz uruchomił `l10n_report.py`.

SHA-256 plików przekazanych reviewerowi:

```text
en-pl-review.json:        d418d81d79b1db838f0e4183305acb993fad544875725cd94885da4cf6dc08ee
bible.yaml:               d581e629bf3743131140449266dce5b4986f55ec85c7d9588b59b1660617a9e7
translation-decisions.md: 4edb25d8b6c4452df59c132c99728af4e639152d7a2c9e5d4d5dc97287e11836
work/l10n-report.md:      f7912518d9a1d8c84c246d208ca9508bbb3effaf61e4f6c505aebbf2bd9c7dcb
```

Po naniesieniu poprawek `en-pl-review.json` ma SHA-256
`afb3ac38c7c8ac3688f23d2878730e09fbc939dd6f36fbd9df8e94954e45fabb`.

Innej ekstrakcji do porównania nie było. Tabela gry ma zduplikowany klucz
`difficulty_select_prompt`, a obecne PL pasuje do obu tekstów EN.

| Partia | Wpisów | Pierwszy klucz | Ostatni klucz |
| --- | ---: | --- | --- |
| Menu, pauza, zapis | 24 | `language_name` | `ok_button` |
| Opcje (options_*, żyroskop) | 112 | `options_language_label` | `options_endless_special_enemy_color` |
| Sterowanie (controls_*, keyboard_*) | 36 | `controls_action_move_vertical` | `controls_action_sniper` |
| Nazwy obszarów | 22 | `tutorial_name` | `endless_run_name` |
| Kombo, fale, HUD | 11 | `kill_combo` | `endless_wave_count` |
| Moce, odblokowania, słowniczek | 15 | `shield_unlock_name` | `comet_glossary_entry` |
| Tablice samouczka | 25 | `tutorial_plaque_throw_top` | `tutorial_plaque_comet_explanation` |
| Tepan: UI | 2 | `millipede_press_to_talk` | `millipede_name` |
| Tepan: statue_room | 14 | `millipede_statue_room_default_1` | `millipede_statue_room_end_line` |
| Tepan: sewers | 16 | `millipede_sewers_default_1` | `millipede_sewers_end_line` |
| Tepan: chasm | 15 | `millipede_chasm_default_1` | `millipede_chasm_end_line` |
| Tepan: sauna | 15 | `millipede_sauna_default_1` | `millipede_sauna_end_line` |
| Tepan: funnel | 16 | `millipede_funnel_default_1` | `millipede_funnel_end_line` |
| Bieg bez końca, ranking | 36 | `endless_run` | `play_again_button` |

Luk w pokryciu nie ma. Sceny Tepana czytano w całości, najpierw po polsku, potem z EN
i notatkami twórców.

Kontrole mechaniczne, reviewer i ponownie agent prowadzący po poprawkach:

- znaczniki `|pause|`, `|short_pause|`, `|long_pause|`, `[[…]]`, `{0}`, `{1}`, `<size>` i `\n`
  są zgodne z EN we wszystkich 359 wpisach;
- limity `max_length` liczone bez znaczników (tak mówią notatki twórców):
  przed poprawkami przekroczone były 3 wpisy, po poprawkach żaden;
- tytuły ekranów sterowania mieszczą się w 15 znakach na wiersz.

**Nowy fakt.** Notatka twórców przy `millipede_statue_room_default_1` mówi:
„many of the characters (Tepan, Kenak) … are not gendered … **if needed, Tepan should be
gendered female, and Kenak male**”. Przekład 1.0 tego nie uwzględniał. Dopisane do biblii
jako źródło `notatka-plec`.

## Błędy — wprowadzone

Agent prowadzący sprawdził każdą przesłankę w pełnym EN, PL i notatce twórców.
Zmienione jest tylko pole `polish`.

| Klucz | EN (fragment) | PL przed | PL po | Przesłanka |
| --- | --- | --- | --- | --- |
| `millipede_statue_room_default_1` | Where have you dropped in from? | Skąd ty się tu wziąłeś? | Skąd ty się tu bierzesz? | Męska forma wobec gracza, sprzeczna z decyzją 2. Kwestia była w verticalu 0.1. |
| `millipede_funnel_lore_3` | from companion to companion I say thank you | jako towarzysz towarzyszowi: dziękuję. | po przyjacielsku: dziękuję. | „Towarzysz” daje Tepanowi rodzaj męski, który wyklucza i decyzja 1, i notatka twórców. „Towarzyszowi” daje rodzaj graczowi. |
| `millipede_chasm_default_2` | They wiped out every last trace of it. | Wymazali po nim wszelki ślad. | Zatarł tu wszelkie ślady. | „They” to Kenak (notatki: „their reign”, rodzaj męski). „Po nim” czyta się jako ślad po Kenaku, czyli odwrotnie niż w EN. |
| `millipede_statue_room_default_6` | all these dark beasts come from it... | …biorą się właśnie stamtąd... | …biorą się właśnie z tego czegoś... | Źródłem potworów jest jedna istota („coś” z `_default_5`), nie miejsce. |
| `millipede_funnel_default_3` | They're all over these caves. | Są w całych tych jaskiniach. | Pełno ich w tych jaskiniach. | Niepoprawna kalka „all over”. |
| `millipede_funnel_default_5` | I never learned what the Yoran did… | tak i nie było mi dane się dowiedzieć, co… | do dziś nie wiem, co… | „Tak i nie” czyta się jako „częściowo”. „Nie było mi dane” zrzuca winę na los, a w notatce Tepan jest zły na siebie. |
| `options_photosensitivity_mode_label` | Photosensitivity Mode | Tryb światłoczuły | Tryb dla wrażliwych na światło | „Światłoczuły” opisuje kliszę. Opcja wyłącza efekty stroboskopowe. 30/50 znaków. |
| `options_confirm_controls_change` | Press a button to assign to\n"{0}" | Naciśnij przycisk, który przypiszesz do\n„{0}” | Naciśnij przycisk dla akcji\n„{0}” | Limit: 42 znaki przy 36 dozwolonych, teraz 30. |
| `options_confirm_controls_change_switch` | jw. | jw. | jw. | jw. |
| `retry_connection_button` | Retry Connection | Spróbuj połączyć ponownie | Połącz ponownie | Limit: 25 znaków przy 20 dozwolonych, teraz 15. |

## Decyzje sprzed verticala — werdykty

1. **Tepan bez rodzaju** — **do rozstrzygnięcia z użytkownikiem** (temat 1 niżej).
   Na całości konstrukcja działa: 76 kwestii i ani jednego rodzajowego czasu przeszłego.
   Ma jednak swoją cenę. Są cztery wyraźnie sztywne miejsca, osiem powtórzeń
   „udało/zdarzyło mi się”, a seria „niosło/zaniosło/wyniosło mnie” odbiera Tepanowi
   sprawczość. Nowa przesłanka to notatka twórców: jeśli rodzaj, to żeński.
2. **Gracz bez rodzaju** — **utrzymać**. Dwa przecieki poprawione, trzeci
   („przyjacielu”) jest do rozmowy.
3. **Kaspidae żeńska, Pustelnik męski** — **utrzymać**. Ryzyko: `sewers_lore_8`
   „przysłał mnie” może dotyczyć Kaspidae (tabela niżej).
4. **Nazwy mocy** (Strumień, Zryw, Odłamki, Igła, Żar, Kometa Zapomnienia, tryb komety) —
   **utrzymać**. Są spójne we wszystkich miejscach i mieszczą się w limitach.
   Osobny temat to „Trafienie …” jako tłumaczenie „… Kill” (temat 3).
5. **Nazwy miejsc** — **utrzymać**. Jedyna propozycja dotyczy „DÓŁ URAZY” (temat 8).
6. **Bieg bez końca** — **utrzymać**. Drobna niespójność: „Przebiegi” (temat 10).
7. **Ograniczenia techniczne** — **utrzymać**. Limity są już poprawione.

Terminy z biblii (tarcza, przywołanie, fala, gniazdo, drzwi/portal, stoper szybkiego
przejścia, wymagany wróg, ranking) są spójne w całej grze.

## Do rozmowy

Obecny tekst zostaje, dopóki użytkownik nie wybierze.

### Najważniejsze

1. **Rodzaj Tepana.** Są dwie drogi:
   - **A (rekomendacja): zostać bez rodzaju** i wygładzić najsztywniejsze miejsca (temat 2).
     Jest to zgodne z „they” w EN i z intencją twórców, że Tepan nie ma płci.
   - **B: rodzaj żeński**, zgodnie z notatką twórców. Trzeba by przepisać około 12–15
     kwestii, za to zniknęłyby wszystkie wymuszone konstrukcje bezosobowe.
     Przykład `millipede_sewers_lore_4`: „Za młodu, przy jakimś tuzinie nóg, wpadłam
     przez takie drzwi”.

   Rodzaju męskiego nie proponujemy, bo twórcy wskazują żeński.

2. **Najsztywniejsze konstrukcje bezosobowe** (dotyczy tylko wariantu A; każdą kwestię
   można zmienić osobno):

   | Klucz | Obecne PL | Propozycja |
   | --- | --- | --- |
   | `millipede_sewers_lore_3` | Udało mi się zobaczyć, jak przechodzisz przez coś podobnego tam, w sanktuarium. | Tam, w sanktuarium, mignęło mi, jak przechodzisz przez coś podobnego. |
   | `millipede_statue_room_default_6` | Udało mi się rzucić okiem tylko przez chwilę, | Tylko parę razy mi to mignęło, |
   | `millipede_sauna_lore_6` | Zostawanie tam tak długo było błędem. | Nie trzeba było w ogóle tak długo tam zostawać. |
   | `millipede_sauna_lore_7` | …wyniosło mnie stamtąd razem ze stoma nogami! | …otworzył, w nogi — wszystkie sto — i precz stamtąd! |
   | `millipede_chasm_default_4` | ale nie zdarzyło mi się zobaczyć, żeby działała. | ale na moich oczach nigdy nie zadziałała. |
   | `millipede_sauna_lore_3` | Ale im dłużej mnie tam trzymało, | Ale z każdym dniem, (wymaga zmiany miejsca `|short_pause|`) |

3. **Powiadomienia „… Kill”** (`air_kill`, `recall_kill`, `chain_kill`, `simultaneous_kill`,
   `realtime_kill`). „Trafienie” oznacza „hit”, a słowniczek konsekwentnie używa „zabić”.
   Propozycja: „Zabójstwo w locie x{0}” itd., przy tej samej długości. Wariant:
   „Eliminacja …”. „Kombo x{0}” zostaje, podobnie jak trafna interpretacja „bez Strumienia”.
4. **`options_hud_scale_label`** „Wielkość interfejsu”: notatka mówi, że opcja zmienia
   tylko HUD, a nie menu. Propozycja: „Wielkość HUD-u” albo „Skala wskaźników”.
5. **`options_remap_keyboard_mouse_controls`** „Zmień klawiaturę i mysz” brzmi jak
   wymiana sprzętu. Propozycja: „Sterowanie klawiaturą i myszą” (29/30), a dla symetrii
   „Sterowanie padem” zamiast „Zmień sterowanie padem”.
6. **`millipede_chasm_default_2`** „wyjątkowo uroczyste”: „solemn” oznacza tu powagę
   i żałobę, nie święto. Propozycja: „otoczone szczególną powagą”.
7. **`millipede_funnel_lore_3`**, pierwsze zdanie: „Nie umiem ci się dostatecznie
   odwdzięczyć” znaczy „odpłacić”, a EN mówi „thank you enough”. Propozycja:
   „Nie wiem, jak ci dziękować.”
8. **`level_2_name`** „DÓŁ URAZY” (THE GRUDGE PIT to arena rozstrzygania sporów walką).
   Propozycja: „DÓŁ PORACHUNKÓW”. Koszt: nazwa była już w verticalu.
9. **Etykiety przełączników w trybie rozkazującym.** „Odtwórz przerywnik otwierający”
   → „Przerywnik na początku gry”; „Odradzaj przy ostatniej fali” → „Odrodzenie od ostatniej fali”.
10. **`allow_all_accessibility_explanation`** „Przebiegi, które na nie pozwalają” →
    „Biegi z tymi ustawieniami trafiają do osobnego rankingu.”

### Pozostałe propozycje reviewera

| Klucz | Obecne PL (fragment) | Propozycja | Uwaga |
| --- | --- | --- | --- |
| `millipede_funnel_default_1` | Witaj, przyjacielu. | Witaj, bratnia duszo. | Męski rzeczownik wobec gracza. „Bratnia dusza” nawiązuje do `sauna_default_3`. Wariant: „Witaj ponownie.” |
| `millipede_chasm_lore_4` | Próbowały! | Niejedno próbowało! | Wcześniej pada tylko „coś”, brak podmiotu. |
| `millipede_funnel_default_4` | Nigdy by mi nie przyszło do głowy... | Nigdy nie przyszło mi do głowy... | Tryb warunkowy zmienia sens. |
| `millipede_funnel_lore_5` | Nie mogę przestać myśleć, czy... | Ciągle się zastanawiam, czy... | |
| `millipede_funnel_lore_6` | zastanę dom, którego już nie ma / przyniosę coś ze sobą | okaże się, że mojego domu po prostu już nie ma / przywlokę coś za sobą | |
| `millipede_sewers_lore_1` | nieprawdaż? | prawda? | Za książkowe jak na ciepły głos. |
| `millipede_chasm_lore_1` | od patrzenia na które boli głowa | na których widok boli głowa | |
| `millipede_sauna_lore_1` | tak głośno myślę | tak tylko głośno myślę | |
| `millipede_sauna_lore_5` | zaczął próbować odtwarzać istoty | zaczął odtwarzać też istoty | |
| `millipede_sewers_default_3` | uskładać | wyszperać / nazbierać | „Uskładać” znaczy zaoszczędzić. |
| `millipede_sewers_default_5` | wsadzali rośliny swoim zmarłym | wsadzali rośliny w swoich zmarłych | |
| `millipede_sewers_end_line` | stuka nogami jedna o drugą | stuka nogą o nogę | Wątpliwy przypadek. |
| `millipede_sewers_lore_8` | przysłał mnie do nich... | zesłało mnie do nich... | Nadawca może być Kaspidae (żeńska). |
| `millipede_statue_room_lore_4` | wstąpiła wyżej? | wzniosła się? | Można zostawić jako zamierzone wahanie. |
| `millipede_statue_room_lore_5` | Aż trudno uwierzyć. | No nie do wiary ze mną. | Niski priorytet. |
| `millipede_sewers_lore_2` | wielonogiego głupca | — | Rodzaj męski ogólny; ruszać tylko po decyzji z tematu 1. |
| `millipede_sauna_default_4` | Choć, | A jednak, | |
| `options_confirm_controls_axis_change` | Porusz osią, którą przypiszesz do | Porusz gałką dla akcji | Spójność z poprawionym przyciskiem; mieści się w limicie. |
| `airstomp_glossary_entry` | wybucha wtedy ognista eksplozja | następuje wtedy ognisty wybuch | Tautologia. |
| `timeslow_glossary_entry` | przytrzymaj[[…]]i ładuj bumerang, a potem naciśnij | przytrzymaj[[…]], żeby ładować bumerang, i naciśnij | |
| `shotgun_glossary_entry` | zabójczych drzazg | ostrych okruchów | Niski priorytet. |
| `options_gameplay_extras_disclaimer` | podkręcić rozgrywkę | urozmaicić rozgrywkę | „Put a spin on”. |
| `options_difficulty_explanation` | przykręcić albo odkręcić ogólne wyzwanie | żeby gra była łatwiejsza albo trudniejsza | |
| `options_weak_points_color` | czułych punktów | słabych punktów | Utarty termin; niski priorytet. |
| `quit_to_main_menu` | Menu główne | Wyjdź do menu | Obecne jest akceptowalne. |
| `controls_action_look_up/down/left/right` | Spójrz w górę… | Patrzenie w górę… | Spójność z „Rozglądanie góra/dół”. |
| `options_invert_x/y_axis_label` | (poziom) / (pion) | (w poziomie) / (w pionie) | Spójność z czułością. |
| `endless_description_canteloupe` | Z ukłonami od szefa kuchni. | Poleca szef kuchni. | |
| `endless_description_hardcore` | Prościej się nie da. | — | Gubi „dead simple”, ale jest akceptowalne. |

**Brak kontekstu:** `tuning_court_name` „DWÓR STROICIELI” (nie wiadomo, czy „court” to
dwór, czy dziedziniec areny), `required` „WYMAGANI:” (zależy od wyglądu HUD),
`options_controller_difficulty_label` „Wyważony pod pada”.

## Do sprawdzenia w grze

1. Okno dialogu Tepana przy najdłuższych kwestiach (`chasm_lore_1`, `chasm_default_2`,
   `funnel_lore_3`, `sauna_lore_3`, `statue_room_default_4`): czy tekst mieści się
   w ramce i czy tempo `|pause|` jest czytelne.
2. Ekran przypisywania klawisza po poprawce („Naciśnij przycisk dla akcji / „Skok””):
   wyśrodkowanie, dwa wiersze, cudzysłów „” w foncie.
3. Powiadomienia kombo w foncie Dead Stock: „Trafienie bez Strumienia x3” — szerokość
   i wielkość liter z fallbacku.
4. Najdłuższe etykiety opcji wobec kolumny wartości: „Kolor wroga bonusowego w Biegu
   bez końca”, „Tryb dla wrażliwych na światło”, „Ostrzeżenia o bliskim zagrożeniu”.
5. Suwak pola widzenia: jeśli pokazuje wartości zakończone na 2–4, forma „{0} stopni” jest
   błędna i trzeba ją zmienić na „{0} st.” albo „{0}°”.
6. Ekrany odblokowań („KOMETA ZAPOMNIENIA / ODBLOKOWANO”, „ŻAR”) i tytuły obszarów
   („ŁAŹNIA PUSTELNIKA”, „FORUM ZAGŁODZONEGO GNIAZDA”): wersaliki z ż, ł, ę.
7. Tablice samouczka z ikonami (`timeslow_bottom`, `sniper_bottom`, `swap_powerup`).
8. Okienko wyboru trudności przy nowym zapisie (oba miejsca `difficulty_select_prompt`).
9. HUD fal: „FALA 2/5” i „WYMAGANI:”.

## Raport regexowy

- Spójność (4): fałszywe alarmy. Normalna/Normalny i Wyłączone/Wyłączony zgadzają się
  z różnymi rzeczownikami.
- Angielskie resztki (4): fałszywe alarmy. Trzy to same ikony, a „Standard” jest słowem polskim.
- Liczebniki (7): „{0} wrogów” jest poprawne dla 2–4 i 5+, bo „wróg” jest męskoosobowy.
  Realnym ryzykiem jest tylko `options_fov_formatting` (punkt 5 w teście).
- Długość (7): to proporcje PL do EN, a nie przekroczenia limitu. Raport nie wychwycił
  trzech rzeczywistych przekroczeń, bo nie czyta `max_length`.
- Raport nie sprawdza rodzaju dla `plec: n` ani dla gracza. Wszystkie trzy przecieki
  wyszły dopiero przy ręcznym czytaniu.

## Stan po poprawkach

Po naniesieniu 10 poprawek agent prowadzący ponownie sprawdził zmienione wpisy.
Znaczniki są zgodne z EN we wszystkich 359 wpisach, żaden wpis nie przekracza
`max_length`, a `l10n_report.py` daje te same zgłoszenia co przed zmianami
(wszystkie opisane wyżej). `tools/check_games.ts` przechodzi.
Paczka 1.1 w `site/public/pobierz/` **nie zawiera tych poprawek** — wejdą przy
następnym buildzie.
