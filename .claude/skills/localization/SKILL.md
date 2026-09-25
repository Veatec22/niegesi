---
name: localization
description: Tłumaczenie verticala i pełnej gry na polski w repo Not Geese, dotłumaczanie i korekty. Stosuj biblię, uzgodniony kierunek, zasady redakcji i raport kontrolny; po fullu przekaż całość osobnemu reviewerowi.
---

# Lokalizacja gry

Cel: trafić samodzielnie w jak najwięcej okazji i pułapek. Raport jest pomocą,
nie blokuje builda. Rób proporcjonalnie: biblia i raport mają oszczędzić
poprawek, a nie stać się osobnym projektem.

## Przebieg

Przed verticalem zastosuj [localization-direction](../localization-direction/SKILL.md).
Przeczytaj zapisane ustalenia w `docs/translation-decisions.md` gry oraz
[zasady redakcji](EDITORIAL.md). Nie otwieraj ponownie uzgodnionych wyborów bez
nowych przesłanek. Full zaczyna się dopiero po potwierdzeniu verticala w grze.

1. **Biblia gry** — rozwiń `games/<gra>/translations/bible.yaml` utworzoną przed
   verticalem. W starszych projektach uzupełnij brakujące ustalenia bez powtarzania
   zakończonych etapów. Format i przykład: [BIBLE.md](BIBLE.md). Zawiera:
   - postacie: płeć, jak mówią i do kogo („ty”/„pan”), regex klucza mówiącego;
   - terminy z przyjętym tłumaczeniem i rdzeniami form;
   - nazwy, które zostają po angielsku;
   - źródło każdego faktu oraz kierunek i przykłady stylu.

   Kolejność źródeł (pełna lista w [SOURCES.md](SOURCES.md)):
   1. **Pliki gry:** klucze wpisów (np. `vo_e3m1_7_syn` = mówi SYN), tabele
      innych języków z tej samej gry (ruski, czeski, ukraiński pokazują płeć
      w czasie przeszłym, francuski — rodzaj rzeczowników), komentarze w tabelach.
   2. **Obsada i napisy końcowe.**
   3. **Wiki, TV Tropes, wypowiedzi twórców.**
   4. **Oficjalne polskie wydania gier z tego gatunku** (utarte terminy).

   Gdy źródła milczą, zdecyduj sam i zapisz w biblii `zrodlo: decyzja`
   z jednym zdaniem uzasadnienia.
2. **Tłumaczenie** według biblii i [PITFALLS.md](PITFALLS.md): płeć mówiącego
   i adresata, liczebniki przy placeholderach, gry słów, długość w UI,
   napisy, typografia, rejestr i wulgaryzmy. Szukaj okazji, nie tylko błędów:
   gra słów po polsku, utarty termin z gatunku, naturalny idiom. Tłumacz scenami
   i grupami funkcjonalnymi, nie przypadkowymi porcjami kluczy. Nowe fakty i kontekst
   dopisuj do biblii; niepewności zachowaj dla reviewera.
3. **Raport kontrolny** po każdej większej partii i przed buildem:
   ```powershell
   .venv\Scripts\python.exe .claude\skills\localization\scripts\l10n_report.py games\<gra>
   ```
   Wynik trafia do `games/<gra>/work/l10n-report.md`. Przejrzyj każdą sekcję.
   Popraw prawdziwe problemy; fałszywe alarmy zignoruj, a powtarzające się
   uciszasz w biblii (`bez_tlumaczenia`, `ignoruj`), nie w skrypcie.
4. **Review po fullu:** zastosuj [localization-review](../localization-review/SKILL.md).
   Osobny reviewer czyta całość i ponownie ocenia decyzje sprzed verticala.
   Przy późniejszych korektach sprawdź zmiany i ich zależności; pełny przegląd
   powtarzaj po nowym fullu lub na prośbę użytkownika, nie po każdej literówce.
5. **Oddanie:** `games/<gra>/docs/translation-decisions.md` plus to samo
   w skrócie w odpowiedzi do użytkownika. Wzór: [HANDOFF.md](HANDOFF.md).

## Zasada oddania

Zwykłe decyzje podejmuj sam. Istotne warianty omawiaj w dwóch miejscach:
przed verticalem na próbce i po fullu na podstawie niezależnego review.
Użytkownik akceptuje albo odrzuca i poprawia. Jego wybór wpisz do biblii
jako `zrodlo: uzytkownik` razem z odrzuconą propozycją. Nie zmieniaj go samowolnie;
nowe dowody z całej gry mogą uzasadniać ponowną rozmowę, nie cichą podmianę.
Pytaj też o brakujące dane, bez których nie da się ruszyć. Zakończ na liście „co
sprawdzić w grze” — konkretne ekrany i sceny, gdzie decyzja jest najmniej pewna.

## Czego nie robić

- Nie zamieniaj heurystyk raportu ani subiektywnych ocen stylu w blokady builda.
- Nie przepisuj działającego tłumaczenia tylko dla zgodności z raportem.
  Raport pokazuje miejsca do obejrzenia, nie wyroki.
- Nie wymyślaj faktów o lore. Jeśli fakt jest decyzją, oznacz go jako decyzję.
