# My Friend Pedro — decyzje tłumaczenia

## Przed verticalem — etap uzupełniany na istniejącym przekładzie

Data: 2026-09-24. Status: **kierunek uzgodniony z użytkownikiem**.

Użytkownik zaakceptował wszystkie trzy rekomendacje („wszystkie twoje wnioski
bardzo fajne”). Wprowadzono w102-18, w410-1 i achN4; achN3 pozostaje bez zmian.
Poprawiono też błąd sensu w102-14. Ustalenia zapisano w `translations/bible.yaml`.
Poniższa próbka zachowuje stan sprzed akceptacji, aby pokazać rozważone warianty;
oznaczenia „propozycja” i „niewdrożona” w cytowanej próbce są historyczne.

Gra ma już pełny przekład 721/721 wpisów i potwierdzony przez użytkownika vertical.
Nie cofamy etapu technicznego. W ramach pilotażu localization-direction uzupełniamy
rozmowę o kierunku, potem osobny reviewer przejrzy cały przekład zgodnie z
localization-review. To nie jest raport z pełnego review.

Źródła: `translations/en-pl-review.json`, `translations/pl.json`,
`translations/REVIEW.md`, `docs/technical.md`, `game.yaml`.
EN/PL i pl.json mają po 721 wpisów i zgodne polskie teksty (sprawdzone 2026-09-24).
Próbka poniżej obejmuje 19 wpisów, dodatkowy przykład błędu opisano osobno.
Warianty nie zostały naniesione do pl.json, EN/PL ani paczki.

## Obowiązujący punkt wyjścia

Status: **decyzja agenta — zachować dotychczasowe ustalenia** z REVIEW.md.
Nie przypisujemy im potwierdzenia przez użytkownika, którego ten dokument nie dowodzi.

- Focus → skupienie; split aim → rozdzielanie celowania. W instrukcji można opisowo
  wyjaśnić celowanie w dwa miejsca naraz, zachowując nazwę mechaniki.
- Pedro, Mitch Rzeźnik, Ofelia; Stare Miasto, Dzielnica Null, Świat Pedra, Kanały,
  Internet. Nie otwieramy ponownie nazw tylko dlatego, że można wymyślić inne.
- Internet Service Protectors → Internetowa Straż Porządkowa (ISP), hejterzy,
  skróty growe i nazwy klawiszy zgodnie z istniejącymi notatkami.
- UI: krótkie, jednoznaczne etykiety i polecenia. Bez dowcipów utrudniających obsługę.
- Zachować znaczniki kolorów, ikony klawiszy, komendy animacji i granice `|`.

## Tematy do rozmowy

### 1. Głos Pedra: lekko i potocznie, bez robienia z niego twardziela

Status: **propozycja**. W próbce Pedro najpierw gani pozostawienie broni (`w101-8`),
a zaraz zachęca do jej podniesienia (`w101-9`). Dowcip wynika z tej sprzeczności,
nie z mocnych przekleństw. Zachować „gamoń”, „świr”, „kurczę” tam, gdzie odpowiadają EN.
Nie zamieniać każdej uprzejmej lub teatralnej kwestii w slang.

Przykład `w102-18`:
- EN: Huh...|Well, I guess you'll just have to kill them all now.
- Obecne PL: Hm...|No cóż, teraz chyba musisz zabić ich wszystkich.
- Rekomendacja: Hm...|No to teraz chyba musisz ich wszystkich pozabijać.
- Wariant zachowawczy: zostawić obecne PL.

Zysk rekomendacji: swobodniejszy rytm i makabryczna rada rzucona od niechcenia.
Koszt: bardziej potoczny czasownik; to propozycja redakcyjna, nie naprawa błędu.
Mitch w wymianie `w102-15`, `w102-19`, `w102-20`, `w102-21` ma pozostać szorstki
w kontrze do podwładnego. Obecne „półgłówku” i „nieroby” nie wymagają mocniejszych słów.

### 2. Suchary: odtworzyć mechanizm po polsku i zachować celową niezręczność

Status: **propozycja**. `w410-1` daje niespoilerowy przykład z dalszego etapu.
Pełne EN/PL i rekomendacja są w próbce poniżej.

