# Pracownia korekty w Not Geese

Status: grillowanie zakończone 2026-09-25, bez wdrożenia. Obowiązują decyzje z sekcji
„Decyzje” na końcu; tam, gdzie przeczą treści poniżej, wygrywają one.
Wzór funkcji: [analiza Weblate](../weblate-analysis.md). Decyzje z grillowania
trafiają do kolejnych plików w tym katalogu i są linkowane w sekcji „Decyzje” na końcu.
Data: 2026-09-25.

## Potrzeba i kierunek użytkownika

Prywatny panel w aplikacji Not Geese, którego kod żyje w tym repo. Jeden użytkownik
koryguje pogrupowane teksty gier w przeglądarce. Supabase przechowuje dane i zmiany,
Auth obsługuje logowanie, Edge Functions operacje importu i eksportu.
Panel nie zapisuje do GitHuba. Użytkownik eksportuje poprawki i przekazuje je agentowi
do naniesienia w repo, walidacji i zbudowania paczki.

Repo pozostaje źródłem wersji wydawanych. Supabase jest miejscem pracy redakcyjnej:
przechowuje niezmienną bazę konkretnego importu oraz korekty względem tej bazy.

## Pierwsza gra

Rekomendacja: Shotgun Cop Man, 485 wpisów we wspólnej tabeli klucz → tekst.
Deadbolt (619 wpisów) to kolejny etap: STRG, dialogi JSON oraz napisy na grafikach
wymagają dodatkowej obsługi. Liczby sprawdzone w lokalnych plikach review.
Założenie użytkownika o stanie na main jest scenariuszem działania, nie wynikiem
weryfikacji zgodności obecnego checkoutu z main ani potwierdzeniem statusu gotowe.

Proponowane grupy Shotgun Cop Mana:

- Menu i nawigacja.
- Ustawienia: obraz, dźwięk, sterowanie, dostępność.
- Samouczek i podpowiedzi.
- Rozgrywka: HUD, cele, wyniki.
- Wypowiedzi i dialogi, z osobną grupą dodatku Pedro.
- Edytor poziomów i kampanie społeczności.
- Osiągnięcia, napisy końcowe i pozostałe komunikaty.

Grupy są zależne od gry. Inna gra może mieć notatki, dziennik, przedmioty lub zadania.
Każdy wpis ma podstawową kategorię; może mieć dodatkowe etykiety i wiele wystąpień
w rozmowach. Nieprzypisane wpisy trafiają do jawnej grupy „Do uporządkowania”.
Początkowe przypisanie przygotowuje agent; użytkownik może je zmieniać w panelu.
Klucz tekstu pozostaje stały. Zmiana kategorii nie zmienia identyfikatora gry.

Kategoria nie dowodzi kolejności. Dialogi mają dodatkowo scenę, kolejność/połączenia,
odnogi i źródło tych ustaleń. Niepewną kolejność oznaczamy. Wspólny klucz używany
w kilku scenach ma jedno tłumaczenie i wiele wystąpień; panel pokazuje zasięg poprawki.

## Przepływ

1. Lokalne narzędzie przygotowuje import z wybranego commita repo: EN, aktualne PL,
   klucze, kontekst, grupy, wersję spolszczenia, SHA commita i skróty zawartości plików.
   Import z niezacommitowanych plików musi być opisany jako taki; nie udaje stanu main.
2. Administrator wgrywa plik w panelu. Import jest walidowany i zapisywany atomowo
   jako niezmienna wersja bazowa. Nie wymaga dostępu Supabase do prywatnego GitHuba.
3. Użytkownik czyta grupy/sceny, edytuje PL, dodaje uwagi, zatwierdza kwestie.
   Zapis z widocznym potwierdzeniem serwera; nieudany zapis pozostawia szkic do ponowienia.
   Numer rewizji chroni przed nadpisaniem z drugiej karty przeglądarki.
4. Eksport tworzy niezmienny zestaw wybranych zatwierdzonych poprawek. Późniejsza
   edycja tworzy nową rewizję, nie zmienia treści już pobranego eksportu.
5. Agent otrzymuje JSON poprawek i czytelne zestawienie Markdown. Narzędzie lokalne
   stosuje dokładne poprawki; agent zajmuje się konfliktami, uwagami i przebudową.
6. Po zastosowaniu i uzgodnieniu nowego stanu repo powstaje raport oraz nowy import.
   Panel rozlicza tylko potwierdzone poprawki. Sam eksport nie oznacza zastosowania.
   Budowanie, publikacja paczki i test w grze pozostają osobnymi krokami.

