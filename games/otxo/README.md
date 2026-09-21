# OTXO po polsku

Pełne spolszczenie OTXO: 1364 wpisy, czyli wszystko, co gra ma do powiedzenia — menu,
ustawienia, samouczek, 102 trunki, dialogi wszystkich postaci z plaży, lore Pisma
Bekatuy, cały dziennik bohatera, nazwy broni i statystyki przebiegu.

Paczka to **jeden plik tekstowy, 72 KB, w całości nasz** — nie ma w niej ani bajta
z gry. Podmieniasz jeden plik i tyle.

## Zanim zainstalujesz

Polski **przejmuje slot chiński**. To nie jest dołożenie ósmego języka: po instalacji
gra nie ma już chińskiego, a pod chińską flagą jest polski. W menu języka flaga
pozostaje chińska — to kosmetyka, nie błąd.

Innego wyjścia nie ma. OTXO to GameMaker skompilowany do kodu natywnego, siedem slotów
językowych to literały w pliku wykonywalnym, a chiński jest jedynym, który dogrywa
czcionkę z dysku — czyli jedynym, który w ogóle umie narysować polskie znaki.
Szczegóły w [technice](docs/technika.md).

## Instalacja

1. Zamknij grę.
2. Zrób kopię pliku `OTXO_script_english_zho-CN.ini` z katalogu gry, gdzieś poza nim.
3. Wypakuj [paczkę ZIP](dist/OTXO-PL-0.1.zip) do katalogu gry i potwierdź zastąpienie.
4. Uruchom grę i w opcjach wybierz język pod **chińską flagą**.

Pełna [instrukcja instalacji i przywrócenia](docs/INSTALL.txt).

## Przywrócenie

Wgraj z powrotem swoją kopię `OTXO_script_english_zho-CN.ini`. Można też zweryfikować
pliki gry w GOG Galaxy albo w Steamie.

## Stan

Sprawdzone w grze: menu, wybór języka i polskie znaki na slocie chińskim.
Pełny przebieg czeka na przejście — do obejrzenia zostaje łamanie dłuższych opisów
trunków i wpisów dziennika oraz ekran statystyk.

Wersja źródłowa: GOG, 1.106.

[Szczegóły techniczne, budowanie i materiały do korekty](docs/technika.md) ·
[Metadane](game.yaml)
