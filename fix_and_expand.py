#!/usr/bin/env python3
# fix page bleed + add 3026 "Before" entry
# NEVER use Edit tool on index.html — it corrupts ASCII quotes to curly quotes

PATH = '/Users/nonarkara/Projects/100daysofnon/site/index.html'

with open(PATH, 'rb') as f:
    s = f.read().decode('utf-8')

changes = 0

# ── 1. CSS: ch-viewport — remove flex:1/min-height, let JS control height ──
old = '.ch-viewport{flex:1;overflow:hidden;min-height:0;}'
new = '.ch-viewport{flex:0 0 auto;overflow:hidden;}'
assert old in s, f'NOT FOUND: {old!r}'
s = s.replace(old, new, 1); changes += 1
print('1. ch-viewport CSS ✓')

# ── 2. CSS: ch-track — remove height:100% so track grows to content ────────
old = '.ch-track{display:flex;align-items:flex-start;height:100%;will-change:transform;transition:transform 0.38s cubic-bezier(0.4,0,0.2,1);}'
new = '.ch-track{display:flex;align-items:flex-start;will-change:transform;transition:transform 0.38s cubic-bezier(0.4,0,0.2,1);}'
assert old in s, f'NOT FOUND: {old!r}'
s = s.replace(old, new, 1); changes += 1
print('2. ch-track CSS ✓')

# ── 3. CSS: ch-page — remove height:auto;max-height:100%, JS sets height ───
old = '.ch-page{flex:0 0 100%;width:100%;height:auto;max-height:100%;overflow-y:auto;padding:1.4rem clamp(1.1rem,3vw,2.2rem) 2.5rem;-webkit-overflow-scrolling:touch;}'
new = '.ch-page{flex:0 0 100%;width:100%;overflow-y:auto;padding:1.4rem clamp(1.1rem,3vw,2.2rem) 2.5rem;-webkit-overflow-scrolling:touch;}'
assert old in s, f'NOT FOUND: {old!r}'
s = s.replace(old, new, 1); changes += 1
print('3. ch-page CSS ✓')

# ── 4. JS: insert setVpH function before goTo ──────────────────────────────
SET_VP_H = '''      function setVpH(){
        var vp=document.querySelector('.ch-viewport');
        var novel=document.querySelector('.col.novel');
        var hdr=document.querySelector('.ch-header');
        var nav=document.querySelector('.ch-pgnav');
        if(!vp||!novel||!hdr||!nav||!pages[cur]) return;
        pages[cur].style.height='';
        var avail=novel.clientHeight-hdr.offsetHeight-nav.offsetHeight;
        var content=pages[cur].scrollHeight;
        var h=Math.min(content,Math.max(avail,80));
        vp.style.height=h+'px';
        pages[cur].style.height=h+'px';
      }
      '''

old = '      function goTo(n){'
new = SET_VP_H + 'function goTo(n){'
assert old in s, f'NOT FOUND: {old!r}'
s = s.replace(old, new, 1); changes += 1
print('4. setVpH inserted ✓')

# ── 5. JS: add requestAnimationFrame(setVpH) at end of goTo body ───────────
old = "          a.style.color=i===cur?'var(--amber)':'';\n        });\n      }\n      prevBtn.addEventListener"
new = "          a.style.color=i===cur?'var(--amber)':'';\n        });\n        requestAnimationFrame(setVpH);\n      }\n      prevBtn.addEventListener"
assert old in s, f'NOT FOUND: {old!r}'
s = s.replace(old, new, 1); changes += 1
print('5. RAF call in goTo ✓')

# ── 6. JS: add window load + resize listeners after goTo(0) ────────────────
old = '      goTo(0);\n    }\n  })();'
new = ('      goTo(0);\n'
       '      window.addEventListener(\'load\',setVpH);\n'
       '      window.addEventListener(\'resize\',function(){requestAnimationFrame(setVpH);});\n'
       '    }\n'
       '  })();')
assert old in s, f'NOT FOUND: {old!r}'
s = s.replace(old, new, 1); changes += 1
print('6. window listeners ✓')

# ── 7. New 3026 entry: "The City That Replaced Bangkok · Before" ───────────
NEW_ENTRY = '''      <div class="entry">
        <p class="when">The City That Replaced Bangkok &middot; Before</p>
        <div class="prose">
          <p>She had seen him in the corridor three times before they spoke. This is typical of 3026. Spatial proximity and social distance coexist without contradiction. You can live beside someone for a year and achieve something that looks exactly like not knowing them.</p>

          <p>The first time, she was carrying a supplement pack. He was looking at his hands in a way she recognized.</p>

          <p>The second time, he was at the window at 4am. She does not know why she was also at the window at 4am. The city outside is always the same. The machine has decided that light variation is suboptimal, so the city holds an even 6000 Kelvin at all hours. The only exception is between three and five in the morning, when usage drops and the streets dim slightly. He was watching this. She was watching this. Neither of them said anything.</p>

          <p>The third time, he asked her when she was planning to go back.</p>

          <p>He meant the hub. Everyone means the hub.</p>

          <p>She said she had not decided. He said he had been thinking of going back soon. She asked what version of the world he had been in. He said 2026, Bangkok. She said she had been in the same run. He said he knew. She asked how. He said: you were the one on the bicycle.</p>

          <p>She had not expected him to say that.</p>

          <p>You are only ever assigned roles in the simulation. The role is played by you but it is not you &#x2014; the machine decides the assignment based on whatever it is modeling. She had not chosen to be the vegetable seller. She had not known he would be the boy at the gate. She had been in character, fully, as the machine requires. But something had passed through the role anyway. Something that the machine logs as an anomaly and she logs as the reason she keeps going back.</p>

          <p>She asked him: what did you feel?</p>

          <p>He said: I recognized you.</p>

          <p>She picked up her supplement. She said she would probably go back next week.</p>

          <p>He said: I&#x2019;ll be in forty-four.</p>

          <p>She went back the following Thursday.</p>
        </div>
      </div>

      '''

PANEL_ANCHOR = '      <div class="entry">\n        <p class="when">The Hub &middot; Room 7 &middot; The Panel</p>'
assert PANEL_ANCHOR in s, f'NOT FOUND: panel anchor'
s = s.replace(PANEL_ANCHOR, NEW_ENTRY + PANEL_ANCHOR, 1); changes += 1
print('7. "Before" entry inserted ✓')

with open(PATH, 'wb') as f:
    f.write(s.encode('utf-8'))

print(f'\nAll {changes} changes applied.')
