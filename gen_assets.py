import math
import os
import random
from xml.sax.saxutils import escape

random.seed(11)
os.makedirs("assets", exist_ok=True)

SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code','SF Mono',Consolas,'Courier New',monospace"
EMOJI = "'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',sans-serif"

# Dark Spruce & Amber Research Dossier Palette (synced with sanchitkrai.me)
SPRUCE_BG = "#0B140F"
SPRUCE_CARD = "#101E17"
SPRUCE_ELEV = "#15281F"
SPRUCE_BORDER = "#1F3B2D"
AMBER = "#F59E0B"
AMBER_SOFT = "#FBBF24"
LIME = "#A3E635"
EMERALD = "#34D399"
SKY = "#38BDF8"
CORAL = "#FB923C"
TEXT_MAIN = "#ECFDF5"
TEXT_MUTED = "#9BB8A8"
TEXT_DIM = "#6A8A79"

XMLNS = 'xmlns="http://www.w3.org/2000/svg"'


def save(name, body):
    with open(os.path.join("assets", name), "w", encoding="utf-8") as f:
        f.write(body)


def gaussian_path(x0, x1, y_base, mu, sigma, amp, steps=70):
    pts = []
    for i in range(steps + 1):
        x = x0 + (x1 - x0) * i / steps
        g = math.exp(-0.5 * ((x - mu) / sigma) ** 2)
        y = y_base - amp * g
        pts.append(f"{'M' if i == 0 else 'L'}{x:.1f} {y:.1f}")
    return " ".join(pts)