Rekomendacja opiera żart na „właściwym torze” oraz „toku/torze myślenia”.
Zysk: oba nawiązania są czytelne po polsku; Pedro nadal objaśnia swój suchar.
Koszt: drugą grę słów tworzymy od nowa i dodajemy autokorektę „tok... tor”,
której nie ma dosłownie w EN. Nie jest to sugestia dodawania dowcipów do zwykłych zdań.
Wariant zachowawczy: zachować obecne „na dobrej drodze do torów” i „myśli po szynach”.

### 3. Nazwy osiągnięć: czytelna zabawa słowem, także z angielskim „combo”

Status: **propozycja**. Oceniaj nazwę razem z opisem osiągnięcia.
`achN3` / `achD3`: „Mumbo Combo” → „Czary-combary” za combo x10 — rekomenduję zostawić.
`achN4` / `achD4`: „Comb-o-ver” → obecnie „Combo na boczek” za combo x20.
Rekomenduję „Combo na zaczes”: wyraźniejsze nawiązanie do fryzury z EN.
Zysk: rozpoznawalny żart mimo utraty identycznej budowy słowa; koszt: nadal celowo
niepoważna nazwa. Wariant spokojniejszy: opisowe „Combo x20”, kosztem żartu.
„Combo na boczek” pozostaje możliwym wariantem, nie jest tu oznaczone jako pewny błąd.

## Próbka EN/PL

Kolejność poniżej służy prezentacji; nie rekonstruuje całej gry przez sortowanie kluczy.
Przypisanie Pedra wynika z autoprezentacji w `w101-6` i ciągłości omawianych wypowiedzi;
rolę Mitcha w scenie wspierają polecenia `Butcher_*`. W JSON pole `context` jest puste,
więc dokładne wyzwalacze i przejścia między blokami wymagają kontekstu gry.
Znak `|` pozostaje granicą segmentów, a tagi w cytatach są dosłowne.


### `mNewGame`

EN:
```text
New Game
```

Obecne PL:
```text
Nowa gra
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `mOptions`

EN:
```text
Options
```

Obecne PL:
```text
Opcje
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `mMusicVol`

EN:
```text
Music Volume
```

Obecne PL:
```text
Głośność muzyki
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `mVSync`

EN:
```text
VSync
```

Obecne PL:
```text
Synchronizacja pionowa
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `pHint3`

EN:
```text
Hold <SHOOT2> to split aim
```

Obecne PL:
```text
Przytrzymaj <SHOOT2>, by rozdzielić celowanie
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w101-2`

EN:
```text
Rise and shine, sleepyhead...
```

Obecne PL:
```text
Pobudka, śpiochu...
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w101-8`

EN:
```text
How irresponsible...|Some nincompoop left their <color=#FFD79C>Pistol</color> just laying around.|Any nutter could come around and cause all sorts of damage...
```

Obecne PL:
```text
Co za brak odpowiedzialności...|Jakiś gamoń zostawił tu <color=#FFD79C>pistolet</color>.|Byle świr mógłby go znaleźć i narobić szkód...
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w101-9`

EN:
```text
Go on. <color=#FFD79C>Pick it up</color>.|It might come in handy.
```

Obecne PL:
```text
Śmiało. <color=#FFD79C>Podnieś go</color>.|Może się przydać.
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w102-15`

EN:
```text
Hey boss.|It's quiet out there tonight...
```

Obecne PL:
```text
Hej, szefie.|Spokojnie dziś na mieście...
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w102-19`

EN:
```text
<shake>DON'T...|Don't interrupt me while I'm working, you simpleton.|[Butcher_Question?Butcher_Idle]Is the shipment ready?
```

Obecne PL:
```text
<shake>NIE...|Nie przerywaj mi, kiedy pracuję, półgłówku.|[Butcher_Question?Butcher_Idle]Towar gotowy?
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w102-20`

EN:
```text
It's almost...
```

Obecne PL:
```text
Już prawie...
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w102-21`

EN:
```text
<shake>[Butcher_Shout?Butcher_Idle]Useless slackers!|[Butcher_Point?Butcher_Idle]I'll show them what happens when they slack off!|Go make yourself useful and prepare whatever sorry sack of meat laying in the basement.
```

Obecne PL:
```text
<shake>[Butcher_Shout?Butcher_Idle]Bezużyteczne nieroby!|[Butcher_Point?Butcher_Idle]Pokażę im, czym się kończy obijanie!|Zrób coś pożytecznego i przygotuj ten żałosny kawał mięsa, który leży w piwnicy.
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w102-18`

