import os
import re
import json
import glob

css = """
    /* ── Artifact Images ────────────────────────────────────── */
    .artifact-img-container { margin: 40px 0; border: 1px solid var(--faint); background: var(--bg); display: block; }
    .artifact-img-container.bleed { margin-left: -28px; margin-right: -28px; border-left: none; border-right: none; }
    .artifact-img { display: block; width: 100%; height: auto; filter: grayscale(100%) contrast(1.2) brightness(0.9); mix-blend-mode: luminosity; }
    .artifact-caption { font-family: var(--mono); font-size: 10px; color: var(--dim); padding: 12px 16px; text-transform: uppercase; letter-spacing: 0.15em; border-top: 1px solid var(--faint); }
"""

def parse_fact_check(md_content):
    claims = []
    for line in md_content.split('\n'):
        if line.startswith('|') and not line.startswith('| # |') and not line.startswith('|---|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5:
                claim_text = parts[2]
                state_raw = parts[3]
                sub_text = parts[4]
                
                state_raw = state_raw.lower()
                if '✓' in state_raw or 'verified' in state_raw:
                    glyph, tag, cx = '&#10003;', 'VERIFIED', ''
                elif '✗' in state_raw or 'contradicted' in state_raw:
                    glyph, tag, cx = '&#10007;', 'CONTRADICTED', ' cx'
                elif '?' in state_raw or 'unverified' in state_raw:
                    glyph, tag, cx = '?', 'UNVERIFIED', ''
                elif '∅' in state_raw or 'un-verifiable' in state_raw or 'unverifiable' in state_raw:
                    glyph, tag, cx = '&#8709;', 'UN-VERIFIABLE', ''
                elif '⚠' in state_raw or 'clarification' in state_raw:
                    glyph, tag, cx = '!', 'CLARIFICATION', ''
                elif '⤬' in state_raw or 'tension' in state_raw:
                    glyph, tag, cx = '&#10799;', 'TENSION', ' cx'
                elif '◆' in state_raw or 'silent' in state_raw or 'system' in state_raw:
                    glyph, tag, cx = '&#9670;', 'SYSTEM NOTE', ''
                else:
                    glyph, tag, cx = '?', 'UNKNOWN', ''
                
                html = f'''        <div class="claim">
          <span class="c-glyph{cx}">{glyph}</span>
          <span class="c-tag{cx}">{tag}</span>
          <span class="c-text">{claim_text}</span>
          <span class="c-sub{cx}">{sub_text}</span>
        </div>'''
                claims.append(html)
    return "\n".join(claims)

def md_to_html(md):
    html = ""
    for p in md.split('\n\n'):
        if p.strip() and not p.startswith('#'):
            html += f"            <p>{p.strip()}</p>\n"
    return html

def build_all():
    diary_dirs = sorted(glob.glob("diary/day-*"))
    completed_days = []
    
    # Pre-pass to find completed days for the strip nav
    for d in diary_dirs:
        ans_path = os.path.join(d, "answer.md")
        if os.path.exists(ans_path) and len(open(ans_path).read().strip()) > 0:
            day_str = os.path.basename(d).split('-')[1]
            completed_days.append(day_str)

    for d in diary_dirs:
        day_str = os.path.basename(d).split('-')[1]
        
        # Check if answered
        ans_path = os.path.join(d, "answer.md")
        if not os.path.exists(ans_path) or len(open(ans_path).read().strip()) == 0:
            continue
            
        site_dir = f"site/day/{day_str}"
        os.makedirs(site_dir, exist_ok=True)
        
        with open(ans_path, "r") as f: answer_md = f.read()
        with open(os.path.join(d, "narration.md"), "r") as f: narration_md = f.read()
        with open(os.path.join(d, "fact-check.md"), "r") as f: fact_check_md = f.read()
        
        # safely read question
        q_path = os.path.join(d, "question.md")
        question_text = ""
        if os.path.exists(q_path):
            question_text = open(q_path).read().strip()
            
        telemetry = {}
        t_path = os.path.join(d, "telemetry.json")
        if os.path.exists(t_path):
            try:
                telemetry = json.load(open(t_path))
            except: pass
            
        answer_html = md_to_html(answer_md)
        narration_html = md_to_html(narration_md)
        fact_check_html = parse_fact_check(fact_check_md)
        
        # Inject known photos based on day if not already handled
        # (This avoids resetting photos injected manually for Day 1 and 2)
        # But we'll just leave existing index.html alone if it's Day 1 or Day 2 to preserve their special photos
        if day_str in ["001", "002"] and os.path.exists(f"{site_dir}/index.html"):
            continue
        
        fc = telemetry.get("fact_check_summary", {})
        tally_v = fc.get("verified", 0)
        tally_c = fc.get("contradicted", 0)
        tally_u = fc.get("unverified", 0)
        tally_n = fc.get("unverifiable", 0)
        
        word_count = telemetry.get("answer_word_count", 0)
        msg_count = telemetry.get("answer_message_count", 0)
        
        # Build Strip Nav
        strip_nav = '<span class="strip-title">100 Days of Non</span>\n'
        for cd in completed_days:
            cls = "day-num active" if cd == day_str else "day-num done"
            strip_nav += f'    <a href="/day/{cd}/" class="{cls}">{cd}</a>\n'

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
{css}
  </style>
</head>
<body>
  <nav class="nav" aria-label="Site navigation">
    <a href="/" class="nav-brand" style="text-decoration:none;">100 Days of Non</a>
    <a href="/day/{completed_days[0]}/" class="here">RECORD</a>
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
{strip_nav}
  </nav>

  <div class="col-rule"></div>

  <main>
    <div class="day-counter">DAY {day_str}</div>
    <div class="day-meta">Phase Pending &nbsp;&middot;&nbsp; Recorded via Chronos</div>
    
    <div class="pull-image">ENTRY {day_str}</div>
    
    <div class="phase-row">
      <div class="phase-tag">Phase Record</div>
      <div class="rule-h"></div>
    </div>
    
    <div class="q-label">Question {day_str}</div>
    <div class="q-text">{question_text}</div>

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
      <div class="t-meta">{word_count} words across {msg_count} messages</div>
    </div>
  </main>
</body>
</html>
'''
        with open(f"{site_dir}/index.html", "w") as f:
            f.write(template)
            
        print(f"Built {site_dir}/index.html")

if __name__ == "__main__":
    build_all()
    print("Intake pipeline run complete.")
