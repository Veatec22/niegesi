"""Resumable EN->PL draft only. Production source is curated separately.

Uses Google's public translation endpoint, sending only untranslated game strings.
No keys, file paths, user data, credentials or existing authored translations sent.
"""
import concurrent.futures
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'work/machine-draft.json'
TOKEN = re.compile(r'<[^>]+>|\{[^}]+\}|\*\w+\*|\*\*')


def translate(text):
    tokens = []
    def protect(m):
        tokens.append(m.group())
        return f' ZZX{len(tokens)-1:04d}XZZ '
    query = TOKEN.sub(protect, text)
    url = 'https://translate.googleapis.com/translate_a/single?' + urllib.parse.urlencode(
        dict(client='gtx', sl='en', tl='pl', dt='t', q=query))
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=35) as response:
                data = json.load(response)
            result = ''.join(part[0] or '' for part in data[0])
            found = re.findall(r'ZZX\s*(\d{4})\s*XZZ', result, re.I)
            assert found == [f'{i:04d}' for i in range(len(tokens))], 'Token loss'
            result = re.sub(r' ?ZZX\s*(\d{4})\s*XZZ ?', lambda m: tokens[int(m[1])], result, flags=re.I)
            assert TOKEN.findall(result) == TOKEN.findall(text)
            return result
        except Exception:
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)


def main():
    rows = json.loads((ROOT / 'translations/en-pl-review.json').read_text(encoding='utf-8'))
    pl = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    cache = json.loads(CACHE.read_text(encoding='utf-8')) if CACHE.exists() else {}
    pending = list(dict.fromkeys(r['english'] for r in rows if r['key'] not in pl and not r['polish'] and r['english'] not in cache))
    print(f'Pending unique strings: {len(pending)}', flush=True)
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs = {pool.submit(translate, text): text for text in pending}
        for i, job in enumerate(concurrent.futures.as_completed(jobs), 1):
            source = jobs[job]
            try:
                cache[source] = job.result()
            except Exception as exc:
                failures.append({'english': source, 'error': str(exc)})
            if i % 25 == 0 or i == len(jobs):
                CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
                print(f'{i}/{len(jobs)} processed, {len(failures)} failures', flush=True)
    (ROOT / 'work/machine-failures.json').write_text(json.dumps(failures, ensure_ascii=False, indent=2), encoding='utf-8')


if __name__ == '__main__':
    main()
