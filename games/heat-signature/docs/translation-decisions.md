# Heat Signature — decyzje tłumaczeniowe

## Przed verticalem — 2026-09-25

Próbka z lokalnego EXE i plików Dialog. Pełne EN i kontekst poniżej.
Kierunek dialogów i terminala przedstawiono użytkownikowi. Użytkownik wybrał
wygładzenie terminala: „wygładź mimo wszystko”. Zapisane niżej pierwotne
propozycje pozostają jako historia; obowiązuje rozstrzygnięcie na końcu dokumentu.

### Humor — propozycja

Scena `Dialog/FiascoMeetPlayer.txt`, blok Start, Fiasco → gracz, odpowiedź gracza:

| EN | Proponowane PL |
| --- | --- |
| Hey. You need something? | Hej. Potrzebujesz czegoś? |
| No, I'm just practicing my awkward hovering. | Nie, tylko ćwiczę niezręczne stanie obok. |
| Probably. Send me the details, I'll put some feelers out. | Pewnie. Podeślij szczegóły, porozpytuję tu i tam. |

Suchy dowcip, bez dopisywania memów i bez sztucznego podkręcania dosadności.
Kolejność: pierwsze dwa wpisy to pytanie i odpowiedź; trzeci jest osobną gałęzią
EngageFiasco, nie odpowiedzią na żart.

### Terminal — propozycja

`Dialog/PracticeTerminal.txt`, Start → EasyShip/HardShip:

| EN | Proponowane PL |
| --- | --- |
| PRACTICE TERMINAL LET YOU VIOLENCE ON UNREAL HUMAN IN MAGIC REALITY | TERMINAL TRENINGOWY POZWALA CI ROBIĆ PRZEMOC NA NIEPRAWDZIWYM CZŁOWIEKU W MAGICZNEJ RZECZYWISTOŚCI |
| TRY OUT YOUR STUFFS IN PRACTICE! HAVE THEM BACK AFTER! | WYPRÓBUJ SWOJE RZECZY NA TRENINGU! POTEM MIEJ JE Z POWROTEM! |
| NO DEATH IS REAL IN MAGIC REALITY. R TO RESTART | ŻADNA ŚMIERĆ NIE JEST PRAWDZIWA W MAGICZNEJ RZECZYWISTOŚCI. R ZACZYNA OD NOWA |
| PRACTICE IS START | TRENING SIĘ ZACZĄĆ |

Alternatywa: poprawne zdania „Terminal pozwala ćwiczyć walkę w wirtualnej
rzeczywistości”, „Trening rozpoczęty”. Zmienia charakter mówiącego, dlatego
przedstawiono jako istotny wybór. Rekomendacja: zachować nieporadny automat.

### UI i instrukcje — decyzja agenta

Kluczem tych literałów jest pełny EN z EXE; krótkie, bezpośrednie instrukcje.

| EN | PL |
| --- | --- |
| Resume | Wznów |
| Options | Ustawienia |
| Restart tutorial | Zacznij samouczek od nowa |
| Sound Volume:  | Głośność dźwięków:  |
| Windowed mode: on | Tryb okienkowy: wł. |
| (Hold) Thrust | (Przytrzymaj) Ciąg |
| Pause now | Teraz włącz pauzę |
| You need this keycard | Potrzebujesz tej karty dostępu |
| Wrench | Klucz francuski |

Spacje na końcach fragmentów zachowujemy w pliku tłumaczenia. Pod towarzyszącymi
instrukcji ikonami przycisków nie dopisujemy na sztywno klawiszy. „Wrench” jest
narzędziem do walki; „keycard” kartą dostępu, bez mylącego wspólnego „klucz”.
Nazwy Fiasco i Breaker pozostają na etapie próbki w oryginale.

## Rozstrzygnięcie przed buildem 0.1.0

**Uzgodnione z użytkownikiem:** terminal pisze gramatycznie poprawnie. Odrzucono
„TRENING SIĘ ZACZĄĆ” i „ROBIĆ PRZEMOC”. Wersja przyjęta: „TRENING ROZPOCZĘTY”,
„TERMINAL TRENINGOWY POZWALA ĆWICZYĆ WALKĘ Z WIRTUALNYMI LUDŹMI W MAGICZNEJ
RZECZYWISTOŚCI”. Pozostają wersaliki, przesadny entuzjazm i żart z magiczną
rzeczywistością. Nie przywracać błędów składniowych podczas review.

