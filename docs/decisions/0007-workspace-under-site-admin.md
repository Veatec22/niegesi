# Panel pod /admin/ statycznej strony

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Panel jest stroną w obecnej aplikacji Astro na GitHub Pages. Przy buildzie powstaje sama
powłoka strony, a teksty przychodzą z Supabase dopiero po zalogowaniu. Dostęp chronią
Supabase Auth i RLS, nie ukrycie adresu. Dzięki temu jest jedna domena i jeden deploy,
a do statycznego HTML nie trafia żaden tekst redakcyjny.

## Rozważone warianty

- **Osobna aplikacja z własnym hostingiem**: odrzucona na start. Wymagałaby drugiego
  deployu, a daje tylko czystszy podział kodu.
- **Wyłącznie lokalnie**: odrzucone. Użytkownik chce otwierać pracownię jak aplikację
  pod adresem strony.
