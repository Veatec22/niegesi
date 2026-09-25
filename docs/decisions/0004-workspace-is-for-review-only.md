# Pracownia służy do korekty, nie do tłumaczenia

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Tłumaczy agent w repo, zgodnie z biblią i kierunkiem gry. Pracownia to miejsce, w którym
użytkownik przegląda teksty, poprawia je i śledzi swoje zmiany. Nie będzie jego głównym
narzędziem pracy. Dlatego nie budujemy w niej tłumaczenia maszynowego, tłumaczenia przez
LLM ani obsługi wielu języków czy wielu użytkowników. Pamięci tłumaczeń też
nie ma (patrz [0011](0011-supabase-holds-only-review-work.md)).

Panel nie sprawdza też jakości: nie ostrzega o znacznikach, długości ani terminach.
Twardą walidację robi agent przy nanoszeniu korekt, istniejącymi narzędziami repo.

## Rozważone warianty

- **Lekki TMS na wzór Weblate** (tłumaczenie z panelu, podpowiedzi maszynowe) —
  odrzucony. Dublowałby proces w repo, a użytkownik w 99% polega na agencie.
