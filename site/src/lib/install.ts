/**
 * Guzik „zainstaluj": spolszczenie trafia do katalogu gry prosto z przeglądarki.
 *
 * Dwa rodzaje gier, ten sam kod aż do ostatniego kroku:
 * - pluginowe (zip): pliki z paczki zapisujemy w katalogu gry,
 * - deltowe (patch): czytamy plik gracza, nakładamy łatkę i zapisujemy wynik.
 *
 * Łatka to format 2 z tools/patch.py — ten sam, który nakłada NieGesiPatch.exe
 * (tools/applier/NieGesiPatch.cs). Zmiana formatu to zmiana we wszystkich trzech.
 *
 * Wymaga File System Access API z zapisem, czyli Chrome albo Edge. Katalogów
 * w Program Files przeglądarka nie udostępnia wcale — wtedy zostaje zwykłe pobranie.
 */

export type Report = (message: string) => void;

export interface Outcome {
  state: 'done' | 'already';
  message: string;
  written: string[];
  backups: string[];
}

export class InstallError extends Error {}

const BACKUP_SUFFIX = '.przed-spolszczeniem';
/** Pliki z paczki, których nie kładziemy w katalogu gry — to instrukcja dla gracza. */
const SKIP = new Set(['READ-ME.txt']);

declare global {
  interface Window {
    showDirectoryPicker?: (options?: {
      id?: string;
      mode?: 'read' | 'readwrite';
      startIn?: string;
    }) => Promise<FileSystemDirectoryHandle>;
  }
}

export function installSupported(): boolean {
  return typeof window !== 'undefined' && typeof window.showDirectoryPicker === 'function';
}

// --- Bajty -----------------------------------------------------------------

async function inflateRaw(data: Uint8Array): Promise<Uint8Array> {
  const stream = new Blob([data as Uint8Array<ArrayBuffer>]).stream().pipeThrough(new DecompressionStream('deflate-raw'));
  return new Uint8Array(await new Response(stream).arrayBuffer());
}

export async function sha256(data: Uint8Array): Promise<string> {
  const digest = new Uint8Array(await crypto.subtle.digest('SHA-256', data as Uint8Array<ArrayBuffer>));
  return Array.from(digest, (byte) => byte.toString(16).padStart(2, '0')).join('');
}

function same(a: Uint8Array, b: Uint8Array): boolean {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
  return true;
}

function files(count: number): string {
  const tens = count % 100;
  const form = count === 1 ? 'plik' : [2, 3, 4].includes(count % 10) && !(tens >= 12 && tens <= 14) ? 'pliki' : 'plików';
  return `${count} ${form}`;
}

// --- Zip -------------------------------------------------------------------

export interface ZipEntry {
  name: string;
  read: () => Promise<Uint8Array>;
}

/** Czytnik zip wystarczający na nasze paczki: stored albo deflate, bez zip64. */
export function readZip(buffer: ArrayBuffer): ZipEntry[] {
  const bytes = new Uint8Array(buffer);
  const view = new DataView(buffer);
  const decoder = new TextDecoder();

  let end = -1;
  for (let at = bytes.length - 22; at >= Math.max(0, bytes.length - 22 - 65535); at--) {
    if (view.getUint32(at, true) === 0x06054b50) {
      end = at;
      break;
    }
  }
  if (end < 0) throw new InstallError('Pobrana paczka nie jest poprawnym archiwum ZIP.');

  const count = view.getUint16(end + 10, true);
  let at = view.getUint32(end + 16, true);
  const entries: ZipEntry[] = [];

  for (let i = 0; i < count; i++) {
    if (view.getUint32(at, true) !== 0x02014b50) throw new InstallError('Uszkodzony spis archiwum ZIP.');
    const method = view.getUint16(at + 10, true);
    const compressed = view.getUint32(at + 20, true);
    const size = view.getUint32(at + 24, true);
    const nameLength = view.getUint16(at + 28, true);
    const extraLength = view.getUint16(at + 30, true);
    const commentLength = view.getUint16(at + 32, true);
    const local = view.getUint32(at + 42, true);
    const name = decoder.decode(bytes.subarray(at + 46, at + 46 + nameLength));
    at += 46 + nameLength + extraLength + commentLength;

    if (name.endsWith('/')) continue;
    const start = local + 30 + view.getUint16(local + 26, true) + view.getUint16(local + 28, true);
    const raw = bytes.subarray(start, start + compressed);

    entries.push({
      name,
      read: async () => {
        const data = method === 0 ? raw : method === 8 ? await inflateRaw(raw) : null;
        if (!data) throw new InstallError(`Nieobsługiwana kompresja w pliku ${name}.`);
        if (data.length !== size) throw new InstallError(`Uszkodzony plik w archiwum: ${name}.`);
        return data;
      },
    });
  }
  return entries;
}

