# Supabase trzyma tylko wynik pracy, grę pobiera się przy wejściu

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Supabase nie jest kopią repo. Przechowuje tylko teksty wynikające z pracy użytkownika:
zaakceptowane brzmienia i pary przed/po. Stan gry pobiera się z main dopiero po jej
otwarciu, a lista gier nie pokazuje postępu gier, których użytkownik nie otwierał.

## Rozważone warianty

- **Pełna kopia każdej gry przy odświeżeniu**, dająca postęp wszystkich gier,
  wyszukiwanie w wielu grach i podgląd podobnych kwestii: odrzucona.
  Użytkownik nie potrzebuje stanu gier, do których nie zajrzał.

## Konsekwencje

Podgląd podobnych kwestii z innych gier (pamięć tłumaczeń) wypada. Wyszukiwanie działa
w obrębie otwartej gry.
