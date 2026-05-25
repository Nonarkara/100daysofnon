import os
import glob
import json

def analyze():
    diary_dirs = sorted(glob.glob("diary/day-*"))
    
    total_v = 0
    total_c = 0
    total_u = 0
    total_n = 0
    total_words = 0
    
    all_claims = []
    
    for d in diary_dirs:
        day_str = os.path.basename(d).split('-')[1]
        t_path = os.path.join(d, "telemetry.json")
        fc_path = os.path.join(d, "fact-check.md")
        
        if os.path.exists(t_path):
            try:
                telemetry = json.load(open(t_path))
                fc = telemetry.get("fact_check_summary", {})
                total_v += fc.get("verified", 0)
                total_c += fc.get("contradicted", 0)
                total_u += fc.get("unverified", 0)
                total_n += fc.get("unverifiable", 0)
                total_words += telemetry.get("answer_word_count", 0)
            except:
                pass
                
        if os.path.exists(fc_path):
            content = open(fc_path).read()
            for line in content.split('\n'):
                if line.startswith('|') and not line.startswith('| # |') and not line.startswith('|---|'):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 5:
                        claim_text = parts[2]
                        state_raw = parts[3]
                        if '✗' in state_raw or 'contradicted' in state_raw.lower():
                            all_claims.append({"day": day_str, "claim": claim_text, "status": "contradicted"})
                        elif '⤬' in state_raw or 'tension' in state_raw.lower():
                            all_claims.append({"day": day_str, "claim": claim_text, "status": "tension"})
                            
    patterns_md = f"""# The Patterns Log

Aggregated telemetry and contradiction tracking across all 100 days.

## Aggregates
- **Total Words Recorded:** {total_words}
- **Total Verified Claims:** {total_v}
- **Total Contradicted Claims:** {total_c}
- **Total Unverified Claims:** {total_u}
- **Total Unverifiable Claims:** {total_n}

## Notable Contradictions & Tensions
"""
    for c in all_claims:
        patterns_md += f"- **Day {c['day']}** ({c['status'].upper()}): {c['claim']}\\n"
        
    with open("docs/patterns.md", "w") as f:
        f.write(patterns_md)
        
    print(f"Analysis complete. Found {len(all_claims)} contradictions/tensions. Wrote docs/patterns.md.")

if __name__ == "__main__":
    analyze()
