"""Zrzut wszystkich języków OTXO z katalogu gry -> work/ref-all.json (poza gitem)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from script_ini import load
game = Path(sys.argv[1] if len(sys.argv) > 1 else 'C:/Games/OTXO')
files = {'en': 'script_english.ini', 'fr': 'OTXO_script_english_fre-FR.ini', 'de': 'OTXO_script_english_ger-DE.ini',
         'pt': 'OTXO_script_english_por-BR.ini', 'ru': 'OTXO_script_english_rus.ini', 'es': 'OTXO_script_english_spa-ES.ini'}
tabs = {lang: load(game / name) for lang, name in files.items()}
out = {k: {lang: tabs[lang].get(k, '') for lang in files} for k in tabs['en']}
Path(__file__).with_name('ref-all.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(out))
