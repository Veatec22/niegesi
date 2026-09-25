"""Populate the independent UI/instruction part of the vertical from verified EN literals."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

UI = {
    'Resume': 'Wznów',
    'Options': 'Ustawienia',
    'Credits': 'Twórcy',
    'Quit': 'Wyjdź',
    'Back': 'Wstecz',
    'Restart tutorial': 'Zacznij samouczek od nowa',
    'Skip tutorial': 'Pomiń samouczek',
    'Replay tutorial': 'Powtórz samouczek',
    'Change character': 'Zmień postać',
    'Change galaxy': 'Zmień galaktykę',
    'Play time: ': 'Czas gry: ',
    'Sound Volume: ': 'Głośność dźwięków: ',
    'Windowed mode: on': 'Tryb okienkowy: wł.',
    'Windowed mode: off': 'Tryb okienkowy: wył.',
    'Customise Controls': 'Zmień sterowanie',
    'Gameplay and Difficulty Options': 'Rozgrywka i poziom trudności',
    'Accessibility Options': 'Ułatwienia dostępu',
    'Technical Options': 'Ustawienia techniczne',
    'Advanced Options': 'Ustawienia zaawansowane',
    'Sharing Options': 'Ustawienia udostępniania',
    'Developer Options': 'Ustawienia deweloperskie',
    'Window Options': 'Ustawienia okna',
    'Capture Cursor: ': 'Przechwytywanie kursora: ',
    'fullscreen only': 'tylko na pełnym ekranie',
    'Pause in Background: ': 'Pauza w tle: ',
    'View Scaling: ': 'Skala obrazu: ',
    'View Scaling: auto': 'Skala obrazu: automatyczna',
    'Reset Scaling': 'Przywróć skalę',
    'Apply Scaling': 'Zastosuj skalę',
    '(Hold) Thrust': '(Przytrzymaj) Ciąg',
    '(Hold) Brake': '(Przytrzymaj) Hamuj',
    'Move': 'Ruch',
    'Move up': 'Ruch w górę',
    'Move left': 'Ruch w lewo',
    'Move down': 'Ruch w dół',
    'Move right': 'Ruch w prawo',
    'Pause now': 'Teraz włącz pauzę',
    'Pause now!': 'Teraz włącz pauzę!',
    'Inventory': 'Ekwipunek',
    'Hold to aim strike': 'Przytrzymaj, by wycelować cios',
    'Release to fire (anywhere)': 'Puść, by strzelić (w dowolnym miejscu)',
    'Hold to aim shot (anywhere)': 'Przytrzymaj, by wycelować (w dowolnym miejscu)',
    'Pause when he reaches you': 'Włącz pauzę, gdy do ciebie podejdzie',
    'Pause a lot! You have as long as you like to:': 'Często włączaj pauzę! Masz wtedy dowolnie dużo czasu na:',
    'Zoom': 'Przybliżenie',
    '(Hold) Move the camera around': '(Przytrzymaj) Przesuwaj kamerę',
    'Aim attacks': 'Celuj',
    "Unpause when you're ready": 'Wyłącz pauzę, gdy zechcesz działać',
    'Pause': 'Pauza',
    'Click to remote control your pod >': 'Kliknij, by zdalnie sterować kapsułą >',
    "Brake will try to match your speed to the thing you're approaching": 'Hamulec dopasowuje prędkość do obiektu, do którego się zbliżasz',
    '(Hold) Fast-forward': '(Przytrzymaj) Przyspiesz czas',
    '(Hold) Hit a guard with your wrench': '(Przytrzymaj) Uderz strażnika kluczem francuskim',
    'Then pause immediately!': 'I od razu włącz pauzę!',
    '< Take his gun': '< Weź jego broń',
    'Equip it': 'Wyposaż się w nią',
    '(Hold) Aim at the other guard': '(Przytrzymaj) Wyceluj w drugiego strażnika',
    '(Release) Shoot them': '(Puść) Strzel do niego',
    '(Hold) Hit a guard with your wrench again': '(Przytrzymaj) Znowu uderz strażnika kluczem francuskim',
    'Enter throw mode': 'Włącz tryb rzucania',
    'Dock here': 'Zadokuj tutaj',
    'You need this keycard': 'Potrzebujesz tej karty dostępu',
    'Hit this guy': 'Uderz go',
    'Take his gun': 'Weź jego broń',
    'This door is locked': 'Te drzwi są zamknięte',
    'Hit the captain': 'Uderz kapitana',
    'Take the helm': 'Przejmij stery',
    'Break the glass': 'Rozbij szybę',
    'Throw yourself into space': 'Wyskocz w przestrzeń kosmiczną',
    'Home': 'Dom',
    'Catch yourself': 'Złap się kapsułą',
    'Talk to Breaker': 'Porozmawiaj z Breaker',
    'Retire': 'Przejdź na emeryturę',
    'Wrench': 'Klucz francuski',
}


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--game', required=True, type=Path)
    game = p.parse_args().game
    exe = (game / 'Heat_Signature.exe').read_bytes()
    for en in UI:
        assert en.encode('utf-8') + b'\0' in exe, f'Not an original literal: {en!r}'
    # Merge preserves later editorial changes: only missing entries are added to the
    # translation file (en-pl-review.json, decision 0021).
    import texts
    changed, added = texts.merge(UI, {en: 'UI/instrukcja; oryginalny literał EXE' for en in UI}, overwrite=False)
    print(f'{added} UI entries added')
    print(f'Verified and prepared {len(UI)} UI/instruction literals; total {len(current)}')
