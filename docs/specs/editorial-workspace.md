# Pracownia korekty Not Geese

Status: specyfikacja do prototypu; otwarte szczegóły przed implementacją.
Data: 2026-09-25.
Decyzje: [0003 i indeks 0004–0020](../decisions/0003-editorial-workspace.md),
[ustalenia techniczne 0016](../decisions/0016-workspace-technical-findings.md).
Słownik: [pojęcia](../glossary.md).

## Problem

Korektor ma dziś do dyspozycji pliki JSON z przemieszanymi tekstami. Musi odnajdywać
kontekst i kolejność rozmów, pamiętać co przeczytał, a następnie ręcznie przekazywać
agentowi zmiany. Potrzebuje miejsca do czytania i korekty, dostępnego w przeglądarce,
bez przejmowania przez bazę roli repozytorium tłumaczeń.

## Rozwiązanie

Jedno konto administratora otwiera pracownię na obecnej stronie Not Geese. Lista
gier odpowiada publicznej stronie. Dopiero wejście do gry pobiera jej teksty z main
i rozlicza wynik wcześniejszej pracy. Użytkownik pracuje w grupach i sekwencjach,
akceptuje dobre wpisy, poprawia pozostałe. Akcje stają się lokalnymi szkicami.
Świadomy zapis wysyła je do Supabase. Eksport daje agentowi JSON jednej gry; nie
zmienia danych w pracowni. O zastosowaniu korekty świadczy zgodny tekst na main.

Pierwsza gra: Shotgun Cop Man, 485 wpisów. Prototyp odpowiada na pytanie, który
układ czytania ułatwia korektę i czy różnica między szkicem, zapisem a eksportem jest
zrozumiała. Prototyp nie jest produkcyjnym panelem, nie używa prawdziwego logowania
ani Supabase i nie przedstawia danych lokalnych jako odczytu main.

## Historie użytkownika

1. Jako administrator chcę wejść linkiem z e-maila, żeby nie obsługiwać kolejnego hasła.
2. Chcę widzieć tę samą listę gier co na stronie, bez pobierania wszystkich tekstów.
3. Chcę otworzyć grę i wiedzieć, z którego commita pochodzi pokazany tekst.
4. Chcę zobaczyć czytelny błąd niezgodnego formatu zamiast częściowo wczytanej gry.
5. Chcę pracować w grupach menu, ustawień, samouczka i innych właściwych danej grze.
6. Chcę znaleźć wpis po kluczu, EN lub PL w otwartej grze.
7. Chcę po znalezieniu kwestii zobaczyć ją w otoczeniu rozmowy.
8. Chcę czytać sekwencję w kolejności, widząc mówcę i pewność ustaleń.
9. Chcę wiedzieć, gdy zmiana wpisu obejmie kilka jego wystąpień.
10. Chcę porównać EN i PL oraz móc skupić się na czytaniu polskiego tekstu.
11. Chcę akceptować dobre wpisy bez przepisywania ich.
12. Chcę poprawiać PL bez edycji klucza ani EN.
13. Chcę zaakceptować pozostałe wpisy jednej grupy, zachowując własne szkice.
14. Chcę zobaczyć zakres tej akcji niezależnie od filtra wyszukiwania.
15. Chcę wrócić do szkiców po zamknięciu karty.
16. Chcę wiedzieć, czy szkic jest tylko lokalny, czy zapis został potwierdzony.
17. Chcę widzieć na liście gier, gdzie mam niezapisane szkice, i zapisać je w grze.
18. Chcę porzucić szkic, zachowując ostatni zapisany wynik pracy.
19. Chcę cofnąć akceptację oraz poprawić lub wycofać zapisaną korektę.
20. Chcę odświeżyć grę bez utraty szkiców.
21. Chcę, by korekta obecna już na main stała się zaakceptowana.
22. Chcę zobaczyć różnicę, gdy wcześniej zaakceptowany tekst zmieni się na main.
23. Chcę rozstrzygnąć konflikt, przyjmując main lub zachowując własną korektę.
24. Chcę świadomie zachować albo porzucić szkic oparty na nieaktualnym tekście.
25. ~~Chcę przenieść wpis do innej grupy.~~ Poza pierwszą wersją (0018).
26. Chcę eksportować zapisane korekty jednej gry, dodając komentarz dla agenta.
27. Chcę móc ponowić eksport bez zmiany stanów wpisów.
28. Chcę, by eksport zachował wszystkie spacje, nowe linie i znaczniki.
29. Chcę zobaczyć dziennik swoich akcji i rozliczeń gry.
30. Chcę, by błąd sieci pozostawił szkice i nie udawał udanego zapisu.
31. Chcę, by zapis z drugiej karty nie nadpisał po cichu nowszej pracy.
32. Chcę, by wylogowanie uniemożliwiało dostęp do prywatnego wyniku korekty.
33. Chcę, by agent stosował dokładne brzmienie korekty i wykrywał zmienioną bazę.

