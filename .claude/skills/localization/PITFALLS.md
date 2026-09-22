# Pułapki i okazje

Lista kontrolna do przejrzenia przed tłumaczeniem dialogów i przed oddaniem.

## Gramatyka zależna od kontekstu

- **Płeć mówiącego i adresata** — czas przeszły, tryb przypuszczający,
  przymiotniki, „pan/pani”. Źródło: biblia. Gdy gracz ma płeć do wyboru
  albo mówiący jest nieznany, formy bezosobowe: „Udało się”, „Trzeba było”.
- **Odmiana obcych imion.** Męskie na spółgłoskę się odmieniają („Mawa”,
  „z Mawem”); żeńskie na spółgłoskę nie („do Ripper”). Imiona na nieme „y”
  z apostrofem („Johnny'ego”). Skrótowce według biblii (np. nieodmienne „SYN”).
- **Liczby w placeholderach.** 1 zabójstwo, 2–4 zabójstwa, 5–21 zabójstw,
  22–24 zabójstwa. Jeśli gra nie ma form mnogich, przebuduj zdanie:
  „Zabójstwa: {0}”. Nie zostawiaj „{0} zabójstw” przy możliwym 1 lub 2.
- **Imiona i nazwy w placeholderach** — rodzaj i przypadek nieznane; buduj zdanie
  tak, by placeholder stał w mianowniku („Gracz: {name}”).

## UI

- **Wielkie litery:** po polsku tylko pierwszy wyraz i nazwy własne
  („Wyjdź z gry”, nie „Wyjdź Z Gry”). Wyjątek: napisy w całości wersalikami
  w oryginale — zachowaj wersaliki.
- **Tryb:** jedna konwencja na grę — przyciski i polecenia w trybie rozkazującym
  2. osoby („Przytrzymaj”, „Zapisz”) albo bezokoliczniku; nie mieszaj.
- **Długość:** polski bywa o 20–30% dłuższy. Krótkie pola (przyciski, zakładki,
  HUD) skracaj synonimem, nie ucinaj znaczenia. Raport wskaże podejrzane.
- **Terminy platformy i ustawień** zgodne z Microsoft Terminology i polskim
  Steamem (Rozdzielczość, Synchronizacja pionowa, Osiągnięcia).

## Napisy dialogów

- Do 42 znaków w wierszu i najwyżej 2 wiersze, o ile gra sama łamie tekst
  do pola napisów. Krótsze zdania > wierne powtórzenie każdego słowa.
- Tempo mowy: napis nie może być wyraźnie dłuższy od kwestii mówionej.

## Styl i ton

- **Rejestr postaci** z biblii: kto przeklina, kto mówi formalnie, kto patetycznie.
- **Wulgaryzmy** tej samej siły co oryginał — nie łagodź, nie dokładaj.
- **Gry słów:** szukaj polskiego odpowiednika (np. SYN/sin → „syna skurwysyna”).
  Jeśli się nie da, zachowaj efekt w inny sposób i zapisz to przy oddaniu.
- **Nazwy mówiące** (wrogowie, umiejętności) tłumacz, jeśli niosą znaczenie;
  nazwy własne miejsc i marek zostaw. Decyzja trafia do biblii.
- **Nawiązania kulturowe** — zostaw, gdy polski gracz je zna; inaczej adaptuj.

## Typografia i technika

- Cudzysłowy „…”, wewnętrzne ‚…’ lub »…«; myślnik „ – ” albo „ — ” zamiast „ - ”.
- Bez spacji przed ? ! : ; — tak jak po polsku, nie jak po francusku.
- Liczby: spacja tysięcy (932 000), przecinek dziesiętny (1,5).
- Zachowaj tokeny, znaczniki i dosłowne `\n` dokładnie jak w oryginale.
- Nie zostawiaj angielskich resztek poza listą `bez_tlumaczenia`.