**Decyzja agenta:** pozostałe rozmowy zachowują suchy humor i siłę przekleństw.
Przykłady z początku: „Nie tak wyobrażałem sobie emeryturę”, „Ale za dużo już w to
włożyłem”, „Teraz wyskoczę w kosmos. Jeśli nie zginę, widzimy się w barze”.
Wybór użytkownika dotyczył wygładzenia terminala, nie cenzury dialogów.

**Decyzja agenta:** Facebreaker → Gębołamacz (nazwa kinetycznej broni Fiasco),
Breacher pozostaje nazwą kapsuły. W pierwszej narracji stacja jest zmienną nazwą:
„<nazwa> — ta stacja już cztery razy zmieniała właściciela w tym roku”, żeby uniknąć
zgadywania rodzaju nazwy. Zachowano granice dynamicznych fragmentów.

Próbka ma 163 wpisy EN/PL: 113 natywnych napisów i 50 kwestii/odpowiedzi z plików
dialogowych. Zawiera początkową narrację, tutorial, menu i ustawienia, rozmowę po
tutorialu oraz terminal treningowy. To nie jest pełna lokalizacja.

Raport kontrolny: trzy ostrzeżenia długości instrukcji/przycisku emerytury pozostają
do oceny w grze; ostrzeżenie wielkich liter dla Gębołamacza jest fałszywym alarmem
(nazwa broni). Brak zgłoszeń uszkodzonych znaczników i niespójnej terminologii.

## Poprawka techniczna 0.1.1

Po zgłoszeniu znikających napisów zastąpiono wadliwie ładowany Arial paskami
glifów z otwartego Xolonium. Powód: font_add zwracał identyfikatory pustych fontów,
a jego zakres kończy się na 255. Dowody i test zabezpieczenia opisuje technical.md.
Treści 163 wpisów, terminologii i decyzji o wygładzeniu terminala nie zmieniano.
Do oceny w grze pozostają widoczność, polskie znaki, odstępy oraz wysokość wierszy.

## Pełne tłumaczenie 0.2.0 — 2026-09-25

Zakres: 2650 wpisów `pl.json` (literały EXE przypisane do funkcji GML, 523 linie
dialogów, szablony dla zdań składanych przez grę) oraz słownik nazw przedmiotów
`items.json` (24 rzeczowniki z rodzajem, 25 przymiotników, 5 określeń końcowych).
Partie źródłowe: `translations/parts/*.json`; szablony misji osobistych generuje
`tools/gen_personal.py`. Logi diagnostyczne gry (ok. 2 tys. literałów) pominięto.

**Poprawka faktu (źródło: dialog).** Fiasco jest kobietą: Breaker mówi o niej „she”
i „this white haired woman” (BartenderDialogueFoundry.txt). Vertical przyjął formy
męskie jako decyzję bez źródła. Poprawiono: „wyobrażałam”, „włożyłam”, „Dostałam
dziesięć kulek”, „Rozniosłabyś”, „Tym razem jedna”. Asli Sixty też jest kobietą
(„She knew that when she pressed the button”).

**Decyzja agenta — płeć.** Breaker, Geneva i Mirfak nie mają płci w plikach gry
(streszczenie TV Tropes niedostępne do weryfikacji), gracz jest postacią losową.
Ich kwestie są neutralne: czas teraźniejszy i konstrukcje bezosobowe
(„Czemu cię tam już nie ma?” zamiast „Czemu odszedłeś?”, „Ja stoję za barem”
zamiast „Zostałem barmanem”, „Kieruję ochroną” zamiast „Jestem szefem”).
Cechy postaci jako rzeczowniki bez rodzaju: Słabość, Technofobia, Duma, Kruchość,
Szczęście, Wytrzymałość, Majątek.

**Decyzja agenta — nazwy przedmiotów.** Gra składa „[określenia] Rzeczownik”.
Po polsku rzeczownik pierwszy, przymiotniki za nim w odwróconej kolejności,
zgodne w rodzaju, a „o dużej pojemności”, „dalekiego zasięgu” na końcu:
„Rechargeable High Capacity Swapper” → „Zamieniacz ładowalny o dużej pojemności”.
Przy ucięciu „...” zostaje najważniejsze słowo. Odrzucono przymiotniki przed
rzeczownikiem (mniej czytelne i gubią rzeczownik przy ucięciu).