## Eksport i konflikty

Nagłówek: wersja formatu, ID zestawu, gra, bazowy snapshot, commit i skróty plików.
Każda poprawka: klucz, EN przy imporcie, PL przed i po, rewizja korekty, kontekst
i ewentualna uwaga. Uwagi bez konkretnego nowego tekstu są osobną listą zadań,
nie instrukcjami automatycznej podmiany. Zmiany grup eksportowane osobno od tekstów,
aby utrzymać je także w metadanych repo i kolejnych importach.

Reguły stosowania do aktualnego checkoutu:

- EN zgodne i PL równe „przed”: można zastosować „po”.
- EN zgodne i PL już równe „po”: zmiana już obecna, nie stosować ponownie.
- Inne PL, inne EN albo brak klucza: konflikt do jawnego rozstrzygnięcia.

Sprawdzać cały zestaw przed zapisem; domyślnie konflikt zatrzymuje zastosowanie zestawu.
Sama różnica SHA commita nie blokuje, jeśli konkretne wpisy nadal pasują.
Walidować znaczniki i aktualizować zarówno pl.json, jak i en-pl-review.json.
Raport wymienia zastosowane, już obecne i konfliktowe zmiany.

Nowy import nie usuwa nierozliczonych szkiców. Gdy jego tekst odpowiada wyeksportowanej
korekcie, rozliczyć tamtą rewizję; jeśli użytkownik zdążył poprawić ją ponownie,
zachować nowszą zmianę względem nowej bazy. Rozbieżności pokazać do rozstrzygnięcia.

## Miejsce w repo i Supabase

- `site/`: panel `/admin/` w istniejącej aplikacji Astro, dane pobierane po zalogowaniu.
- `supabase/`: konfiguracja, migracje bazy i kod Edge Functions.
- `tools/`: przygotowanie importu, sprawdzanie i nakładanie eksportowanych poprawek.
- `games/<gra>/translations/`: istniejące teksty oraz metadane grup i kolejności.

Supabase Auth: konto jednego administratora. Dostęp do danych ograniczony po stronie
bazy do tego konta przez RLS; każda Edge Function też sprawdza to uprawnienie.
Publiczny frontend dostaje wyłącznie publishable key, nigdy secret/service_role.
Teksty redakcyjne nie trafiają do statycznego publicznego HTML ani bundla danych.

Postgres przechowuje snapshoty, wpisy, grupy/wystąpienia, bieżące korekty, historię
i zestawy eksportowe. To model pojęciowy, nie ustalona liczba tabel.
Atomowe operacje złożone realizują transakcje bazy/RPC; kilka osobnych wywołań
z Edge Function nie daje samo w sobie transakcji.
Edge Functions walidują importy, tworzą eksporty i przyjmują raporty rozliczenia.
Zwykły odczyt i zapis korekty może korzystać z API bazy/RPC z sesją administratora.
Storage można dodać później na prywatne screeny. Realtime nie jest potrzebne na start.