// --- Łatka -------------------------------------------------------------------

export interface Patch {
  header: Record<string, string>;
  payload: Uint8Array;
}

export function readPatch(buffer: ArrayBuffer): Patch {
  const bytes = new Uint8Array(buffer);
  let split = -1;
  for (let i = 0; i + 1 < bytes.length; i++) {
    if (bytes[i] === 10 && bytes[i + 1] === 10) {
      split = i;
      break;
    }
  }
  const lines = split > 0 ? new TextDecoder().decode(bytes.subarray(0, split)).split('\n') : [];
  if (lines[0] !== 'NIEGESI-PATCH') throw new InstallError('Pobrany plik nie jest łatką Nie gęsi.');

  const header: Record<string, string> = {};
  for (const line of lines.slice(1)) {
    const space = line.indexOf(' ');
    if (space > 0) header[line.slice(0, space)] = line.slice(space + 1);
  }
  if (header.format !== '2') throw new InstallError(`Nieznana wersja formatu łatki: ${header.format}.`);
  return { header, payload: bytes.subarray(split + 2) };
}

/** Nakłada operacje łatki na oryginał. Lustro `run` z tools/patch.py. */
export async function applyPatch(source: Uint8Array, patch: Patch): Promise<Uint8Array> {
  const ops = await inflateRaw(patch.payload);
  const size = Number(patch.header['target-size']);
  const output = new Uint8Array(size);
  let at = 0;
  let written = 0;
  let cursor = 0;

  const varint = () => {
    let value = 0;
    let scale = 1;
    for (;;) {
      const byte = ops[at++]!;
      // Mnożenie zamiast przesunięć bitowych: pliki gier bywają większe niż 2 GB.
      value += (byte & 0x7f) * scale;
      scale *= 128;
      if (!(byte & 0x80)) return value;
    }
  };

  for (;;) {
    const op = ops[at++];
    if (op === 0) break;
    const length = varint();
    if (written + length > size) throw new InstallError('Łatka daje za duży plik.');
    if (op === 1) {
      const delta = varint();
      const origin = cursor + (delta % 2 === 0 ? delta / 2 : -(delta + 1) / 2);
      if (origin < 0 || origin + length > source.length) throw new InstallError('Łatka sięga poza oryginał.');
      output.set(source.subarray(origin, origin + length), written);
      cursor = origin + length;
    } else if (op === 2) {
      output.set(ops.subarray(at, at + length), written);
      at += length;
    } else {
      throw new InstallError(`Nieznana operacja w łatce: ${op}.`);
    }
    written += length;
  }
  if (written !== size) throw new InstallError('Łatka dała plik innej długości niż powinna.');
  return output;
}

// --- Katalog gry -------------------------------------------------------------

async function fileIn(
  root: FileSystemDirectoryHandle,
  path: string,
  create: boolean,
): Promise<FileSystemFileHandle | null> {
  const parts = path.split('/').filter(Boolean);
  let directory = root;
  try {
    for (const part of parts.slice(0, -1)) directory = await directory.getDirectoryHandle(part, { create });
    return await directory.getFileHandle(parts[parts.length - 1]!, { create });
  } catch (error) {
    if (!create && error instanceof DOMException && error.name === 'NotFoundError') return null;
    throw error;
  }
}

async function readFile(handle: FileSystemFileHandle): Promise<Uint8Array> {
  return new Uint8Array(await (await handle.getFile()).arrayBuffer());
}

