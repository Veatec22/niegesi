# Hyper Light Drifter — niezależny przegląd lokalizacji (0.1.0)

Data: 2026-09-25. Reviewer: osobny subagent w świeżym kontekście, tylko do odczytu
(skill `localization-review`). Poprawki naniósł agent prowadzący.

## Zakres

Wejście (SHA-256):

- `translations/en-pl-review.json` przed przeglądem: `8f95994ae941b601a9a4e35776eab5158bf8bd6c36289e7521c6b97dfcfd88b7`,
  po poprawkach: `1d697a27feb19f8bb6e37804139a5534bc1da9c90051e6a7fedf4117b85da1ab`
- `translations/bible.yaml`: `9b37538103a60c4d4059ab75b1879e1f6bbf0f4b038c2f1edd48132f8bfe5e44`
- `docs/translation-decisions.md`: `e8739823e1fadf77076339a76a0e6dabaa050f5cdf364f965a9aaf62c1aa3c89`

Wpisy: 126 wszystkich, 126 przeczytanych w całości (EN, PL, kontekst ITA, uwagi autorów
o limitach). Luk nie ma. Partie:

| Partia | Wpisy | Klucze |
| --- | --- | --- |
| A. Menu główne, pauza, przyciski | 23 | CONTINUE … EXITGAME, RESUMEGAME, QUITTOTITLE, MAIN_MENU_TITLE, MENU_TITLE, QUIT_TO_TITLE_TEXT, SwitchUser, CopyWrite, Select, Back, Yes, CONFIRM, DELETE, CANCEL |
| B. Ustawienia | 25 | CONTROLS, SCREENMODE, BRIGHTNESS, SFXVOL, MUSVOL, VIBRATION, LANGUAGE, DASHTYPE, COOP, COOP_DISABLED, THIRDPARTYCONTROLS, Windowed, WINDOW_MAX, FULLSCREEN, ON, OFF, MOUSE_DIR, MOVE_DIR, NEED_GAMEPAD, MODE, OVERSCAN, FRAMERATE, VSYNC, Alternative, DISABLE_XBOX_DVR |
| C. Sterowanie i konfiguracja | 23 | GAMEPAD, RESET, 12 × `*Config`, KeyboardAndMouseConfigTitleName, notapplicable, CONTROLMODETYPES, STANDARDCONTROLS, COOPCONTROLS, PLAYERONE/TWOCOOPCONTROLMODE, PlaysBestWithController, ControllersItPlaysBestWith |
| D. Tryby i odblokowania | 14 | NEWCOMER, STANDARD, 10 × `*DESCRIPTION*`, UnlockedAtEndGame, `(LOCKED: missing Alt Drifter DLC)` |
| E. Maraton bossów | 12 | BossRush, FullyLoaded, MidRange, Naked, BossRushComplete, 2 × `*BossRushLoadoutUnlocked`, 5 opisów zestawów |
| F. Zapis | 13 | LESS_THAN_A_MINUTE, MINUTE, MINUTES, SINCE_LAST_SAVE, APPEARS_WHEN_PROGRESS_IS_SAVED, ENTER_NAME, `REPLACE THIS SAVE?`, EMPTY, AutoSaveFeature(2), DoNotTurnOff(Console/PS4) |
| G. Podpowiedzi (`Phrases`) | 16 | HEAL, COLLECT, INTERACT, AIM, AMMO, MAP, WARPPAD, WARP, REMINDERGUN, CAPE, SWAP, LOADOUT, PING, NOACHIEVEMENTS, NEWCOMERHOARDE(PS4) |

Ograniczenia: pliki gry (`MenuText.txt`, `Phrases.txt`) nie były dostępne w środowisku
przeglądu, więc EN nie zostało porównane z bieżącą ekstrakcją. Jedynym obcym kontekstem
był włoski z pola `context`; wersji FR/ES/DE, na które powołuje się biblia, reviewer nie
widział. Znaczniki `[BUTTON_*]` i `[spr_*]` są zachowane 1:1, spacje wokół nich poprawne,
poczwórna spacja w `Phrases/AIM` zachowana. Limity z uwag autorów dotrzymane poza
świadomym wyjątkiem `SwapWepConfig` (12 znaków przy 11).

Raport automatyczny (`work/l10n-report.md`) przed i po poprawkach: 11 zgłoszeń, te same
fałszywe alarmy co w decyzjach — reviewer zgadza się z ich objaśnieniem.

## Błędy

Błędów sensu, gramatyki, negacji ani zepsutych znaczników nie znaleziono. Dwie drobne
poprawki:

