import os
import re

photos_dir = "/Users/nonarkara/Projects/100daysofnon/site/assets/photos"
archive_file = "/Users/nonarkara/Projects/100daysofnon/site/archive/index.html"

# Get all photos
photos = []
for f in sorted(os.listdir(photos_dir)):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.heic', '.gif', '.webp')):
        photos.append(f)

# Generate HTML
html_parts = []
html_parts.append('<div class="gallery-section">')
html_parts.append('  <div class="gallery-title">Archive Appendices / 01 Photographs</div>')
html_parts.append('  <div class="gallery-grid">')

for photo in photos:
    # Use filename as label, strip extension, replace _ with space
    label = os.path.splitext(photo)[0]
    label = label.replace('_', ' ').replace('+', ' ').strip()
    
    html_parts.append('    <div class="gallery-item artifact-container">')
    html_parts.append(f'      <img src="/assets/photos/{photo}" alt="{label}" class="artifact-img" loading="lazy">')
    html_parts.append(f'      <div class="gallery-label">{label}</div>')
    html_parts.append('    </div>')

html_parts.append('  </div>')
html_parts.append('</div>')

gallery_html = "\n".join(html_parts)

# Read archive.html
with open(archive_file, "r", encoding="utf-8") as f:
    content = f.read()

# Add CSS if not present
css = """
    .gallery-section {
      border-top: 1px solid var(--faint);
      padding: 64px 48px;
    }
    .gallery-title {
      font-family: var(--mono); font-size: 11px; color: var(--accent);
      letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 40px;
    }
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1px;
      background: var(--faint);
      border-top: 1px solid var(--faint);
      border-bottom: 1px solid var(--faint);
    }
    .gallery-item {
      background: var(--bg);
      display: flex;
      flex-direction: column;
    }
    .gallery-item img {
      width: 100%;
      aspect-ratio: 4 / 3;
      object-fit: cover;
    }
    .gallery-label {
      padding: 12px 16px;
      font-family: var(--mono); font-size: 9px; color: var(--dim);
      text-transform: uppercase; letter-spacing: 0.1em;
      border-top: 1px solid var(--faint);
      flex: 1;
    }
    @media (max-width: 1024px) {
      .gallery-section { padding: 48px 24px; }
      .gallery-grid { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); }
    }
"""

if '.gallery-section' not in content:
    content = content.replace('</style>', css + '\n  </style>')

# Inject gallery right after <div class="facts"> ... </div>
# Finding the closing div of facts is tricky. Let's just find the end of facts.
# The facts div ends right before `    </div>` (col-1 end)
# We can just replace `      </div>\n\n    </div>\n  </div>` with `      </div>\n\n` + gallery_html + `\n    </div>\n  </div>`

# A safer way: replace `      </div>\n\n    </div>\n  </div>`
pattern = r'(      </div>\s*</div>\s*</div>\s*</body>)'
replacement = r'      </div>\n\n' + gallery_html + r'\n    </div>\n  </div>\n</body>'

content = re.sub(pattern, replacement, content)

with open(archive_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Added {len(photos)} photos to archive.")
