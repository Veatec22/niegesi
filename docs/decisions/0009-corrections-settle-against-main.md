# Stan wpisu rozlicza się przez porównanie z main

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Każdy wpis zaczyna jako *do przejrzenia*, bo całe tłumaczenie zrobił agent. Użytkownik
albo *akceptuje* wpis, albo go przepisuje: wtedy wpis jest *do wdrożenia*. Pracownia
zapisuje zaakceptowany PL albo parę PL przed i po. Przy odświeżeniu gry porównuje je z main:

| Stan w pracowni | Na main | Wynik |
|---|---|---|
| zaakceptowany | ten sam PL i EN | zostaje zaakceptowany |
| zaakceptowany | inny PL albo EN | wraca do przejrzenia, z różnicą |
| do wdrożenia | PL „po” | od razu zaakceptowany |
| do wdrożenia | PL „przed” | zostaje do wdrożenia |
| do wdrożenia | inny PL albo EN | konflikt |

Każda akcja i każde rozliczenie trafia do dziennika gry z datą. Użytkownik może cofnąć
akceptację (wpis wraca do przejrzenia), a korektę do wdrożenia poprawić albo wycofać,
nawet jeśli była już w eksporcie.

Konflikt rozstrzyga użytkownik. Może **przyjąć stan z main** (wpis staje się
zaakceptowany) albo **zostać przy swoim**: korekta liczy się wtedy od nowego stanu main
i jest dalej do wdrożenia.

Akcja w panelu najpierw jest *szkicem*: leży w pamięci przeglądarki, przetrwa zamknięcie
karty i obejmuje wiele gier. Do Supabase trafia po zapisaniu gry (zapis „wszystkich” zastąpiło
[0019](0019-save-inside-game-only.md)).
Szkic można porzucić. Jeśli wpis zmienił się na main od powstania szkicu, szkic jest
*nieaktualny*: użytkownik widzi oba teksty i wybiera, czy go zachować, czy porzucić.
Do tego czasu nie da się go zapisać.

Po ocenie prototypu (2026-09-25) „Zaakceptuj na stronie” zastępuje akceptację całej
grupy: obejmuje wyłącznie widoczną stronę po zastosowaniu wyszukiwania i filtra,
wpisy do przejrzenia bez szkiców. Nie ma akceptacji całej gry naraz.
„Cofnij wszystko” porzuca wyłącznie niezapisane zmiany otwartej gry.

Eksport to plik JSON jednej gry, np. `shotgun-cop-man-korekty-2026-09-28.json`. Zawiera
SHA main z ostatniego odświeżenia, wolny komentarz użytkownika, korekty (identyfikator,
EN, PL przed, PL po); przeniesień w pierwszej wersji nie ma ([0018](0018-no-group-moves-in-first-version.md)). Akceptacji w nim nie ma, bo agent
nic z nimi nie robi. JSON, a nie Markdown, bo spacje na końcu, `
` i znaczniki muszą
dojść bez zmian. Eksport nie zmienia niczego w bazie i niczego nie zamraża. Kolejny eksport może powtórzyć
zmianę jeszcze nienaniesioną, więc przy nanoszeniu agent pomija to, co już jest na main.

## Rozważone warianty

- **Stan „pobrana przez agenta” i zamrażanie zestawu eksportu**: odrzucone.
  O naniesieniu świadczy tylko main.
- **Osobny stan „naniesiona” przed akceptacją**: odrzucone. Zmiana, która dotarła
  na main w brzmieniu użytkownika, jest przez niego zaakceptowana.
- **Uwagi przy pojedynczych wpisach**: odrzucone na start. Jeśli użytkownik nie ma
  lepszego tekstu, zostawia wpis; ogólne uwagi dopisuje do eksportu.
