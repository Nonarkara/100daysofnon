import os
import re

files_to_process = [
    "site/corpus/index.html",
    "site/day/001/index.html",
    "site/game/index.html",
    "site/lexicon/index.html",
    "site/map/index.html",
    "site/method/index.html",
    "site/subject/index.html",
    "site/voices/index.html"
]

# Patterns for standard styles we want to remove from the inline style blocks
to_remove = [
    r":root\s*\{[^}]*\}",
    r"\*,\s*\*\:\:before,\s*\*\:\:after\s*\{[^}]*\}",
    r"html\s*\{[^}]*\}",
    r"body\s*\{[^}]*\}",
    r"\.nav\s*\{[^}]*\}",
    r"\.nav-brand\s*\{[^}]*\}",
    r"\.nav\s+a\s*\{[^}]*\}",
    r"\.nav\s+a:hover\s*\{[^}]*\}",
    r"\.nav\s+a\.here\s*\{[^}]*\}",
    r"header\.page\s*\{[^}]*\}",
    r"\.room-num\s*\{[^}]*\}",
    r"\.room-title\s*\{[^}]*\}",
    r"\.room-sub\s*\{[^}]*\}",
]

base_dir = "/Users/nonarkara/Projects/100daysofnon"

for rel_path in files_to_process:
    path = os.path.join(base_dir, rel_path)
    if not os.path.exists(path):
        print(f"Skipping {path}")
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add main.css link before the style tag if not there
    if '<link rel="stylesheet" href="/assets/css/main.css">' not in content:
        content = re.sub(
            r"(<style>)", 
            r'<link rel="stylesheet" href="/assets/css/main.css">\n  \1', 
            content
        )

    # Clean up standard styles from the inline block
    for pattern in to_remove:
        content = re.sub(pattern, "", content, flags=re.MULTILINE)

    # Remove extra blank lines inside style block
    def clean_style(match):
        s = match.group(0)
        s = re.sub(r"\n\s*\n", "\n", s)
        return s
    
    content = re.sub(r"<style>.*?</style>", clean_style, content, flags=re.DOTALL)

    # Wrap body contents in layout-grid
    # Find <body> and </body>
    
    # We want to insert the layout grid right after the nav
    if '<div class="layout-grid">' not in content:
        # split at </nav>
        parts = content.split("</nav>")
        if len(parts) > 1:
            head_and_nav = parts[0] + "</nav>"
            rest = parts[1]
            
            rest_parts = re.split(r"</body\s*>", rest, flags=re.IGNORECASE)
            if len(rest_parts) > 1:
                body_content = rest_parts[0]
                tail = "</body>" + rest_parts[1]
            else:
                body_content = rest
                tail = "</body>\n</html>"
                
            room_num = "000"
            if "corpus" in path: room_num = "003 /// CORPUS"
            if "day" in path: room_num = "001 /// RECORD"
            if "game" in path: room_num = "009 /// GAME"
            if "lexicon" in path: room_num = "005 /// LEXICON"
            if "map" in path: room_num = "002 /// MAP"
            if "method" in path: room_num = "008 /// METHOD"
            if "subject" in path: room_num = "010 /// SUBJECT"
            if "voices" in path: room_num = "007 /// VOICES"

            wrapped_body = f"""
  <div class="layout-grid">
    <div class="col-0 index-col-0" style="writing-mode: vertical-rl; text-orientation: mixed; display: flex; align-items: center; justify-content: center; letter-spacing: 0.2em; font-family: var(--mono); font-size: 11px; color: var(--faint);">
      {room_num}
    </div>
    <div class="col-1">
{body_content}
    </div>
  </div>
"""
            content = head_and_nav + wrapped_body + tail

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Done")
