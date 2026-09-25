# Słownik Not Geese

Pojęcia używane przy spolszczeniach i w pracowni korekty. Definicje mówią, czym coś jest;
decyzje są w [decisions/](decisions/).

## Teksty gry

**Wpis**:
Jeden tekst gry pod stałym kluczem: angielski oryginał i polskie tłumaczenie.
_Unikaj_: string, linijka, jednostka

**Grupa**:
Część gry, do której wpis należy z punktu widzenia gracza, np. menu, ustawienia, dialogi.
Każdy wpis ma dokładnie jedną grupę.
_Unikaj_: kategoria, etykieta, sekcja

**Sekwencja**:
Uporządkowany ciąg wystąpień wpisów, który gracz widzi po kolei, zwykle rozmowa.
Ma zapisane źródło kolejności i to, czy kolejność jest pewna czy odtworzona.
_Unikaj_: scena (to miejsce w grze, nie ciąg tekstów), konwersacja

**Wystąpienie**:
Miejsce wpisu w sekwencji, z mówcą. Jeden wpis może mieć kilka wystąpień, a jego poprawka
obejmuje wszystkie.

## Korekta

**Pracownia**:
Prywatny panel, w którym użytkownik przegląda i poprawia teksty gier. Nie służy do tłumaczenia.
_Unikaj_: TMS, edytor tłumaczeń

**Stan wpisu**:
Miejsce wpisu w korekcie: do przejrzenia, zaakceptowany, do wdrożenia albo konflikt.
Każda gra zaczyna z wszystkimi wpisami do przejrzenia.
_Unikaj_: status korekty, przejrzany/nieprzejrzany

**Zaakceptowany wpis**:
Wpis, którego brzmienie na main użytkownik uznał za dobre, bo sam je zatwierdził
albo jego korektę naniesiono.

**Korekta**:
Tekst PL, którym użytkownik zastąpił brzmienie z main, zapisany razem z brzmieniem sprzed zmiany.
Wpis z korektą czekającą na main jest do wdrożenia.
_Unikaj_: poprawka (potocznie wolno), edycja, sugestia

**Konflikt**:
Stan wpisu do wdrożenia, gdy main ma PL inny niż przed korektą i po niej albo zmienił się EN.

**Szkic**:
Niezapisana akcja w pracowni (akceptacja albo korekta), trzymana w przeglądarce do zapisania
lub porzucenia.

**Odświeżenie**:
Pobranie stanu otwartej gry z main i rozliczenie z nim stanów wpisów.
_Unikaj_: synchronizacja, import

**Eksport**:
Plik jednej gry ze zmianami do wdrożenia i komentarzem dla agenta. Nie zmienia niczego w pracowni.

**Dziennik**:
Chronologiczny zapis akcji użytkownika i rozliczeń w jednej grze.
_Unikaj_: log, historia zmian
