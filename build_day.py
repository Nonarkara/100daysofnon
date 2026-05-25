import os
import re
import json

def parse_fact_check(md_content):
    claims = []
    # match rows like | 1 | Mother holds... | ✓ | Note... |
    for line in md_content.split('\n'):
        if line.startswith('|') and not line.startswith('| # |') and not line.startswith('|---|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5:
                claim_text = parts[2]
                state_raw = parts[3]
                sub_text = parts[4]
                
                # normalize state
                state_raw = state_raw.lower()
                if '✓' in state_raw or 'verified' in state_raw:
                    glyph = '&#10003;'
                    tag = 'VERIFIED'
                    cx = ''
                elif '✗' in state_raw or 'contradicted' in state_raw:
                    glyph = '&#10007;'
                    tag = 'CONTRADICTED'
                    cx = ' cx'
                elif '?' in state_raw or 'unverified' in state_raw:
                    glyph = '?'
                    tag = 'UNVERIFIED'
                    cx = ''
                elif '∅' in state_raw or 'un-verifiable' in state_raw or 'unverifiable' in state_raw:
                    glyph = '&#8709;'
                    tag = 'UN-VERIFIABLE'
                    cx = ''
                elif '⚠' in state_raw or 'clarification' in state_raw:
                    glyph = '!'
                    tag = 'CLARIFICATION'
                    cx = ''
                elif '⤬' in state_raw or 'tension' in state_raw:
                    glyph = '&#10799;'
                    tag = 'TENSION'
                    cx = ' cx'
                elif '◆' in state_raw or 'silent' in state_raw or 'system' in state_raw:
                    glyph = '&#9670;'
                    tag = 'SYSTEM NOTE'
                    cx = ''
                else:
                    glyph = '?'
                    tag = 'UNKNOWN'
                    cx = ''
                
                html = f'''        <div class="claim">
          <span class="c-glyph{cx}">{glyph}</span>
          <span class="c-tag{cx}">{tag}</span>
          <span class="c-text">{claim_text}</span>
          <span class="c-sub{cx}">{sub_text}</span>
        </div>'''
                claims.append(html)
    return "\n".join(claims)

def build_day(day_num, day_title):
    day_str = str(day_num).zfill(3)
    diary_dir = f"diary/day-{day_str}"
    site_dir = f"site/day/{day_str}"
    
    if not os.path.exists(diary_dir):
        print(f"Directory {diary_dir} does not exist.")
        return
        
    os.makedirs(site_dir, exist_ok=True)
    
    # Read materials
    with open(f"{diary_dir}/answer.md", "r") as f:
        answer_md = f.read()
    with open(f"{diary_dir}/narration.md", "r") as f:
        narration_md = f.read()
    with open(f"{diary_dir}/fact-check.md", "r") as f:
        fact_check_md = f.read()
    with open(f"{diary_dir}/telemetry.json", "r") as f:
        telemetry = json.load(f)
        
    # Convert markdown to html basic (paragraphs)
    def md_to_html(md):
        html = ""
        for p in md.split('\n\n'):
            if p.strip() and not p.startswith('#'):
                html += f"            <p>{p.strip()}</p>\n"
        return html
        
    answer_html = md_to_html(answer_md)
    narration_html = md_to_html(narration_md)
    fact_check_html = parse_fact_check(fact_check_md)
    
    fc = telemetry.get("fact_check_summary", {})
    tally_v = fc.get("verified", 0)
    tally_c = fc.get("contradicted", 0)
    tally_u = fc.get("unverified", 0)
    tally_n = fc.get("unverifiable", 0)
    
    word_count = telemetry.get("answer_word_count", 0)
    msg_count = telemetry.get("answer_message_count", 0)
    
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{day_str} — 100 Days of Non</title>
  <link rel="stylesheet" href="/assets/css/main.css">
  <style>
    .strip {{ position: fixed; top: var(--nav-h); left: 0; right: 0; height: var(--strip-h); background: var(--bg); border-bottom: 1px solid var(--faint); display: flex; align-items: center; padding: 0 48px; gap: 6px; overflow-x: auto; z-index: 100; font-family: var(--mono); font-size: var(--micro); letter-spacing: 0.08em; scrollbar-width: none; }}
    .strip::-webkit-scrollbar {{ display: none; }}
    .strip-title {{ display: none; }}
    .day-num {{ color: var(--faint); text-decoration: none; padding: 2px 4px; white-space: nowrap; transition: color 0.1s; }}
    .day-num:hover {{ color: rgba(255,255,255,0.5); }}
    .day-num.done  {{ color: rgba(255,255,255,0.55); }}
    .day-num.active {{ color: var(--accent); }}
    .col-rule {{ position: fixed; top: var(--header-h); left: var(--col-x); bottom: 0; width: 1px; background: var(--faint); z-index: 10; }}
    main {{ margin-top: var(--header-h); padding: 56px 56px 120px 56px; }}
    .day-counter {{ font-family: var(--mono); font-size: clamp(48px, 8vw, 96px); font-weight: 700; line-height: 0.85; letter-spacing: -0.04em; color: var(--fg); }}
    .day-meta {{ font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; margin-top: 10px; }}
    .pull-image {{ font-family: var(--sans); font-size: clamp(32px, 5vw, 64px); font-weight: 700; line-height: 0.88; letter-spacing: -0.025em; text-transform: uppercase; white-space: nowrap; overflow: hidden; text-overflow: clip; color: var(--fg); margin-top: 64px; margin-left: -56px; padding-left: 56px; }}
    .phase-row {{ display: flex; align-items: baseline; gap: 16px; margin-top: 72px; }}
    .phase-tag {{ font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; white-space: nowrap; }}
    .rule-h {{ width: 100%; height: 1px; background: var(--faint); }}
    .q-label {{ font-family: var(--mono); font-size: var(--micro); color: var(--accent); letter-spacing: 0.15em; text-transform: uppercase; margin-top: 20px; }}
    .q-text {{ font-size: clamp(24px, 4vw, 32px); line-height: 1.5; color: rgba(255,255,255,0.8); max-width: 660px; margin-top: 10px; }}
    .content-grid {{ display: grid; grid-template-columns: 1fr 320px; gap: 0 64px; margin-top: 56px; align-items: start; }}
    .col-label {{ font-family: var(--mono); font-size: var(--micro); color: var(--dim); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 16px; }}
    .answer-text p {{ font-size: var(--body); line-height: 1.8; color: rgba(255,255,255,0.88); }}
    .answer-text p + p {{ margin-top: 1.4em; }}
    .narration {{ margin-top: 56px; padding-left: 28px; border-left: 1px solid var(--faint); }}
    .narration .col-label {{ margin-bottom: 14px; }}
    .narration-text p {{ font-size: var(--body); line-height: 1.8; color: rgba(255,255,255,0.45); }}
    .narration-text p + p {{ margin-top: 1.3em; }}
    .fc-col {{ font-family: var(--mono); font-size: 11px; position: sticky; top: calc(var(--header-h) + 16px); height: calc(100vh - var(--header-h) - 32px); overflow-y: auto; scrollbar-width: none; padding-right: 16px; }}
    .fc-col::-webkit-scrollbar {{ display: none; }}
    .claim {{ display: grid; grid-template-columns: 14px 80px 1fr; column-gap: 6px; padding: 7px 0; border-bottom: 1px solid rgba(255,255,255,0.05); align-items: start; }}
    .c-glyph {{ color: var(--dim); line-height: 1.4; }}
    .c-glyph.cx {{ color: var(--accent); }}
    .c-tag {{ color: rgba(255,255,255,0.25); text-transform: uppercase; letter-spacing: 0.05em; line-height: 1.4; }}
    .c-tag.cx {{ color: var(--accent); }}
    .c-text {{ color: rgba(255,255,255,0.7); line-height: 1.4; }}
    .c-sub {{ grid-column: 3; color: rgba(255,255,255,0.3); font-size: 10px; margin-top: 2px; line-height: 1.4; }}
    .c-sub.cx {{ color: var(--accent); }}
    .fc-tally {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 0; margin-top: 20px; padding-top: 14px; border-top: 1px solid var(--faint); }}
    .tally-n {{ font-size: 22px; font-weight: 700; line-height: 1; color: rgba(255,255,255,0.85); }}
    .tally-n.cx {{ color: var(--accent); }}
    .tally-l {{ font-size: 9px; color: rgba(255,255,255,0.25); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 4px; }}
    .telemetry {{ margin-top: 88px; padding-top: 32px; border-top: 1px solid var(--faint); }}
    .t-number {{ font-family: var(--mono); font-size: clamp(48px, 8vw, 96px); font-weight: 700; line-height: 0.85; letter-spacing: -0.04em; color: rgba(255,255,255,0.08); }}
    .t-meta {{ font-family: var(--mono); font-size: var(--micro); color: rgba(255,255,255,0.2); letter-spacing: 0.12em; text-transform: uppercase; margin-top: 10px; }}
    @media (max-width: 1024px) {{ .content-grid {{ grid-template-columns: 1fr; }} .fc-col {{ position: static; height: auto; overflow: visible; }} }}
  </style>
