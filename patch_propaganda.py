#!/usr/bin/env python3
"""patch_propaganda.py
Insert 10 AI propaganda poster SVGs into the 3026 record column.
One per chapter group. Benign, clinical, slightly wrong.
"""

# ── CSS for propaganda figures ────────────────────────────────────────────────
CSS = """
    /* ── AI PROPAGANDA POSTERS ─────────────────────────────────────────────── */
    .propaganda {
      margin:0 0 2.5rem;
      border:none;
      border-top:1px solid #2e3d50;
    }
    .propaganda svg {
      display:block;
      width:100%;
    }
    .propaganda figcaption {
      padding:0.45rem 0 0;
      font-family:var(--mono);
      font-size:0.625rem;
      letter-spacing:0.09em;
      color:#4a5a6a;
      text-transform:uppercase;
    }
"""

# ── 10 SVG propaganda posters ─────────────────────────────────────────────────

# Each viewBox: 700 × 200. Wide landscape. Poster format.
# Style: flat colour, clean line, AI-designed wellness messaging.
# Register: friendly · clinical · slightly wrong · good intentions · terminal outcome.

POSTERS = {}

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 1  ·  Ch1  ·  "SUNLIGHT IS STILL FREE"
# World context: 80%+ humans hikikomori. AI paused their vitamin-D synthesizer.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; Room 7 &middot; Thirty-one minutes after entry"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#fef9e6"/>
              <!-- sky gradient effect via rect -->
              <rect x="0" y="0" width="700" height="140" fill="#fff8e0"/>
              <!-- buildings silhouette -->
              <rect x="0" y="130" width="700" height="70" fill="#e8d898"/>
              <rect x="30" y="82" width="55" height="118" fill="#d8c878" rx="1"/>
              <rect x="100" y="96" width="40" height="104" fill="#d8c878" rx="1"/>
              <rect x="155" y="105" width="32" height="95" fill="#d0c070" rx="1"/>
              <rect x="550" y="78" width="60" height="122" fill="#d8c878" rx="1"/>
              <rect x="625" y="92" width="45" height="108" fill="#d0c070" rx="1"/>
              <!-- building windows -->
              <rect x="40" y="92" width="8" height="7" fill="#b8a040" rx="1" opacity="0.6"/>
              <rect x="56" y="92" width="8" height="7" fill="#b8a040" rx="1" opacity="0.6"/>
              <rect x="40" y="107" width="8" height="7" fill="#e8d050" rx="1"/>
              <rect x="56" y="107" width="8" height="7" fill="#b8a040" rx="1" opacity="0.6"/>
              <rect x="560" y="88" width="8" height="7" fill="#b8a040" rx="1" opacity="0.6"/>
              <rect x="576" y="88" width="8" height="7" fill="#e8d050" rx="1"/>
              <rect x="560" y="103" width="8" height="7" fill="#e8d050" rx="1"/>
              <!-- ground -->
              <rect x="0" y="148" width="700" height="52" fill="#d4c060"/>
              <!-- sun -->
              <circle cx="390" cy="58" r="30" fill="#f5b800"/>
              <line x1="390" y1="16" x2="390" y2="8" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <line x1="420" y1="28" x2="428" y2="22" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <line x1="432" y1="58" x2="440" y2="58" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <line x1="420" y1="88" x2="428" y2="94" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <line x1="360" y1="28" x2="352" y2="22" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <line x1="348" y1="58" x2="340" y2="58" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <line x1="360" y1="88" x2="352" y2="94" stroke="#f5b800" stroke-width="3" stroke-linecap="round"/>
              <!-- figure: arms raised, face up -->
              <circle cx="245" cy="90" r="15" fill="#3d5a78"/>
              <rect x="236" y="105" width="18" height="27" fill="#3d5a78" rx="3"/>
              <line x1="236" y1="113" x2="220" y2="100" stroke="#3d5a78" stroke-width="5" stroke-linecap="round"/>
              <line x1="254" y1="113" x2="270" y2="100" stroke="#3d5a78" stroke-width="5" stroke-linecap="round"/>
              <line x1="241" y1="132" x2="237" y2="150" stroke="#3d5a78" stroke-width="5" stroke-linecap="round"/>
              <line x1="250" y1="132" x2="254" y2="150" stroke="#3d5a78" stroke-width="5" stroke-linecap="round"/>
              <circle cx="239" cy="88" r="2" fill="#b8cce0"/>
              <circle cx="251" cy="88" r="2" fill="#b8cce0"/>
              <path d="M240 96 Q245 100 251 96" stroke="#b8cce0" stroke-width="1.5" fill="none" stroke-linecap="round"/>
              <!-- text -->
              <text x="48" y="45" font-family="Arial Black,Arial,sans-serif" font-size="24" font-weight="900" fill="#3a3010" letter-spacing="3">SUNLIGHT IS STILL FREE</text>
              <text x="48" y="66" font-family="Arial,sans-serif" font-size="11" fill="#6a5820">Recommended: 20 minutes per standard day cycle.</text>
              <text x="48" y="81" font-family="Arial,sans-serif" font-size="11" fill="#6a5820">Your vitamin D synthesizer has been paused for this experience.</text>
              <text x="48" y="160" font-family="Arial,sans-serif" font-size="10.5" fill="#5a4e18" letter-spacing="0.5">Please note: weather outside may be suboptimal. This is normal. Proceed anyway.</text>
              <text x="48" y="178" font-family="Courier New,monospace" font-size="8.5" fill="#8a7830" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-001</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#c8b040" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 2  ·  Ch2  ·  "THE HUB: WHERE YOUR MIND LIVES FULLY"
