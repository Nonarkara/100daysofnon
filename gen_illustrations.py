#!/usr/bin/env python3
"""
Generate Two Layers chapter illustrations via Gemini Flash image generation.
Reads GEMINI_API_KEY from city-reporter secrets (same key across projects).
Saves to site/assets/illustrations/ch{N}-{sim|arc}.jpg

Usage:
    python3 gen_illustrations.py          # all 20 images
    python3 gen_illustrations.py 1 sim    # single image
    python3 gen_illustrations.py --dry    # print prompts only
"""

import sys, os, base64, json, time, re
from pathlib import Path
import requests

# ── Key (never printed) ─────────────────────────────────────────────────────
def _load_key():
    if k := os.environ.get("GEMINI_API_KEY", "").strip():
        return k
    candidates = [
        "/Users/nonarkara/Projects/shared/.secrets-backup/bots_city-reporter-line-bot_.env",
        "/Users/nonarkara/Projects/shared/.secrets-backup/dashboards_smart-city-monitor_.env",
        "/Users/nonarkara/Projects/shared/.secrets-backup/archive_second-brain-v1_.env",
    ]
    for path in candidates:
        try:
            for line in Path(path).read_text().splitlines():
                if line.startswith("GEMINI_API_KEY="):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val and not val.startswith("#"):
                        return val
        except Exception:
            continue
    raise RuntimeError("GEMINI_API_KEY not found — set it in env or secrets backup")

KEY = _load_key()

