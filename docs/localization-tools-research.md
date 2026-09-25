# Wizualna korekta lokalizacji — narzędzia i kierunek

Sprawdzone 2026-09-25. Rozpoznanie na oficjalnej dokumentacji; rekomendacje poniżej są oceną dopasowania do Not Geese, a nie wynikami wdrożenia tych narzędzi.

## Jak robią to narzędzia profesjonalne

Profesjonalne środowiska rozdzielają tekst gry od interfejsu tłumacza. Edytor pokazuje oryginał i przekład, kontekst, terminologię i stan pracy. Pamięć tłumaczeń pomaga ponownie wykorzystać wcześniejsze przekłady. Nie trzeba ręcznie redagować składni JSON. Przykładem jest [edytor Crowdin](https://support.crowdin.com/online-editor/), oferujący również komentarze, zatwierdzanie, screeny i wytyczne stylistyczne.

Istotne jest przygotowanie wejścia: [import tabel w memoQ](https://docs.memoq.com/current/en/Workspace/multilingual-excel-and-delimit.html) pozwala wskazać osobne kolumny źródła, tłumaczenia, identyfikatora kontekstu i komentarza. Scena, postać czy sytuacja muszą zatem zostać dostarczone jako dane. Sam fakt użycia profesjonalnego edytora nie odtwarza scenariusza z rozsypanej tabeli.

## Konkretne narzędzia

| Narzędzie | Co wnosi | Dopasowanie do naszego problemu |
|---|---|---|
| Crowdin | Przeglądarkowy edytor, kontekst, screeny, komentarze, terminologia, zatwierdzanie. Funkcja sąsiednich wpisów pokazuje do pięciu wcześniejszych i późniejszych tekstów **w pliku źródłowym**. | Dobry gotowy warsztat korekty. Jeśli plik źródłowy jest rozsypany, sąsiednie wpisy nadal nie oznaczają kolejnych kwestii. |
| memoQ | Środowisko CAT/TMS: bazy terminologiczne, filtry tabel, identyfikatory, ponowny import zmienionego źródła i wykorzystanie istniejących przekładów. | Dobre przy dużym wolumenie i pracy tłumacza. Trzeba przygotować czytelny eksport z kolejnością oraz kontekstem. |
| Weblate | Edytor webowy, integracja z repozytorium i kontekst ekranowy; można uruchomić własną instancję. | Najbardziej naturalny gotowiec, jeśli priorytetem jest korekta w przeglądarce i powrót zmian do Git. Nie daje automatycznie modelu rozmów ze skryptów konkretnej gry. |
| articy:draft X | Środowisko narracyjne z dedykowanym widokiem lokalizacji, strukturą dialogów oraz eksportem/importem Excel. | Najbliższe wzorcowi „czytam rozmowę”. Jednak wykorzystuje istniejący projekt narracyjny; u nas trzeba najpierw odtworzyć strukturę z plików cudzej gry. |

Źródła funkcji: [Crowdin Editor](https://support.crowdin.com/online-editor/), [memoQ dla gier](https://www.memoq.com/solutions/game-localization/), [Weblate — cykl synchronizacji](https://docs.weblate.org/en/latest/admin/continuous.html), [Weblate — kontekst ekranowy](https://docs.weblate.org/en/latest/admin/translating.html), [kod i instalacja Weblate](https://github.com/WeblateOrg/weblate), [articy — widok lokalizacji](https://www.articy.com/help/adx/Localization_View.html), [articy — eksport/import](https://www.articy.com/help/adx/Localization_TextExport.html).

Szczególnie wartościowy wzorzec daje articy: widok lokalizacji może porządkować rozgałęziony dialog w głąb, wszerz lub zaczynając od krótszych odnóg. Przerywana linia oznacza, że następny pokazany element nie jest bezpośrednim sąsiadem poprzedniego. To uczciwe pokazanie nieliniowej historii w liniowym edytorze, bez udawania jednej rozmowy. [Opis sortowania](https://www.articy.com/help/adx/Localization_View.html).

## Gotowiec czy własny panel

**Ocena:** dla Not Geese sensowny jest niewielki lokalny panel korekty oparty na plikach repozytorium. Największą własną pracą i tak będzie wydobycie struktury dialogów, więc gotowy CAT nie usuwa najtrudniejszej części problemu. Panel może zapewnić dokładnie potrzebny sposób czytania i nie wymagać od użytkownika obsługi plików.

Minimum użyteczne:

1. Lista gier, scen i rozmów z postępem korekty.
2. Rozmowa jako scenariusz: postać, EN, edytowalne PL, kolejność i jawne odnogi.
3. Kontekst obok: biblia postaci, terminy, uwagi, screen.
4. Statusy „do korekty”, „sprawdzone”, „pytanie” oraz osobny stan testu w grze.
5. Wyszukiwanie prowadzące do kwestii w rozmowie, zachowujące otoczenie.
6. Zapis aktualizujący kanoniczne tłumaczenie i regenerujący EN/PL; kontrola placeholderów i wykrywanie zmiany pliku przez innego edytora/agenta.

Nie należy mylić wpisu tekstowego z wystąpieniem w scenie: jeden klucz może pojawiać się w kilku rozmowach, a poprawka dotyczy wszystkich jego użyć. Kolejność, postacie i warunki powinny być dodatkowymi metadanymi; nie należy zgadywać ich z podobieństwa zdań. Jeśli struktury nie uda się ustalić, interfejs powinien to jasno pokazać.

Gotowiec warto wybrać, jeśli główną potrzebą stanie się obsługa wielu korektorów, wielu języków, pamięci tłumaczeń i zespołowych uprawnień. Najpierw można sprawdzić Weblate na próbce, porównując wygodę czytania rozmowy z naszym celem. Utrzymanie własnej instancji jest dodatkową pracą; samo dostępne źródło nie oznacza braku kosztu wdrożenia.

Integracje mają też własny model zapisu. [Crowdin z GitHub](https://support.crowdin.com/github-integration/) używa gałęzi usługowej i PR-ów, a [Weblate](https://docs.weblate.org/en/latest/admin/continuous.html) zatwierdza zmiany w swoim repozytorium i może wysyłać je do repozytorium nadrzędnego. To wymaga świadomego dopasowania do naszej pracy bezpośrednio w repo; nie jest po prostu edycją lokalnego pliku w przeglądarce.

Nie porównywano cen ani limitów planów. Nie instalowano produktów, nie podłączano repozytorium do usług i nie wysyłano tekstów gry do zewnętrznych platform.