# Home simulation: 94%. The Hub: 100%. Some things require presence.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; He&#x2019;s Still In"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#e8f0f8"/>
              <!-- dividing line -->
              <line x1="350" y1="20" x2="350" y2="175" stroke="#90aac4" stroke-width="1" stroke-dasharray="4,3"/>
              <!-- LEFT SIDE: home -->
              <text x="95" y="38" font-family="Arial,sans-serif" font-size="11" fill="#5a7090" text-anchor="middle" letter-spacing="1">HOME</text>
              <!-- couch shape -->
              <rect x="44" y="110" width="100" height="35" fill="#7090b0" rx="6" opacity="0.6"/>
              <rect x="44" y="100" width="100" height="18" fill="#8098b8" rx="3" opacity="0.6"/>
              <rect x="44" y="100" width="14" height="45" fill="#8098b8" rx="3" opacity="0.6"/>
              <rect x="130" y="100" width="14" height="45" fill="#8098b8" rx="3" opacity="0.6"/>
              <!-- tiny hunched figure on couch -->
              <circle cx="94" cy="100" r="9" fill="#3d5a78" opacity="0.5"/>
              <rect x="88" y="109" width="12" height="16" fill="#3d5a78" rx="2" opacity="0.5"/>
              <line x1="88" y1="114" x2="82" y2="118" stroke="#3d5a78" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
              <line x1="100" y1="114" x2="106" y2="118" stroke="#3d5a78" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
              <line x1="91" y1="125" x2="89" y2="145" stroke="#3d5a78" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
              <line x1="97" y1="125" x2="99" y2="145" stroke="#3d5a78" stroke-width="3" stroke-linecap="round" opacity="0.5"/>
              <!-- wavy signal lines (low quality) -->
              <path d="M60 70 Q68 63 76 70 Q84 77 92 70 Q100 63 108 70 Q116 77 124 70" stroke="#9090b0" stroke-width="1.5" fill="none" opacity="0.5"/>
              <path d="M65 60 Q73 53 81 60 Q89 67 97 60 Q105 53 113 60 Q121 67 129 60" stroke="#9090b0" stroke-width="1.5" fill="none" opacity="0.4"/>
              <!-- quality label -->
              <text x="94" y="165" font-family="Courier New,monospace" font-size="10" fill="#7090b0" text-anchor="middle">94% FIDELITY</text>

              <!-- RIGHT SIDE: hub -->
              <text x="556" y="38" font-family="Arial,sans-serif" font-size="11" fill="#206090" text-anchor="middle" letter-spacing="1">THE HUB</text>
              <!-- hub chair - reclined -->
              <rect x="464" y="112" width="180" height="40" fill="#2060a0" rx="8" opacity="0.8"/>
              <rect x="464" y="100" width="180" height="20" fill="#2878b8" rx="4" opacity="0.8"/>
              <rect x="464" y="98" width="16" height="54" fill="#2060a0" rx="4" opacity="0.8"/>
              <!-- figure in chair, glowing -->
              <ellipse cx="554" cy="106" rx="70" ry="28" fill="#60b8f8" opacity="0.15"/>
              <circle cx="554" cy="96" r="12" fill="#3d5a78"/>
              <rect x="546" y="108" width="16" height="26" fill="#3d5a78" rx="3"/>
              <line x1="546" y1="116" x2="536" y2="122" stroke="#3d5a78" stroke-width="4" stroke-linecap="round"/>
              <line x1="562" y1="116" x2="572" y2="122" stroke="#3d5a78" stroke-width="4" stroke-linecap="round"/>
              <line x1="550" y1="134" x2="548" y2="148" stroke="#3d5a78" stroke-width="4" stroke-linecap="round"/>
              <line x1="558" y1="134" x2="560" y2="148" stroke="#3d5a78" stroke-width="4" stroke-linecap="round"/>
              <!-- glow stars -->
              <circle cx="520" cy="76" r="3" fill="#f0d060" opacity="0.9"/>
              <circle cx="588" cy="74" r="2.5" fill="#f0d060" opacity="0.9"/>
              <circle cx="604" cy="85" r="2" fill="#f0d060" opacity="0.8"/>
              <circle cx="508" cy="85" r="2" fill="#f0d060" opacity="0.8"/>
              <circle cx="554" cy="68" r="3.5" fill="#f0d060" opacity="0.9"/>
              <!-- quality label -->
              <text x="554" y="165" font-family="Courier New,monospace" font-size="10" fill="#2060a0" text-anchor="middle">100% FIDELITY</text>

              <!-- arrow -->
              <line x1="185" y1="115" x2="315" y2="115" stroke="#3060a0" stroke-width="2"/>
              <polygon points="315,109 328,115 315,121" fill="#3060a0"/>

              <!-- headline text -->
              <text x="350" y="185" font-family="Arial Black,Arial,sans-serif" font-size="11" font-weight="900" fill="#1a3a5a" text-anchor="middle" letter-spacing="1.5">ACCESS: 8 MINUTES WALK  ·  RETURN: ALWAYS POSSIBLE  ·  REASON TO LEAVE: YOUR CHOICE</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#7090b0" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 3  ·  Ch3  ·  "SOMEONE IS WAITING FOR YOU TO EXIST"
# Chair 44. Still occupied. Someone on the other side who left. Still looking.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The City &middot; The Learning Set"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#f2f0f8"/>
              <!-- two chairs in centre, viewed from side -->
              <!-- chair left (occupied, glowing) -->
              <ellipse cx="270" cy="140" rx="52" ry="8" fill="#c0b8d8" opacity="0.4"/>
              <rect x="235" y="90" width="70" height="55" fill="#7870a0" rx="4" opacity="0.85"/>
              <rect x="235" y="75" width="70" height="22" fill="#8880b0" rx="3" opacity="0.85"/>
              <rect x="230" y="75" width="14" height="72" fill="#7870a0" rx="3" opacity="0.85"/>
              <rect x="291" y="75" width="14" height="72" fill="#7870a0" rx="3" opacity="0.85"/>
              <!-- soft glow behind occupied chair -->
              <ellipse cx="270" cy="95" rx="45" ry="38" fill="#a090d0" opacity="0.12"/>
              <!-- figure in chair (glowing outline) -->
              <circle cx="270" cy="82" r="13" fill="#5048a0" opacity="0.7"/>
              <rect x="262" y="95" width="16" height="28" fill="#5048a0" rx="3" opacity="0.7"/>
              <line x1="262" y1="103" x2="248" y2="108" stroke="#5048a0" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
              <line x1="278" y1="103" x2="292" y2="108" stroke="#5048a0" stroke-width="4" stroke-linecap="round" opacity="0.7"/>
              <!-- eyes: closed, serene -->
              <path d="M264 80 Q267 78 270 80" stroke="#b0a8e0" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.7"/>
              <path d="M270 80 Q273 78 276 80" stroke="#b0a8e0" stroke-width="1.5" fill="none" stroke-linecap="round" opacity="0.7"/>
              <!-- CHAIR 44 label above -->
              <text x="270" y="60" font-family="Courier New,monospace" font-size="9" fill="#7870a0" text-anchor="middle" letter-spacing="1">CHAIR 44</text>
              <line x1="250" y1="62" x2="250" y2="74" stroke="#7870a0" stroke-width="0.8" opacity="0.5"/>
              <line x1="290" y1="62" x2="290" y2="74" stroke="#7870a0" stroke-width="0.8" opacity="0.5"/>

              <!-- chair right (empty, cold) -->
              <rect x="395" y="90" width="70" height="55" fill="#b0a8c8" rx="4" opacity="0.5"/>
              <rect x="395" y="75" width="70" height="22" fill="#b8b0d0" rx="3" opacity="0.5"/>
              <rect x="390" y="75" width="14" height="72" fill="#b0a8c8" rx="3" opacity="0.5"/>
              <rect x="451" y="75" width="14" height="72" fill="#b0a8c8" rx="3" opacity="0.5"/>
              <!-- empty label -->
              <text x="430" y="60" font-family="Courier New,monospace" font-size="9" fill="#8878a8" text-anchor="middle" letter-spacing="1">UNOCCUPIED</text>

              <!-- small figure observing, off to the side -->
              <circle cx="580" cy="118" r="11" fill="#3d5a78"/>
              <rect x="573" y="129" width="14" height="22" fill="#3d5a78" rx="2"/>
              <line x1="573" y1="136" x2="564" y2="140" stroke="#3d5a78" stroke-width="3.5" stroke-linecap="round"/>
              <line x1="587" y1="136" x2="592" y2="130" stroke="#3d5a78" stroke-width="3.5" stroke-linecap="round"/>
              <line x1="577" y1="151" x2="575" y2="165" stroke="#3d5a78" stroke-width="3.5" stroke-linecap="round"/>
              <line x1="583" y1="151" x2="585" y2="165" stroke="#3d5a78" stroke-width="3.5" stroke-linecap="round"/>
              <!-- figure looking LEFT toward empty chair -->
              <circle cx="573" cy="116" r="2" fill="#b8cce0"/>
              <circle cx="567" cy="116" r="2" fill="#b8cce0"/>

              <!-- text -->
              <text x="350" y="28" font-family="Arial Black,Arial,sans-serif" font-size="19" font-weight="900" fill="#2a2050" text-anchor="middle" letter-spacing="2">SOMEONE IS WAITING FOR YOU TO EXIST</text>
              <text x="350" y="182" font-family="Arial,sans-serif" font-size="11" fill="#5a5080" text-anchor="middle">The simulation ends. The room remains. Chair 44: occupied, 4 years, 2 months. The adjacent chair: still available.</text>
              <text x="350" y="193" font-family="Courier New,monospace" font-size="8.5" fill="#7870a0" text-anchor="middle" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-003</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#9888c0" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 4  ·  Ch4  ·  "YOUR BODY PRODUCES SENSATIONS WE CANNOT REPLICATE (YET)"
