#!/usr/bin/env python3
"""patch_artwork.py — add one artwork per chapter + 3 for 3026 column"""

MET = "Metropolitan Museum of Art, New York · Open Access"

# ── artwork registry ──────────────────────────────────────────────────────────
CHAPTER_ART = [
    # (ch_first_words, img_url, alt, credit_line, focal_point)
    (
        'The apartment is exactly the right temperature.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP273105.jpg',
        'Moonlight, Strandgade 30 by Vilhelm Hammershøi, 1900–1906',
        'Moonlight, Strandgade 30 · Vilhelm Hammershøi, 1900–1906 · ' + MET,
        'center center',
    ),
    (
        'Three days after the Facebook wall, he watched',
        'https://images.metmuseum.org/CRDImages/ep/original/DP355525.jpg',
        'A Maid Asleep by Johannes Vermeer, ca. 1656–57',
        'A Maid Asleep · Johannes Vermeer, ca. 1656–57 · ' + MET,
        'center 30%',
    ),
    (
        'The dream lasted longer than twelve minutes.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP145929.jpg',
        'Still Life with a Skull and a Writing Quill by Pieter Claesz, 1628',
        'Still Life with a Skull and a Writing Quill · Pieter Claesz, 1628 · ' + MET,
        'center center',
    ),
    (
        'I tried marijuana first.',
        'https://images.metmuseum.org/CRDImages/ep/original/DT1947.jpg',
        'Shoes by Vincent van Gogh, 1888',
        'Shoes · Vincent van Gogh, 1888 · ' + MET,
        'center center',
    ),
    (
        'She was asleep. I was looking at the ceiling.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP-25460-001.jpg',
        'A Woman Seated beside a Vase of Flowers by Edgar Degas, 1865',
        'A Woman Seated beside a Vase of Flowers · Edgar Degas, 1865 · ' + MET,
        'center top',
    ),
    (
        'I found it in an Austrian expat forum.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP-25461-001.jpg',
        'The Collector of Prints by Edgar Degas, 1866',
        'The Collector of Prints · Edgar Degas, 1866 · ' + MET,
        'center top',
    ),
    (
        'He had watched <em>The Island</em> again that evening.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP-31997-001-NEW.jpg',
        'Two Men Contemplating the Moon by Caspar David Friedrich, ca. 1825–30',
        'Two Men Contemplating the Moon · Caspar David Friedrich, ca. 1825–30 · ' + MET,
        'center 60%',
    ),
    (
        'This started in Kuala Lumpur.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP143209.jpg',
        'Vanitas Still Life by Jacques de Gheyn II, 1603',
        'Vanitas Still Life · Jacques de Gheyn II, 1603 · ' + MET,
        'center center',
    ),
    (
        'We went back to her apartment first.',
        'https://images.metmuseum.org/CRDImages/ep/original/DP-17680-001.jpg',
        'Woman with a Parrot by Gustave Courbet, 1866',
        'Woman with a Parrot · Gustave Courbet, 1866 · ' + MET,
        'center 25%',
    ),
    (
        'He had been reading about the Mandela Effect',
        'https://images.metmuseum.org/CRDImages/ep/original/DP-14201-023.jpg',
        'Oedipus and the Sphinx by Gustave Moreau, 1864',
        'Oedipus and the Sphinx · Gustave Moreau, 1864 · ' + MET,
        'center top',
    ),
]

ENTRY_ART = [
    # (prose_first_words, img_url, alt, credit_line)
    (
        'Before you go in, they don',
        'https://images.metmuseum.org/CRDImages/ep/original/DP-20339-001.jpg',
        'Pandora by Odilon Redon, ca. 1914',
        'Pandora · Odilon Redon, ca. 1914 · ' + MET,
    ),
    (
        'One hundred thousand years ',
        'https://images.metmuseum.org/CRDImages/ep/original/DP375450_cropped.jpg',
        'Circus Sideshow (Parade de cirque) by Georges Seurat, 1887–88',
        'Circus Sideshow (Parade de cirque) · Georges Seurat, 1887–88 · ' + MET,
    ),
    (
        'Duration: 4 minutes, 12 sec',
        'https://images.metmuseum.org/CRDImages/ep/original/DT1029.jpg',
        'The Gulf of Marseille Seen from L\'Estaque by Paul Cézanne, ca. 1885',
        'The Gulf of Marseille Seen from L’Estaque · Paul Cézanne, ca. 1885 · ' + MET,
    ),
]


def chapter_figure(img_url, alt, credit, focal):
    return (
        f'        <figure class="ch-art">\n'
        f'          <img src="{img_url}" alt="{alt}" loading="lazy" style="object-position:{focal};">\n'
        f'          <figcaption>{credit}</figcaption>\n'
        f'        </figure>\n'
    )


def entry_figure(img_url, alt, credit):
    return (
        f'          <figure class="ch-art ch-art--entry">\n'
        f'            <img src="{img_url}" alt="{alt}" loading="lazy">\n'
        f'            <figcaption>{credit}</figcaption>\n'
        f'          </figure>\n'
    )


with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# ── CSS ──────────────────────────────────────────────────────────────────────
OLD_CSS = '    .ch-image{display:block;width:100%;height:auto;margin-bottom:0;}'
NEW_CSS = (
    '    .ch-image{display:block;width:100%;height:auto;margin-bottom:0;}\n'
    '    .ch-art{margin:0 0 1.4rem;border:1px solid var(--rule);}'
    '.ch-art img{display:block;width:100%;height:200px;object-fit:cover;}'
    '.ch-art figcaption{padding:5px 10px 6px;font-family:var(--mono);'
    'font-size:0.5625rem;letter-spacing:0.06em;color:var(--faint);'
    'border-top:1px solid var(--rule);}\n'
    '    .ch-art--entry img{height:140px;}'
)
c = html.count(OLD_CSS)
print(f'CSS: {c}')
if c == 1:
    html = html.replace(OLD_CSS, NEW_CSS, 1)
    changes += 1

# ── chapters ─────────────────────────────────────────────────────────────────
for first_words, img_url, alt, credit, focal in CHAPTER_ART:
    # anchor: prose div + first-p opening
    old = f'<div class="prose">\n        <p class="first">{first_words}'
    new = (
        '<div class="prose">\n'
        + chapter_figure(img_url, alt, credit, focal)
        + f'        <p class="first">{first_words}'
    )
    c = html.count(old)
    mark = '✓' if c == 1 else f'✗({c})'
    print(f'{mark} chapter: {first_words[:40]}')
    if c == 1:
        html = html.replace(old, new, 1)
        changes += 1

# ── 3026 entries ──────────────────────────────────────────────────────────────
for first_words, img_url, alt, credit in ENTRY_ART:
    old = f'<div class="prose">\n          <p>{first_words}'
    new = (
        '<div class="prose">\n'
        + entry_figure(img_url, alt, credit)
        + f'          <p>{first_words}'
    )
    c = html.count(old)
    mark = '✓' if c == 1 else f'✗({c})'
    print(f'{mark} 3026 entry: {first_words[:40]}')
    if c == 1:
        html = html.replace(old, new, 1)
        changes += 1

# ── write ─────────────────────────────────────────────────────────────────────
print(f'\nTotal changes: {changes}/14')
with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Written. {len(html):,} chars')
