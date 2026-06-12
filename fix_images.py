import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make TOC horizontal
html = html.replace('.ch-nav-label{grid-column:1 / -1;display:block;', '.ch-nav-label{display:none;')
html = html.replace('.ch-nav-item{display:block;', '.ch-nav-item{display:inline-block;white-space:nowrap;background:var(--rule);padding:0.3rem 0.6rem;border-radius:4px;')
html = html.replace('.ch-header .ch-nav{margin:0.8rem 0 0;}', '.ch-header .ch-nav{margin:0.8rem 0 0;display:flex;overflow-x:auto;gap:0.5rem;padding-bottom:0.5rem;scrollbar-width:none;}\n    .ch-header .ch-nav::-webkit-scrollbar{display:none;}')

# Inject images
ch_map = {
    'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
    'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10
}

def inject_image(match):
    full_match = match.group(1)
    ch_text = match.group(2)
    ch_num = ch_map.get(ch_text, 1)
    img_tag = f'\n      <figure class="ch-art" style="margin: 1.5rem 0;"><img src="./images/v5_2026_ch_{ch_num}.png" alt="2026 Scene" loading="lazy" style="width:100%; border-radius:4px; border:1px solid var(--rule);"></figure>'
    return full_match + img_tag

# Only do this if we haven't already injected the v5 images
if 'v5_2026_ch_' not in html:
    html = re.sub(r'(<p class="chapter-mark">Chapter (One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten).*?</p>)', inject_image, html)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