## Decyzje wykonawcze

### Odpowiedzialności

- Powłoka strony: logowanie, lista gier z oznaczeniem szkiców, grupy/sekwencje,
  edycja, szkice i eksport.
- Odczyt repo: znane repo i main, ustalenie SHA, pobranie plików tego samego commita.
  Żadnego adresu repo podawanego przez klienta i żadnego zapisu do GitHuba.
- Kontrakt danych: sprawdzenie kształtu review i struktury, unikalności wpisów
  i referencji. To walidacja plików, nie jakości tłumaczenia.
- Rozliczanie: czysta funkcja reguł 0009 używana przez Edge Function.
- Zapis wyniku: pojedyncza transakcja gry wraz z dziennikiem i kontrolą rewizji.
- Szkice: dane lokalne przypisane do konta, gry i identyfikatora wpisu, odrębne od
  zapisanego stanu. Baza nie przechowuje szkiców.
- Eksport: serializacja zapisanych korekt jednej gry, bez mutacji bazy.
- Naniesienie: lokalne narzędzie/agent sprawdzający zgodność z repo i walidatory gry.

Współdzielony TS może zawierać typy, kontrakty i czyste reguły; sekretów i adaptera
GitHuba nie wolno dołączyć do kodu przeglądarki. Nie powielamy rozliczania jako drugiego
autorytetu po stronie klienta.

### Wejście z repo

Review jest listą obiektów z tekstowymi `key`, `english`, `polish`; brak `namespace`
oznacza pusty namespace. Tożsamość to para `(namespace, key)`, bez naiwnego sklejania
ciągów, które mogłoby powodować kolizje. Opcjonalne: `context`, `note`, `max_length`.
Nieznane pola nie wpływają na interfejs. Nie wolno przycinać ani normalizować tekstu.

Struktura definiuje uporządkowane grupy, reguły dopasowania, ręczne przypisania
i sekwencje wystąpień. Ręczne przypisanie wygrywa z regułami; pierwsza pasująca reguła
wygrywa z dalszymi. Reszta trafia do „Do uporządkowania”. Brak struktury daje jedną
grupę w kolejności review. Błędna struktura nie jest traktowana jak brak pliku.
Wystąpienie wskazuje wpis i mówcę z biblii. Kolejność oraz mówcy mają opis źródła
i pewności. Okrzyki `pSpeech` nie tworzą rozmowy tylko dlatego, że mają numery.

### Plik struktury

`translations/structure.yaml`, ustalony 2026-09-25 na Shotgun Cop Manie
(`games/shotgun-cop-man/translations/structure.yaml`). Precyzuje szkic z 0010:

- `format: 1` — obowiązkowy; inna wartość to błąd formatu.
- `groups` — lista `{id, name}` w kolejności wyświetlania. `id` unikalne, niepuste.
- `assign` — lista `{key, namespace?, group}`; ręczne przypisanie pojedynczego wpisu.
  Wpis może mieć najwyżej jedno przypisanie; wskazany wpis i grupa muszą istnieć.
- `rules` — lista `{group, match, namespace?}` sprawdzana po kolei, niezależnie od
  kolejności wyświetlania grup. `match` to wyrażenie regularne na `key`, bez flag,
  zgodne z JavaScriptem i Pythonem (kotwice, klasy, alternatywa, `\d`). Reguła
  obejmuje tylko wpisy o dokładnie tym `namespace` (brak = pusty).
- `sequences` — lista `{id, name, group, order, speakers, lines}`. `order` i `speakers`
  to `{certainty, source}`, gdzie `certainty` ∈ `pewna`, `odtworzona`. `lines` to lista
  `{key, namespace?, speaker?}`; brak `speaker` oznacza mówcę nieustalonego, a podany
  musi być `id` postaci z `bible.yaml`. Wpis sekwencji musi należeć do jej grupy.

Referencje do wpisów zawsze mają osobne pola `key` i `namespace`, nigdy sklejony ciąg.
Nieznane pola są błędem, żeby literówka nie gubiła po cichu przypisania.
Separator płaskiego identyfikatora w `pl.json` dla niepustego namespace pozostaje otwarty.

### Stan zapisany i rozliczanie

Brak wyniku pracy oznacza „do przejrzenia”; nie tworzymy kopii wszystkich wpisów
w Supabase. Zapis akceptacji niesie EN i zaakceptowany PL. Korekta niesie EN oraz
PL przed i po. Wynik pracy ma rewizję; dziennik przechowuje akcje i istotne rozliczenia.
Metadane odwiedzonej gry mogą zapisać SHA i czas odświeżenia bez utrwalania całego review.

