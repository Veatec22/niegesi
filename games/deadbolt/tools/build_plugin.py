"""Buduje plugin DEADBOLT PL (d3d9.dll) i paczkę ZIP. Nie instaluje i nie uruchamia gry.

Wymaga MSVC x86 i źródeł MinHook 1.3.4 w work/minhook-1.3.4
(https://github.com/TsudaKageyu/minhook/archive/refs/tags/v1.3.4.zip).

    .venv\\Scripts\\python.exe games\\deadbolt\\tools\\build_plugin.py
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import zipfile
from pathlib import Path

import fonts
import labels

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.2.0'
PACKAGE = f'Deadbolt-PL-{VERSION}.zip'
FILES = ['d3d9.dll', 'notgeese/pl.tsv', 'notgeese/fonts.txt', 'notgeese/labels.txt', 'notgeese/LICENSE-MINHOOK.txt',
         'READ-ME.txt']
GAME = Path(r'C:\SteamLibrary\steamapps\common\DEADBOLT')


def compiler_environment():
    vswhere = Path(os.environ['ProgramFiles(x86)']) / 'Microsoft Visual Studio/Installer/vswhere.exe'
    vs = subprocess.check_output([str(vswhere), '-latest', '-property', 'installationPath'], text=True).strip()
    script = Path(vs) / 'VC/Auxiliary/Build/vcvars32.bat'
    output = subprocess.check_output(f'"{script}" >nul && set', shell=True, text=True)
    return dict(line.split('=', 1) for line in output.splitlines() if '=' in line and not line.startswith('='))


def compile_plugin(out: Path):
    work = ROOT / 'work/build'
    work.mkdir(parents=True, exist_ok=True)
    mh = ROOT / 'work/minhook-1.3.4'
    if not (mh / 'include/MinHook.h').is_file():
        raise SystemExit('Brak źródeł MinHook 1.3.4 w work/minhook-1.3.4')
    exports = ['Direct3DCreate9', 'Direct3DCreate9Ex', 'Direct3DShaderValidatorCreate9',
               'D3DPERF_BeginEvent', 'D3DPERF_EndEvent', 'D3DPERF_SetMarker',
               'D3DPERF_SetRegion', 'D3DPERF_QueryRepeatFrame', 'D3DPERF_SetOptions',
               'D3DPERF_GetStatus', 'DebugSetLevel', 'DebugSetMute', 'PSGPError', 'PSGPSampleTexture']
    proxy = ['#include <windows.h>', 'extern "C" FARPROC __cdecl Resolve(const char*);']
    for name in exports:
        proxy.extend([f'static const char name_{name}[] = "{name}";',
                      f'extern "C" __declspec(naked) void proxy_{name}() {{',
                      '  __asm { pushad }', f'  __asm {{ push offset name_{name} }}',
                      '  __asm { call Resolve }', '  __asm { add esp, 4 }',
                      '  __asm { mov dword ptr [esp+28], eax }', '  __asm { popad }',
                      '  __asm { jmp eax }', '}'])
    (work / 'Proxy.cpp').write_text('\n'.join(proxy), encoding='utf-8')
    (work / 'Proxy.def').write_text('LIBRARY d3d9\nEXPORTS\n' + '\n'.join(f'{n}=proxy_{n}' for n in exports),
                                    encoding='ascii')
    env = compiler_environment()
    compiler = shutil.which('cl.exe', path=next(v for k, v in env.items() if k.lower() == 'path'))
    if not compiler:
        raise SystemExit('Brak kompilatora MSVC x86')
    sources = [mh / 'src' / name for name in ['buffer.c', 'hook.c', 'trampoline.c', 'hde/hde32.c']]
    subprocess.run([compiler, '/nologo', '/c', '/O2', '/MT', '/W3', '/I' + str(mh / 'include'),
                    *map(str, sources)], cwd=work, env=env, check=True)
    subprocess.run([compiler, '/nologo', '/LD', '/O2', '/MT', '/EHsc', '/std:c++17', '/utf-8', '/W4',
                    '/I' + str(mh / 'include'), str(ROOT / 'plugin/Plugin.cpp'), str(work / 'Proxy.cpp'),
                    *[str(work / (p.stem + '.obj')) for p in sources],
                    'version.lib', 'user32.lib', 'ole32.lib', 'shlwapi.lib', 'windowscodecs.lib',
                    '/link', '/DEF:' + str(work / 'Proxy.def'), '/OUT:' + str(out / 'd3d9.dll')],
                   cwd=work, env=env, check=True)


def escape(value: str) -> str:
    return value.replace('\\', '\\\\').replace('\t', '\\t').replace('\n', '\\n').replace('\r', '\\r')


def write_tsv(path: Path) -> int:
    """pl.tsv dla pluginu: rodzaj, EN, PL[, wpis CODE]. Źródło: review zgodny z pl.json."""
    pl = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    review = json.loads((ROOT / 'translations/en-pl-review.json').read_text(encoding='utf-8'))
    if [r['key'] for r in review] != list(pl) or any(pl[r['key']] != r['polish'] for r in review):
        raise SystemExit('en-pl-review.json nie zgadza się z pl.json — uruchom tools/review.py')
    lines, json_rows = [], {}
    for r in review:
        key, en, polish = r['key'], r['english'], r['polish']
        if key.startswith('j:'):
            json_rows.setdefault(en, polish)
            continue
        if '@' in key:
            lines.append(f'c\t{escape(en)}\t{escape(polish)}\t{key.split("@", 1)[1]}\n')
        else:
            lines.append(f's\t{escape(en)}\t{escape(polish)}\n')
    lines += [f'j\t{escape(en)}\t{escape(polish)}\n' for en, polish in json_rows.items()]
    path.write_text('# DEADBOLT PL: rodzaj (s napis, c napis w jednym wpisie kodu, j dialog JSON), EN, PL[, wpis kodu]\n'
                    + ''.join(lines), encoding='utf-8', newline='\n')
    return len(review)


def build(binary_only=False):
    out = ROOT / 'dist'
    (out / 'notgeese').mkdir(parents=True, exist_ok=True)
    compile_plugin(out)
    if binary_only:
        print('Zbudowano sam d3d9.dll.')
        return
    entries = write_tsv(out / 'notgeese/pl.tsv')
    glyphs = fonts.write_recipes(out / 'notgeese/fonts.txt')
    label_ops = labels.write_recipe(out / 'notgeese/labels.txt', GAME)
    shutil.copyfile(ROOT / 'work/minhook-1.3.4/LICENSE.txt', out / 'notgeese/LICENSE-MINHOOK.txt')
    shutil.copyfile(ROOT / 'docs/INSTALL.txt', out / 'READ-ME.txt')
    archive = out / PACKAGE
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            z.write(out / name, name)
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        assert sorted(names) == sorted(FILES), names
        # Paczka nie niesie zawartości gry: żadnych plików danych, obrazów, dźwięków ani JSON-ów gry.
        assert not any(n.lower().endswith(('.win', '.exe', '.ogg', '.png', '.json', '.nc')) for n in names)
        assert z.testzip() is None
    report = {'version': VERSION, 'entries': entries, 'glyph_recipes': glyphs, 'label_ops': label_ops,
              'package': PACKAGE, 'package_bytes': archive.stat().st_size,
              'package_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(), 'files': FILES}
    (out / 'build-report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'Zbudowano {archive} ({archive.stat().st_size} B): {entries} wpisów, {glyphs} liter')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--binary-only', action='store_true')
    build(p.parse_args().binary_only)
