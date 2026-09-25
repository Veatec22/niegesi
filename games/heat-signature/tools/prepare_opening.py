"""Verified opening sample; smooth terminal language selected by the user."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE = {
    'This is not how I pictured my retirement.': 'Nie tak wyobrażałem sobie emeryturę.',
    'Getting shot over a nebula of battery acid in the ass-end of nowhere.': 'Dostaję kulkę nad mgławicą kwasu akumulatorowego, na kompletnym zadupiu.',
    "But I'm invested now.": 'Ale za dużo już w to włożyłem.',
    "And there's one last thing I wanna do before I quit.": 'I zanim skończę, chcę zrobić jeszcze jedną rzecz.',
    '< You can click items in this list to teleport them to you': '< Klikaj przedmioty na liście, by teleportować je do siebie',
    '< Teleport your Facebreaker to you': '< Teleportuj Gębołamacz do siebie',
    'Left Click the Facebreaker to make it your main attack': 'Kliknij Gębołamacz LPM, by przypisać go do głównego ataku',
    'Humour me and Right Click on the gun, just so I know you know you can': 'Zrób mi tę przyjemność i kliknij broń PPM. Chcę wiedzieć, że umiesz',
    'Right Click the gun to make it your Right Click attack': 'Kliknij broń PPM, by przypisać ją do ataku prawym przyciskiem',
    'Responding': 'Reaguje',
    'Confronting': 'Interweniuje',
    "                            ALARMS\r\n        #Guards sound the alarm if they:# - Hear a shot # - Find a body# - See you\r\n        #If the countdown hits 0, you'll be captured.\r\n        #Taking out the captain cancels the countdown.": "                            ALARMY\r\n        #Strażnicy wszczynają alarm, gdy:# - Usłyszą strzał # - Znajdą ciało# - Zobaczą cię\r\n        #Gdy licznik dojdzie do zera, wpadniesz w niewolę.\r\n        #Obezwładnienie kapitana zatrzyma odliczanie.",
    'Set course for ': 'Ustaw kurs na: ',
    "Breaker, I've got the siege ship.": 'Breaker, mam okręt oblężniczy.',
    "I've laid in a course for ": 'Kurs ustawiony na: ',
    "This ship can crash the defenses, but you've gotta reprogram them from the inside while they're down.": 'Ten okręt może wyłączyć obronę, ale trzeba ją wtedy przeprogramować od środka.',
    "I'm gonna throw myself into space now, meet me in the bar if I don't die.": 'Teraz wyskoczę w kosmos. Jeśli nie zginę, widzimy się w barze.',
    ' has been captured and re-captured four times this year.': ' — ta stacja już cztery razy zmieniała właściciela w tym roku.',
    'First three times, no-one who lived there could fight it.': 'Za pierwszymi trzema razami nikt z mieszkańców nie mógł się przeciwstawić.',
    'This time one of them can.': 'Tym razem jeden może.',
    'This time one of them has a forty year career in espionage, a Breacher stealth pod, and a kinetic Facebreaker.': 'Tym razem jeden ma za sobą czterdzieści lat szpiegostwa, kapsułę infiltracyjną Breacher i kinetyczny Gębołamacz.',
    "So it's gonna change hands one last time.": 'Więc stacja zmieni właściciela jeszcze ten ostatni raz.',
    "This time, I'm taking it.": 'Tym razem przejmę ją ja.',
    'Choose a character for this life:': 'Wybierz postać na to życie:',
    "You see where we're going with this": 'Już chyba wiesz, do czego zmierzamy',
    'Handle this one however you like': 'Z tym rozpraw się, jak chcesz',
    'Remember: everything cool requires pausing': 'Pamiętaj: żeby zrobić coś efektownego, trzeba włączyć pauzę',
    'Practice being cool': 'Poćwicz efektowne zagrania',
    'Take an Easy mission': 'Weź łatwą misję',
    'Other practice sims': 'Inne symulacje treningowe',
    "Leave when you're ready": 'Ruszaj, kiedy zechcesz',
    'Sound: off': 'Dźwięk: wył.',
    'Gamepad: enabled': 'Pad: wł.',
    'Gamepad: disabled': 'Pad: wył.',
    'Controls': 'Sterowanie',
    'Cancel': 'Anuluj',
    'Difficulty': 'Poziom trudności',
    'Facebreaker': 'Gębołamacz',
    "Fiasco's Facebreaker": 'Gębołamacz Fiasco',
}

DIALOG = {
    'PRACTICE TERMINAL LET YOU VIOLENCE ON UNREAL HUMAN IN MAGIC REALITY': 'TERMINAL TRENINGOWY POZWALA ĆWICZYĆ WALKĘ Z WIRTUALNYMI LUDŹMI W MAGICZNEJ RZECZYWISTOŚCI',
    'TRY OUT YOUR STUFFS IN PRACTICE! HAVE THEM BACK AFTER!': 'WYPRÓBUJ SWÓJ SPRZĘT NA TRENINGU! PO TRENINGU GO ODZYSKASZ!',
    'NO DEATH IS REAL IN MAGIC REALITY. R TO RESTART': 'W MAGICZNEJ RZECZYWISTOŚCI NIKT NIE GINIE NAPRAWDĘ. R — ZACZNIJ OD NOWA',
    'PRACTICE RANDOM EASY': 'LOSUJ ŁATWY TRENING',
    'PRACTICE RANDOM HARD': 'LOSUJ TRUDNY TRENING',
    'PRACTICE IS START': 'TRENING ROZPOCZĘTY',
    'PRACTICE IS NO': 'TRENING ZAKOŃCZONY',
    'YOU ARE NOW COOL ENOUGH FOR REALITY': 'MASZ JUŻ DOŚĆ WPRAWY, BY WRÓCIĆ DO RZECZYWISTOŚCI',
    'FINISH VIOLENCE': 'ZAKOŃCZ WALKĘ',
    'THIS VIOLENCE AGAIN': 'POWTÓRZ WALKĘ',
    'EXCELLENT VIOLENCE!': 'ŚWIETNA WALKA!',
    'NEXT VIOLENCE': 'NASTĘPNA WALKA',
    'SKIP EXCITING VIOLENCE': 'POMIŃ EMOCJONUJĄCĄ WALKĘ',
    "Holy shit you're alive.": 'O kurwa, żyjesz.',
    'Because you reprogrammed the station defenses... right?': 'Bo obrona stacji jest przeprogramowana… prawda?',
    "I get that more than you'd think.": 'Słyszę to częściej, niż myślisz.',
    "Yeah, I'm just surprised when anything I touch still works.": 'Tak, po prostu dziwi mnie, kiedy coś jeszcze działa po mojej interwencji.',
    "Maybe it doesn't, let's wait to see if it shoots the bad guys before we relax.": 'Może nie działa. Zanim odetchniemy, sprawdźmy, czy strzela do tych złych.',
    "Turns out you're pretty good.": 'Jak widać, znasz się na rzeczy.',
    'Good point.': 'Słuszna uwaga.',
    '[Continue]': '[Dalej]',
    'Hey: we have a station!': 'Hej, mamy stację!',
    'We have a station.': 'Mamy stację.',
    'I have a station.': 'Ja mam stację.',
    'Almost hard to believe nine people have shot you, Sader.': 'Aż trudno uwierzyć, że dziewięć osób do ciebie strzeliło, Sader.',
    "It's ten now.": 'Teraz już dziesięć.',
    "It's like no-one can take a joke.": 'Jakby nikt nie znał się na żartach.',
    'I believe it when I lift my left arm.': 'Ja wierzę, kiedy podnoszę lewą rękę.',
    "And somehow it's never enough.": 'I jakoś ciągle za mało.',
    'This is gonna start something, you know. Other stations are gonna want to throw off the shackles like this.': 'Wiesz, to dopiero początek. Inne stacje też będą chciały zrzucić kajdany.',
    'Four factions fighting over this cloud. If we ever get their strongholds, this war just ends.': 'Cztery frakcje walczą o tę chmurę. Jeśli zdobędziemy ich twierdze, wojna się skończy.',
    "That's a long shot.": 'Marne szanse.',
    "That's an interesting idea.": 'Ciekawy pomysł.',
    "That's the plan.": 'Taki jest plan.',
    "It's weird being your friend.": 'Dziwnie tak się z tobą przyjaźnić.',
    "Sure you don't wanna postpone your retirement and help out? You'd tear through these amateurs.": 'Na pewno nie chcesz odłożyć emerytury i pomóc? Rozniósłbyś tych amatorów.',
    "I've been shot ten times, Breaker, I'll be lucky if I make it to the couch.": 'Dostałem dziesięć kulek, Breaker. Będę miał szczęście, jeśli dojdę do kanapy.',
    "I'm really goddamn tired, Breaker.": 'Jestem cholernie zmęczony, Breaker.',
    "I'm helping! I'm drinking and helping.": 'Przecież pomagam! Piję i pomagam.',
    "Fair enough. So that's it? You're really gonna retire? I can't picture it. What're you gonna do?": 'No dobra. Więc to koniec? Naprawdę idziesz na emeryturę? Nie umiem sobie tego wyobrazić. Co będziesz robić?',
    "I have connections. People here have problems. I'm gonna help out.": 'Mam znajomości. Ludzie tutaj mają problemy. Będę pomagać.',
    "I have connections. People here have money. I'm gonna sell out.": 'Mam znajomości. Ludzie tutaj mają pieniądze. Będę się sprzedawać.',
    "I'm gonna sit in that booth watching you guys do all the hard work.": 'Usiądę w tamtym boksie i popatrzę, jak odwalacie całą ciężką robotę.',
    "Well, they're probably gonna come to me with those, but I'll point them your way.": 'Pewnie przyjdą z nimi do mnie, ale odeślę ich do ciebie.',
    'Thanks, B.': 'Dzięki, B.',
    "Well, if I can't make them spend it all on liquor, I'll send them to you.": 'Jeśli nie zdołam wyciągnąć od nich wszystkiego na alkohol, odeślę ich do ciebie.',
    "I'm gonna make the station kill you on sight again.": 'Znowu każę stacji strzelać do ciebie bez ostrzeżenia.',
    "That's fair.": 'Uczciwie.',
    "I can never tell when you're joking.": 'Nigdy nie wiem, kiedy żartujesz.',
    "I'll let you know.": 'Dam ci znać.',
}


def main(game):
    exe = (game / 'Heat_Signature.exe').read_bytes()
    originals = {}
    for path in (game / 'Dialog').glob('*.txt'):
        for line_no, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
            line = line.strip()
            if not line or re.fullmatch(r'\[[^]]+\]', line):
                continue
            line = re.sub(r'\s*\{[^}]*\}\s*$', '', line)
            line = line.lstrip('#= ').strip()
            if line:
                originals.setdefault(line, []).append(f'Dialog/{path.name}:{line_no}')
    for en in NATIVE:
        assert en.encode() + b'\0' in exe, f'Missing native literal {en!r}'
    for en in DIALOG:
        assert en in originals, f'Missing dialogue {en!r}'
    path = ROOT / 'translations/pl.json'
    pl = json.loads(path.read_text(encoding='utf-8'))
    pl.update(NATIVE | DIALOG)
    path.write_text(json.dumps(pl, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    review = [dict(key=en, english=en, polish=value,
                  context='; '.join(originals[en]) if en in DIALOG else 'Literał EXE; UI, narracja lub instrukcja samouczka')
              for en, value in pl.items()]
    (ROOT / 'translations/en-pl-review.json').write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(pl)} verified entries; {len(NATIVE)} opening/native and {len(DIALOG)} dialogue additions')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True)
    main(parser.parse_args().game)