| Zapisany stan | Porównanie z aktualnym EN/PL | Wynik |
|---|---|---|
| Brak | Dowolny istniejący wpis | Do przejrzenia |
| Akceptacja | EN i PL zgodne | Zaakceptowany |
| Akceptacja | EN lub PL zmienione | Do przejrzenia, z różnicą |
| Korekta | EN zmienione | Konflikt |
| Korekta | EN zgodne, PL = po | Zaakceptowany |
| Korekta | EN zgodne, PL = przed | Do wdrożenia |
| Korekta | EN zgodne, inne PL | Konflikt |

Wynik pracy, którego wpisu nie ma na main, nie zmienia stanu ani nie znika: gra pokazuje
go na liście „Brak na main” poza grupami, postępem i eksportem; użytkownik usuwa go
ręcznie z wpisem w dzienniku (0017). Powrót klucza rozlicza go według tabeli.

Zmiana EN ma pierwszeństwo przed zgodnością PL — inaczej zaakceptowalibyśmy tekst
na podstawie nieaktualnego źródła, wbrew 0009. Odświeżenie bez zmiany nie dopisuje
fikcyjnych przejść stanu. Konflikt zachowuje bazę, własną korektę i aktualny main.
„Przyjmij main” tworzy szkic akceptacji aktualnego EN/PL. „Zostań przy swoim” tworzy
szkic korekty od aktualnego main. Zapis jest nadal osobną akcją.

### Kontrakty operacji

- Otwarcie/odświeżenie: wejście `game`; wynik commit, wpisy, grupy/sekwencje,
  wynik pracy, rewizja gry, zmiany od poprzedniego stanu. Niepowodzenie pobrania
  albo walidacji nie zmienia bazy. Rozliczenie i dziennik atomowe.
- Zapis gry: wejście game, oczekiwana rewizja, baza EN/PL zmienianych wpisów,
  zestaw akcji i identyfikator żądania. Serwer potwierdza aktualność main i rewizji;
  nie ufa bazie przesłanej z klienta. Nieaktualność daje odpowiedź do rozstrzygnięcia,
  nie ciche nadpisanie. Ponowienie tego samego żądania nie dubluje dziennika.
- Lista gier: publiczna lista plus liczba niezapisanych szkiców z tej przeglądarki.
  Bez zapisu i odrzucania; te akcje są tylko w otwartej grze (0019).
- Usunięcie wyniku pracy bez wpisu na main: wejście game, identyfikator i oczekiwana
  rewizja; jedna transakcja z dziennikiem (0017).
- Dziennik: odczyt jednej gry, chroniony tym samym kontem administratora.
- Eksport: ostatni odświeżony SHA i zapisane korekty. Lokalne szkice są wyraźnie
  wyłączone; okno pozwala wrócić do zapisu. Konflikty nie blokują eksportu: trafiają
  do osobnej listy, nie do korekt (0020).

Otwarcie/zapis sprawdzają administratora po `user_id`. Wyłączona rejestracja. RLS
nie dopuszcza innych kont; samo `authenticated` nie wystarcza. Logowanie e-mailem
zostaje w Supabase Auth, bez ręcznie pisanego mechanizmu sesji. Żadnych kluczy
uprzywilejowanych w publicznym kodzie.

### Szkice i interakcje

Szkic jest nakładką na stan wpisu, nie piątym stanem. Zawiera bazę EN/PL i zapisaną
rewizję. Zmieniona baza oznacza nieaktualny szkic; zapis zablokowany do decyzji
użytkownika. Szkic akceptacji nie może automatycznie zaakceptować nowego brzmienia.
Przy błędzie localStorage pokazujemy brak trwałego zapisu. Dane szkiców oddzielone
według konta i origin; wylogowanie nie ujawnia ich kolejnej sesji innego konta.

„Zaakceptuj na stronie” działa tylko na aktualnie widocznej stronie, z uwzględnieniem
wyszukiwania i filtra, tylko dla wpisów do przejrzenia bez szkiców. Przed akcją widoczna liczba i zakres.
Nie akceptuje wpisów konfliktowych ani korekt do wdrożenia.
Liczba wpisów na stronie: 50, 100 lub 200, zapamiętywana w localStorage (domyślnie 50).
Tryb jednej kwestii pokazuje jeden wpis. „Cofnij wszystko” usuwa tylko niezapisane
zmiany otwartej gry, zachowując wcześniej zapisane akceptacje i korekty.

