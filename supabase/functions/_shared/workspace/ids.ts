import type { EntryRef } from './types.ts';

/**
 * Klucz mapy dla pary (namespace, key). JSON tablicy jest jednoznaczny dla dowolnych
 * ciągów, więc nie ma kolizji jak przy sklejaniu separatorem (specyfikacja, „Wejście z repo”).
 * Tylko do użytku w pamięci — nie jest identyfikatorem w plikach ani w eksporcie.
 */
export function refId(ref: EntryRef): string {
  return JSON.stringify([ref.namespace, ref.key]);
}

export function sameRef(a: EntryRef, b: EntryRef): boolean {
  return a.namespace === b.namespace && a.key === b.key;
}

export function describeRef(ref: EntryRef): string {
  return ref.namespace ? `${ref.namespace} / ${ref.key}` : ref.key;
}
