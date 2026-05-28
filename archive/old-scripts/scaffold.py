import os
import re
import json

def scaffold_days():
    # Read ARC.md to extract questions
    arc_path = "docs/ARC.md"
    questions = {}
    if os.path.exists(arc_path):
        with open(arc_path, "r") as f:
            for line in f:
                m = re.match(r"^\*\*Day (\d+)\.\*\*\s*(.*)", line)
                if m:
                    day_num = int(m.group(1))
                    questions[day_num] = m.group(2)

    for day in range(3, 101):
        day_str = str(day).zfill(3)
        dir_path = f"diary/day-{day_str}"
        os.makedirs(dir_path, exist_ok=True)
        
        # question.md
        q_path = os.path.join(dir_path, "question.md")
        if not os.path.exists(q_path):
            question_text = questions.get(day, "Question pending generation.")
            with open(q_path, "w") as f:
                f.write(question_text)
                
        # Empty files
        for filename in ["answer.md", "fact-check.md", "narration.md"]:
            p = os.path.join(dir_path, filename)
            if not os.path.exists(p):
                with open(p, "w") as f:
                    f.write("")
                    
        # Telemetry
        telemetry_path = os.path.join(dir_path, "telemetry.json")
        if not os.path.exists(telemetry_path):
            with open(telemetry_path, "w") as f:
                json.dump({
                  "day": day,
                  "phase": "",
                  "T0_approx": None,
                  "T0_local_approx": None,
                  "T2": None,
                  "T3_approx": None,
                  "T4_approx": None,
                  "latency_ms_approx": None,
                  "composition_ms_approx": None,
                  "answer_word_count": 0,
                  "answer_message_count": 0,
                  "artifact_count": 0,
                  "notes": "",
                  "fact_check_summary": {
                    "verified": 0,
                    "contradicted": 0,
                    "unverified": 0,
                    "unverifiable": 0,
                    "total_claims": 0,
                    "hard_record_contradictions": 0
                  }
                }, f, indent=2)

if __name__ == "__main__":
    scaffold_days()
    print("Scaffolded Day 003 through 100 successfully.")
