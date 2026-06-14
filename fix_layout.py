#!/usr/bin/env python3
"""Fix the malformed header that causes all chapters to lay out horizontally.

Root cause: The lang-toggle's style attribute is never closed — the <div class="timeline">
tag got consumed into the style value, so the real timeline div never existed.
All chapter-blocks became flex children of .lh-row (display:flex) → horizontal 10-column layout.

Fix:
1. Replace malformed header block with proper closed header + lang buttons
2. Wrap chapter-blocks in <div class="timeline"> … </div>
"""

with open('site/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. Fix the malformed header ──────────────────────────────────────────────
# The bad block starts at the lh header and ends just before <div class="chapter-block" id="ch1">
BROKEN_HEADER = '<header class="lh">\n    <div class="lh-row">\n      <div class="lang-toggle" role="group" aria-label="Language" style="margin-left:auto; disp<div class="timeline">\n\n    <div class="chapter-block" id="ch1">'

FIXED_HEADER = '''<header class="lh">
  <div class="lh-row">
    <div class="lang-toggle" role="group" aria-label="Language">
      <button class="lang-btn" data-lang="en" aria-pressed="true">EN</button>
      <button class="lang-btn" data-lang="th" aria-pressed="false">TH</button>
      <button class="lang-btn" data-lang="zh" aria-pressed="false">ZH</button>
    </div>
  </div>
</header>

<div class="timeline">

    <div class="chapter-block" id="ch1">'''

if BROKEN_HEADER not in html:
    print("ERROR: Broken header pattern not found. Dumping search area:")
    idx = html.find('<header class="lh">')
    print(repr(html[idx:idx+400]))
    exit(1)

html = html.replace(BROKEN_HEADER, FIXED_HEADER, 1)
print("✓ Header fixed")

# ── 2. Close the timeline div ────────────────────────────────────────────────
# The chapter blocks used to end and then there's a section with ch-pgbtn etc.
# We need </div> to close .timeline before the footer.
# Find the </section> or the </div> that closes the old chapter nav wrapper.
# Looking at the structure: after last chapter-block there's a section with ch-pgbtn,
# then </div>, then <footer>. We close timeline before <footer>.

BEFORE_FOOTER = '  <footer class="lf">'
if BEFORE_FOOTER not in html:
    print("ERROR: footer not found")
    exit(1)

html = html.replace(BEFORE_FOOTER, '</div><!-- /.timeline -->\n\n  <footer class="lf">', 1)
print("✓ Timeline closing div added before footer")

# ── 3. Remove old dual-column split JS (no longer needed) ────────────────────
# Find the old split/v-rec/v-nov script block
import re
# The old script starts with (function(){ var split=document.getElementById('split');
old_split_pattern = r"\(function\(\)\{\s*var split=document\.getElementById\('split'\);.*?set\('record'\);\s*\}\(\)\);"
match = re.search(old_split_pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + html[match.end():]
    print("✓ Old split JS removed")
else:
    print("  (old split JS not found — may already be gone)")

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nDone. File length: {len(html):,} chars")

# Quick sanity: count chapter-blocks
blocks = len(re.findall(r'class="chapter-block"', html))
print(f"Chapter blocks found: {blocks}")

# Check timeline opens/closes
tl_open = html.count('<div class="timeline">')
tl_close = html.count('<!-- /.timeline -->')
print(f"Timeline opens: {tl_open}, closes: {tl_close}")

# Check lang buttons
lang_btns = html.count('class="lang-btn"')
print(f"Lang buttons: {lang_btns}")

# Check no broken style attribute
broken = 'style="margin-left:auto; disp<div' in html
print(f"Broken style attribute: {broken}")
