# Nie gęsi

> *A niechaj narodowie wżdy postronni znają, iż Polacy nie gęsi, iż swój język mają.*
> — Mikołaj Rej, 1562

Nieoficjalne polskie tłumaczenia gier, które polskiej wersji nie dostały. Jedno repozytorium
na wszystkie: teksty, narzędzia budujące i dokumentacja instalacji dla każdego tytułu osobno.

Repozytorium zawiera wyłącznie **teksty tłumaczeń i kod narzędzi**. Nie ma tu plików gier —
żadnych zasobów, bibliotek ani plików wykonywalnych. Gotowe paczki powstają lokalnie, z twojej
własnej, legalnie posiadanej kopii gry.

## Gry

| Gra | Zakres | Wersja | Status |
| --- | --- | --- | --- |
| [Shotgun Cop Man](games/shotgun-cop-man/) | 485 wpisów — menu, sterowanie, samouczek, dialogi, edytor poziomów, osiągnięcia | 0.1 | Polski dodany jako jedenasty język; zweryfikowany strukturalnie, test w grze jeszcze przed nami |
| [Anger Foot](games/anger-foot/) | 1774 z 1776 wpisów — menu, ustawienia, samouczki, dialogi, nazwy poziomów, buty, osiągnięcia, napisy końcowe | 0.1 | Polski wchodzi w pusty slot włoski; przetestowany ekran tytułowy i menu |
| [Dread Templar](games/dread-templar/) | 636 wpisów — menu, ustawienia, sterowanie, samouczek, dialogi, przerywniki, nazwy poziomów i bossów, opisy run | 0.1 | Polski wchodzi w pusty slot `pol` zostawiony przez twórców, plus przycisk w menu i łatka na jedną metodę w kodzie |
| [SPRAWL](games/sprawl/) | 75 z 717 wpisów — na razie menu i HUD, reszta w drodze | 0.1 wip | Unreal bierze język z systemu, więc wystarczy dołożyć plik `pl/Game.locres` |

Szczegóły — jak dana gra trzyma teksty, co dokładnie zostało podmienione i czego nie ruszono —
opisuje README każdej gry. Instrukcja dla gracza leży w `games/<gra>/docs/INSTALL.txt`.

## Układ repozytorium

```
games/<gra>/
  README.md          opis tłumaczenia i sposobu, w jaki gra przechowuje teksty
  docs/INSTALL.txt   instrukcja dla gracza, trafia do paczki jako READ-ME.txt
  tools/build.py     budowanie plików gry z oryginałów (nigdy nie pisze do katalogu gry)
  tools/*.py         narzędzia pomocnicze, np. wyciąganie tekstów z oryginału
  translations/pl.json          polskie teksty, klucz zależny od gry
  translations/en-pl-review.json  angielski oryginał obok tłumaczenia, do korekty
```

Każda gra jest samodzielna. Narzędzia nie współdzielą kodu — formaty plików i sposoby
przechowywania tekstu różnią się na tyle, że wspólna warstwa byłaby tylko kosztem.
Wspólne są: licencja, `requirements.txt` i konwencje opisane w
[docs/dodawanie-gry.md](docs/dodawanie-gry.md).

## Budowanie

Wymagania: Python 3.11 i oryginalne pliki danej gry. Żadne narzędzie nie pisze do katalogu gry
ani jej nie uruchamia. Środowisko zakłada się raz, w katalogu głównym repozytorium:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Potem, dla wybranej gry:

```powershell
.venv\Scripts\python.exe games\shotgun-cop-man\tools\build.py --original "D:\Backup\Shotgun Cop Man_Data\resources.assets"
.venv\Scripts\python.exe games\anger-foot\tools\build.py --game "D:\Backup\Anger Foot_Data"
```

Wynik trafia domyślnie do `games/<gra>/dist/` — katalog nie jest śledzony przez Gita.
Każdy build sprawdza sumę SHA-256 plików wejściowych i odmawia pracy na innej wersji gry
albo na pliku już zmodyfikowanym. Po aktualizacji gry trzeba przeanalizować układ danych
od nowa, samo podbicie sumy kontrolnej nie wystarczy.

## Materiał źródłowy gier

Nazwy gier, ich teksty i postacie należą do ich autorów. Te tłumaczenia są nieoficjalne,
nie są z nikim powiązane ani przez nikogo firmowane. Licencja MIT poniżej obejmuje zawartość
tego repozytorium — polskie teksty, narzędzia i dokumentację.

## Licencja

[MIT](LICENSE).
