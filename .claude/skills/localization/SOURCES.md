# Źródła faktów i norm

Zasady redakcji wyciągnięte z materiałów branżowych są w [EDITORIAL.md](EDITORIAL.md).
Stosuj je lokalnie. Poniższa bibliografia służy rozstrzyganiu konkretnych problemów,
nie jest listą lektur do powtarzania przy każdej grze.

## Fakty o grze (od najmocniejszych)

1. **Pliki gry**
   - Klucze i identyfikatory wpisów: mówiący, scena, typ tekstu (UI, napis, opis).
     Wypisz raz listę sufiksów/prefiksów i przypisz je postaciom w biblii.
   - **Inne języki w tej samej grze.** Przed zgadywaniem płci zajrzyj do tabeli,
     która ją gramatycznie koduje: rosyjski, ukraiński, czeski (czas przeszły,
     przymiotniki), francuski, hiszpański, niemiecki (rodzaj rzeczowników,
     przymiotniki). To mocna poszlaka, ale nie wyrocznia: tamci tłumacze też
     pracowali bez kontekstu. W Turbo Overkill rosyjski daje SYN poprawnie
     „я пришла”, a Ripper błędnie „я убил”, choć gra mówi o niej „her”.
     Rozstrzyga zgodność co najmniej dwóch niezależnych źródeł.
     Zrzut tabeli: narzędzie gry do odczytu (np. `tools/other_languages.py`),
     wynik w `work/ref-<język>.json` — poza gitem, to treść wydawcy.
   - Komentarze, metadane i nazwy kolumn w tabelach lokalizacji; nazwy scen.
2. **Obsada i napisy końcowe** — identyfikacja ról. Płeć aktora nie dowodzi płci
   postaci; sprawdź tekst gry i opis postaci. W grze bywa tabela z creditsami
   (w Turbo Overkill: TurboEx1).
3. **Wiki, TV Tropes, strona i posty twórców** — lore, relacje, kontekst żartów.
4. **Nasze tłumaczenia powiązanych gier w `games/`** — crossovery, DLC
   z postaciami z innej gry, ten sam twórca. Imiona i terminy mają się zgadzać
   (Shotgun Cop Man ma dodatek z Pedro; My Friend Pedro PL ma „Ofelia”, „Pedra”).
5. **Oficjalne polskie wydania gier z gatunku i poprzednie części serii** —
   utarte terminy, które gracz zna (np. słownictwo cyberpunkowe, FPS-owe).
6. **Oficjalne polskie teksty platform:** Steam, GOG, konsole („Osiągnięcia”,
   „Zapisz grę”, nazwy przycisków kontrolera).

## Normy języka i formy

- **Microsoft Polish Localization Style Guide** — UI, ton, placeholdery,
  komunikaty: https://download.microsoft.com/download/b/d/c/bdc253ac-dbf3-4261-86a2-ffedfa718425/pol-pol-StyleGuide.pdf
- **Microsoft Terminology** — ustawienia grafiki, dźwięku, sterowania:
  https://learn.microsoft.com/en-us/globalization/reference/microsoft-terminology
- **Netflix Polish Timed Text Style Guide** — napisy dialogów:
  https://partnerhelp.netflixstudios.com/hc/en-us/articles/216787928-Polish-Timed-Text-Style-Guide
  oraz ogólne wymagania:
  https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements
  Limity napisów filmowych nie są automatycznie limitami gry; sprawdź jej UI i timing.
- **WSJP** (odmiana, łączliwość): https://wsjp.pl · **SJP PWN i Poradnia PWN**:
  https://sjp.pwn.pl/poradnia · **Rada Języka Polskiego**: https://rjp.pan.pl
- Odmiana obcych imion i nazw: Poradnia PWN (hasła „odmiana nazwisk obcych”).

Z sieci korzystaj celowo: jedno pytanie, jedno źródło, zapis w biblii.
Nie przepisuj cudzych tekstów do repo; wystarczy link i wniosek.