**Decyzja agenta — terminy.** Swapper → Zamieniacz, Visitor → Wizytator,
Sidewinder → Omijacz, Slipstream → Poślizg, Crashbeam → Zawieszacz,
Subverter → Przeprogramator, Key Cloner → Kopiarka kart, crash → zawiesić,
Glory → chwała, clause → klauzula, vow → przysięga, Defector → dezerter,
Contractor → najemnik, Drift → Dryf, Voidmother → Matka Pustki. Frakcje, kapsuły
specjalne (Offworld Angel, Sovereign Coldfire, Glitchers Tick, Foundry Brick)
i imiona zostają w oryginale; Sovereign/Foundry/Offworld traktujemy jak rodzaj
nijaki („Sovereign zjawiło się”), Glitchers jak liczbę mnogą.

**Decyzja agenta — etykiety cech.** Etykiety cech broni to rzeczowniki lub
krótkie frazy: Tłumik, Cichy strzał, Szybki ogień, Przebija pancerz, Ogłuszanie,
Zapalnik czasowy. Te same słowa w nazwie przedmiotu są przymiotnikami
(„Pistolet wytłumiony”). Raport pokazuje to jako „różne PL” — zamierzone.

**Decyzja agenta — liczby.** Zdania z liczbą z luki buduje się bez odmiany:
„Liczba użyć: 3.”, „Zabójstwa: 12”, „Wystrzeliwuje salwę granatów, 3 naraz.”.
„Zabij 3 oficerów Glitchers” jest poprawne dla każdej liczby od 2.

**Decyzja agenta — misje osobiste.** Każda relacja (brat, siostra, mama…) ma
własne szablony z odpowiednim przypadkiem i rodzajem: „Uratuj moją mamę z rąk
Glitchers”, „Uratuj mojego durnego brata, który dał się złapać…”. „Partner”
→ „moja druga połówka” (neutralne znaczeniowo). Adaptacja Foundry: „Better.” →
„Bywało lepiej.”, żeby zachować żart Breaker o dwóch znaczeniach.

**Technika dialogów.** Pliki `Dialog/*.txt` są tłumaczone w chwili wczytania
(kopia w `notgeese/cache`), więc stopniowo wypisywany tekst jest polski.
Odpowiedzi w nawiasach kwadratowych ([Continue], [Something else]) zostają
w pliku bez zmian i tłumaczy je dopiero wyświetlanie — gra może je rozpoznawać.

## Rozstrzygnięcia użytkownika po przeglądzie — 2026-09-25

Przedstawiono 6 tematów z niezależnego przeglądu (`docs/localization-review.md`).
Użytkownik przyjął wszystkie rekomendacje, z jedną zmianą kierunku:

| Temat | Było | Jest (użytkownik) |
| --- | --- | --- |
| Odpowiedź gracza „Yep.” | No. / Aha. No. | No tak. / Aha. No tak.; u Mirfaka „No jasne.” |
| „Holy shit you're alive.” (Breaker) | O kurwa, żyjesz. | Jasna cholera, żyjesz. |
| „Yeah, you stole a station!” | No właśnie, stacja ukradziona! | No właśnie, ukradliście stację! |
| Ocena misji PACIFIST, cecha Liberator | PACYFISTA, Wyzwoliciel | PACYFIZM, Wyzwolenie (dostępne) |
| Shiplocked w nazwie / etykieta | przypisany do statku | pokładowy/-a/-e; „Sprzęt pokładowy” |
| missions board / jobs board / listings | tablica misji i zleceń wymieszane | wszędzie „tablica zleceń”, „Oferty zleceń” — **użytkownik wybrał zlecenia**, odrzucając rekomendację recenzenta („tablica misji”) |

Odrzucone warianty (nie proponować ponownie bez nowych przesłanek): „No.” jako
„tak”, „O kurwa”, „stacja ukradziona”, „przypisany do statku”, ujednolicenie na
„tablicę misji”. Źródło w biblii: `uzytkownik`.
