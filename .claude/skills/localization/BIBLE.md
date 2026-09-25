# Biblia gry — format

Plik: `games/<gra>/translations/bible.yaml`. Czyta go człowiek i `l10n_report.py`.
Sekcje dobieraj do gry. Przed verticalem wystarczy profil stylu, postacie i kilka
terminów z próbki; przy fullu rozszerz biblię o powracające terminy i nowe postacie.
Pola stylu i przykłady czyta agent; raport regexowy ich nie ocenia.

```yaml
zrodla:                      # identyfikatory, do których odwołują się fakty
  - id: klucze
    opis: Pole `term` w review, np. vo_e3m1_7_syn — mówiący na końcu klucza.
  - id: obsada
    opis: Obsada głosowa
    url: https://english-voice-over.fandom.com/wiki/Turbo_Overkill_(2023)
  - id: ru
    opis: Rosyjska tabela gry — płeć w czasie przeszłym

styl:
  ton: suchy humor, krótkie riposty, bez współczesnych memów
  adaptacja: idiomy swobodnie; bez dopisywania lore i wzmacniania wulgaryzmów
  zrodlo: decyzja             # uzytkownik dopiero po rzeczywistym uzgodnieniu
  uwaga: punkt wyjścia z próbki, do ponownej oceny po fullu

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
  dialog_klucz: '^vo_'        # regex na term/key: napisy dialogów
  max_wiersz: 42              # orientacyjne; potwierdzić w grze, raport nie sprawdza tego pola

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
propozycję, żeby kolejny przegląd nie proponował jej ponownie bez nowych przesłanek.
Jeśli pełna gra ujawnia konflikt z ustaleniem, reviewer pokazuje go użytkownikowi;
nie nadpisuje ustalenia. Brak odpowiedzi nie uprawnia do wpisania `uzytkownik`.

## Przykłady głosu i pamięć decyzji

Do postaci można dodać `przyklady`: listę z `klucz`, `en`, `pl`, `uwaga`, `zrodlo`.
Wybierz 1–3 rzeczywiste kwestie pokazujące sposób mówienia, zamiast mnożyć etykiety.
Zaznacz, jeśli rejestr zależy od rozmówcy albo zmienia się wraz z fabułą.

W biblii trzymaj obowiązujące ustalenia. Próbki, nierozstrzygnięte alternatywy
i uzasadnienia rozmów zachowuj w `docs/translation-decisions.md` gry.
Przy zmianie uzgodnienia odnotuj poprzedni wybór, nową przesłankę i rozstrzygnięcie;
nie kasuj pamięci odrzuconych wariantów.

## Płeć w polskim, na co wpływa

- 1. osoba czasu przeszłego: „zrobiłem/zrobiłam”, tryb przypuszczający „-łbym/-łabym”.
- Przymiotniki o sobie: „jestem gotowy/gotowa”.
- Adresat: „jesteś pewien/pewna”, „zrobiłeś/zrobiłaś”, forma „pan/pani”.
- Mowa o postaci w 3. osobie: „SYN pochłonęła”, „Ripper zabiła”.
