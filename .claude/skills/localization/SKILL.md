---
name: localization
description: Standard lokalizacji gier w repo Nie gęsi, oparty na faktach zamiast przeczucia. Opisuje biblię gry (postacie, płeć, formy zwracania się, terminy ze źródłami), pułapki języka polskiego, raport kontrolny l10n_report.py i podsumowanie decyzji przy oddaniu. Użyj przy tłumaczeniu pełnej gry (full) po verticalu, przy dotłumaczaniu lub poprawianiu games/<gra>/translations/pl.json oraz przy oddawaniu tłumaczenia do akceptacji.
---

# Lokalizacja gry

Cel: trafić samodzielnie w jak najwięcej okazji i pułapek. Wszystko jest pomocą,
nic nie blokuje builda. Rób proporcjonalnie: biblia i raport mają oszczędzić
poprawek, a nie stać się osobnym projektem.

## Przebieg (etap full; w verticalu wystarczy krok 1 w skrócie)

1. **Biblia gry** — `games/<gra>/translations/bible.yaml`, zanim zaczniesz
   tłumaczyć dialogi. Format i przykład: [BIBLE.md](BIBLE.md). Zawiera:
   - postacie: płeć, jak mówią i do kogo („ty”/„pan”), regex klucza mówiącego;
   - terminy z przyjętym tłumaczeniem i rdzeniami form;
   - nazwy, które zostają po angielsku;
   - źródło każdego faktu.

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
   gra słów po polsku, utarty termin z gatunku, naturalny idiom.
3. **Raport kontrolny** po każdej większej partii i przed buildem:
   ```powershell
   .venv\Scripts\python.exe .claude\skills\localization\scripts\l10n_report.py games\<gra>
   ```
   Wynik trafia do `games/<gra>/work/l10n-report.md`. Przejrzyj każdą sekcję.
   Popraw prawdziwe problemy; fałszywe alarmy zignoruj, a powtarzające się
   uciszasz w biblii (`bez_tlumaczenia`, `ignoruj`), nie w skrypcie.
4. **Oddanie:** `games/<gra>/docs/translation-decisions.md` plus to samo
   w skrócie w odpowiedzi do użytkownika. Wzór: [HANDOFF.md](HANDOFF.md).

## Zasada oddania

Nie pytaj o decyzje w trakcie. Podejmij je, uzasadnij i wypisz przy oddaniu.
Użytkownik akceptuje albo odrzuca i poprawia. Odrzucenie wpisz do biblii
jako `zrodlo: uzytkownik` razem z odrzuconą propozycją. Takich terminów
nie ruszaj w kolejnych przeglądach. Pytać wolno tylko o to, bez czego
nie da się ruszyć (brak plików gry, brak dostępu). Zakończ na liście „co
sprawdzić w grze” — konkretne ekrany i sceny, gdzie decyzja jest najmniej pewna.

## Czego nie robić

- Nie dodawaj blokad do buildów ani obowiązkowych kroków do AGENTS.md.
- Nie przepisuj działającego tłumaczenia tylko dla zgodności z raportem.
  Raport pokazuje miejsca do obejrzenia, nie wyroki.
- Nie wymyślaj faktów o lore. Jeśli fakt jest decyzją, oznacz go jako decyzję.