Dokumentacja: [Supabase Auth](https://supabase.com/docs/guides/auth),
[RLS](https://supabase.com/docs/guides/database/postgres/row-level-security),
[klucze API](https://supabase.com/docs/guides/api/api-keys),
[Edge Functions](https://supabase.com/docs/guides/functions).

## Pierwszy zakres do wdrożenia

Jedno konto, Shotgun Cop Man, import pliku, kategorie, lista EN/PL, edycja i historia,
zatwierdzanie, eksport zmian, lokalne stosowanie z kontrolą konfliktów oraz ponowny import.
Warunek powodzenia: poprawka wykonana w panelu trafia dokładnie raz do obu plików
repo, a panel potrafi odróżnić rozliczoną poprawkę od późniejszej edycji.
Graf rozgałęzionych dialogów i pełne zarządzanie wydaniami pozostają kolejnymi etapami.

Nie wybrano ani nie utworzono projektu Supabase, nie wykonano migracji ani deployu.

## Decyzje

- [0004 Pracownia służy do korekty, nie do tłumaczenia](0004-workspace-is-for-review-only.md)
- [0005 Repo przechowuje wydania, Supabase pracę redakcyjną](0005-repo-is-source-of-truth.md)
- [0006 Z Weblate bierzemy pomysły, nie kod](0006-weblate-concepts-not-code.md)
- [0007 Panel pod /admin/ statycznej strony](0007-workspace-under-site-admin.md)
- [0008 Pracownia czyta stan gry prosto z main](0008-workspace-reads-main-from-github.md)
  (zastępuje import pliku z sekcji „Przepływ”)
- [0009 Stan wpisu rozlicza się przez porównanie z main](0009-corrections-settle-against-main.md)
  (zastępuje stany i zamrażane zestawy eksportu z sekcji „Eksport i konflikty”)
- [0010 Grupy i sekwencje są zapisane w repo](0010-groups-and-sequences-live-in-repo.md)
- [0011 Supabase trzyma tylko wynik pracy, grę pobiera się przy wejściu](0011-supabase-holds-only-review-work.md)
  (zastępuje niezmienne wersje bazowe z sekcji „Przepływ”)
- [0012 Rozliczanie stanu gry działa w Edge Function](0012-reconciliation-in-edge-function.md)
- [0013 Jeden format pliku review dla wszystkich gier](0013-one-review-file-format.md)
- [0014 Jedno konto, logowanie linkiem na e-mail](0014-single-admin-email-login.md)
- [0015 Docelowo ujednolicamy też pl.json](0015-unify-pl-json-too.md)
- [0017 Wynik pracy bez wpisu na main czeka na ręczne usunięcie](0017-removed-entries-kept-for-manual-cleanup.md)
- [0018 Pierwsza wersja nie przenosi wpisów między grupami](0018-no-group-moves-in-first-version.md)
- [0019 Szkice zapisuje się i odrzuca tylko w grze](0019-save-inside-game-only.md)
  (zastępuje zapis wszystkich gier z 0009)
- Pierwsza wersja ma grupy i sekwencje (rozmowy po kolei, z mówcą i pewnością
  kolejności), bez grafu odnóg. Graf dojdzie przy Laice.

Ustalenia bez osobnego pliku decyzji:

- Lista gier w pracowni jest taka sama jak publiczna lista na stronie. Nie sprawdza plików
  z góry; błąd formatu pokazuje dopiero po wejściu do gry.
- Pierwsza gra: Shotgun Cop Man (485 wpisów, ma rozmowę z Pedro jako sekwencję).
- Po specyfikacji, przed kodem: klikalny prototyp HTML na danych SCM, do wyrzucenia.

## Stan po specyfikacji i prototypie (2026-09-25)

- [Specyfikacja](../specs/editorial-workspace.md) opiera się na 0004–0015 i słowniku.
- [0016 — sprawdzone fakty techniczne](0016-workspace-technical-findings.md): repo
  publiczne, limity GitHuba, wspólny TS, układ Supabase i osobne szkice według origin.
- Projekt Supabase wybrany: Not Geese (`kulwhymoxgaiqpipwbav`); jedno konto
  administratora uzgodnione w rozmowie. Nie wykonano migracji ani deployu.
- Prototyp: `/admin/prototype/?variant=A` w lokalnym Astro. Trzy układy: A — EN/PL,
  B — czytanie rozmowy, C — jedna kwestia. Szczegóły w
  [instrukcji prototypu](../../site/src/prototype/README.md).
- Prototyp używa prawdziwych lokalnych tekstów SCM; stany i zmiany main są symulowane.
  Grupy są propozycją, nie przyjętym plikiem `structure.yaml`.
- Użytkownik potwierdził trzy obszary testowania zapisane w specyfikacji.

## Następne kroki

1. Użytkownik ocenia warianty i przepływ prototypu. Nie uznawać braku odpowiedzi za wybór.
2. Rozstrzygnąć pozostałe szczegóły ze specyfikacji: eksport przy konfliktach
   i identyfikatory z namespace. Usunięte wpisy, przeniesienia i zapis wielu gier
   rozstrzygnięte 2026-09-25 (0017–0019).
3. ~~Doprowadzić SCM do formatu 0013, przygotować strukturę 0010 i zgodność z 0015.~~
   SCM spełniał już 0013 i 0015; `structure.yaml` dodany 2026-09-25 (485/485 wpisów w grupach).
4. Implementować Supabase, `/admin/` oraz narzędzie nanoszenia eksportu.

## Pozostałe kwestie

- Token GitHuba tylko do odczytu: opcja wdrożeniowa; publiczny odczyt bez tokena
  zachowany zgodnie z 0008. Szczegóły i źródła w 0016.
- Wspólny moduł TS: zgodność potwierdzona dokumentacją; próbę w Deno i bundlerze
  Astro wykonać podczas implementacji. Lokalnie Deno nie było dostępne w PATH.
- Ekran czytania wybieramy po prototypie.
- Graf rozgałęzień wraca dopiero przy Laice.