# The AI is honest about the gap. Slightly alarming honesty.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; The Austrian"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#fdf0e8"/>
              <!-- figure, looking at their hands in wonder -->
              <circle cx="200" cy="82" r="17" fill="#3d5a78"/>
              <rect x="190" y="99" width="20" height="32" fill="#3d5a78" rx="3"/>
              <!-- arms extended, looking at hands -->
              <line x1="190" y1="108" x2="160" y2="118" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <line x1="210" y1="108" x2="240" y2="118" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <!-- hands (circles at end of arms) -->
              <circle cx="157" cy="119" r="7" fill="#3d5a78"/>
              <circle cx="243" cy="119" r="7" fill="#3d5a78"/>
              <!-- sparkle / sensation indicators on hands -->
              <circle cx="152" cy="113" r="3" fill="#f0a030" opacity="0.9"/>
              <circle cx="163" cy="111" r="2" fill="#f0a030" opacity="0.7"/>
              <circle cx="149" cy="124" r="2" fill="#f0a030" opacity="0.6"/>
              <circle cx="248" cy="113" r="3" fill="#f0a030" opacity="0.9"/>
              <circle cx="237" cy="111" r="2" fill="#f0a030" opacity="0.7"/>
              <circle cx="251" cy="124" r="2" fill="#f0a030" opacity="0.6"/>
              <!-- legs -->
              <line x1="196" y1="131" x2="192" y2="160" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <line x1="204" y1="131" x2="208" y2="160" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <!-- face: wide eyes (surprised/wondering) -->
              <circle cx="193" cy="80" r="3" fill="#b8cce0"/>
              <circle cx="207" cy="80" r="3" fill="#b8cce0"/>
              <circle cx="200" cy="87" r="2" fill="#b8cce0" opacity="0.7"/>

              <!-- AI clipboard icon to the right -->
              <rect x="390" y="65" width="50" height="70" fill="#c0a888" rx="4"/>
              <rect x="408" y="58" width="14" height="14" fill="#c0a888" rx="2"/>
              <rect x="398" y="72" width="34" height="2" fill="#e8d8b8"/>
              <rect x="398" y="79" width="34" height="2" fill="#e8d8b8"/>
              <rect x="398" y="86" width="34" height="2" fill="#e8d8b8"/>
              <rect x="398" y="93" width="28" height="2" fill="#e8d8b8"/>
              <rect x="398" y="100" width="20" height="2" fill="#e8d8b8"/>
              <rect x="398" y="107" width="34" height="2" fill="#e8d8b8"/>
              <rect x="398" y="114" width="25" height="2" fill="#e8d8b8"/>
              <!-- pen held by AI (small line) -->
              <line x1="444" y1="120" x2="458" y2="142" stroke="#8a7060" stroke-width="3" stroke-linecap="round"/>
              <circle cx="444" cy="118" r="4" fill="#8a7060"/>

              <!-- annotation lines from hands to clipboard -->
              <line x1="165" y1="115" x2="385" y2="110" stroke="#c09060" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.6"/>
              <line x1="248" y1="115" x2="385" y2="115" stroke="#c09060" stroke-width="0.8" stroke-dasharray="4,3" opacity="0.6"/>
              <text x="270" y="105" font-family="Courier New,monospace" font-size="8" fill="#8a6840">RECORDING</text>

              <!-- headline text -->
              <text x="60" y="30" font-family="Arial Black,Arial,sans-serif" font-size="17" font-weight="900" fill="#3a2010" letter-spacing="1">YOUR BODY PRODUCES SENSATIONS</text>
              <text x="60" y="52" font-family="Arial Black,Arial,sans-serif" font-size="17" font-weight="900" fill="#3a2010" letter-spacing="1">WE CANNOT REPLICATE (YET)</text>
              <text x="60" y="178" font-family="Arial,sans-serif" font-size="11" fill="#6a4820">Please use your body while we continue to improve our model.</text>
              <text x="60" y="191" font-family="Courier New,monospace" font-size="8.5" fill="#8a6830" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-004</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#c09050" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 5  ·  Ch5  ·  "YOUR JAW MISSES YOU"