| Klucz | EN | Było | Jest | Przesłanka | Status |
| --- | --- | --- | --- | --- | --- |
| `Phrases/REMINDERGUN` | Gun is fully charged from slashing | Broń palna naładowana cięciami miecza | Broń palna w pełni naładowana cięciami miecza | pominięte „fully”; 45 znaków (ITA 39, inne podpowiedzi do 53) | wprowadzone |
| `MenuText/MidRangeBossRushLoadoutUnlocked` | Mid-Range boss rush loadout unlocked | Odblokowano zestaw Średni w Maratonie bossów | Odblokowano Średni zestaw w Maratonie bossów | nazwa zestawu wszędzie indziej to „Średni zestaw” (biblia, MidRange, NAKEDUNLOCKDESCRIPTION); ta sama długość | wprowadzone |

„Odblokowano zestaw Na golasa…” zostaje — nazwa „Na golasa” nie zawiera słowa „zestaw”.

Paczka 0.1.0 nie zawiera tych poprawek; wejdą przy następnym buildzie.

## Decyzje sprzed verticala

| Decyzja | Werdykt | Uwagi |
| --- | --- | --- |
| Polski w miejscu włoskiego, „POLSKI” | utrzymać | pola, które włoski przekraczał, sprawdzone w grze na tej długości |
| dash → zryw | utrzymać | „Rodzaj zrywu”, „ZRYW”; mieści się w polach |
| gun(s) → broń palna | utrzymać | pełna forma przy rozróżnieniu z mieczem (AMMO, REMINDERGUN), „broń” tam, gdzie jasne (SWAP, LOADOUT) |
| warp → teleportować się | utrzymać | spójne w WARPPAD i WARP |
| Home → dom | utrzymać / brak kontekstu | klucz `CAPE` sugeruje zmianę peleryny/stroju; „dom” działa w obu odczytach |
| gear → wyposażenie / sprzęt | utrzymać | jeśli w CAPE chodzi o strój, „sprzęt” jest nieco techniczny, ale wierny ogólnemu „gear” |
| Newcomer → Nowicjusz | utrzymać | konsekwentnie „w trybie Nowicjusz” |
| Boss Rush → Maraton bossów | utrzymać | dobrze się odmienia; koszt: długość komunikatów o odblokowaniu (test) |
| Pełny / Średni zestaw / Na golasa | utrzymać | z poprawką spójności powyżej |
| osiągnięcia / trofea | utrzymać | spójne w 6 wpisach |
| co-op → kooperacja | utrzymać jako termin | forma etykiety trybu sterowania — do rozmowy |
| Credits → Twórcy | utrzymać | |
| Efekty / Muzyka | utrzymać | „Głośność efektów” ma 16 znaków przy limicie 15 |
| Minutes → min, Minute → minuta | utrzymać | drobna niekonsekwencja „1 minuta” / „2 min” — do rozmowy |
| Wróć do domu, by zmienić sprzęt | utrzymać | teleportację uczą WARPPAD i WARP |
| Wyjdź do menu głównego | utrzymać | krótsze niż włoskie (31 znaków) |
| Klawisze jako rzeczowniki wersalikami | utrzymać zasadę | dwa odstępstwa (STRZAŁ, SPECJALNY) — do rozmowy |
| Font z samymi wersalikami, bez „” i półpauz | utrzymać | nigdzie nie są potrzebne |

## Do rozmowy

Obecny tekst zostaje do decyzji użytkownika.

1. **`Phrases/REMINDERGUN` — kiedy się pokazuje.** EN i ITA czytają się jak komunikat
   o stanie, ale klucz REMINDER sugeruje przypomnienie, być może przy pustej broni. Wtedy
   „naładowana” wprowadza w błąd. Rekomendacja: sprawdzić w grze; jeśli przy pustej
   broni → „Cięcia mieczem ładują broń palną”.
2. **`SpecialConfig` „SPECJALNY”** — jedyny przymiotnik bez rzeczownika wśród nazw akcji.
   Warianty: „GRANAT” (jeśli przycisk rzuca granat — do potwierdzenia w grze),
   „BROŃ SPEC.” (10 znaków) albo zostawić. **`ShootConfig` „STRZAŁ”** obok CELOWANIE,
   LECZENIE → „STRZELANIE” (11 znaków); czysto stylistyczne, niski priorytet.
3. **`notapplicable` N/A → „Brak”.** „Brak” czyta się jak „nie przypisano”, N/A to
   „nie dotyczy”. Wariant „N/D” (jak ITA). Rozstrzygnąć po zobaczeniu ekranu.
4. **Tryby sterowania:** „Standardowe / Kooperacja / Alternatywne” — dwa przymiotniki
   i rzeczownik w jednym przełączniku. Wariant `COOPCONTROLS` → „Kooperacyjne”
   (12 znaków). Zależy też od tego, czy „Alternative” należy do tej grupy.
