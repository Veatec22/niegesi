# Turbo Overkill — decyzje tłumaczenia (0.2.0)

Fakty i źródła: `translations/biblia.yaml`. Raport kontrolny: `work/l10n-report.md`.

## Postacie

- **SYN — forma żeńska, nazwa nieodmienna** („bez SYN”, „SYN pochłonęła”).
  Źródła: głos Patricii Summersett (obsada), rosyjska wersja gry „я пришла”,
  kwestie „protect your mother” i „her” u S.A.M.M. Gdzie rządzi rzeczownik
  („wirus SYN”, „program SYN, który…”), zostaje zgoda z rzeczownikiem.
- **Dyrektor (The Exec) — kobieta.** Głos DB Cooper (aktorka), „boss lady” u Ripper.
  Etykieta „Dyrektor” zostaje, bo rzeczownik pasuje do obu płci; kwestie mają
  formy żeńskie albo bezosobowe.
- **Ripper — kobieta, imię nieodmienne** („do Ripper”). Rosyjska wersja daje jej
  formę męską „я убил”, ale gra wprost mówi „bless her heart” — rosyjski uznany za błąd.
- **S.A.M.M. mówi do Johnny'ego „sir” / per pan**, pozostali na „ty”.
- **Kapitan Cynobrowego Frontu i Jazz — mężczyźni** (sierżant mówi do kapitana
  „sir”; S.A.M.M. o Jazzie „he’s been mulched”).

## Terminy

| EN | PL | Dlaczego |
| --- | --- | --- |
| biocore | biordzeń | jeden wyraz, odmiana jak „rdzeń”; „megabiordzeń” |
| augment(ation) | wszczep | utarte w polskim cyberpunku |
| Street Cleaner | czyściciel ulic | dosłownie, bo to ironiczna nazwa zawodu |
| Regulator | Regulator | nazwa formacji, wielką literą |
| Vermilion Front | Cynobrowy Front | nazwa mówiąca; cynober = vermilion |
| chainsaw leg / Chegg | piłonoga | krótkie, zgrabne w UI i w dialogach |
| TitanCell | ogniwo Tytana | czytelne, odmienia się |
| contingency | plan awaryjny / urządzenie | fabularnie to przedmiot, więc „urządzenie” tam, gdzie się go trzyma |
| Stimpack | Stymulant | ujednolicone (było też „Stympak”) |
| Secondary Fire | Strzał dodatkowy | ujednolicone z samouczkiem („dodatkowy tryb strzału”) |
| Superior Maw | Udoskonalony Maw | ujednolicone z samouczkiem (pasek bossa miał „Ulepszony”) |
| Wallrun Boots | Buty ścianołaza | ujednolicone i krótsze |

Nazwy broni (Waster, Boomer, Twincendiary, Telefragger, Instagibber), miejsc
(Paradise, Vector-4, Los Haven) i tytuły utworów zostają po angielsku.

## Okazje wykorzystane

- Gra słów SYN/sin: „Kochacie SYN, co? Dobrze... to macie tu syna skurwysyna!”
- Błąd w oryginale: wpis `coop_prompt_joinroomfailed` ma tekst „Create Room
  Failed”. PL mówi „Nie udało się dołączyć do pokoju”, zgodnie z kluczem.
- Sam finał mówi „system32? Tu odpalę polecenie usuwania” — żart zostawiony
  w wersji zrozumiałej dla polskiego gracza.

## Świadome odstępstwa

- „Hit Markers” ma dwa tłumaczenia: „Dźwięki trafień” (ustawienie dźwięku)
  i „Znaczniki trafień” (krzyżyk w HUD) — opisy ustawień pokazują, że to dwie opcje.
- Licznik amunicji: „Naboje”, infodeks: „Naboje do strzelby”.
- Ręcznie łamane wiersze w czterech nagraniach-rozmowach połączone; pole zawija samo.

## Mniej pewne (sprawdź w grze)

- **Zakładka sklepu „Zdrowie i pancerz”** (EN „Vitals”, 6 znaków) — możliwe ucięcie.
- **Napisy centralne** „Znaleziono czerwony/niebieski klucz!”, „PRZYTRZYMAJ, ABY POMINĄĆ...”.
- **Ustawienia**: „Synchronizacja pionowa”, „Natychmiastowy strzał granatnika”,
  „Przechył przy biegu po ścianie” — długie etykiety w wąskiej kolumnie.
- **Najdłuższe napisy dialogów** — finał epizodu 3 (monolog Dyrektora, kwestie Mawa).

## Raport kontrolny

Pierwszy przebieg: 207 zgłoszeń. Po poprawkach i opisanych wyjątkach zostały
32 zgłoszenia długości (lista wyżej obejmuje najbardziej ryzykowne).
Poprawiono 28 wpisów: 11 niespójności, 4 skrócenia, 2 tytuły [BŁĄD: USZKODZENIE],
10 tytułów utworów w cudzysłowach „”, 1 błąd źródła. Pozostałe zgłoszenia to
opisane wyjątki (formy -łać, wypowiedzi S.A.M.M. do SYN, nazwy własne).
