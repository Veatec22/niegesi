# Biblia gry — format

Plik: `games/<gra>/translations/bible.yaml`. Czyta go człowiek i `l10n_report.py`.
Wszystkie sekcje są opcjonalne. Zacznij od postaci mówiących i 20–50 terminów,
które wracają najczęściej albo są nazwami własnymi świata gry.

```yaml
zrodla:                      # identyfikatory, do których odwołują się fakty
  - id: klucze
    opis: Pole `term` w review, np. vo_e3m1_7_syn — mówiący na końcu klucza.
  - id: obsada
    opis: Obsada głosowa
    url: https://english-voice-over.fandom.com/wiki/Turbo_Overkill_(2023)
  - id: ru
    opis: Rosyjska tabela gry — płeć w czasie przeszłym

postacie:
  - id: syn
    nazwa: SYN                # jak w polskim tekście
    plec: k                   # m | k | n (nijaki/zbiorowy) | ? (nieustalona)
    klucz: '_syn$'            # regex na `term` albo `key`; wtedy raport sprawdza płeć
    mowi_do_gracza: ty        # ty | pan | pani | wy | -
    rejestr: patetyczny, boski, bez wulgaryzmów
    odmiana: nieodmienna („bez SYN”)
    zrodlo: [obsada, ru, klucze]
  - id: samm
    nazwa: S.A.M.M.
    plec: m
    klucz: '_samm$'
    mowi_do_gracza: pan („sir”)
    zrodlo: [klucze]

terminy:
  - en: biocore               # dopasowanie bez wielkości liter; może być regexem
    pl: biordzeń
    formy: [biordz]           # rdzenie akceptowanych form w PL (bez wielkości liter)
    zrodlo: decyzja
    uwaga: jeden wyraz, jak „rdzeń”; spójne z UI i dialogami
  - en: Street Cleaner
    pl: czyściciel ulic
    formy: [czyściciel, czyścicielk]
    zrodlo: decyzja

bez_tlumaczenia:              # nazwy zostające w oryginale; raport nie zgłosi ich jako resztek EN
  - Paradise
  - Vector-4

ustawienia:
  dialog_klucz: '^vo_'        # regex na term/key: napisy dialogów (limit wiersza)
  max_wiersz: 42              # znaków w wierszu napisów (Netflix PL)

ignoruj:                      # świadome wyjątki od raportu
  - sprawdzenie: plec
    klucz: 'vo_e3m9_24_syn'
    powod: cytat innej postaci
```

## Rdzenie w `formy`

Tnij rdzeń przed spółgłoską, która się wymienia w odmianie: „artefak” (Artefakt,
Artefakcie), „warszta” (Warsztat, Warsztacie), „piłonog” (piłonoga, piłonodze →
dopisz też „piłonodz”). Za krótki rdzeń łapie przypadkowe słowa, za długi gubi przypadki.

## Pola `zrodlo`

Lista identyfikatorów z `zrodla` albo słowo `decyzja`. Przy decyzji dopisz
`uwaga` z jednym zdaniem uzasadnienia. Trafia to potem do podsumowania oddania.

`zrodlo: uzytkownik` oznacza rozstrzygnięcie użytkownika przy akceptacji.
Jest nadrzędne wobec wszystkich innych źródeł. W `uwaga` zapisz też odrzuconą
propozycję, żeby kolejny przegląd nie proponował jej ponownie.

## Płeć w polskim, na co wpływa

- 1. osoba czasu przeszłego: „zrobiłem/zrobiłam”, tryb przypuszczający „-łbym/-łabym”.
- Przymiotniki o sobie: „jestem gotowy/gotowa”.
- Adresat: „jesteś pewien/pewna”, „zrobiłeś/zrobiłaś”, forma „pan/pani”.
- Mowa o postaci w 3. osobie: „SYN pochłonęła”, „Ripper zabiła”.