# --------------------------------------------------------------------------- header
def header():
    W, H = 1000, 260
    s = []
    a = s.append
    a(f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
      'aria-label="Sanchit Kumar Rai — Dark Spruce and Amber Research Dossier">')
    a('<defs>')
    a(f'<clipPath id="round"><rect width="{W}" height="{H}" rx="18"/></clipPath>')
    a(f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
      f'<stop offset="0" stop-color="{SPRUCE_BG}"/>'
      f'<stop offset="0.55" stop-color="#0F2118"><animate attributeName="stop-color" '
      f'values="#0F2118;#132A1E;#0D1C15;#0F2118" dur="10s" repeatCount="indefinite"/></stop>'
      f'<stop offset="1" stop-color="#08100C"/></linearGradient>')
    a('<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="380" y2="0" spreadMethod="repeat">'
      f'<stop offset="0" stop-color="{TEXT_MAIN}"/><stop offset="0.38" stop-color="{AMBER_SOFT}"/>'
      f'<stop offset="0.68" stop-color="{LIME}"/><stop offset="1" stop-color="{TEXT_MAIN}"/>'
      '<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="340 0" dur="5s" repeatCount="indefinite"/>'
      '</linearGradient>')
    a(f'<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">'
      f'<stop offset="0" stop-color="{AMBER}"/><stop offset="0.6" stop-color="{LIME}"/><stop offset="1" stop-color="{EMERALD}"/></linearGradient>')
    a('<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">'
      f'<path d="M32 0H0V32" fill="none" stroke="{EMERALD}" stroke-opacity="0.06"/>'
      '<animateTransform attributeName="patternTransform" type="translate" from="0 0" to="32 32" dur="8s" repeatCount="indefinite"/>'
      '</pattern>')
    a(f'<radialGradient id="orbA"><stop offset="0" stop-color="{AMBER}" stop-opacity="0.24"/>'
      f'<stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></radialGradient>')
    a(f'<radialGradient id="orbL"><stop offset="0" stop-color="{LIME}" stop-opacity="0.16"/>'
      f'<stop offset="1" stop-color="{LIME}" stop-opacity="0"/></radialGradient>')
    a('<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">'
      '<feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    a('</defs>')

    a('<g clip-path="url(#round)">')
    a(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    a(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
    a('<circle cx="820" cy="65" r="190" fill="url(#orbA)"><animate attributeName="cx" values="820;760;820" dur="10s" repeatCount="indefinite"/></circle>')
    a('<circle cx="220" cy="245" r="180" fill="url(#orbL)"><animate attributeName="cx" values="220;290;220" dur="12s" repeatCount="indefinite"/></circle>')

    # Normal-distribution + telemetry waveform curves on right/lower field
    g1a = gaussian_path(520, 990, 224, 760, 74, 132)
    g1b = gaussian_path(520, 990, 224, 790, 82, 108)
    g2a = gaussian_path(520, 990, 224, 835, 58, 92)
    g2b = gaussian_path(520, 990, 224, 730, 62, 114)
    a(f'<path d="{g1a} L 990 260 L 520 260 Z" fill="{AMBER}" fill-opacity="0.06">'
      f'<animate attributeName="d" values="{g1a} L 990 260 L 520 260 Z;{g1b} L 990 260 L 520 260 Z;{g1a} L 990 260 L 520 260 Z" dur="9s" repeatCount="indefinite"/></path>')
    a(f'<path d="{g1a}" fill="none" stroke="{AMBER}" stroke-width="2" stroke-opacity="0.7" filter="url(#glow)">'
      f'<animate attributeName="d" values="{g1a};{g1b};{g1a}" dur="9s" repeatCount="indefinite"/></path>')
    a(f'<path d="{g2a}" fill="none" stroke="{LIME}" stroke-width="1.6" stroke-opacity="0.55" stroke-dasharray="5 5">'
      f'<animate attributeName="d" values="{g2a};{g2b};{g2a}" dur="7s" repeatCount="indefinite"/></path>')

    # ECG / biosignal pulse line across bottom
    ecg = ("M 0 224 L 300 224 L 325 224 L 336 206 L 348 242 L 360 184 L 372 238 L 384 218 L 396 224 L 1000 224")
    a(f'<path d="{ecg}" fill="none" stroke="{EMERALD}" stroke-opacity="0.22" stroke-width="1.5"/>')
    a(f'<circle r="3.5" fill="{LIME}" filter="url(#glow)"><animateMotion dur="5.5s" repeatCount="indefinite" path="{ecg}"/></circle>')

    # Corner brackets
    a(f'<path d="M18 36 V18 H36 M964 18 H982 V36 M18 224 V242 H36 M964 242 H982 V224" fill="none" stroke="{AMBER}" stroke-width="2" stroke-opacity="0.75"/>')

    # Eyebrow + Name + Tagline
    a(f'<text x="48" y="54" font-family="{MONO}" font-size="12" font-weight="700" fill="{AMBER}" letter-spacing="2">'
      'RESEARCH DOSSIER // SANCHITKRAI.ME</text>')
    a(f'<text x="46" y="108" font-family="{SANS}" font-weight="800" font-size="46" fill="url(#shine)" '
      'letter-spacing="0.5" filter="url(#glow)">SANCHIT KUMAR RAI</text>')
    a('<rect x="48" y="124" width="0" height="3" rx="1.5" fill="url(#rule)">'
      '<animate attributeName="width" from="0" to="530" begin="0.3s" dur="0.9s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .2 1"/></rect>')
    a(f'<text x="48" y="156" font-family="{SANS}" font-size="15.5" font-weight="600" fill="{TEXT_MAIN}">'
      'B.Sc. Life Sciences · University of Delhi</text>')
    a(f'<text x="48" y="180" font-family="{MONO}" font-size="13" fill="{TEXT_MUTED}">'
      'Clinical AI · Computational Biology · Predictive ML · Full-Stack Data Apps</text>')

    chips = ["Python", "TypeScript", "FastAPI", "React 19", "SQL", "Power BI", "SHAP"]
    x = 48
    for c in chips:
        w = len(c) * 7.4 + 22
        a(f'<rect x="{x:.1f}" y="200" width="{w:.1f}" height="24" rx="12" fill="{SPRUCE_ELEV}" stroke="{SPRUCE_BORDER}" stroke-width="1.2"/>')
        a(f'<text x="{x + w / 2:.1f}" y="216" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="{LIME}">{escape(c)}</text>')
        x += w + 8

    a(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="17" fill="none" stroke="{SPRUCE_BORDER}" stroke-width="1.8"/>')
    a('</g>')
    a('</svg>')
    save("header.svg", "".join(s))


# --------------------------------------------------------------------------- bento-overview
def bento_overview():
    W, H = 660, 360
    s = [f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         'aria-label="Whoami telemetry, domain mix, and recent project pipeline">']
    a = s.append
    a('<defs>')
    a(f'<linearGradient id="bbg" x1="0" y1="0" x2="1" y2="1">'
      f'<stop offset="0" stop-color="{SPRUCE_BG}"/><stop offset="1" stop-color="{SPRUCE_CARD}"/></linearGradient>')
    a(f'<radialGradient id="bglow" cx="0.92" cy="0.08" r="0.7">'
      f'<stop offset="0" stop-color="{AMBER}" stop-opacity="0.14"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></radialGradient>')
    a('<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0">'
      '<stop offset="0" stop-color="#fff" stop-opacity="0"/>'
      '<stop offset="0.5" stop-color="#fff" stop-opacity="0.28"/>'
      '<stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>')
    a('</defs>')

    a(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#bbg)" stroke="{SPRUCE_BORDER}" stroke-width="1.8"/>')
    a(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="url(#bglow)"/>')
    a(f'<path d="M16 32 V16 H32 M628 16 H644 V32 M16 328 V344 H32 M628 344 H644 V328" fill="none" stroke="{AMBER}" stroke-width="1.8" stroke-opacity="0.7"/>')

    # Section 1: WHOAMI TELEMETRY
    a(f'<text x="28" y="38" font-family="{MONO}" font-size="11" font-weight="700" fill="{AMBER}" letter-spacing="1.6">WHOAMI // FIELD TELEMETRY</text>')
    a(f'<text x="632" y="38" text-anchor="end" font-family="{MONO}" font-size="11" fill="{LIME}">DELHI, IN · DU</text>')
    a(f'<text x="28" y="68" font-family="{SANS}" font-size="18" font-weight="700" fill="{TEXT_MAIN}">'
      'Turning raw bio, clinical &amp; sports data into shipped products.</text>')
    a(f'<text x="28" y="92" font-family="{SANS}" font-size="13" fill="{TEXT_MUTED}">'
      'From messy CSVs, blood PDFs &amp; PDB structures to validated ML, FHIR exports &amp; 3D web apps.</text>')

    badges = [
        ("39 PUBLIC REPOS", AMBER),
        ("COMP. BIO + HEALTH AI", LIME),
        ("HACKATHONS & LABS", EMERALD),
    ]
    bx = 28
    for label, col in badges:
        bw = len(label) * 6.8 + 20
        a(f'<rect x="{bx:.1f}" y="108" width="{bw:.1f}" height="22" rx="11" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-opacity="0.45"/>')
        a(f'<text x="{bx + bw / 2:.1f}" y="123" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="700" fill="{col}">{escape(label)}</text>')
        bx += bw + 10

    a(f'<line x1="28" y1="146" x2="632" y2="146" stroke="{SPRUCE_BORDER}" stroke-width="1"/>')

    # Section 2: DOMAIN MIX BAR
    a(f'<text x="28" y="168" font-family="{MONO}" font-size="11" font-weight="700" fill="{TEXT_DIM}" letter-spacing="1.4">DOMAIN MIX</text>')
    segs = [
        (40, AMBER, "40% Data Science & ML", "XGBoost · SHAP · Forecasting"),
        (30, LIME, "30% Comp. Bio & Health", "PhenoAge · FHIR · 3D Bio"),
        (30, EMERALD, "30% Analytics & Web", "SQL · Power BI · FastAPI"),
    ]
    x0, total, gap = 28, 604, 6
    avail = total - gap * 2
    a('<clipPath id="barclip"><rect x="28" y="178" width="604" height="18" rx="9"/></clipPath>')
    a('<g clip-path="url(#barclip)">')
    x = x0
    meta = []
    for pct, col, title, sub in segs:
        w = avail * pct / 100
        a(f'<rect x="{x:.1f}" y="178" width="{w:.1f}" height="18" rx="9" fill="{col}"/>')
        meta.append((x, col, title, sub))
        x += w + gap
    a('<rect x="-80" y="178" width="80" height="18" fill="url(#sh)"><animate attributeName="x" values="-80;660" dur="3.4s" repeatCount="indefinite"/></rect>')
    a('</g>')

    for mx, col, title, sub in meta:
        a(f'<circle cx="{mx + 5:.1f}" cy="215" r="4" fill="{col}"/>')
        a(f'<text x="{mx + 14:.1f}" y="219" font-family="{SANS}" font-size="12" font-weight="700" fill="{TEXT_MAIN}">{escape(title)}</text>')
        a(f'<text x="{mx + 14:.1f}" y="236" font-family="{MONO}" font-size="10.5" fill="{TEXT_MUTED}">{escape(sub)}</text>')

    a(f'<line x1="28" y1="254" x2="632" y2="254" stroke="{SPRUCE_BORDER}" stroke-width="1"/>')

    # Section 3: WORKFLOW LOOP + SHIPPED TICKER
    a(f'<text x="28" y="276" font-family="{MONO}" font-size="11" font-weight="700" fill="{TEXT_DIM}" letter-spacing="1.4">WORKFLOW &amp; RECENT SHIPS</text>')
    steps = [("DATA", AMBER), ("MODELS", LIME), ("INSIGHTS", EMERALD), ("IMPACT", SKY)]
    a(f'<path d="M 85 302 H 575" stroke="{SPRUCE_BORDER}" stroke-width="2" fill="none"/>')
    a(f'<circle r="4" fill="{AMBER}"><animateMotion dur="4.5s" repeatCount="indefinite" path="M 85 302 H 575"/></circle>')
    for i, (lbl, col) in enumerate(steps):
        cx = 85 + i * 163.3
        a(f'<rect x="{cx - 52:.1f}" y="288" width="104" height="28" rx="8" fill="{SPRUCE_ELEV}" stroke="{col}" stroke-width="1.4"/>')
        a(f'<text x="{cx:.1f}" y="306" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" fill="{TEXT_MAIN}">{lbl}</text>')

    a(f'<text x="28" y="340" font-family="{MONO}" font-size="11" fill="{LIME}">▸ shipped:</text>')
    a(f'<text x="104" y="340" font-family="{MONO}" font-size="11" fill="{TEXT_MUTED}">'
      'healthspan-passport · rr-war-room · bioverse · data-arena · genome-explorer</text>')
    a('</svg>')
    save("bento-overview.svg", "".join(s))


# --------------------------------------------------------------------------- divider
def divider():
    s = [f'<svg {XMLNS} viewBox="0 0 900 24" width="900" height="24" role="presentation">']
    s.append(f'<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="900" y2="0">'
             f'<stop offset="0" stop-color="{AMBER}" stop-opacity="0"/><stop offset="0.5" stop-color="{AMBER}"/>'
             f'<stop offset="1" stop-color="{LIME}" stop-opacity="0"/></linearGradient></defs>')
    s.append('<line x1="0" y1="12" x2="900" y2="12" stroke="url(#g)" stroke-width="1.5" stroke-opacity="0.7"/>')
    s.append(f'<circle r="3" cy="12" fill="{LIME}"><animate attributeName="cx" values="70;830;70" dur="7s" repeatCount="indefinite"/></circle>')
    s.append(f'<rect x="443" y="5" width="14" height="14" rx="2" transform="rotate(45 450 12)" fill="{SPRUCE_BG}" stroke="{AMBER}" stroke-width="1.8"/>')
    s.append('</svg>')
    save("divider.svg", "".join(s))


# --------------------------------------------------------------------------- cards
def card(fname, emoji, tag, title, sub, desc, tech, accent, cta=None, metric=None):
    W, H = 460, 210
    s = [f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(title)}">']
    s.append('<defs><clipPath id="r"><rect width="460" height="210" rx="16"/></clipPath>'
             f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{SPRUCE_BG}"/><stop offset="1" stop-color="{SPRUCE_CARD}"/></linearGradient>'
             f'<radialGradient id="glow" cx="1" cy="0" r="0.95"><stop offset="0" stop-color="{accent}" stop-opacity="0.22"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>'
             '<linearGradient id="sw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             '<stop offset="0.5" stop-color="#fff" stop-opacity="0.06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>')
    s.append('<g clip-path="url(#r)">')
    s.append('<rect width="460" height="210" fill="url(#bg)"/><rect width="460" height="210" fill="url(#glow)"/>')
    s.append('<rect x="-140" y="-20" width="110" height="260" fill="url(#sw)" transform="skewX(-18)">'
             '<animate attributeName="x" values="-140;520;520" keyTimes="0;0.5;1" dur="7s" repeatCount="indefinite"/></rect>')
    s.append('</g>')
    s.append(f'<rect x="1" y="1" width="458" height="208" rx="15" fill="none" stroke="{SPRUCE_BORDER}" stroke-width="1.5"/>')
    # Corner bracket accents
    s.append(f'<path d="M10 24 V10 H24 M436 10 H450 V24 M10 186 V200 H24 M436 200 H450 V186" fill="none" stroke="{accent}" stroke-width="1.8" stroke-opacity="0.75"/>')
    s.append(f'<rect x="1" y="1" width="458" height="208" rx="15" fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round" '
             'pathLength="1000" stroke-dasharray="110 890" stroke-opacity="0.85"><animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="7s" repeatCount="indefinite"/></rect>')

    tw = len(tag) * 7.6 + 22
    s.append(f'<rect x="24" y="22" width="{tw:.1f}" height="22" rx="11" fill="{accent}" fill-opacity="0.14" stroke="{accent}" stroke-opacity="0.55"/>')
    s.append(f'<text x="{24 + tw / 2:.1f}" y="37" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="700" fill="{accent}" letter-spacing="1">{escape(tag)}</text>')
    s.append(f'<text x="434" y="54" font-size="28" text-anchor="end" font-family="{EMOJI}">{emoji}'
             '<animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0" dur="3.4s" repeatCount="indefinite"/></text>')
    s.append(f'<text x="24" y="88" font-family="{SANS}" font-weight="800" font-size="21.5" fill="{TEXT_MAIN}">{escape(title)}</text>')
    y = 112
    if sub:
        s.append(f'<text x="24" y="110" font-family="{SANS}" font-weight="600" font-size="13" fill="{accent}">{escape(sub)}</text>')
        y = 132
    for line in desc:
        s.append(f'<text x="24" y="{y}" font-family="{SANS}" font-size="13" fill="{TEXT_MUTED}">{escape(line)}</text>')
        y += 18
    s.append(f'<text x="24" y="176" font-family="{MONO}" font-size="11.5" fill="{EMERALD}">{escape(tech)}</text>')
    if metric:
        s.append(f'<text x="24" y="197" font-family="{MONO}" font-size="11" font-weight="600" fill="{AMBER_SOFT}">{escape(metric)}</text>')
    if cta:
        s.append(f'<text x="436" y="197" text-anchor="end" font-family="{MONO}" font-size="11" font-weight="700" fill="{accent}" letter-spacing="1">{escape(cta)}'
                 '<animate attributeName="opacity" values="1;0.55;1" dur="2.5s" repeatCount="indefinite"/></text>')
    s.append('</svg>')
    save(fname, "".join(s))


header()
bento_overview()
divider()

# Competitive & Hackathon Builds
card("card-rr.svg", "🏏", "UNSTOP · SUBMITTED", "RR War Room", "Rajasthan Royals · SupeRR Selector S2",
     ["Pressure-reliability scouting across 200,999 deliveries", "and 867 matches with Bayesian-calibrated PRS."],
     "Python · Bayesian PRS · Dashboard · PDF", AMBER, "OPEN LIVE APP ↗", "Nov 16, 2026")
card("card-diabetes.svg", "🩺", "HAPPIEST HEALTH · SUBMITTED", "Type 2 Diabetes Digital Twin", "Digital Twin Challenge 2026",
     ["2-hour-ahead glucose-spike prediction from synthetic", "CGM, wearable, and EHR-style clinical signals."],
     "Python · pandas · XGBoost · SHAP", SKY, "OPEN STREAMLIT ↗", "Oct 18, 2026")
card("card-loc.svg", "🛡️", "FUTURE HEALTH · SUBMITTED", "LOC — Men's Health Check", "Future Health Digital Innovation",
     ["Privacy-first rules-driven clinical triage & care", "navigation with legacy XGBoost/TreeSHAP model."],
     "React · TypeScript · FastAPI · SHAP", EMERALD, "OPEN DEMO ↗", "Nov 20, 2026")
card("card-bioverse.svg", "🧬", "COMPETITIVE BUILD", "BIOVERSE", "3D Systems Biology & Clinical Sim",
     ["Interactive 3D anatomy & Bergman Minimal Model game", "with live UniProt, RCSB PDB & Reactome APIs."],
     "React 19 · TypeScript · Three.js · WebGL", LIME, "VIEW REPO ↗")

# Featured Projects & Active Builds
card("card-healthspan.svg", "🩺", "BUILD 2036 · CLINICAL AI", "Healthspan Passport", None,
     ["Ingests blood test PDFs/photos for Levine PhenoAge,", "multi-organ risk flags, AI companion chat, doctor PDF", "and HL7 FHIR R4 export."],
     "FastAPI · Next.js 15 · RapidOCR · FHIR R4", EMERALD, "OPEN LIVE APP ↗", "70 pytest passed")
card("card-vyaparflow.svg", "🎙️", "BUILD WITH GEMINI · BUILDING", "VyaparFlow", "Voice-Driven Agentic Workflow Automation",
     ["Voice-first agentic automation built for Google Gemini", "track — turning spoken ops into structured workflows."],
     "Gemini · Voice · Agentic Workflows", AMBER_SOFT, None, "Round ends Dec 03, 2026")
card("card-dataarena.svg", "🏟️", "DATA PLATFORM", "Data Skills Arena", None,
     ["Adaptive, gamified data science & SQL challenges", "featuring an in-browser Python IDE powered by", "Pyodide WebAssembly."],
     "React 19 · TypeScript · Pyodide · Monaco", AMBER, "OPEN LIVE APP ↗")
card("card-docklens.svg", "🧪", "COMP. BIOLOGY", "DockLens", None,
     ["Computational drug-discovery prototype combining docking", "workflows with ML-based affinity estimation and", "model explainability."],
     "Python · AutoDock Vina · XGBoost/RF · SHAP", LIME, "OPEN STREAMLIT ↗")
card("card-ev.svg", "⚡", "CASE STUDY", "EV Charging Demand Forecasting", None,
     ["End-to-end forecasting: clean charging-session data,", "analyse usage patterns, and present 30/90/365-day", "forecasts in Power BI."],
     "Python · time series · Prophet · Power BI", CORAL, "VIEW REPO ↗", "RMSE 3,782 · MAPE 16.57%")
card("card-airbnb.svg", "🏙️", "LIVE ML APP", "NYC Airbnb Predictor", None,
     ["Machine-learning web app that predicts an Airbnb", "room-type category from listing features."],
     "Python · pandas · scikit-learn · FastAPI", EMERALD, "OPEN LIVE APP ↗")
print("done:", sorted(os.listdir("assets")))