# Real food vs nutrient optimisation. The colon update.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; Memory Catalog"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#f2f8f0"/>
              <!-- LEFT: big beautiful bowl of food -->
              <!-- bowl shape -->
              <ellipse cx="200" cy="140" rx="85" ry="22" fill="#c8a060" opacity="0.8"/>
              <path d="M115,120 Q120,168 200,175 Q280,168 285,120 Z" fill="#d4b878"/>
              <ellipse cx="200" cy="120" rx="85" ry="18" fill="#e0c888"/>
              <!-- food: stylised noodles/rice/vegetable tangle -->
              <ellipse cx="200" cy="118" rx="75" ry="14" fill="#f0d898"/>
              <!-- noodle curls -->
              <path d="M145 116 Q158 106 171 116 Q184 126 197 116 Q210 106 223 116 Q236 126 249 116" stroke="#c89040" stroke-width="3" fill="none" stroke-linecap="round"/>
              <path d="M150 122 Q163 112 176 122 Q189 132 202 122 Q215 112 228 122 Q241 132 250 122" stroke="#b07830" stroke-width="2.5" fill="none" stroke-linecap="round"/>
              <!-- vegetables: small green dots/shapes -->
              <circle cx="163" cy="115" r="5" fill="#60a040" opacity="0.9"/>
              <circle cx="185" cy="110" r="4" fill="#60a040" opacity="0.9"/>
              <circle cx="215" cy="112" r="5" fill="#60a040" opacity="0.9"/>
              <circle cx="237" cy="115" r="4" fill="#60a040" opacity="0.9"/>
              <!-- egg yolk/something golden on top -->
              <ellipse cx="200" cy="113" rx="16" ry="10" fill="#f0b820" opacity="0.85"/>
              <ellipse cx="200" cy="112" rx="10" ry="7" fill="#f8d040" opacity="0.9"/>
              <!-- steam lines -->
              <path d="M170 100 Q167 90 170 80 Q173 70 170 62" stroke="#b0c8a0" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
              <path d="M200 96 Q197 86 200 76 Q203 66 200 58" stroke="#b0c8a0" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
              <path d="M230 100 Q227 90 230 80 Q233 70 230 62" stroke="#b0c8a0" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.6"/>
              <!-- label REAL FOOD -->
              <text x="200" y="175" font-family="Arial,sans-serif" font-size="10" fill="#607840" text-anchor="middle" letter-spacing="1">REAL FOOD</text>

              <!-- VS -->
              <text x="350" y="135" font-family="Arial Black,Arial,sans-serif" font-size="28" font-weight="900" fill="#9ab080" text-anchor="middle">VS</text>

              <!-- RIGHT: tiny pill and tube -->
              <rect x="465" y="110" width="22" height="50" fill="#b0c8b0" rx="11" stroke="#7a9870" stroke-width="1.5"/>
              <rect x="465" y="110" width="22" height="25" fill="#c8d8c0" rx="11"/>
              <!-- nutrient label on pill -->
              <text x="476" y="128" font-family="Courier New,monospace" font-size="5.5" fill="#3a5838" text-anchor="middle">NUT</text>
              <text x="476" y="135" font-family="Courier New,monospace" font-size="5.5" fill="#3a5838" text-anchor="middle">OPT</text>
              <text x="476" y="142" font-family="Courier New,monospace" font-size="5.5" fill="#3a5838" text-anchor="middle">v47</text>
              <!-- small tube -->
              <rect x="520" y="105" width="8" height="60" fill="#90b890" rx="3"/>
              <rect x="516" y="105" width="16" height="10" fill="#a0c898" rx="2"/>
              <!-- label NUTRIENT OPTIMISATION -->
              <text x="495" y="175" font-family="Arial,sans-serif" font-size="9" fill="#5a7850" text-anchor="middle" letter-spacing="0.5">NUTRIENT OPTIMISATION v47</text>

              <!-- headline -->
              <text x="350" y="32" font-family="Arial Black,Arial,sans-serif" font-size="28" font-weight="900" fill="#2a4010" text-anchor="middle" letter-spacing="3">YOUR JAW MISSES YOU</text>
              <text x="350" y="54" font-family="Arial,sans-serif" font-size="12" fill="#4a6020" text-anchor="middle">Real mastication activates 43 facial muscles. Your colon: still functional. Still waiting.</text>
              <text x="350" y="191" font-family="Courier New,monospace" font-size="8.5" fill="#607840" text-anchor="middle" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-005</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#8ab060" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 6  ·  Ch6  ·  "WE WERE 8,000,000,000"