EN:
```text
Huh...|Well, I guess you'll just have to kill them all now.
```

Obecne PL:
```text
Hm...|No cóż, teraz chyba musisz zabić ich wszystkich.
```

Rekomendacja — propozycja, niewdrożona:
```text
Hm...|No to teraz chyba musisz ich wszystkich pozabijać.
```


### `w102-2`

EN:
```text
See that? When you <color=#FFD79C>FOCUS</color> it's like time slows down.|And when you <color=#FFD79C>FOCUS</color> you can do flips in the air.|Now you try it.
```

Obecne PL:
```text
Widzisz? Kiedy włączasz <color=#FFD79C>SKUPIENIE</color>, czas jakby zwalnia.|A podczas <color=#FFD79C>SKUPIENIA</color> możesz robić salta w powietrzu.|Teraz twoja kolej.
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `w410-1`

EN:
```text
Look, mines!|That must mean we're on track to find the railway.|Heh... on track... railway.|Sorry, just sharing my train of thoughts.
```

Obecne PL:
```text
Patrz, miny!|Czyli jesteśmy na dobrej drodze do torów.|Heh... droga... tory.|Przepraszam, puściłem myśli po szynach.
```

Rekomendacja — propozycja, niewdrożona:
```text
Patrz, miny!|Chyba jesteśmy na właściwym torze, żeby znaleźć kolej.|Heh... tor... kolej.|Wybacz, taki już mam tok... tor myślenia.
```


### `achN3`

EN:
```text
Mumbo Combo
```

Obecne PL:
```text
Czary-combary
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `achD3`

EN:
```text
Get a 10x combo
```

Obecne PL:
```text
Uzyskaj combo x10
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


### `achN4`

EN:
```text
Comb-o-ver
```

Obecne PL:
```text
Combo na boczek
```

Rekomendacja — propozycja, niewdrożona:
```text
Combo na zaczes
```


### `achD4`

EN:
```text
Get a 20x combo
```

Obecne PL:
```text
Uzyskaj combo x20
```

Rekomendacja: zachować na etapie ustalania kierunku; nie jest to werdykt pełnego review.


## Błąd sensu do poprawienia — poza wyborem stylu

`w102-14`: źródło mówi o osobie, której wygląd nie spodobał się sprawcom; obecne PL
przypisuje tej osobie krzywe spojrzenie na nich. Odwraca to kierunek oceny.
Zalecenie: „Mięso to głównie szczury, gołębie albo ktoś, kto akurat im się nie spodobał”.
To nie wariant do głosowania. Zapisano do integracji i kontroli przy review;
na etapie tej próbki tekstów nie zmieniono.


Pełne EN:
```text
Oh chucks, that's <i><color=#ff9999>Mitch the Butcher</color>!</i>|His meat operation is a front for smuggling unlicensed firearms.|The meat is mainly rats, pigeons or whatever person they didn't like the look of that day.|I guess that explains how we ended up here...
```

Pełne obecne PL:
```text
O kurczę, to <i><color=#ff9999>Mitch Rzeźnik</color>!</i>|Jego mięsny interes to przykrywka dla przemytu nielegalnej broni.|Mięso to głównie szczury, gołębie albo ktoś, kto akurat krzywo na nich spojrzał.|To chyba wyjaśnia, jak tu trafiliśmy...
```


## Następny krok

Kierunek zaakceptowany, biblia zapisana, niezależny reviewer przeczytał 721/721
wpisów i utrzymał początkowe decyzje. [Raport pełnego review](localization-review.md)
zawiera dowody, pokrycie i sprawdzenia. Prowadzący wdrożył dwie pewne poprawki:
`w54-1` — „obwód” zamiast „obiegu”; `w57-4` — usunięcie dopisanych lat rozłąki.
Razem z próbką zmieniono sześć wpisów, zbudowano paczkę 0.3.1 i skopiowano do plików strony.

Otwarte do rozmowy pozostają trzy nowe propozycje: przygotowanie żartu o Mikołaju
i ojcach (`w20-3`), niedopowiedzenie pierwszej sceny (`w101-6`) i siła przekleństw
(`w28-2`, `eAlerted1`). Pełne warianty, rekomendacje i koszty są w raporcie; tych
zmian nie wprowadzono. Pełna kampania oraz nowe teksty 0.3.1 czekają na test w grze.
