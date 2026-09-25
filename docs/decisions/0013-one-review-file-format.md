# Jeden format pliku review dla wszystkich gier

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Pracownia czyta jeden format `en-pl-review.json` i nie ma adapterów dla poszczególnych gier.
Format ustalamy na podstawie obecnych plików. Gry, które go nie spełniają, doprowadzamy
do niego w repo. Wcześniej pracownia pokazuje przy otwarciu takiej gry czytelny błąd,
a nie zgaduje. Stan z 2026-09-25: Dread Templar ma słownik zamiast listy, a Boomerang X
zdublowany wpis `difficulty_select_prompt`.

## Format

Lista obiektów, jeden obiekt na wpis:

```json
{ "key": "pSpeech3", "namespace": "", "english": "…", "polish": "…",
  "context": "skąd tekst: mówca, ekran, komentarz twórcy",
  "note": "uwaga tłumacza dla korektora",
  "max_length": 30 }
```

Obowiązkowe są `key`, `english` i `polish`. Identyfikatorem wpisu jest `namespace` + `key`
i musi być unikalny. `context`, `note` i `max_length` są opcjonalne. Panel pokazuje
`max_length` tylko jako informację („27/30”), bez sprawdzania. Inne pola są dozwolone,
ale panel ich nie czyta. Obecne `notes`/`note` przechodzą w `note`, a `max_char_limit`
w `max_length`.

## Rozważone warianty

- **Adapter Edge Function dla każdego kształtu pliku**: odrzucony. Byłby w kodzie
  na zawsze i trzeba by go dopisywać przy każdej nowej grze.
