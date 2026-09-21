# Skate Story — rozpoznanie, 2026-09-20

## Werdykt

TAK, dobry kandydat. Trudność średnia, większy zakres niż Pedro/SPRAWL.
Osobny polski slot już istnieje, lecz jest wyłączony i niemal pusty.
Największy punkt ryzyka: fonty/TMP i zachowanie autorskiej typografii.
Nie uruchamiano gry, nie zmieniano instalacji, nie budowano jeszcze verticala.

## Internet

Nie znaleziono dostępnego spolszczenia. Oficjalny [Steam](https://store.steampowered.com/app/1263240/Skate_Story/?l=polish)
oznacza polski jako nieobsługiwany. Polski opis sklepu i tytuły gameplayów PL
nie stanowią dowodu tłumaczenia gry. [Strona autora](https://skatestory.com/).
Nie znaleziono użytecznej publikacji fanowskiego tłumaczenia ani instrukcji
technicznej po wyszukaniu tytułu ze spolszczenie, translation mod/fan,
Türkçe yama i українізатор. Brak wyniku nie dowodzi nieistnienia projektu.

## Lokalna instalacja

`C:/Games/Skate Story/SkateStory_Data`, wydanie GOG.
Unity 6000.0.45f1, Mono, I2-Localization.dll, Assembly-CSharp.dll.
resources.assets SHA-256:
`3e65be29272f5879bd907a0d0c7f8134f5b5bd35902263dc65381bb0c3a7a82c`.
StreamingAssets/aa zawiera catalog.bin i 5651 bundli Addressables, ale główną
tabelę językową znaleziono bezpośrednio w resources.assets.

MonoBehaviour path ID 785, I2Languages: 2314 rekordów, w tym 2305 tekstowych
oraz 9 referencji fontów (3 typu Font i 6 TMP Font). Kolumna angielska tekstów
ma 113244 znaki; brak pustych angielskich rekordów tekstowych.
Parser terminów z Shotgun Cop Man odczytuje tabelę; parser końcówki trzeba
zmienić, bo OnMissingTranslation ma inną wartość i jest 20 kolumn.
Nie wykonano jeszcze pełnego testu zapisu zmodyfikowanego zasobu.

Kategorie: dialogi ch1–ch10, UI (236), Item (253), Achievement (54), Levels (44),
Speaker (37), tut (25), boss (24), quests (18) i inne. Liczby oznaczają rekordy,
a nie gwarancję pokrycia wszystkich tekstów zaszytych poza tabelą lub grafik.

## Języki i selektor

20 kolumn: 11 aktywnych języków, wyłączone języki oraz kolumny techniczne
TYPE, NOTES, TIMESTAMP, guid, English (Last Translated).
Polish/pl jest na indeksie 15, flaga 1 (wyłączony); 3 niepuste wartości:
UI/language = Polski oraz dwa elementy ostrzeżenia zdrowotnego.
Pozostałe 2302 rekordy tekstowe PL są puste, podobnie wszystkie 9 referencji fontów.
To nie jest pełne ukryte spolszczenie.

Analiza IL SettingsMenu.BuildLanguageMenu: GetAllLanguages, GetAllLanguagesCode,
pominięcie kodów rozpoczynających się od meta, IsLanguageEnabled,
GetTranslation(UI/language), CreateButton, SetOverrideLang.
LocMan udostępnia SetLanguageByCode, SetLanguageByIndex, NextLanguage itd.
Mocna przesłanka: wystarczy włączyć istniejący slot, uzupełnić teksty i fonty.
Zapis wyboru i inne ścieżki zmiany języka nie zostały sprawdzone w grze.

## Fonty

Wbudowany HelveticaRounded-Bold i pokrewne warianty mają tylko 4 z 18 polskich
małych/wielkich liter w sprawdzonym cmap formatu 4. Nie nadają się bez zmian
jako pewny komplet dla PL. W grze istnieją fonty z kompletem 18 znaków:
ru-serif-bigcaslon Regular/Italic, IMFellDoublePica-Regular/Italic,
Inconsolata-SemiBold, LiberationSans i inne.
Należy sprawdzić atlas SDF, fallbacki, faktyczne przypisanie i wygląd ekranów;
sama kompletność TTF nie dowodzi, że atlas TMP zawiera te glify.
Referencje I2 obejmują BigCaslon, Cochin, HelveticaRounded, IMFellDoublePica
oraz PortraitDialogue-Text. Nie wolno tłumaczyć nazw technicznych fontów jak tekstu.

## Proponowany vertical

1. Kopia oryginału; włączenie pl bez zmiany pozostałych języków/metadanych.
2. Próbka menu, początek rozgrywki, dialog i tutorial z ikonami przycisków.
3. Dobór/uzupełnienie fontów dla PL, próbka ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.
4. Zapis i odczyt zasobu, kontrola innych obiektów i kolumn.
5. Użytkownik sprawdza wybór Polski, powrót do English, restart, fonty i układ.

Dopiero po potwierdzonym verticalu pełne tłumaczenie. Językowo większe zadanie:
około 4,6 razy więcej znaków źródłowych niż w tabeli Pedro; surrealistyczne dialogi
wymagają konsekwentnej terminologii i korekty tonu.