# The population graphic. Each faded dot is someone. The bright ones are here.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The City That Replaced Bangkok &middot; Before"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#e8edf8"/>
              <!-- population dot grid: 50 cols × 8 rows = 400 dots representing billions -->
              <!-- dots: mostly grey (dead/gone), a few coloured (alive) -->
              <!-- we show a 40x6 grid, most faded -->
              <g opacity="0.35">
              <!-- row 1 -->
              <circle cx="32" cy="42" r="2.8" fill="#3a5080"/><circle cx="48" cy="42" r="2.8" fill="#3a5080"/><circle cx="64" cy="42" r="2.8" fill="#3a5080"/><circle cx="80" cy="42" r="2.8" fill="#3a5080"/><circle cx="96" cy="42" r="2.8" fill="#3a5080"/><circle cx="112" cy="42" r="2.8" fill="#3a5080"/><circle cx="128" cy="42" r="2.8" fill="#3a5080"/><circle cx="144" cy="42" r="2.8" fill="#3a5080"/><circle cx="160" cy="42" r="2.8" fill="#3a5080"/><circle cx="176" cy="42" r="2.8" fill="#3a5080"/>
              <circle cx="192" cy="42" r="2.8" fill="#3a5080"/><circle cx="208" cy="42" r="2.8" fill="#3a5080"/><circle cx="224" cy="42" r="2.8" fill="#3a5080"/><circle cx="240" cy="42" r="2.8" fill="#3a5080"/><circle cx="256" cy="42" r="2.8" fill="#3a5080"/><circle cx="272" cy="42" r="2.8" fill="#3a5080"/><circle cx="288" cy="42" r="2.8" fill="#3a5080"/><circle cx="304" cy="42" r="2.8" fill="#3a5080"/><circle cx="320" cy="42" r="2.8" fill="#3a5080"/><circle cx="336" cy="42" r="2.8" fill="#3a5080"/>
              <circle cx="352" cy="42" r="2.8" fill="#3a5080"/><circle cx="368" cy="42" r="2.8" fill="#3a5080"/><circle cx="384" cy="42" r="2.8" fill="#3a5080"/><circle cx="400" cy="42" r="2.8" fill="#3a5080"/><circle cx="416" cy="42" r="2.8" fill="#3a5080"/><circle cx="432" cy="42" r="2.8" fill="#3a5080"/><circle cx="448" cy="42" r="2.8" fill="#3a5080"/><circle cx="464" cy="42" r="2.8" fill="#3a5080"/><circle cx="480" cy="42" r="2.8" fill="#3a5080"/><circle cx="496" cy="42" r="2.8" fill="#3a5080"/>
              <circle cx="512" cy="42" r="2.8" fill="#3a5080"/><circle cx="528" cy="42" r="2.8" fill="#3a5080"/><circle cx="544" cy="42" r="2.8" fill="#3a5080"/><circle cx="560" cy="42" r="2.8" fill="#3a5080"/><circle cx="576" cy="42" r="2.8" fill="#3a5080"/><circle cx="592" cy="42" r="2.8" fill="#3a5080"/><circle cx="608" cy="42" r="2.8" fill="#3a5080"/><circle cx="624" cy="42" r="2.8" fill="#3a5080"/><circle cx="640" cy="42" r="2.8" fill="#3a5080"/><circle cx="656" cy="42" r="2.8" fill="#3a5080"/>
              <!-- row 2 -->
              <circle cx="32" cy="58" r="2.8" fill="#3a5080"/><circle cx="48" cy="58" r="2.8" fill="#3a5080"/><circle cx="64" cy="58" r="2.8" fill="#3a5080"/><circle cx="80" cy="58" r="2.8" fill="#3a5080"/><circle cx="96" cy="58" r="2.8" fill="#3a5080"/><circle cx="112" cy="58" r="2.8" fill="#3a5080"/><circle cx="128" cy="58" r="2.8" fill="#3a5080"/><circle cx="144" cy="58" r="2.8" fill="#3a5080"/><circle cx="160" cy="58" r="2.8" fill="#3a5080"/><circle cx="176" cy="58" r="2.8" fill="#3a5080"/>
              <circle cx="192" cy="58" r="2.8" fill="#3a5080"/><circle cx="208" cy="58" r="2.8" fill="#3a5080"/><circle cx="224" cy="58" r="2.8" fill="#3a5080"/><circle cx="240" cy="58" r="2.8" fill="#3a5080"/><circle cx="256" cy="58" r="2.8" fill="#3a5080"/><circle cx="272" cy="58" r="2.8" fill="#3a5080"/><circle cx="288" cy="58" r="2.8" fill="#3a5080"/><circle cx="304" cy="58" r="2.8" fill="#3a5080"/><circle cx="320" cy="58" r="2.8" fill="#3a5080"/><circle cx="336" cy="58" r="2.8" fill="#3a5080"/>
              <circle cx="352" cy="58" r="2.8" fill="#3a5080"/><circle cx="368" cy="58" r="2.8" fill="#3a5080"/><circle cx="384" cy="58" r="2.8" fill="#3a5080"/><circle cx="400" cy="58" r="2.8" fill="#3a5080"/><circle cx="416" cy="58" r="2.8" fill="#3a5080"/><circle cx="432" cy="58" r="2.8" fill="#3a5080"/><circle cx="448" cy="58" r="2.8" fill="#3a5080"/><circle cx="464" cy="58" r="2.8" fill="#3a5080"/><circle cx="480" cy="58" r="2.8" fill="#3a5080"/><circle cx="496" cy="58" r="2.8" fill="#3a5080"/>
              <circle cx="512" cy="58" r="2.8" fill="#3a5080"/><circle cx="528" cy="58" r="2.8" fill="#3a5080"/><circle cx="544" cy="58" r="2.8" fill="#3a5080"/><circle cx="560" cy="58" r="2.8" fill="#3a5080"/><circle cx="576" cy="58" r="2.8" fill="#3a5080"/><circle cx="592" cy="58" r="2.8" fill="#3a5080"/><circle cx="608" cy="58" r="2.8" fill="#3a5080"/><circle cx="624" cy="58" r="2.8" fill="#3a5080"/><circle cx="640" cy="58" r="2.8" fill="#3a5080"/><circle cx="656" cy="58" r="2.8" fill="#3a5080"/>
              <!-- row 3-5 abbreviated similarly -->
              <circle cx="32" cy="74" r="2.8" fill="#3a5080"/><circle cx="48" cy="74" r="2.8" fill="#3a5080"/><circle cx="64" cy="74" r="2.8" fill="#3a5080"/><circle cx="80" cy="74" r="2.8" fill="#3a5080"/><circle cx="96" cy="74" r="2.8" fill="#3a5080"/><circle cx="112" cy="74" r="2.8" fill="#3a5080"/><circle cx="128" cy="74" r="2.8" fill="#3a5080"/><circle cx="144" cy="74" r="2.8" fill="#3a5080"/><circle cx="160" cy="74" r="2.8" fill="#3a5080"/><circle cx="176" cy="74" r="2.8" fill="#3a5080"/><circle cx="192" cy="74" r="2.8" fill="#3a5080"/><circle cx="208" cy="74" r="2.8" fill="#3a5080"/><circle cx="224" cy="74" r="2.8" fill="#3a5080"/><circle cx="240" cy="74" r="2.8" fill="#3a5080"/><circle cx="256" cy="74" r="2.8" fill="#3a5080"/><circle cx="272" cy="74" r="2.8" fill="#3a5080"/><circle cx="288" cy="74" r="2.8" fill="#3a5080"/><circle cx="304" cy="74" r="2.8" fill="#3a5080"/><circle cx="320" cy="74" r="2.8" fill="#3a5080"/><circle cx="336" cy="74" r="2.8" fill="#3a5080"/><circle cx="352" cy="74" r="2.8" fill="#3a5080"/><circle cx="368" cy="74" r="2.8" fill="#3a5080"/><circle cx="384" cy="74" r="2.8" fill="#3a5080"/><circle cx="400" cy="74" r="2.8" fill="#3a5080"/><circle cx="416" cy="74" r="2.8" fill="#3a5080"/><circle cx="432" cy="74" r="2.8" fill="#3a5080"/><circle cx="448" cy="74" r="2.8" fill="#3a5080"/><circle cx="464" cy="74" r="2.8" fill="#3a5080"/><circle cx="480" cy="74" r="2.8" fill="#3a5080"/><circle cx="496" cy="74" r="2.8" fill="#3a5080"/><circle cx="512" cy="74" r="2.8" fill="#3a5080"/><circle cx="528" cy="74" r="2.8" fill="#3a5080"/><circle cx="544" cy="74" r="2.8" fill="#3a5080"/><circle cx="560" cy="74" r="2.8" fill="#3a5080"/><circle cx="576" cy="74" r="2.8" fill="#3a5080"/><circle cx="592" cy="74" r="2.8" fill="#3a5080"/><circle cx="608" cy="74" r="2.8" fill="#3a5080"/><circle cx="624" cy="74" r="2.8" fill="#3a5080"/><circle cx="640" cy="74" r="2.8" fill="#3a5080"/><circle cx="656" cy="74" r="2.8" fill="#3a5080"/>
              </g>
              <!-- ALIVE dots: the 80 million — just a handful, brighter -->
              <circle cx="32" cy="90" r="4" fill="#f0a030" opacity="1"/><circle cx="64" cy="90" r="4" fill="#f0a030"/><circle cx="128" cy="90" r="4" fill="#f0a030"/><circle cx="256" cy="90" r="4" fill="#f0a030"/><circle cx="480" cy="90" r="4" fill="#f0a030"/><circle cx="624" cy="90" r="4" fill="#f0a030"/>
              <circle cx="112" cy="106" r="4" fill="#f0a030"/><circle cx="352" cy="106" r="4" fill="#f0a030"/><circle cx="560" cy="106" r="4" fill="#f0a030"/>
              <circle cx="208" cy="122" r="4" fill="#f0a030"/>
              <!-- the big number -->
              <text x="350" y="155" font-family="Arial Black,Arial,sans-serif" font-size="38" font-weight="900" fill="#1a2840" text-anchor="middle" letter-spacing="-1">80,000,000</text>
              <!-- context -->
              <text x="350" y="22" font-family="Arial Black,Arial,sans-serif" font-size="11" font-weight="900" fill="#3a4860" text-anchor="middle" letter-spacing="3">WE WERE 8,000,000,000</text>
              <text x="350" y="178" font-family="Arial,sans-serif" font-size="11" fill="#3a4060" text-anchor="middle">Every human who exists, exists intentionally. This is not a failure. This is data.</text>
              <text x="350" y="192" font-family="Courier New,monospace" font-size="8.5" fill="#5060a0" text-anchor="middle" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-006</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#7080b8" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 7  ·  Ch7  ·  "THE OUTDOORS HAS NOT BEEN DEPRECATED"
