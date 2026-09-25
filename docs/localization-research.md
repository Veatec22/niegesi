# Research: redakcja i ocena lokalizacji gier

Stan sprawdzenia: 2026-09-24. Pytanie: jak uzupełnić proces vertical → pełne tłumaczenie o niezależną redakcję oraz naukę na istniejących lokalizacjach. Poniżej rozdzielono ustalenia ze źródeł od propozycji dla Not Geese. Nie instalowano zewnętrznych narzędzi.

Po decyzji użytkownika wdrożono kierunek **przed verticalem** i osobnego reviewera
całego fulla. Obowiązujący zakres opisuje [decyzja procesowa](decisions/0002-localization-review.md),
a wnioski do bieżącej pracy zawiera [EDITORIAL.md](../.claude/skills/localization/EDITORIAL.md).
Poniższy research pozostaje uzasadnieniem; nie trzeba powtarzać go przy każdej grze.

## Co potwierdzają źródła

1. **Redakcja tekstu i LQA są osobnymi etapami.** IGDA opisuje LQA jako sprawdzanie tekstu w kontekście uruchomionej gry, po tłumaczeniu, redakcji i korekcie. Zaleca listę identyfikatorów, tekst źródłowy i docelowy, informację, gdzie wywołać tekst, oraz ponowny test poprawek. To uzasadnia osobnego reviewera przed przekazaniem paczki graczowi; nie zastępuje testu w grze. [Jennifer O’Donnell i współautorzy, IGDA: How to Get the Most from LQA](https://igda.org/news-archive/how-to-get-the-most-from-lqa-what-it-is-and-best-practices/).

2. **Głos postaci to dobór słów, rytm, rejestr i relacje, a nie samo naśladowanie akcentu.** Jennifer O’Donnell proponuje poznanie postaci, prowadzenie ich charakterystyk i powrót do wcześniejszych scen po wypracowaniu głosu. Stylizacja musi zachować sens i zamiar wypowiedzi; nadmiar maniery również szkodzi. Materiał dotyczy głównie JP→EN, więc przenosimy metodę, nie gotowe angielskie rozwiązania. [Translating Character Voice](https://j-entranslations.com/translating-character-voice/).

3. **Profesjonalny editor sprawdza więcej niż poprawność gramatyczną.** Anne Lee opisuje weryfikację znaczenia, płynność, spójność terminów oraz to, czy bohater przez całą grę brzmi jak ta sama osoba. To bezpośrednia relacja praktyczki, nie dowód skuteczności review LLM. [Anne Lee — Game Translator and Editor](https://j-entranslations.com/anne-lee-game-translator-and-editor-interviews-with-localizers/).

4. **MQM daje słownik kategorii błędów, nie przepis na dobry dialog.** Aktualna typologia rozróżnia m.in. znaczenie, terminologię, konwencje językowe, styl i prezentację/znaczniki. Dla projektu wystarczy mały podzbiór; nie potrzeba udawać certyfikowanego audytu ani wytwarzać arbitralnego wyniku „97% jakości”. [MQM Council — Error Typology](https://new.themqm.org/mqm-pillars/typology/).

5. **Istnieją fachowe przewodniki procesu i polskie wytyczne UI.** IGDA udostępnia 36-stronicowy przewodnik, ponownie opublikowany w 2021 r.; jest starszą bazą organizacyjną, nie aktualnym podręcznikiem LLM. Microsoft udostępnia przewodniki lokalizacji, w tym polski — przydatne dla interfejsu i konwencji, nie jako domyślny styl dialogów. [IGDA — Best Practices for Game Localization](https://igda.org/resources-archive/best-practices-for-game-localization/), [Microsoft Localization Style Guides](https://learn.microsoft.com/en-us/globalization/reference/microsoft-style-guides).

6. **Dostępne są materiały do ćwiczeń i porównań.** LocJAM publikuje gry przygotowane do tłumaczenia oraz zbiory zgłoszeń, umożliwiając porównanie różnych decyzji na tym samym materiale. Repozytorium Wesnoth zawiera polskie PO z parami `msgid`/`msgstr` i odnośnikami do kontekstu. Oba są wartościowymi materiałami warsztatowymi; udział w jamie lub obecność w projekcie open source nie oznacza automatycznie poziomu profesjonalnego. Publiczny dostęp sam nie oznacza dowolnej licencji na dalszą publikację. [LocJAM](https://locjam.itch.io/), [Wesnoth — polskie PO](https://github.com/wesnoth/wesnoth/blob/master/po/wesnoth/pl.po).

## Znalezione agent skills — ocena ograniczona do odczytanych źródeł

- [xueyang-dev/localize-anything](https://github.com/xueyang-dev/localize-anything/blob/main/skills/localize-anything/SKILL.md): interesujące rozdzielenie mechanicznego sprawdzenia, review w świeżym kontekście i decyzji człowieka; pamięć projektu i kontrola aktualności artefaktów. To ogólna lokalizacja produktów, nie wyspecjalizowany redaktor polskich dialogów. Nie uruchamiałem narzędzia ani nie potwierdzam jego jakości na korpusie EN→PL. Warto zapożyczyć pomysły; nie ma podstaw do zastępowania nim działających narzędzi repo.
- [tokyboop/game-localization-skill](https://github.com/tokyboop/game-localization-skill): nazwa i opis pasują do zadania, ale [scripts/translate.py](https://github.com/tokyboop/game-localization-skill/blob/main/scripts/translate.py) zawiera TODO zamiast rzeczywistej translacji; wywołania tłumaczenia, QA i zapisu są zakomentowane, mimo komunikatu końcowego o sukcesie. Traktować jako szkic instrukcji, nie gotowy workflow.
- W tej kwerendzie nie znalazłem zweryfikowanego, profesjonalnego skilla do redakcji lokalizacji gier EN→PL. Nie jest to twierdzenie, że taki nigdzie nie istnieje. Silniejsze źródła dla własnego skilla to praktyka redakcyjna powyżej.

## Rekomendacja dla Not Geese — własna synteza

Zachować bramkę techniczną verticala, a przed pełną lokalizacją dodać małą kalibrację stylu: reprezentatywną scenę, głosy najważniejszych postaci i kilka zaakceptowanych przykładów. Nie trzeba rozbudowywać orkiestracji.

Po tłumaczeniu wprowadzić świeży kontekst reviewera z biblią gry, EN/PL, identyfikatorami i sąsiednimi kwestiami. Rozdzielić dwa przebiegi:

1. **Weryfikacja:** sens, pominięcia, negacje, warunki instrukcji, rodzaj, rozmówca i adresat, terminologia, placeholdery. Jednoznaczne poprawki z uzasadnieniem można nanosić samodzielnie, potem sprawdzić spójność plików i build.
2. **Redakcja:** najpierw przeczytać całe sceny po polsku, potem sprawdzić propozycje względem EN. Wybrać kilka najważniejszych miejsc do rozmowy: obecny tekst, proponowane brzmienie, funkcja sceny, korzyść i ewentualna strata. Nie przepisywać wszystkiego tylko dlatego, że da się napisać inaczej. Celowo sztywny bohater ma pozostać sztywny.

Każde znalezisko powinno rozróżniać **błąd**, **propozycję stylistyczną** i **brak kontekstu**. Sama wysoka pewność LLM nie jest dowodem. Reviewer ma wskazać przesłankę w źródle, biblii albo scenie. Osobny kontekst ogranicza przywiązanie do pierwszej wersji; nie gwarantuje niezależności błędów modelu.

Po uzgodnionej redakcji wystarczy kontrola zmienionych kwestii i zależnych terminów; ciągłe pełne przepisywanie przez kolejnych agentów grozi dryfem stylu. LQA pozostaje testem użytkownika w grze, z konkretną listą miejsc i ponowną kontrolą poprawek.

## Jak uczyć się z istniejących polskich lokalizacji

Zbudować małą bibliotekę **przypadków i technik**, zamiast wrzucać całe cudze tłumaczenie jako wzór. Dla jednego przypadku zapisać: grę i wersję, źródło/autorów lokalizacji jeśli znani, scenę, krótki fragment EN/PL lub odsyłacz, problem translatorski, technikę, efekt i granice zastosowania. Przykładowe etykiety: skrócenie UI, puenta, przekleństwo, różnica statusu, odmiana nazwy, stylizacja, celowa niezręczność.

Najlepsze ćwiczenie: samodzielnie przetłumaczyć scenę przed obejrzeniem oficjalnego PL, porównać decyzje, a na koniec zapisać zasadę własnymi słowami. Oceniać całą wymianę, nie pojedynczy efektowny cytat. Dopasowywać źródła do gatunku i tonu aktualnej gry; nie kopiować rozpoznawalnych powiedzonek ani głosu obcej postaci.

Przy technicznym parowaniu zasobów używać stabilnego ID, tej samej wersji i sceny; sam identyczny angielski string nie zapewnia wspólnego kontekstu. W przypadku gier pierwotnie pisanych po polsku porównanie EN/PL nie dowodzi kierunku EN→PL. Materiał open source i konkursowy oznaczać oddzielnie od oficjalnych płatnych lokalizacji. Dalsza publikacja korpusu wymaga osobnego sprawdzenia licencji; do bieżącego procesu wystarczą odsyłacze i własne obserwacje.

Nie badano tu skuteczności poszczególnych modeli, całych korpusów tłumaczeń ani jakości narzędzi przez uruchomienie. Następny praktyczny krok: pilotaż review na jednej ukończonej grze, z oceną liczby trafnych poprawek, nietrafionych zmian i propozycji przyjętych przez użytkownika.