async function writeFile(handle: FileSystemFileHandle, data: Uint8Array): Promise<void> {
  // Chrome pisze do pliku tymczasowego i podmienia go dopiero przy close() —
  // przerwanie w połowie nie zostawia w grze uszkodzonego pliku.
  const writable = await handle.createWritable();
  await writable.write(data as Uint8Array<ArrayBuffer>);
  await writable.close();
}

/** Oryginał odkładamy obok tylko raz — kolejne instalacje nie nadpiszą go naszą wersją. */
async function backup(root: FileSystemDirectoryHandle, path: string, data: Uint8Array): Promise<string | null> {
  const target = path + BACKUP_SUFFIX;
  if (await fileIn(root, target, false)) return null;
  await writeFile((await fileIn(root, target, true))!, data);
  return target;
}

export async function pickGameFolder(slug: string, marker: string): Promise<FileSystemDirectoryHandle> {
  const root = await window.showDirectoryPicker!({ id: `niegesi-${slug}`, mode: 'readwrite' });
  if (!(await fileIn(root, marker, false))) {
    throw new InstallError(
      `W katalogu „${root.name}" nie ma pliku ${marker}. Wskaż katalog, w którym leży gra.`,
    );
  }
  return root;
}

async function download(url: string, report: Report): Promise<ArrayBuffer> {
  report('Pobieram spolszczenie…');
  const response = await fetch(url);
  if (!response.ok) throw new InstallError(`Nie udało się pobrać paczki (HTTP ${response.status}).`);
  return response.arrayBuffer();
}

export async function installZip(root: FileSystemDirectoryHandle, url: string, report: Report): Promise<Outcome> {
  const entries = readZip(await download(url, report)).filter((entry) => !SKIP.has(entry.name));
  const written: string[] = [];
  const backups: string[] = [];

  for (const [index, entry] of entries.entries()) {
    report(`Zapisuję pliki ${index + 1}/${entries.length}…`);
    const data = await entry.read();
    const existing = await fileIn(root, entry.name, false);
    if (existing) {
      const current = await readFile(existing);
      if (same(current, data)) continue;
      const saved = await backup(root, entry.name, current);
      if (saved) backups.push(saved);
    }
    await writeFile(existing ?? (await fileIn(root, entry.name, true))!, data);
    written.push(entry.name);
  }

  if (written.length === 0) {
    return { state: 'already', message: 'Spolszczenie jest już wgrane — wszystkie pliki się zgadzają.', written, backups };
  }
  return { state: 'done', message: `Gotowe. Zapisano w katalogu gry: ${files(written.length)}.`, written, backups };
}

export async function installPatch(root: FileSystemDirectoryHandle, url: string, report: Report): Promise<Outcome> {
  const patch = readPatch(await download(url, report));
  const path = patch.header.file!;
  const handle = await fileIn(root, path, false);
  if (!handle) throw new InstallError(`W katalogu gry nie ma pliku ${path}.`);

  report('Sprawdzam sumę kontrolną pliku gry…');
  const source = await readFile(handle);
  const digest = await sha256(source);
  if (digest === patch.header['target-sha256']) {
    return { state: 'already', message: 'Spolszczenie jest już wgrane.', written: [], backups: [] };
  }
  if (digest !== patch.header['source-sha256']) {
    throw new InstallError(
      'Ten plik gry nie jest tym, pod który zrobiono łatkę — gra jest w innej wersji albo plik był już zmieniany. Nic nie zostało zapisane.',
    );
  }

  report('Nakładam łatkę…');
  const result = await applyPatch(source, patch);
  if ((await sha256(result)) !== patch.header['target-sha256']) {
    throw new InstallError('Odtworzony plik ma inną sumę kontrolną niż powinien. Nic nie zostało zapisane.');
  }

  report('Zapisuję…');
  const saved = await backup(root, path, source);
  await writeFile(handle, result);
  return {
    state: 'done',
    message: 'Gotowe. Spolszczenie wgrane.',
    written: [path],
    backups: saved ? [saved] : [],
  };
}