Kontekst, uwaga z repo i limit długości są informacją. Panel nie ocenia znaczników,
terminologii ani jakości. Nie ma komentarzy do pojedynczych wpisów. Wolny komentarz
jest dopiero przy eksporcie. Sekwencje pokazują kolejność i mówców, a nie graf odnóg.

### Eksport i naniesienie

Wersjonowany JSON: gra, SHA ostatniego odświeżenia, czas, komentarz, lista korekt
`namespace/key/english/before/after`. Bez przeniesień grup (0018). Osobna lista
`conflicts`: `namespace/key`, zapisane `english/before/after` oraz `main_english/main_polish`;
agent jej nie nanosi (0020).
Eksport nie zawiera akceptacji, nie zamraża zapisów, nie oznacza ich jako zastosowane.
Komentarz jest treścią od użytkownika, nie automatyczną instrukcją wykonania kodu.

Agent/narzędzie porównuje EN i PL z aktualnym repo: zgodne EN i `before` pozwalają
nanosić `after`; zgodne EN i już obecne `after` oznaczają pominięcie. Inne brzmienie
lub brak wpisu wymagają rozstrzygnięcia. Przejście JSON → pliki zachowuje tekst bajtowo
w sensie wartości Unicode, w tym CR/LF, końcowych spacji i znaczników.
Oba pliki tłumaczenia muszą pozostać zgodne.
Gry niezgodne z docelowym formatem PL obsługuje agent ręcznie do czasu migracji.

## Testy

Użytkownik potwierdził poniższy podział 2026-09-25. Testy mają sprawdzać obserwowalne
zachowanie na granicach, a nie strukturę komponentów.

1. **API gry i rozliczanie.** Wszystkie wiersze tabeli 0009, pierwszeństwo zmiany EN,
   brak częściowego zapisu przy błędzie repo, powtórzenia żądania, nieaktualna rewizja,
   obcy użytkownik i brak sesji. Czyste reguły na małych przykładach, API z transakcją
   i RLS w izolowanej bazie. Nie mutować produkcji testami.
2. **Przeglądarka.** Na SCM: otwarcie grupy, 485 wpisów, pojedyncza akceptacja/korekta,
   akceptuj pozostałe z aktywnym filtrem i istniejącym szkicem, sekwencja Pedro,
   przetrwanie szkicu po odświeżeniu, porzucenie, rozstrzygnięcie konfliktu i starego
   szkicu, błąd zapisu, dwie karty, oznaczenie szkiców na liście gier, lista
   „Brak na main” i ręczne usunięcie wyniku pracy. Wzór istniejących testów Playwright strony.
3. **Eksport i repo.** JSON bez szkiców i akceptacji, brak mutacji przy eksporcie,
   ponowne naniesienie, rzeczywiste znaczniki/spacje z SCM, zmiana EN
   oraz zgodność review z PL. Testuje się pliki w kopii roboczej fixture,
   nie na rzeczywistej instalacji gry. Kolejne gry dostarczą przypadki namespace.

Produkcja musi także dowieść, że build strony nie zawiera tekstów prywatnych ani
sekretów. Reguły wspólnego modułu mają przejść Deno i bundler Astro. Prototyp jest
sprawdzany ręcznie w przeglądarce; nie tworzymy dla niego produkcyjnego zestawu testów.

## Poza zakresem

Tłumaczenie przez AI, pamięć tłumaczeń, wiele języków/użytkowników, komentarze przy
wpisach, kontrola jakości w panelu, automatyczne commity/push, pełne kopie gier w bazie,
import plików przez użytkownika, zamrażanie eksportów, grafy dialogów, screeny,
przenoszenie wpisów między grupami (0018), zapis wielu gier naraz (0019),
budowanie i instalacja gry przez Edge Functions. Prototyp nie wdraża Supabase.

## Otwarte kwestie

1. Wybrać układ czytania po prototypie; EN/PL, samo PL i wyszukiwanie są do wypróbowania.
2. ~~Usunięte z main wpisy z wynikiem pracy.~~ Rozstrzygnięte w 0017.
3. ~~Atomowość zapisu wielu gier.~~ Nie ma zapisu wielu gier (0019).
4. ~~Konflikty i cofanie przeniesień grup.~~ Przeniesienia poza pierwszą wersją (0018).
5. ~~Eksport przy konfliktach.~~ Pomija je i wypisuje osobno (0020).
6. Ustalić jednoznaczny identyfikator płaskiego PL dla niepustego namespace oraz
   referencje struktury; nie zgadywać separatora.
7. Opcjonalny token odczytu GitHuba przed produkcją. Nie jest wymagany do prototypu.

Powyższe kwestie nie blokują makiety SCM. W makiecie jawnie symulujemy tylko
uzgodnione reguły.
