# Pedro — uwagi do korekty

721/721 rekordów tabeli I2 ma polską wersję. Pełne dialogi zawierają zakończenie gry.

- Focus: **skupienie**; split aim: **rozdzielanie celowania**.
- Mitch the Butcher: **Mitch Rzeźnik**; Ophelia: **Ofelia**. Pozostałe imiona,
  pseudonimy i oznaczenia ISP zachowane.
- Old Town: **Stare Miasto**; District Null: **Dzielnica Null**;
  Pedro's World: **Świat Pedra**; The Sewer: **Kanały**; The Internet: **Internet**.
- Internet Service Protectors: **Internetowa Straż Porządkowa**, skrót ISP.
- Haters: **hejterzy**; odzywki graczy zachowują slang i skróty LOL, GG, GLHF itp.
- Nazwy osiągnięć adaptują gry słowne; do oceny zwłaszcza achN3/4/5/9/12/27.
  Dopowiedzenia ocen A/B/C/S zaczynają się od odpowiedniej litery.
- Żart kolejowy w410-1 jest adaptacją gry słów; do oceny w kontekście sceny.
- Angielskie nazwy na klawiszach (Tab, Home itd.), tytuł gry i skróty pozostają.
- Zachowano ikony <...>, kolorowanie, kolejność komend animacji [...] i separator |.
  Wyjątek: [Not mapped] to tekst ekranowy, przetłumaczony na [Nieprzypisane].
- Teksty starej integracji z Twitterem są tłumaczone zgodnie ze źródłem;
  nie weryfikowano działania tej integracji.

Użytkownik potwierdził działanie verticala bez potrzeby screenów: selektor,
zapis wyboru, polskie znaki i początek rozgrywki. Pełnej kampanii i wszystkich
układów ekranowych jeszcze nie przetestowano. Sprawdź szczególnie długie dialogi,
opisy trudności, menu modyfikatorów oraz dopowiedzenia ocen.

Korekta: zmień pl.json, uruchom build.py --extract na oryginale z backups,
następnie review.py i build.py. JSON EN/PL musi zgadzać się z pl.json.
HTML to podgląd z wyszukiwaniem, nie edytor zapisujący zmiany.
