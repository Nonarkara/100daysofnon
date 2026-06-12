# -*- coding: utf-8 -*-
"""patch_translate.py
Replace plain <p>TEXT</p> paragraphs in the 3026 record column with
trilingual <p lang="en/th/zh"> triplets.
"""
import json, re

def encode(text):
    text = text.replace('&', '&amp;')
    text = text.replace('—', '&#x2014;')
    text = text.replace('’', '&#x2019;')
    text = text.replace('‘', '&#x2018;')
    text = text.replace('“', '&#x201C;')
    text = text.replace('”', '&#x201D;')
    return text

with open('/Users/nonarkara/Projects/100daysofnon/translations_recovered.json', encoding='utf-8') as f:
    translations = json.load(f)
with open('/Users/nonarkara/Projects/100daysofnon/to_translate.json', encoding='utf-8') as f:
    source = json.load(f)
with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', encoding='utf-8') as f:
    html = f.read()

# Build a lookup: when -> (paragraphs_th, paragraphs_zh)
tr_map = {e['when']: e for e in translations}
src_map = {e['when']: e['paragraphs'] for e in source}

original_len = len(html)
total_replacements = 0

for entry_when, src_paragraphs in src_map.items():
    tr = tr_map.get(entry_when)
    if not tr:
        print(f"  MISSING translation for: {entry_when[:50]}")
        continue

    paragraphs_th = tr['paragraphs_th']
    paragraphs_zh = tr['paragraphs_zh']

    if len(src_paragraphs) != len(paragraphs_th) or len(src_paragraphs) != len(paragraphs_zh):
        print(f"  COUNT MISMATCH: {entry_when[:50]}  src:{len(src_paragraphs)} th:{len(paragraphs_th)} zh:{len(paragraphs_zh)}")
        continue

    # Find the entry in the HTML by its <p class="when"> text
    when_tag = f'<p class="when">{entry_when}</p>'
    entry_pos = html.find(when_tag)
    if entry_pos == -1:
        print(f"  NOT FOUND in HTML: {entry_when[:50]}")
        continue

    # Find prose div start after the when tag
    prose_start = html.find('<div class="prose">', entry_pos)
    # Find closing </div> of prose — the entry closing div
    prose_end = html.find('        </div>', prose_start)

    # Extract the prose content between prose div open and close
    open_tag = '<div class="prose">'
    prose_content_start = html.find(open_tag, entry_pos) + len(open_tag)
    prose_content = html[prose_content_start:prose_end]

    # Build new prose content: replace each plain <p>TEXT</p> with trilingual triplet
    new_prose = prose_content
    replaced = 0

    for i, (src_p, th_p, zh_p) in enumerate(zip(src_paragraphs, paragraphs_th, paragraphs_zh)):
        # The source paragraph text may contain HTML entities — match exactly
        old_tag = f'          <p>{src_p}</p>'
        new_tag = (
            f'          <p lang="en">{src_p}</p>\n'
            f'          <p lang="th">{encode(th_p)}</p>\n'
            f'          <p lang="zh">{encode(zh_p)}</p>'
        )
        if old_tag in new_prose:
            new_prose = new_prose.replace(old_tag, new_tag, 1)
            replaced += 1
        else:
            # Try with 10-space indent (some entries)
            old_tag_10 = f'          <p>{src_p}</p>'
            if old_tag_10 in new_prose:
                new_prose = new_prose.replace(old_tag_10, new_tag, 1)
                replaced += 1
            else:
                print(f"    Para {i} not found verbatim in entry: {src_p[:60]}")

    # Replace the prose content in the full html
    html = html[:prose_content_start] + new_prose + html[prose_end:]
    total_replacements += replaced
    print(f"  {replaced:2d}/{len(src_paragraphs)} replaced  {entry_when[:55]}")

print(f"\nOriginal: {original_len:,} → New: {len(html):,} (+{len(html)-original_len:,})")
print(f"Total paragraph triplets written: {total_replacements}")

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Written.")
