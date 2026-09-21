"""Łatka różnicowa: wysyłamy różnicę, gracz odtwarza plik ze swojej kopii gry.

Używane tam, gdzie plugin jest niemożliwy, a spolszczony plik jest za duży albo
w zbyt dużej części należy do wydawcy, żeby go publikować. Łatka niesie wyłącznie
to, czym spolszczony plik różni się od oryginału — resztę składa z pliku, który
gracz już ma na dysku.

Format jest prosty i możliwy do obejrzenia zwykłym edytorem: nagłówek tekstowy,
pusta linia, dane binarne. Nagłówek podaje sumy kontrolne obu stron, więc
nakładanie odmawia pracy na innej wersji gry i nie da się po cichu zepsuć pliku.

Dane binarne to lista operacji spakowana zwykłym DEFLATE (bez nagłówka zlib),
który ma każde środowisko: .NET Framework, przeglądarka, Python. Dzięki temu
tę samą łatkę nakłada `NieGesiPatch.exe` z paczki i guzik „zainstaluj" na stronie,
bez żadnej biblioteki. Po rozpakowaniu:

    0x01 <długość> <przesunięcie>   skopiuj bajty z oryginału
    0x02 <długość> <bajty>          wstaw nowe bajty
    0x00                            koniec

Liczby to varinty LEB128. Przesunięcie jest liczone ze znakiem (zigzag) od końca
poprzedniego kopiowania, więc przy pliku, który tylko się przesunął, wynosi zero.
Implementacje nakładania: tutaj, `tools/applier/NieGesiPatch.cs`
i `site/src/lib/install.ts` — zmiana formatu to zmiana we wszystkich trzech.

    python tools/patch.py release --original <plik> --built <plik> --readme <txt> ...
    python tools/patch.py apply   --game <katalog gry> --patch <latka>

`release` to jedno polecenie dla całej gry: buduje łatkę, sprawdza ją przez
ponowne nałożenie i składa paczkę z łatką, aplikatorem i instrukcją.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import zipfile
import zlib
from pathlib import Path

MAGIC = 'NIEGESI-PATCH'
FORMAT = '2'
END, COPY, ADD = 0, 1, 2

# Oryginał indeksujemy w blokach tej długości. Krótsze dopasowania trafiają do
# literałów i ściska je DEFLATE; dłuższe bloki to mniejszy indeks w pamięci.
BLOCK = 64
# Kopiowanie krótsze niż tyle nie opłaca się wobec kosztu samej operacji.
MIN_COPY = 24

ROOT = Path(__file__).resolve().parents[1]
APPLIER = ROOT / 'tools' / 'applier'


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def varint(value: int) -> bytes:
    out = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value:
            out.append(byte | 0x80)
        else:
            out.append(byte)
            return bytes(out)


def zigzag(value: int) -> int:
    return value * 2 if value >= 0 else -value * 2 - 1


def common_length(a: memoryview, a_at: int, b: memoryview, b_at: int, limit: int) -> int:
    """Ile bajtów od podanych pozycji jest wspólnych — porównania kawałkami w C."""
    length, step = 0, 4096
    while length < limit:
        size = min(step, limit - length)
        if a[a_at + length:a_at + length + size] == b[b_at + length:b_at + length + size]:
            length += size
            step = min(step * 2, 1 << 20)
        elif size <= 16:
            while length < limit and a[a_at + length] == b[b_at + length]:
                length += 1
            return length
        else:
            step = max(size // 4, 16)
    return length


def diff(source: bytes, target: bytes) -> bytes:
    """Lista operacji odtwarzających `target` z `source`, jeszcze nieskompresowana."""
    src, dst = memoryview(source), memoryview(target)
    index: dict[int, int] = {}
    for at in range(len(source) - BLOCK, -1, -BLOCK):
        index[hash(src[at:at + BLOCK].tobytes())] = at

    ops = bytearray()
    cursor = 0          # koniec ostatniego kopiowania w oryginale
    pending = 0         # początek niezapisanego literału w pliku wynikowym

    def emit_add(end: int) -> None:
        if end > pending:
            ops.append(ADD)
            ops.extend(varint(end - pending))
            ops.extend(dst[pending:end])

    def emit_copy(at: int, length: int) -> None:
        nonlocal cursor
        ops.append(COPY)
        ops.extend(varint(length))
        ops.extend(varint(zigzag(at - cursor)))
        cursor = at + length

    at, end = 0, len(target)
    while at < end:
        # Najpierw zgadujemy, że plik biegnie dalej z tym samym przesunięciem
        # co poprzednio — tak wygląda większość pliku, który się tylko przesunął.
        guess = cursor + (at - pending)
        if guess + MIN_COPY <= len(source) and at + MIN_COPY <= end:
            length = common_length(dst, at, src, guess, min(end - at, len(source) - guess))
            if length >= MIN_COPY:
                emit_add(at)
                emit_copy(guess, length)
                at += length
                pending = at
                continue

        found = None
        if at + BLOCK <= end:
            candidate = index.get(hash(dst[at:at + BLOCK].tobytes()))
            if candidate is not None and src[candidate:candidate + BLOCK] == dst[at:at + BLOCK]:
                found = candidate
        if found is None:
            at += 1
            continue

        # Dopasowanie rozciągamy wstecz, w głąb jeszcze niezapisanego literału.
        back = 0
        while back < at - pending and back < found and src[found - back - 1] == dst[at - back - 1]:
            back += 1
        start, origin = at - back, found - back
        length = back + common_length(dst, at, src, found, min(end - at, len(source) - found))
        if length < MIN_COPY:
            at += 1
            continue
        emit_add(start)
        emit_copy(origin, length)
        at = start + length
        pending = at

    emit_add(end)
    ops.append(END)
    return bytes(ops)


def deflate(data: bytes) -> bytes:
    packer = zlib.compressobj(9, zlib.DEFLATED, -15, 9)
    return packer.compress(data) + packer.flush()


def inflate(data: bytes) -> bytes:
    return zlib.decompress(data, -15)


def read_varint(data: bytes, at: int) -> tuple[int, int]:
    value = shift = 0
    while True:
        byte = data[at]
        at += 1
        value |= (byte & 0x7F) << shift
        shift += 7
        if not byte & 0x80:
            return value, at


def run(source: bytes, ops: bytes, size: int) -> bytes:
    """Nakłada operacje na oryginał. Lustro `NieGesiPatch.cs` i `install.ts`."""
    out = bytearray()
    at = cursor = 0
    while True:
        op = ops[at]
        at += 1
        if op == END:
            break
        length, at = read_varint(ops, at)
        if op == COPY:
            delta, at = read_varint(ops, at)
            origin = cursor + ((delta >> 1) ^ -(delta & 1))
            assert 0 <= origin and origin + length <= len(source), 'łatka sięga poza oryginał'
            out += source[origin:origin + length]
            cursor = origin + length
        elif op == ADD:
            out += ops[at:at + length]
            at += length
        else:
            raise AssertionError(f'nieznana operacja {op}')
        assert len(out) <= size, 'łatka daje za duży plik'
    return bytes(out)


def build(original: Path, built: Path, out: Path, game: str, relative: str) -> dict:
    source, target = original.read_bytes(), built.read_bytes()
    ops = diff(source, target)
    payload = deflate(ops)

    header = '\n'.join([
        MAGIC,
        f'format {FORMAT}',
        f'game {game}',
        f'file {relative}',
        f'source-sha256 {sha256(source)}',
        f'source-size {len(source)}',
        f'target-sha256 {sha256(target)}',
        f'target-size {len(target)}',
        '',
        '',
    ]).encode('utf-8')

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(header + payload)

    # Nakładamy własną łatkę na oryginał i sprawdzamy, czy wychodzi dokładnie plik wynikowy.
    restored = run(source, inflate(payload), len(target))
    assert restored == target, 'łatka nie odtwarza pliku wynikowego'

    return {
        'patch': str(out),
        'patch_bytes': out.stat().st_size,
        'target_bytes': len(target),
        'share_of_file': round(out.stat().st_size / len(target) * 100, 3),
    }


def read_header(raw: bytes) -> tuple[dict, bytes]:
    split = raw.find(b'\n\n')
    assert split > 0, 'to nie jest nasza łatka'
    lines = raw[:split].decode('utf-8').splitlines()
    assert lines and lines[0] == MAGIC, 'to nie jest nasza łatka'

    header = {}
    for line in lines[1:]:
        key, _, value = line.partition(' ')
        header[key] = value
    assert header.get('format') == FORMAT, f'nieznana wersja formatu: {header.get("format")}'
    return header, raw[split + 2:]


def apply(game: Path, patch: Path, backup: Path | None) -> dict:
    header, payload = read_header(patch.read_bytes())
    target_file = game / header['file']
    assert target_file.exists(), f'nie znalazłem {target_file}'

    source = target_file.read_bytes()
    digest = sha256(source)
    if digest == header['target-sha256']:
        return {'status': 'juz zainstalowane', 'file': str(target_file)}
    assert digest == header['source-sha256'], (
        'Ten plik gry nie jest tym, pod który zrobiono łatkę.\n'
        f'  oczekiwano {header["source-sha256"]}\n'
        f'  jest       {digest}\n'
        'Jeśli masz już wgrane spolszczenie, przywróć oryginał. '
        'Jeśli gra dostała aktualizację, potrzebna jest nowa łatka.'
    )

    restored = run(source, inflate(payload), int(header['target-size']))
    assert sha256(restored) == header['target-sha256'], 'odtworzony plik ma inną sumę kontrolną'

    if backup is not None:
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(source)

    target_file.write_bytes(restored)
    return {
        'status': 'gotowe',
        'file': str(target_file),
        'backup': str(backup) if backup else None,
        'bytes': len(restored),
    }


def applier() -> Path:
    """Aplikator .exe dla gracza; budowany z `tools/applier`, gdy go jeszcze nie ma."""
    exe = APPLIER / 'bin' / 'NieGesiPatch.exe'
    source = APPLIER / 'NieGesiPatch.cs'
    if not exe.exists() or exe.stat().st_mtime < source.stat().st_mtime:
        import subprocess
        subprocess.run([sys.executable, str(APPLIER / 'build.py')], check=True)
    return exe


def release(original: Path, built: Path, readme: Path, out_dir: Path,
            game: str, relative: str, name: str, version: str) -> dict:
    """Łatka plus paczka gotowa dla gracza — jedno polecenie na grę."""
    patch = out_dir / f'{name}-PL-{version}.patch'
    result = build(original, built, patch, game, relative)
    exe = applier()

    package = out_dir / f'{name}-PL-{version}-latka.zip'
    with zipfile.ZipFile(package, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(patch, patch.name)
        archive.write(exe, exe.name)
        archive.write(readme, 'READ-ME.txt')

    with zipfile.ZipFile(package) as archive:
        assert archive.testzip() is None
        assert archive.read(patch.name) == patch.read_bytes(), 'łatka w archiwum się różni'

    result['package'] = str(package)
    result['package_bytes'] = package.stat().st_size
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest='command', required=True)

    make = commands.add_parser('build', help='zbuduj łatkę z oryginału i pliku wynikowego')
    make.add_argument('--original', type=Path, required=True)
    make.add_argument('--built', type=Path, required=True)
    make.add_argument('--out', type=Path, required=True)
    make.add_argument('--game-name', required=True)
    make.add_argument('--relative', required=True, help='ścieżka pliku wewnątrz katalogu gry')

    ship = commands.add_parser('release', help='zbuduj łatkę i złóż paczkę dla gracza')
    ship.add_argument('--original', type=Path, required=True)
    ship.add_argument('--built', type=Path, required=True)
    ship.add_argument('--readme', type=Path, required=True)
    ship.add_argument('--out-dir', type=Path, required=True)
    ship.add_argument('--game-name', required=True, help='slug gry, np. skate-story')
    ship.add_argument('--relative', required=True, help='ścieżka pliku wewnątrz katalogu gry')
    ship.add_argument('--package-name', required=True, help='nazwa paczki, np. Skate-Story')
    ship.add_argument('--version', required=True)

    use = commands.add_parser('apply', help='nałóż łatkę na własną kopię gry')
    use.add_argument('--game', type=Path, required=True, help='katalog gry')
    use.add_argument('--patch', type=Path, required=True)
    use.add_argument('--backup', type=Path, help='gdzie odłożyć oryginał przed podmianą')

    args = parser.parse_args()
    import json
    if args.command == 'build':
        result = build(args.original, args.built, args.out, args.game_name, args.relative)
    elif args.command == 'release':
        result = release(args.original, args.built, args.readme, args.out_dir,
                         args.game_name, args.relative, args.package_name, args.version)
    else:
        result = apply(args.game, args.patch, args.backup)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