</head>
<body>
  <nav class="nav" aria-label="Site navigation">
    <a href="/" class="nav-brand" style="text-decoration:none;">100 Days of Non</a>
    <a href="/day/001/" class="here">RECORD</a>
    <a href="/map/">MAP</a>
    <a href="/corpus/">CORPUS</a>
    <a href="/chronos/">CHRONOS</a>
    <a href="/lexicon/">LEXICON</a>
    <a href="/voices/">VOICES</a>
    <a href="/archive/">ARCHIVE</a>
    <a href="/method/">METHOD</a>
    <a href="/game/">GAME</a>
    <a href="/subject/">SUBJECT</a>
    <a href="/bot/">BOT</a>
    <a href="/notes/">NOTES</a>
  </nav>

  <nav class="strip" aria-label="Day navigation">
    <span class="strip-title">100 Days of Non</span>
    <a href="/day/001/" class="day-num done">001</a>
    <a href="/day/002/" class="day-num active">002</a>
    <!-- Render the rest dynamically if needed -->
  </nav>

  <div class="col-rule"></div>

  <main>
    <div class="day-counter">DAY {day_str}</div>
    <div class="day-meta">Phase I: Origin &amp; Place &nbsp;&middot;&nbsp; 2026-05-25</div>
    
    <div class="pull-image">{day_title}</div>
    
    <div class="phase-row">
      <div class="phase-tag">Phase I &mdash; Origin &amp; Place</div>
      <div class="rule-h"></div>
    </div>
    
    <div class="q-label">Question 002</div>
    <div class="q-text">What is your mother's full name, birth year, city, and occupation when you were five? What is the one story she tells about you most often?</div>

    <div class="content-grid">
      <div class="answer-col">
        <div class="col-label">Answer</div>
        <div class="answer-text">
{answer_html}
        </div>
        <div class="narration">
          <div class="col-label">Biographer's Note</div>
          <div class="narration-text">
{narration_html}
          </div>
        </div>
      </div>

      <div class="fc-col">
        <div class="col-label">Fact-check</div>
{fact_check_html}
        
        <div class="fc-tally">
          <div><div class="tally-n">{tally_v}</div><div class="tally-l">&#10003; Verified</div></div>
          <div><div class="tally-n{ ' cx' if tally_c > 0 else '' }">{tally_c}</div><div class="tally-l">&#10007; Contradicted</div></div>
          <div><div class="tally-n">{tally_u}</div><div class="tally-l">? Unverified</div></div>
          <div><div class="tally-n">{tally_n}</div><div class="tally-l">&#8709; Unverifiable</div></div>
        </div>
      </div>
    </div>
    
    <div class="telemetry">
      <div class="t-number">&mdash;:&mdash;:&mdash;</div>
      <div class="t-meta">{word_count} words across {msg_count} messages &nbsp;&middot;&nbsp; 2026-05-25 Asia/Bangkok</div>
    </div>
  </main>
</body>
</html>
'''
    with open(f"{site_dir}/index.html", "w") as f:
        f.write(template)

if __name__ == "__main__":
    build_day(2, "THE LINEAGE ENCODED")
