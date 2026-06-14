#!/usr/bin/env python3
"""Add audio field to ch1 in JSON, add audio player to build.py."""
import json, re
from pathlib import Path

ROOT = Path(__file__).parent

# ── 1. JSON: add audio src to ch1 ────────────────────────────────────────────
with open(ROOT / 'data' / 'two-layers.json', encoding='utf-8') as f:
    data = json.load(f)

data['chapters'][0]['audio'] = './assets/artifacts/ch1-narration-cloned.mp3'

with open(ROOT / 'data' / 'two-layers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('✓ JSON updated')

# ── 2. build.py: add audio CSS + render_chapter audio block ──────────────────
with open(ROOT / 'build.py', encoding='utf-8') as f:
    src = f.read()

# Add audio CSS before the artifact_css() call placeholder
AUDIO_CSS = '''
    /* Audio player */
    .ch-audio-bar {{
      display:flex; align-items:center; gap:0.75rem;
      padding:0.7rem 1.2rem; border-top:1px solid var(--rule);
      background:var(--paper); flex:0 0 auto;
    }}
    body.view-3026 .ch-audio-bar {{ background:var(--bg); border-color:#333; }}
    .audio-play-btn {{
      font-family:var(--mono); font-size:0.6rem; letter-spacing:0.12em;
      text-transform:uppercase; background:transparent;
      border:1px solid var(--ink); color:var(--ink);
      padding:0.3rem 0.7rem; cursor:pointer; flex:0 0 auto; line-height:1;
    }}
    body.view-3026 .audio-play-btn {{ border-color:#fff; color:#fff; }}
    .audio-play-btn:hover {{ background:var(--accent); border-color:var(--accent); color:#000; }}
    .audio-progress {{
      flex:1; height:2px; background:var(--rule); cursor:pointer; position:relative;
    }}
    body.view-3026 .audio-progress {{ background:#333; }}
    .audio-progress-fill {{
      height:100%; background:var(--accent); width:0%; pointer-events:none;
    }}
    .audio-time {{
      font-family:var(--mono); font-size:0.55rem; color:var(--soft);
      letter-spacing:0.08em; white-space:nowrap; flex:0 0 auto;
    }}
    body.view-3026 .audio-time {{ color:#888; }}
'''

# Insert CSS before the artifact_css() return in render_html
OLD_CSS_BLOCK = "    {artifact_css()}"
NEW_CSS_BLOCK = AUDIO_CSS + "    {artifact_css()}"
src = src.replace(OLD_CSS_BLOCK, NEW_CSS_BLOCK, 1)
print('✓ CSS inserted')

# Update render_chapter to output audio bar when chapter has audio
OLD_RENDER_SIG = "def render_chapter(ch, is_first=False):"
OLD_ARTICLE_END = "</article>\n'''"

NEW_ARTICLE_END = """  {audio_bar}
</article>
'''"""

# Replace the article close
src = src.replace(
    '  </article>\n\'\'\'',
    '  {audio_bar}\n</article>\n\'\'\'',
    1
)

# Replace the f-string dict to add audio_bar var
OLD_FSTRING_RETURN = "    cls = 'chapter-page active' if is_first else 'chapter-page'\n    return f'''"
NEW_FSTRING_RETURN = """    cls = 'chapter-page active' if is_first else 'chapter-page'
    audio_src = ch.get('audio', '')
    if audio_src:
        audio_bar = f'''<div class="ch-audio-bar" id="audio-bar-{ch_id}">
    <audio id="ch-audio-{ch_id}" src="{audio_src}" preload="none"></audio>
    <button class="audio-play-btn" data-audio="ch-audio-{ch_id}" aria-label="Play narration">&#9654; PLAY</button>
    <div class="audio-progress" data-audio="ch-audio-{ch_id}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
      <div class="audio-progress-fill" id="fill-{ch_id}"></div>
    </div>
    <span class="audio-time" id="atime-{ch_id}">0:00</span>
  </div>'''
    else:
        audio_bar = ''
    return f'''"""

src = src.replace(OLD_FSTRING_RETURN, NEW_FSTRING_RETURN, 1)
print('✓ render_chapter updated')

# ── 3. Add audio JS before the closing </body> in the HTML template ───────────
AUDIO_JS = """
  <script>
  // ── AUDIO PLAYER ────────────────────────────────────────────────────────
  (function() {{
    function fmt(s) {{
      s = Math.floor(s || 0);
      return Math.floor(s/60) + ':' + String(s%60).padStart(2,'0');
    }}
    document.querySelectorAll('.audio-play-btn').forEach(function(btn) {{
      var id  = btn.getAttribute('data-audio');
      var aud = document.getElementById(id);
      var bar = document.querySelector('.audio-progress[data-audio="'+id+'"]');
      var fill = bar ? bar.querySelector('.audio-progress-fill') : null;
      var timeEl = btn.closest('.ch-audio-bar').querySelector('.audio-time');
      if (!aud) return;

      btn.addEventListener('click', function() {{
        if (aud.paused) {{ aud.play(); btn.innerHTML = '&#9646;&#9646; PAUSE'; }}
        else {{ aud.pause(); btn.innerHTML = '&#9654; PLAY'; }}
      }});
      aud.addEventListener('ended', function() {{ btn.innerHTML = '&#9654; PLAY'; if(fill) fill.style.width='0%'; }});
      aud.addEventListener('timeupdate', function() {{
        if (!aud.duration) return;
        var pct = (aud.currentTime / aud.duration) * 100;
        if (fill) fill.style.width = pct + '%';
        if (bar) bar.setAttribute('aria-valuenow', Math.round(pct));
        if (timeEl) timeEl.textContent = fmt(aud.currentTime) + ' / ' + fmt(aud.duration);
      }});
      if (bar) {{
        bar.addEventListener('click', function(e) {{
          if (!aud.duration) return;
          var rect = bar.getBoundingClientRect();
          aud.currentTime = ((e.clientX - rect.left) / rect.width) * aud.duration;
        }});
      }}
    }});
  }})();
  </script>"""

OLD_BODY_CLOSE = "  </body>"
NEW_BODY_CLOSE = AUDIO_JS + "\n  </body>"
src = src.replace(OLD_BODY_CLOSE, NEW_BODY_CLOSE, 1)
print('✓ Audio JS inserted')

with open(ROOT / 'build.py', 'w', encoding='utf-8') as f:
    f.write(src)

print('\nAll patches applied. Running build…')
import subprocess
result = subprocess.run(['python3', 'build.py'], capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print('BUILD ERROR:', result.stderr)
