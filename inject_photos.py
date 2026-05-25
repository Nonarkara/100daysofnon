import os
import re

css = """
    /* ── Artifact Images ────────────────────────────────────── */
    .artifact-img-container { margin: 40px 0; border: 1px solid var(--faint); background: var(--bg); display: block; }
    .artifact-img-container.bleed { margin-left: -28px; margin-right: -28px; border-left: none; border-right: none; }
    .artifact-img { display: block; width: 100%; height: auto; filter: grayscale(100%) contrast(1.2) brightness(0.9); mix-blend-mode: luminosity; }
    .artifact-caption { font-family: var(--mono); font-size: 10px; color: var(--dim); padding: 12px 16px; text-transform: uppercase; letter-spacing: 0.15em; border-top: 1px solid var(--faint); }
"""

photo1 = """
          <div class="artifact-img-container bleed">
            <img class="artifact-img" src="/assets/photos/Non Just Born For Real.jpg" alt="Non just born">
            <div class="artifact-caption">FIG. 1 — The Record Begins (Phyathai Hospital, 1981)</div>
          </div>
"""

photo2 = """
          <div class="artifact-img-container bleed">
            <img class="artifact-img" src="/assets/photos/Non Young House.jpg" alt="Non's childhood house">
            <div class="artifact-caption">FIG. 2 — 42 Years in the Same House</div>
          </div>
"""

photo3 = """
          <div class="artifact-img-container bleed">
            <img class="artifact-img" src="/assets/photos/Non Preschool.jpg" alt="Non in preschool">
            <div class="artifact-caption">FIG. 3 — Nam Sai Alleyway Neighborhood</div>
          </div>
"""

def process_day(file_path, injection_pairs):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r') as f:
        content = f.read()
    
    # inject css if not there
    if "artifact-img-container" not in content:
        content = content.replace("</style>", css + "</style>")
        
    for target, injection in injection_pairs:
        if injection not in content:
            content = content.replace(target, injection + target)
            
    with open(file_path, 'w') as f:
        f.write(content)

# Day 1
day1_pairs = [
    ('<p>Then there is the geography of the memory.', photo1),
    ('<p>It takes a certain kind of stubbornness', photo2)
]
process_day("site/day/001/index.html", day1_pairs)

# Day 2
day2_pairs = [
    ('<p>Then there was the Bank of Asia', photo3)
]
process_day("site/day/002/index.html", day2_pairs)

print("Done injecting photos.")
