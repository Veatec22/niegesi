# Format decyzji

Decyzje leżą w `docs/decisions/`, numerowane kolejno: `NNNN-slug.md` (slug po angielsku,
treść po polsku). Numer: najwyższy istniejący + 1.

Starsze pliki (0001–0003) są dłuższymi dokumentami tematu. Nowe decyzje z grillowania
są krótkie; dokument tematu linkuje do nich w sekcji decyzji.

## Szablon

```md
# <Krótki tytuł decyzji>

Status: przyjęte · Data: RRRR-MM-DD · Temat: [<dokument tematu>](NNNN-....md)

<1–3 zdania: kontekst, co postanowiliśmy i dlaczego.>
```

Tyle wystarczy. Decyzja może być jednym akapitem. Wartość jest w tym, że zapisano
*że* i *dlaczego*, nie w wypełnianiu sekcji.

## Sekcje opcjonalne

Tylko gdy wnoszą coś realnego:

- **Rozważone warianty** — gdy odrzucenie nie jest oczywiste i ktoś za pół roku
  zaproponuje to samo.
- **Konsekwencje** — gdy decyzja ma nieoczywiste skutki dalej.
- **Status** `zastąpione przez NNNN` — gdy decyzję zmieniamy. Starego pliku nie kasujemy.

## Co się kwalifikuje

- Kształt architektury: „Supabase trzyma pracę redakcyjną, repo — wydane wersje”.
- Granice i zakres, także jawne „nie”: „panel nie pisze do GitHuba”.
- Technologie z lock-inem: baza, auth, hosting panelu.
- Świadome odejście od oczywistej drogi: „nie przenosimy kodu Weblate, tylko pojęcia”.
- Ograniczenia niewidoczne w kodzie: licencje, limity Edge Functions.
- Odrzucone warianty, gdy odrzucenie nie jest oczywiste.