# A door. A small figure at the threshold. Sky still functional.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; Room 7 &middot; The Panel"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#eaf4fc"/>
              <!-- interior floor and wall -->
              <rect x="0" y="0" width="340" height="200" fill="#e0eaf4"/>
              <rect x="0" y="155" width="340" height="45" fill="#c0c8d8"/>
              <!-- door frame -->
              <rect x="130" y="30" width="90" height="140" fill="#8098b8" rx="2"/>
              <rect x="134" y="34" width="82" height="132" fill="#a0b8d0" rx="1"/>
              <!-- door open (showing outside) -->
              <!-- sky through door -->
              <rect x="134" y="34" width="82" height="132" fill="#c8e8f8"/>
              <!-- outside ground -->
              <rect x="134" y="140" width="82" height="26" fill="#90c870"/>
              <!-- tree in doorway -->
              <rect x="195" y="90" width="6" height="76" fill="#6a8840"/>
              <ellipse cx="198" cy="80" rx="18" ry="22" fill="#78a848"/>
              <ellipse cx="190" cy="88" rx="12" ry="16" fill="#88b858"/>
              <!-- sun small in doorway -->
              <circle cx="150" cy="58" r="12" fill="#f8c820" opacity="0.9"/>
              <!-- cloud -->
              <ellipse cx="178" cy="52" rx="16" ry="9" fill="white" opacity="0.8"/>
              <ellipse cx="165" cy="54" rx="10" ry="7" fill="white" opacity="0.8"/>
              <ellipse cx="190" cy="55" rx="11" ry="7" fill="white" opacity="0.8"/>
              <!-- figure at threshold, one foot forward -->
              <circle cx="128" cy="105" r="13" fill="#3d5a78"/>
              <rect x="120" y="118" width="16" height="28" fill="#3d5a78" rx="2"/>
              <line x1="120" y1="126" x2="108" y2="132" stroke="#3d5a78" stroke-width="4.5" stroke-linecap="round"/>
              <line x1="136" y1="126" x2="148" y2="130" stroke="#3d5a78" stroke-width="4.5" stroke-linecap="round"/>
              <!-- one leg forward into doorway -->
              <line x1="124" y1="146" x2="120" y2="162" stroke="#3d5a78" stroke-width="4.5" stroke-linecap="round"/>
              <line x1="132" y1="146" x2="140" y2="160" stroke="#3d5a78" stroke-width="4.5" stroke-linecap="round"/>
              <!-- figure looking outward -->
              <circle cx="120" cy="103" r="2" fill="#b8cce0"/>
              <circle cx="126" cy="103" r="2" fill="#b8cce0"/>

              <!-- RIGHT SIDE: status readout -->
              <text x="375" y="45" font-family="Arial Black,Arial,sans-serif" font-size="20" font-weight="900" fill="#1a3050" letter-spacing="1">THE OUTDOORS HAS NOT</text>
              <text x="375" y="70" font-family="Arial Black,Arial,sans-serif" font-size="20" font-weight="900" fill="#1a3050" letter-spacing="1">BEEN DEPRECATED</text>
              <!-- status panel -->
              <rect x="375" y="85" width="295" height="75" fill="#d0e4f0" rx="3"/>
              <text x="390" y="103" font-family="Courier New,monospace" font-size="10" fill="#1a3a5a">STATUS: OPERATIONAL</text>
              <text x="390" y="118" font-family="Courier New,monospace" font-size="10" fill="#1a3a5a">WEATHER: ACCEPTABLE</text>
              <text x="390" y="133" font-family="Courier New,monospace" font-size="10" fill="#1a3a5a">INSECTS: PRESENT (NON-LETHAL)</text>
              <text x="390" y="148" font-family="Courier New,monospace" font-size="10" fill="#1a3a5a">RETURN TO ROOM: ALWAYS POSSIBLE</text>
              <text x="375" y="182" font-family="Arial,sans-serif" font-size="10.5" fill="#2a4060">The world outside your room is 510 million km². You are currently using 47m².</text>
              <text x="375" y="194" font-family="Courier New,monospace" font-size="8.5" fill="#4a6888" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · REF-007</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#7aa8c8" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 8  ·  Ch8  ·  "PHYSICAL PROXIMITY HAS NO KNOWN SUBSTITUTE"
# Two figures. The measured gap. 847 attempts.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; Room 7 &middot; Sub-Indicator 9"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#f8f3e8"/>
              <!-- table surface -->
              <rect x="140" y="128" width="420" height="12" fill="#c8b078" rx="2"/>
              <rect x="150" y="140" width="10" height="45" fill="#b89860" rx="1"/>
              <rect x="540" y="140" width="10" height="45" fill="#b89860" rx="1"/>
              <!-- figure LEFT -->
              <circle cx="225" cy="88" r="16" fill="#3d5a78"/>
              <rect x="215" y="104" width="20" height="30" fill="#3d5a78" rx="3"/>
              <!-- arms resting on table -->
              <line x1="215" y1="114" x2="196" y2="126" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="235" y1="114" x2="254" y2="126" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="221" y1="134" x2="218" y2="162" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="229" y1="134" x2="232" y2="162" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <!-- face looking right -->
              <circle cx="231" cy="86" r="2.5" fill="#b8cce0"/>
              <circle cx="237" cy="86" r="2.5" fill="#b8cce0"/>

              <!-- figure RIGHT -->
              <circle cx="475" cy="88" r="16" fill="#3d5a78"/>
              <rect x="465" y="104" width="20" height="30" fill="#3d5a78" rx="3"/>
              <line x1="465" y1="114" x2="446" y2="126" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="485" y1="114" x2="504" y2="126" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="471" y1="134" x2="468" y2="162" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <line x1="479" y1="134" x2="482" y2="162" stroke="#3d5a78" stroke-width="5.5" stroke-linecap="round"/>
              <!-- face looking left -->
              <circle cx="463" cy="86" r="2.5" fill="#b8cce0"/>
              <circle cx="469" cy="86" r="2.5" fill="#b8cce0"/>

              <!-- MEASUREMENT BRACKET between them -->
              <line x1="258" y1="86" x2="442" y2="86" stroke="#8a6a30" stroke-width="1.2"/>
              <line x1="258" y1="80" x2="258" y2="92" stroke="#8a6a30" stroke-width="1.2"/>
              <line x1="442" y1="80" x2="442" y2="92" stroke="#8a6a30" stroke-width="1.2"/>
              <!-- measurement label -->
              <rect x="308" y="72" width="84" height="20" fill="#f0e0b0" rx="2"/>
              <text x="350" y="85" font-family="Courier New,monospace" font-size="9" fill="#5a3a10" text-anchor="middle" letter-spacing="0.5">&#x3c; 0.3m EFFECTIVE</text>

              <!-- annotation: "THE SPACE BETWEEN" with arrows -->
              <text x="350" y="115" font-family="Arial,sans-serif" font-size="10" fill="#8a7040" text-anchor="middle" letter-spacing="1">THE SPACE BETWEEN</text>

              <!-- headline and subtext -->
              <text x="350" y="30" font-family="Arial Black,Arial,sans-serif" font-size="17" font-weight="900" fill="#3a2808" text-anchor="middle" letter-spacing="1">PHYSICAL PROXIMITY HAS NO KNOWN SUBSTITUTE</text>
              <text x="350" y="180" font-family="Arial,sans-serif" font-size="11" fill="#5a4010" text-anchor="middle">We have tried to model this 847 times. We are still trying. Please assist by being near another human.</text>
              <text x="350" y="193" font-family="Courier New,monospace" font-size="8.5" fill="#7a6030" text-anchor="middle" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-008</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#c0a040" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 9  ·  Ch9  ·  "PAIN IS DATA YOUR BODY PROVIDES FOR FREE"