5. **Włącz/wyłącz:** `ON`/`OFF` „Włączone/Wyłączone”, `COOP_DISABLED` „Wyłączona”.
   Jeśli wiersz „Kooperacja” pokazuje ON i COOP_DISABLED, wyjdzie niezgodność rodzaju.
   Wariant bezpieczny: COOP_DISABLED → „Wyłączone”.
6. **`STANDARDDESCRIPTIONONE`** „Zamierzony poziom trudności.” — poprawne, lekko kalkowe.
   Wariant „Poziom trudności według twórców.” (32). Niski priorytet.
7. **`Phrases/AMMO`** „Tnij wrogów i przedmioty…” — „przedmioty” to też rzeczy do
   podniesienia (COLLECT). Wariant „Tnij wrogów i obiekty, by ładować broń palną”.
   Niski priorytet.
8. **Drobne (reviewer rekomenduje zostawić):** `SFXVOL` „Efekty” → „Dźwięki”;
   `Windowed` „Okno” → „W oknie”; „ZASTĄPIĆ TEN ZAPIS?” → „NADPISAĆ TEN ZAPIS?”;
   `DASHTYPE` „Rodzaj zrywu” → „Kierunek zrywu” (wartości to kierunki; limit pola
   nieznany); `MINUTE` „minuta” → „min” dla spójności z MINUTES.

## Do sprawdzenia w grze

1. Lista języków i wszystkie ekrany: „POLSKI”, 16 dorobionych liter (puste pola =
   przycinanie współrzędnych, rozsypany font = PNG), ogonki ą/ę na ekranie trybów
   („ŁAGODNIEJSZE WYZWANIE.”, „MNIEJ SPRZĘTU, WIĘCEJ WYZWANIA.”) i Maratonu bossów.
2. Ustawienia: „Rodzaj zrywu: Za kursorem”, „Tryb ekranu: Okno maks. / Pełny ekran”,
   „Wibracje: Wyłączone / Wymaga pada”, „Kontrolery innych firm”; jakie wartości ma
   wiersz „Kooperacja” (pkt 5); gdzie pojawia się „Alternatywne”.
3. Konfiguracja klawiszy (Klaw.+mysz i Pad): „ZMIANA BRONI” (12 przy limicie 11),
   „INTERAKCJA”, „CELOWANIE”, „SPECJALNY”; co robi SPECIAL (pkt 2); gdzie stoi „Brak”
   (pkt 3); „Reset” na przycisku.
4. Menu pauzy: „Wyjdź do menu głównego” i okno „Wyjść do menu głównego?” z „Tak”.
5. Wczytywanie: „Mniej niż minuta od ostatniego zapisu”, „1 minuta od…”, „N min od…”
   (kolejność i spacje); „PUSTY” przy slocie; okno „ZASTĄPIĆ TEN ZAPIS?”.
6. Maraton bossów: komunikat „Odblokowano zestaw Na golasa w Maratonie bossów”
   (47 znaków; EN 32, ITA 40) i „Maraton bossów ukończony”.
7. Wybór nowej gry: „(Odblokowane po ukończeniu gry)” (31; EN 21) i
   „(ZABLOKOWANE: brak DLC Alt Drifter)”.
8. Pierwsze podpowiedzi: przecinek tuż po ikonie („Użyj [apteczka], by się uleczyć”),
   najdłuższa „Przytrzymaj […], by podnieść przedmioty”; kiedy pojawia się REMINDERGUN
   (pkt 1) i CAPE (co jest „domem”); LOADOUT bez końcowej spacji.
9. Ekran startowy o autozapisie (trzy linie) i „Najlepiej grać na kontrolerze /
   XBOX 360/ONE/PS4”.

## Przeczytane, nierozstrzygnięte z braku kontekstu

`THIRDPARTYCONTROLS` (przełącznik czy ekran), `Alternative` (do której etykiety — rodzaj),
`COOP_DISABLED`, `notapplicable`, `SpecialConfig`, `MODE`, `ENTER_NAME` („nazwa” zapisu
czy imię postaci), `SwitchUser`, `UnlockedAtEndGame` (co jest odblokowane; forma nijaka
bezpieczna), `EMPTY`, `MINUTE` (czy tylko dla 1), `REMINDERGUN`, `CAPE`,
`DoNotTurnOffPS4` (oficjalne brzmienie Sony nieznane; na PC się nie pojawia).

## Ponowna kontrola po poprawkach

Sprawdzone oba zmienione wpisy i ich zależności (nazwa „Średni zestaw” w MidRange,
NAKEDUNLOCKDESCRIPTION; „broń palna” w AMMO). Raport kontrolny bez zmian (11 zgłoszeń,
fałszywe alarmy), `tools/check_games.ts` przechodzi. Paczki nie przebudowano. Test w grze
nadal czeka.
