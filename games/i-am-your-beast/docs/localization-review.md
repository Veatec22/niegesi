# I Am Your Beast — niezależny przegląd lokalizacji

Data: 2026-09-25. Reviewer: osobny subagent w świeżym kontekście, tylko do odczytu,
według `.claude/skills/localization-review/SKILL.md`. Stan wejściowy: 0.2.0 przed poprawkami.

## 1. Pokrycie

- `en-pl-review.json` i `pl.json`: po 1601 kluczy, zgodne co do znaku.
- Przeczytane w całości: 1581 wpisów z tekstem — 870 odcinków w 44 scenach po kolei
  z mówiącym, 687 wpisów Fleece w 99 folderach z kontekstem planszy, 44 napisy TMP.
- Zdania narastające sprawdzone skryptem we wszystkich scenach; znaczniki bez błędów.
- Przeczytane, nierozstrzygnięte: mówiący przy kolorze 0 (`20 Helper Delta/25–30`,
  `RELEASE/40–44`, `7 Peekaboo/16`, `SCENE 1/10–11`, `24 Goodbye/13`); fragmenty bez
  kontekstu (`fleece/12694` „full”, folder 74196, `tmp/Base:\nReclaimed:`); napisy
  składane w folderze 66204.

## 2. Pewne błędy — naniesione

| Klucz | Było | Jest | Kategoria |
|---|---|---|---|
| `phrase/6 Help Wanted/54` | Puści go pan. | Puści mnie pan. | znaczenie |
| `phrase/4_ImpoliteDispute/22` | …rozerwaną na pół z broni… | …rozerwaną na pół przez broń… | język |
| `phrase/FINAL CUTSCENE/25` | To powiedziawszy... | No dobrze... | język (kalka) |
| `phrase/12 Helper Gamma/13–16` | Jest za mgliście… | Jest za mglisto… | język |
| `fleece/2306` | Nie zabij nikogo | Nie zabijaj nikogo | język |
| `tmp/These settings are designed…` | …za rangę S… | …za ocenę S… | terminologia |
| `fleece/48222` | Okno | W oknie | terminologia |
| `phrase/SCENE 1/4` | No weź, stary. Stephen jest tutaj. | No weź. Stephen jest tutaj. | rodzaj adresata |

Dodatkowo przez agenta prowadzącego: „pieprzony” → „pierdolony” (`fleece/29393`,
`SCENE 1/14`) zgodnie z decyzją o wulgaryzmach; Nathan do Burkina jedną formą
(`SCENE 9/26–27`); składanie napisu odblokowania (`fleece/99330`, `fleece/84896`).

## 3. Warianty do rozmowy z użytkownikiem

1. ~~Nathan: ty/pan do Burkina~~ — naniesione jako niespójność.
2. `fleece/36027` „Złap i wypuść” → „Złów i wypuść” (termin wędkarski; ryby wracają w fabule).
3. `fleece/34877` „Nie patrz w dół” → „Spójrz w dół” (EN nie ma przeczenia) — zależy od poziomu.
4. Kalki w dialogach:
   - `SCENE 3/1` → „Nie bez powodu nie daje się księgowym wyrzutni rakiet.”
   - `20 Helper Delta/28` „przez to przejdziesz” → „wyjdziesz z tego cało”.
   - `17 Acceptance/8–9` → „Tyle razy próbowałeś mnie ściągnąć... / a ani razu nie przyszedłeś tu sam.”
   - `SCENE 8/14` → „Sporo patosu jak na parę wybitych zębów-”.
   - `SCENE 7/6`, `RELEASE/24` „albo coś” → „czy coś”.
5. Wulgaryzmy: `fleece/35367` „Harding rzuca czym popadnie!” (EN „throwing shit”) — świadomie zostawić.
6. `SCENE 9/19`, `/22` „GENERALE BURKIN!” → „GENERAŁ BURKIN!” (okrzyk rozpoznania).
7. `RELEASE/42–43` → „Dobrze ci szło! / Dobrze?”; `24 Goodbye/13` „...No wiesz?” → „...Nie?”.
8. Drobne: fałszywe starty `SCENE 1/6` „Do...”, `SCENE 5/16` „Prze-”; ujednolicenie
   didaskaliów (`*prycha*` vs `*westchnienie*`); `tmp/[Esc] to close` → „[Esc] – zamknij”;
   `SCENE 9/1` „Weź się ogar-” → „Nie przesadzaj-”; `fleece/19117` „Zamknięcie” → „Domknięcie”.

## 4. Decyzje sprzed verticala

1. Głos Hardinga — **utrzymać** (9 Anger, 14 Depression, 18 Stalemate, 24 Goodbye).
2. Formy zwracania się — **utrzymać**; „pan” Byrona tylko w 6 Help Wanted; gra słów
   „Mów mi Charles” / „Nie zamierzam w ogóle do ciebie mówić” działa.
3. Nazwy poziomów — **utrzymać** (ustalenia użytkownika i pozostałe).
4. Wulgaryzmy tej samej siły — **utrzymać**; trzy łagodniejsze miejsca (sekcja 3.5).
5. Zdania narastające — **utrzymać**.
6. Terminy — **utrzymać**: I.T.O. (18 wystąpień, rodzaj żeński spójny), ostatnia robota,
   skarbie (8), helikopter, szufladka, Zimny pot, Grupa wsparcia, Drogi pamiętniku,
   ziołowe krzaki, szybki obrót, kopnięcie, sidła. Perch: w dokumentach „przyczajka”,
   w grze „Przyczaj się” — poprawiono zapis. Jodie/Iris jako kobiety — utrzymać; nowa
   przesłanka: `fleece/47208` „*she finds this extremely funny*”.

## 5. Co sprawdzić w grze

- 6 Help Wanted #53–58 po poprawce; ekran odblokowań („Ukończ: Fabuła – cele dodatkowe x5”).
- `tmp/Base:\nReclaimed:` — czego dotyczy (rodzaj „Bazowy/Odzyskany”).
- Długie etykiety: „Media społecznościowe i społeczność”, „Synchronizacja pionowa”,
  „Tylko zabójstwa z celowaniem”, „Pole widzenia przy sprincie”, „Projektant efektów dźwiękowych”.
- Polskie litery w wersalikach Octin: „PIERDOLĘ”, „ŁOOOOŁ”, „ZNALAZŁEM CIAŁO!”.
- Grupa wsparcia: głosy Jodie i Iris; wygląd „I.T.O. ...”; czy widać też narrację z folderu 44072.
- Poziom „Look Down”; podpowiedź przejścia między gałęziami (35726); rytm „Masz / się / wycofać”.