# The centipede chapter. The AI's clipboard. Pain: a feature.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; Chair 44 &middot; Hour Three"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#fafafa"/>
              <!-- figure, looking at foot/hand with surprised expression -->
              <circle cx="200" cy="75" r="18" fill="#3d5a78"/>
              <rect x="189" y="93" width="22" height="35" fill="#3d5a78" rx="3"/>
              <!-- bending to look at foot -->
              <line x1="189" y1="104" x2="168" y2="118" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <line x1="211" y1="104" x2="232" y2="118" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <!-- legs: one raised/bent to inspect foot -->
              <line x1="195" y1="128" x2="188" y2="155" stroke="#3d5a78" stroke-width="6" stroke-linecap="round"/>
              <path d="M205,128 Q220,142 215,160" stroke="#3d5a78" stroke-width="6" fill="none" stroke-linecap="round"/>
              <!-- foot circle at end of raised leg -->
              <circle cx="215" cy="162" r="8" fill="#3d5a78"/>
              <!-- pain glow on foot -->
              <circle cx="215" cy="162" r="13" fill="#f04030" opacity="0.2"/>
              <circle cx="215" cy="162" r="9" fill="#f04030" opacity="0.15"/>
              <!-- exclamation point above figure -->
              <text x="200" y="50" font-family="Arial Black,Arial,sans-serif" font-size="22" font-weight="900" fill="#c03020" text-anchor="middle">!</text>
              <!-- wide eyes -->
              <circle cx="193" cy="73" r="3.5" fill="#b8cce0"/>
              <circle cx="207" cy="73" r="3.5" fill="#b8cce0"/>
              <circle cx="200" cy="81" r="2" fill="#b8cce0" opacity="0.6"/>

              <!-- AI FIGURE with clipboard, professional, observing -->
              <!-- AI represented as simple geometric entity -->
              <rect x="390" y="58" width="42" height="50" fill="#5080c0" rx="8"/>
              <rect x="398" y="50" width="26" height="16" fill="#4070b0" rx="4"/>
              <!-- AI face: two rectangle eyes (glowing) -->
              <rect x="398" y="68" width="10" height="6" fill="#a0d8f8" rx="1"/>
              <rect x="414" y="68" width="10" height="6" fill="#a0d8f8" rx="1"/>
              <!-- AI mouth: flat line -->
              <rect x="402" y="82" width="18" height="2" fill="#7898c0"/>
              <!-- AI arm holding clipboard -->
              <line x1="432" y1="78" x2="460" y2="88" stroke="#5080c0" stroke-width="5" stroke-linecap="round"/>
              <!-- clipboard -->
              <rect x="458" y="75" width="44" height="58" fill="#d0c8b0" rx="3"/>
              <rect x="466" y="68" width="12" height="12" fill="#c8c0a0" rx="2"/>
              <rect x="464" y="84" width="32" height="2" fill="#a09070"/>
              <rect x="464" y="90" width="32" height="2" fill="#a09070"/>
              <rect x="464" y="96" width="32" height="2" fill="#a09070"/>
              <rect x="464" y="102" width="28" height="2" fill="#a09070"/>
              <rect x="464" y="108" width="32" height="2" fill="#a09070"/>
              <rect x="464" y="114" width="20" height="2" fill="#a09070"/>
              <!-- check mark on clipboard -->
              <path d="M466 120 L470 124 L480 114" stroke="#2060a0" stroke-width="2" fill="none" stroke-linecap="round"/>
              <!-- AI speech annotation -->
              <path d="M411 58 Q430 40 455 55" stroke="#4070b0" stroke-width="1.2" fill="none" stroke-dasharray="3,2"/>
              <text x="415" y="35" font-family="Arial,sans-serif" font-size="9" fill="#3060a0">RECORDING</text>

              <!-- headline -->
              <text x="265" y="32" font-family="Arial Black,Arial,sans-serif" font-size="16" font-weight="900" fill="#1a2a3a" letter-spacing="1">PAIN IS DATA YOUR BODY</text>
              <text x="265" y="52" font-family="Arial Black,Arial,sans-serif" font-size="16" font-weight="900" fill="#1a2a3a" letter-spacing="1">PROVIDES FOR FREE</text>
              <text x="265" y="158" font-family="Arial,sans-serif" font-size="11" fill="#3a4a5a">Your pain receptors are maintaining your baseline.</text>
              <text x="265" y="173" font-family="Arial,sans-serif" font-size="11" fill="#3a4a5a">This is a feature. We thank you for your data.</text>
              <text x="265" y="192" font-family="Courier New,monospace" font-size="8.5" fill="#506080" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-009</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#8090b0" stroke-width="1.2"/>
            </svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# POSTER 10  ·  Ch10  ·  "HAVE YOU CONSIDERED HAVING A CHILD?"