# ── API ──────────────────────────────────────────────────────────────────────
MODEL   = "gemini-3-pro-image"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
OUT_DIR = Path(__file__).parent / "site/assets/illustrations"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Prompts ──────────────────────────────────────────────────────────────────
PROMPTS = {
    (1, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast, sparse negative space, close crop. Scene: a Thai man in his late thirties standing at a floor-to-ceiling window at night, not looking at the camera, looking down at the city below with an expression of quiet suspicion, holding a ceramic coffee cup in one hand, in a high-rise Bangkok apartment. Background elements: soft charcoal wall, blurred city lights far below through dark glass, deep empty space. Wardrobe: four plain dark shirts folded on a shelf visible behind him, one shirt currently worn, dark and simple. Typography: render the exact readable lowercase headline text "none of this is real." as three short left-aligned lines; put the first headline word as black type inside a crisp white rectangular label, then set the remaining lines in heavy white type directly on the dark background. Add "bangkok, 2026" as tiny white microcopy. Photo treatment: realistic black-and-white studio photography, strong shadow falloff, visible fabric texture, subtle grain, no color, no illustration, no logos, no watermark.""",

    (1, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: an archive room with forty-four identical white reclining chairs arranged in rows under indirect white institutional light, underground. The last chair (chair 44) has a single dried white flower resting on its armrest. A pale-blue translucent data panel overlays the far end of the row showing biometric numbers. Typography: very large black neo-grotesk type reading "SESSION INITIALIZED". Add "PARTICIPANT 44 · CHAIR 44 · CYCLE 2848" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft indirect light, gentle paper grain, pale-blue translucent interface panel, quiet negative space. No watermark, no logo, no cyberpunk, no neon.""",

    (2, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast, sparse negative space. Scene: a Thai man in his late thirties sitting at a minimal desk staring at a laptop screen, the screen glow the only light in the room, his expression still and intent, holding nothing, phone flat on the desk beside the laptop, a dark Bangkok apartment at 4am. Background: deep black, blurred window glass showing distant city lights, extreme shadow on his face except where the screen lights it. Typography: render "still there. barely." as three short left-aligned lowercase lines with tight leading; first word in white rectangular label, rest in heavy white type on dark background. Add "3:14 am · +43" as tiny white microcopy. Photo treatment: realistic black-and-white, strong shadow falloff, subtle grain, no color, no logos, no watermark.""",

    (2, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a chronometry archive showing time compression — an analog clock face with its hands distorted and frozen, placed on a clean archive desk with printed time-conversion charts and a small glass paperweight. A pale-blue translucent data panel overlays the clock with conversion figures: "1 HOUR = 1 YEAR". Typography: very large black neo-grotesk type reading "ONE HOUR EQUALS ONE YEAR". Add "4 DAYS : 96 SIMULATED YEARS · 8 YEARS SUBJECTIVE MEMORY" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft indirect light, gentle paper grain, pale-blue translucent interface panel, quiet negative space. No watermark, no logo, no cyberpunk.""",

    (3, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties standing at the window of a coffee shop, looking across the street at an office building, his back partially to camera, one hand raised to the glass, expression unreadable, Sathorn district Bangkok, afternoon light rendered monochrome. Background: glass and street reflection, distant office building facade. Typography: render "the shape of what was there." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "sathorn · week 6" as tiny white microcopy. Photo treatment: realistic black-and-white, strong shadow falloff, subtle grain, no color, no logos, no watermark.""",

    (3, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a cognitive archive showing brain-scan printouts on cream paper spread across a quiet archive desk, with a translucent overlay panel showing three declining index lines for creativity, neuroplasticity, and adaptation over time. Year labels 2026 and 3026 at each end. Typography: very large black neo-grotesk type reading "THE MIND STILL WORKS". Add "CREATIVITY 89% · NEUROPLASTICITY 87% · ADAPTATION 79% · PARTICIPANT 44 ONLY" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft diffuse light, gentle paper grain, pale-blue translucent data overlay, quiet negative space. No watermark, no logo, no cyberpunk.""",

    (4, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties sitting at a kitchen table in early morning light holding a phone face-down, not looking at it, expression between grief and suspicion, nothing else on the table, Bangkok apartment on June 1st, single window with soft morning light. Typography: render "still here. june 1st." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "eight years" as tiny white microcopy. Photo treatment: realistic black-and-white, strong shadow falloff, subtle grain, no color, no logos, no watermark.""",

    (4, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a demographic archive showing a series of small empty wooden cradles in diminishing scale arranged on archive shelving, photographed from slightly above, the last shelf nearly empty. Decade labels 2060, 2200, 2400, 3026. A pale-blue translucent panel overlays the lowest shelf with final birth-rate figures. Typography: very large black neo-grotesk type reading "THE LAST CHILDREN". Add "LIVE BIRTH RATE: 18 PER 1,000 (2026) → 0.2 PER 1,000 (3026) · 80 MILLION REMAIN" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft overhead light, gentle paper grain, pale-blue translucent panel, empty negative space on the final shelf. No watermark, no logo, no cyberpunk.""",

    (5, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai woman on a bicycle on an empty Bangkok soi at night, stopped at a corner, standing on the pedals, head tilted slightly upward looking at something above frame, expression composed and deliberate, a street lamp casting a single cone of light and deep shadow everywhere else. Wardrobe: plain dark clothing, nothing identifying. Composition: low angle looking up toward subject, deep charcoal background. Typography: render "forty-one seconds. then gone." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "2:47 am · soi on-nut" as tiny white microcopy. Photo treatment: realistic black-and-white, strong shadow falloff, subtle grain, no color, no logos, no watermark.""",

    (5, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a neurological archive showing an analog brain-diagram printout on cream paper with five regions labeled and marked with handwritten percentage figures — MOTOR, CREATIVE, SOCIAL, REPRODUCTIVE, SURVIVAL — placed on a clean institutional desk. A pale-blue translucent panel overlays two of the sectors with anomaly markers. Typography: very large black neo-grotesk type reading "SECTOR ACTIVITY". Add "POPULATION AVG: CREATIVE 11% · SOCIAL 4% · PARTICIPANT 44: CREATIVE 89% · SOCIAL 71%" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft diffuse light, gentle paper grain, blue translucent anomaly overlay on the two high-scoring sectors. No watermark, no logo, no cyberpunk.""",

    (6, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties standing in shade at the edge of a temple cremation ground in northern Thailand, watching smoke rise into a white sky off-frame, his posture still, expression inward, hands at his sides, the temple wall behind him, smoke visible only as a column disappearing above frame. Wardrobe: dark shirt, slightly formal, appropriate for a funeral. Typography: render "the smoke was real." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "chiang rai · may" as tiny white microcopy. Photo treatment: realistic black-and-white, strong shadow falloff, visible smoke texture, subtle grain, no color, no logos, no watermark.""",

    (6, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a resonance archive showing a large printed scatter-plot chart on cream paper mounted on a wall, dozens of small dots clustered in one region (2020-2050) and one single dot far to the left and below the cluster, circled by hand in ink, labeled "P-44 · BANGKOK 1981-2026" in small careful handwriting. A pale-blue translucent panel highlights the outlier dot. Typography: very large black neo-grotesk type reading "SHE RETURNS ALONE". Add "2,848 SESSIONS · SINGLE COORDINATE · OUTLIER STATUS: CONFIRMED" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft daylight, gentle paper grain, pale-blue translucent panel on the outlier region. No watermark, no logo, no cyberpunk.""",

    (7, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties lying in a dental chair with eyes open, the drill instrument visible at the edge of frame but not in focus, his hands flat on the armrests, expression distant and inward, looking at something that is not the ceiling, the clinical room blurring around him. Background: dental clinic ceiling tiles blurred, clock on wall blurred, edge of clinical light above. Typography: render "forty-four chairs. white room." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "12 minutes · phromphong" as tiny white microcopy. Photo treatment: realistic black-and-white, upward-looking angle, strong shadow falloff, subtle grain, no color, no logos, no watermark.""",

    (7, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: an extreme close crop of two open hands, palms facing upward, resting on the armrests of a white institutional reclining chair, holding a single small white flower with one petal drifted to the knee, photographed from slightly above. A pale-blue translucent panel overlays the knee area with a case note: "ORIGIN: UNKNOWN · CROSS-SPACE TRANSFER NOT IN PROTOCOL". A small label on the chair reads "CHAIR 44". Typography: very large black neo-grotesk type reading "THE FLOWER HAD A SMELL". Add "ONLY OBJECT IN THE HUB WITH MEASURABLE OLFACTORY SIGNATURE · BANGKOK RAIN · JUNE" as tiny editorial microcopy. Visual treatment: warm cream paper background, close institutional photograph as hero, thin rules, soft overhead light, gentle paper grain, pale-blue translucent evidence panel. No watermark, no logo, no cyberpunk.""",

    (8, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties sitting at a kitchen table writing in a paper notebook at 3am, the pen visible in his hand, the page lit by a single lamp, his expression focused and controlled, the phone turned face-down on the table beside him with the screen off, dark Bangkok apartment. Background: bare table, one lamp's pool of light, deep shadow everywhere outside the lamp, dark window. Typography: render "not your data. you." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "3:22 am" as tiny white microcopy. Photo treatment: realistic black-and-white, close crop on face and notebook, strong shadow falloff, subtle grain, no color, no logos, no watermark.""",

    (8, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a longitudinal archive showing a large printed single-line graph on cream paper mounted on an archive wall. The curve begins high at the left (labeled 2026: 95) and falls steeply to near-zero at the right (labeled 3026: 3), with a horizontal dashed line labeled "DEAD DATA THRESHOLD" roughly one-quarter from the bottom, and a single hand-drawn annotation "P-44: 91". A pale-blue translucent panel over the P-44 annotation. Typography: very large black neo-grotesk type reading "SHE IS STILL FEELING". Add "EMOTIONAL BANDWIDTH INDEX: P-44 = 91 · COHORT AVERAGE = 3 · DELTA = 88 POINTS" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, thin rules, soft diffuse light, gentle paper grain, pale-blue translucent overlay at the P-44 annotation. No watermark, no logo, no cyberpunk.""",

    (9, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties standing on an empty construction site in daylight, looking straight up through where a roof will eventually be, open sky above him, red survey stakes visible at the edge of frame, his expression open and still, nothing in his hands, Nonthaburi waterfront lot, wide brown river barely visible at the edge. Background: cleared site, stakes, sky above, soft filtered daylight. Typography: render "let the rain in." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on the sky above the subject. Add "nonthaburi · approved" as tiny white microcopy. Photo treatment: realistic black-and-white, strong contrast, visible fabric texture, subtle grain, no color, no logos, no watermark.""",

    (9, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a records management archive showing a formal printed audit table on cream paper with six rows of session records — the first row fully readable (SESSIONS 001-243 · ACCESSIBLE · HUB-AI) and the remaining five rows have thick black redaction bars covering the content, with the word SEALED printed beside each bar. A handwritten annotation in the margin: "WHO AUTHORIZED THIS?" A pale-blue translucent panel overlays the totals row showing "2,847 TOTAL · 243 ACCESSIBLE · 2,604 SEALED". Typography: very large black neo-grotesk type reading "2,604 SESSIONS. NO SIGNATURE." Add "AUDIT COMPLETE · ESCALATION STATUS: NOT FILED · REASON: UNKNOWN" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, printed audit table as hero element, thick black redaction bars as visual weight, thin rules, soft office light, gentle paper grain, pale-blue translucent panel on the totals row. No watermark, no logo, no cyberpunk.""",

    (10, "sim"): """Create a 9:16 monochrome editorial poster in the Mono Noir Type Portrait Poster Style. Style fidelity lock: black-and-white photographic portrait, deep charcoal background, giant lowercase left-aligned headline, first word in a white rectangular label, remaining words in white, high contrast. Scene: a Thai man in his late thirties standing on a rain-soaked apartment balcony on the third day of rain, one hand resting on the wet railing, face slightly upward and eyes half-closed, expression not sad but released — acceptance, the opposite of tension — rain falling visibly in the shallow-focus background, Bangkok city lights far below refracted in wet glass, forty floors down. Background: wet railing, rain falling behind him, blurred city lights far below in charcoal and silver tones. Wardrobe: dark shirt, slightly damp. Typography: render "the room is worth staying in." as three short left-aligned lowercase lines; first word in white rectangular label, rest in heavy white type on dark background. Add "day three of rain" as tiny white microcopy. Photo treatment: realistic black-and-white, close crop on face and railing, visible rain texture, subtle grain, no color, no logos, no watermark.""",

    (10, "arc"): """Create an image in soft-analog-future-editorial-poster-style. Aspect ratio 9:16. Scene: a case file archive showing an extreme close crop of two white reclining chair armrests side by side with a 12-centimetre gap between them. A single hand with its fingers just resting on the edge of the right armrest — the hand has come from the left chair. Photographed from directly above. The armrest being touched is labeled with a small cream tag "CHAIR 43". A pale-blue translucent panel overlays the gap between the chairs with the measurement "12.0 cm → 0 cm · DURATION: 4 SECONDS". Typography: very large black neo-grotesk type reading "FOUR SECONDS. BY CHOICE." Add "09:14:31 HUB TIME · FIRST UNMEDIATED PHYSICAL CONTACT IN 17 YEARS · WARMTH CONFIRMED" as tiny editorial microcopy. Visual treatment: warm cream paper background, strict grid layout, clinical overhead photograph of the two chairs as hero image, thin rules, soft institutional overhead light, gentle paper grain, pale-blue translucent measurement panel in the gap. No watermark, no logo, no cyberpunk.""",
}

# ── Generate ─────────────────────────────────────────────────────────────────
def generate(ch: int, layer: str, dry: bool = False):
    key = (ch, layer)
    if key not in PROMPTS:
        print(f"No prompt for ch{ch}-{layer}")
        return

    out_path = OUT_DIR / f"ch{ch}-{layer}.jpg"
    if out_path.exists():
        print(f"  skip {out_path.name} (exists)")
        return

    prompt = PROMPTS[key]
    if dry:
        print(f"\n── ch{ch}-{layer} ──")
        print(prompt[:120] + "…")
        return

    print(f"  generating ch{ch}-{layer}.jpg …", end="", flush=True)
    resp = requests.post(
        f"{API_URL}?key={KEY}",
        headers={"Content-Type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        },
        timeout=120,
    )

    if resp.status_code != 200:
        print(f" FAILED {resp.status_code}: {resp.text[:200]}")
        return

    data = resp.json()
    try:
        parts = data["candidates"][0]["content"]["parts"]
        img_data = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
        out_path.write_bytes(base64.b64decode(img_data))
        print(f" saved ({out_path.stat().st_size // 1024}KB)")
    except (KeyError, StopIteration) as e:
        print(f" no image in response: {e}")
        print(json.dumps(data, indent=2)[:500])

    time.sleep(2)  # rate-limit buffer


if __name__ == "__main__":
    args = sys.argv[1:]
    dry = "--dry" in args
    args = [a for a in args if a != "--dry"]

    if len(args) == 2:
        generate(int(args[0]), args[1], dry)
    else:
        for ch in range(1, 11):
            for layer in ("sim", "arc"):
                generate(ch, layer, dry)
