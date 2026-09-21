# Labyrinth Of The Demon King — rozpoznanie tłumaczeń

Stan sprawdzenia: 20 września 2026. Zakres: dostępność PL oraz fanowskie tłumaczenia
przydatne do dalszej analizy lokalnych plików. Nie uruchamiano gry ani instalatorów.

## Werdykt

**Nie znaleziono dostępnego spolszczenia. Projekt pozostaje otwarty do analizy
technicznej i verticala.** Nie jest to twierdzenie, że żadne tłumaczenie nigdy nie
powstało. Nie znaleziono konkretnego polskiego autora z działającą paczką do pobrania.

[Oficjalna karta Steam](https://store.steampowered.com/app/1804010/_/?l=polish)
wprost oznacza polski jako nieobsługiwany. Wymienia 11 języków: angielski, japoński,
chiński uproszczony, francuski, włoski, niemiecki, portugalski brazylijski, rosyjski,
chiński tradycyjny, hiszpański i arabski. [Karta GOG](https://www.gog.com/en/game/labyrinth_of_the_demon_king)
również nie wymienia polskiego; jej lista nie jest identyczna ze Steam.

Uwaga na fałszywy trop: [zestaw Demon West](https://store.steampowered.com/bundle/77573/)
wymienia polski, ale dotyczy to zbiorczej listy języków gier w zestawie. Strona
uprzedza, że języki nie muszą być obsługiwane przez każdą grę. Nie dowodzi to PL
w Labyrinth Of The Demon King.

Sprawdzono zapytania tytuł + „spolszczenie”, „polskie tłumaczenie”, „Polish
translation”, „translation mod”, a także wyszukiwanie w Graj Po Polsku i
spolszczenia.pl. Trafienia dotyczące starej gry Labyrinth na MSX oraz przypadkowe
wyniki z nazwą Demon King nie dotyczą tej gry (Steam app 1804010).

## Fanowskie tłumaczenie koreańskie

Znaleziono publikację autora **Eueeeeeeeek / 으잌**:

- [Aktualny wpis autora](https://eueeeeeeeek.kr/56), datowany 15 marca 2026.
- [Główny link paczki na pCloud](https://u.pcloud.link/publink/show?code=XZgS8h5ZNLnNuSMBUe7DA7lGXtV8T5W6vuzk).
- [Lustro na Proton Drive](https://drive.proton.me/urls/M0XCRAED5W#Ee8t1ztqUwpz).
- [Starszy adres publikacji autora](https://blog.naver.com/dkfvls1/223866430192).

Wpis autora udało się odczytać bezpośrednio przez HTTP, mimo błędu narzędzia web.
Potwierdzono tytuł gry, autora, instrukcję rozpakowania do katalogu gry i oba
powyższe odsyłacze. Autor podaje hasło `eueeeeeeeek.kr`, jeśli archiwum go wymaga.
**Nie pobierano archiwum i nie potwierdzono zawartości ani zgodności z lokalnym
wydaniem.** pCloud nie został zweryfikowany na poziomie pliku (błąd narzędzia web,
następnie błąd łańcucha certyfikatu przy odczycie API). Nie oznacza to, że paczka
jest niedostępna dla użytkownika.

Wskazówka do sprawdzenia, nie ustalenie o formacie: starszy
[wpis katalogowy z 18 maja 2025](https://lifeculture.tistory.com/1645) odsyła do tego
samego autora i opisuje wybór pierwszej pozycji English po skopiowaniu paczki.
To źródło wtórne sugeruje podmianę angielskiej wersji. Aktualny odczytany wpis
autora nie wyjaśnia formatu zasobów, użytych narzędzi ani sposobu dodania własnego
języka. Nie należy zakładać, że koreańska paczka zapewnia osobny selektor.

## Techniczne wskazówki ze źródeł pierwotnych

[Steam](https://store.steampowered.com/app/1804010/_/?l=polish) informuje, że demo
bazuje na starszej wersji i ma m.in. poprawione w pełnej grze problemy z częściowym
wyświetlaniem lokalizacji. Analizę i testy trzeba oprzeć na pełnej lokalnej wersji.

[Odpowiedź dewelopera z 15 maja 2025](https://steamcommunity.com/profiles/76561198245161600/recommended/1804010/)
potwierdza użycie arkusza lokalizacyjnego i osobnych nazw języków na ekranie wyboru.
Nie określa formatu plików w buildzie. Samo istnienie arkusza nie dowodzi, że jest
on dostarczany z grą albo że można łatwo dopisać PL.

Dalszy krok: lokalnie ustalić format tekstów, kompletność zakresu, fonty i drogę
do własnego języka w selektorze. Koreański mod stanowi praktyczny trop, ale bez
zbadania jego plików nie wyciągamy wniosków o narzędziach ani montowaniu paczki.