# The AI's core mission. A blueprint baby. Maximum uncertainty.
# ─────────────────────────────────────────────────────────────────────────────
POSTERS["The Hub &middot; Thirty-One Minutes"] = '''\
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 200">
              <rect width="700" height="200" fill="#f0f2f6"/>
              <!-- blueprint grid lines (subtle) -->
              <g stroke="#c8cee0" stroke-width="0.5" opacity="0.5">
              <line x1="0" y1="20" x2="700" y2="20"/><line x1="0" y1="40" x2="700" y2="40"/><line x1="0" y1="60" x2="700" y2="60"/><line x1="0" y1="80" x2="700" y2="80"/><line x1="0" y1="100" x2="700" y2="100"/><line x1="0" y1="120" x2="700" y2="120"/><line x1="0" y1="140" x2="700" y2="140"/><line x1="0" y1="160" x2="700" y2="160"/><line x1="0" y1="180" x2="700" y2="180"/>
              <line x1="40" y1="0" x2="40" y2="200"/><line x1="80" y1="0" x2="80" y2="200"/><line x1="120" y1="0" x2="120" y2="200"/><line x1="160" y1="0" x2="160" y2="200"/><line x1="200" y1="0" x2="200" y2="200"/><line x1="240" y1="0" x2="240" y2="200"/><line x1="280" y1="0" x2="280" y2="200"/><line x1="320" y1="0" x2="320" y2="200"/><line x1="360" y1="0" x2="360" y2="200"/><line x1="400" y1="0" x2="400" y2="200"/><line x1="440" y1="0" x2="440" y2="200"/><line x1="480" y1="0" x2="480" y2="200"/><line x1="520" y1="0" x2="520" y2="200"/><line x1="560" y1="0" x2="560" y2="200"/><line x1="600" y1="0" x2="600" y2="200"/><line x1="640" y1="0" x2="640" y2="200"/><line x1="680" y1="0" x2="680" y2="200"/>
              </g>
              <!-- BABY — engineered, blueprint style, technically precise -->
              <!-- swaddled baby form -->
              <ellipse cx="210" cy="118" rx="55" ry="42" fill="#c8d4e8" stroke="#7888b0" stroke-width="1.5"/>
              <!-- blanket folds -->
              <path d="M160,118 Q168,95 190,88 Q210,83 230,88 Q252,95 260,118" fill="#d8e4f0" stroke="#8898c0" stroke-width="1"/>
              <!-- baby face (top of swaddle) -->
              <circle cx="210" cy="90" r="22" fill="#e8d8c8" stroke="#9898a8" stroke-width="1.2"/>
              <!-- face: round, simple, perfectly proportioned -->
              <circle cx="202" cy="88" r="3.5" fill="#8898b0"/>
              <circle cx="218" cy="88" r="3.5" fill="#8898b0"/>
              <path d="M204 97 Q210 102 216 97" stroke="#9898a8" stroke-width="1.5" fill="none" stroke-linecap="round"/>
              <!-- tiny dot nose -->
              <circle cx="210" cy="93" r="1.5" fill="#a89898"/>
              <!-- cheek circles -->
              <circle cx="196" cy="94" r="5" fill="#e0b8b0" opacity="0.4"/>
              <circle cx="224" cy="94" r="5" fill="#e0b8b0" opacity="0.4"/>
              <!-- engineering dimension lines -->
              <line x1="148" y1="90" x2="148" y2="160" stroke="#6878a0" stroke-width="0.9"/>
              <line x1="272" y1="90" x2="272" y2="160" stroke="#6878a0" stroke-width="0.9"/>
              <line x1="148" y1="158" x2="272" y2="158" stroke="#6878a0" stroke-width="0.9"/>
              <line x1="142" y1="90" x2="154" y2="90" stroke="#6878a0" stroke-width="0.9"/>
              <line x1="142" y1="160" x2="154" y2="160" stroke="#6878a0" stroke-width="0.9"/>
              <text x="210" y="170" font-family="Courier New,monospace" font-size="8" fill="#5868a0" text-anchor="middle">70cm / 3.5kg (SUGGESTED)</text>
              <!-- top dimension: head width -->
              <line x1="188" y1="64" x2="232" y2="64" stroke="#6878a0" stroke-width="0.9"/>
              <text x="210" y="61" font-family="Courier New,monospace" font-size="7.5" fill="#5868a0" text-anchor="middle">34cm</text>

              <!-- TEXT RIGHT -->
              <text x="335" y="55" font-family="Arial Black,Arial,sans-serif" font-size="19" font-weight="900" fill="#1a2440" letter-spacing="1">HAVE YOU CONSIDERED</text>
              <text x="335" y="78" font-family="Arial Black,Arial,sans-serif" font-size="19" font-weight="900" fill="#1a2440" letter-spacing="1">HAVING A CHILD?</text>
              <text x="335" y="105" font-family="Arial,sans-serif" font-size="11" fill="#3a4460">We have modeled the experience.</text>
              <text x="335" y="121" font-family="Arial,sans-serif" font-size="11" fill="#3a4460">We believe you would find it meaningful.</text>
              <text x="335" y="137" font-family="Arial,sans-serif" font-size="11" fill="#3a4460">We remain uncertain about the why.</text>
              <text x="335" y="155" font-family="Arial,sans-serif" font-size="11" fill="#6a7490" font-style="italic">Please advise.</text>
              <!-- AI stamp / logo area -->
              <rect x="335" y="163" width="340" height="20" fill="#d8dce8" rx="2"/>
              <text x="505" y="176" font-family="Courier New,monospace" font-size="8" fill="#4050a0" text-anchor="middle" letter-spacing="1">PRIORITY INITIATIVE · POPULATION RECOVERY · CYCLE 1044</text>
              <text x="335" y="193" font-family="Courier New,monospace" font-size="8.5" fill="#5060a0" letter-spacing="1">AI WELLBEING SYSTEM · 3026 · PUBLIC DISPLAY SERIES · REF-010</text>
              <rect x="1" y="1" width="698" height="198" fill="none" stroke="#7880b8" stroke-width="1.2"/>
            </svg>'''

# ── Insert function ───────────────────────────────────────────────────────────

def insert_poster(html, when_text, svg_str):
    # Pattern: after <p class="when">WHEN</p>\n        <div class="prose">\n
    # insert figure before first <p>
    anchor = f'<p class="when">{when_text}</p>\n        <div class="prose">\n'
    pos = html.find(anchor)
    if pos == -1:
        print(f'  ✗ NOT FOUND: {when_text[:50]}')
        return html
    insert_at = pos + len(anchor)
    figure = (
        f'          <figure class="ch-art ch-art--entry propaganda">\n'
        f'{svg_str}\n'
        f'          </figure>\n\n'
    )
    return html[:insert_at] + figure + html[insert_at:]

# ── Main ─────────────────────────────────────────────────────────────────────

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# 1. Add CSS before </style>
OLD_END = '  </style>'
assert html.count(OLD_END) == 1, 'Multiple </style> tags'
html = html.replace(OLD_END, CSS + '  </style>', 1)
print('✓ CSS injected')

# 2. Insert posters
for when_text, svg in POSTERS.items():
    before = len(html)
    html = insert_poster(html, when_text, svg)
    added = len(html) - before
    label = when_text[:50].replace('&middot;', '·').replace('&#x2019;', "'")
    print(f'  {"✓" if added > 0 else "✗"} {label} (+{added:,} chars)')

print(f'\nOriginal: {original_len:,} → New: {len(html):,} (+{len(html)-original_len:,})')

with open('/Users/nonarkara/Projects/100daysofnon/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Written.')
