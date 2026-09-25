# Wynik pracy bez wpisu na main czeka na ręczne usunięcie

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Gdy przy odświeżeniu na main nie ma już wpisu (namespace + key), dla którego pracownia
ma zapisaną akceptację albo korektę, wynik pracy zostaje w bazie bez zmian. Gra pokazuje
go na osobnej liście „Brak na main”, obok zwykłych grup: identyfikator, stan, EN i PL
zapisane w bazie. Lista nie liczy się do postępu gry i nie trafia do eksportu.

Użytkownik usuwa taki wynik pracy ręcznie; usunięcie trafia do dziennika z pełną treścią.
Jeśli klucz wróci na main, wpis rozlicza się normalnie według
[0009](0009-corrections-settle-against-main.md). Zmiana nazwy klucza to dla pracowni
usunięcie i nowy wpis — nie wiążemy ich automatycznie. Szkic oparty na wpisie, którego
nie ma na main, jest nieaktualny i nie da się go zapisać; można go tylko porzucić.

To nie jest piąty stan wpisu: wpisu nie ma, zostaje tylko wynik pracy.

## Rozważone warianty

- **Automatyczne usunięcie przy odświeżeniu, z treścią w dzienniku**: odrzucone.
  Nienaniesiona korekta znikałaby bez decyzji użytkownika.
- **Blokada zapisu i eksportu gry do rozstrzygnięcia każdego takiego wpisu**: odrzucone.
  Jeden usunięty klucz wstrzymywałby pracę nad całą grą.
