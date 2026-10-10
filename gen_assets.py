import math, os, random
from xml.sax.saxutils import escape

random.seed(11)
os.makedirs("assets", exist_ok=True)

SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code','SF Mono',Consolas,'Courier New',monospace"
EMOJI = "'Segoe UI Emoji','Apple Color Emoji','Noto Color Emoji',sans-serif"
TEAL, BLUE, VIOLET, AMBER, SKY = "#00D4AA", "#4C8DFF", "#B783FF", "#FFB84C", "#3CC8FF"
XMLNS = 'xmlns="http://www.w3.org/2000/svg"'


def save(name, body):
    with open(os.path.join("assets", name), "w", encoding="utf-8") as f:
        f.write(body)


def typed_clip(cid, x, y, h, n, cw, start, dur, T):
    """Character-by-character reveal that loops every T seconds."""
    vals = [0] + [round(j * cw, 1) for j in range(1, n + 1)]
    vals[-1] = vals[-1] + 4
    kts = [0] + [(start + (j - 1) * dur / n) / T for j in range(1, n + 1)]
    v = ";".join(str(i) for i in vals)
    k = ";".join(f"{i:.5f}" for i in kts)
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="0" height="{h}">'
            f'<animate attributeName="width" calcMode="discrete" values="{v}" keyTimes="{k}" '
            f'dur="{T:.2f}s" repeatCount="indefinite"/></rect></clipPath>')


# --------------------------------------------------------------------------- header
def header():
    W, H = 1000, 340
    s = []
    a = s.append
    a(f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
      'aria-label="Sanchit Kumar Rai: Data Science, Machine Learning, Analytics and Computational Biology">')
    a('<defs>')
    a('<clipPath id="round"><rect width="1000" height="340" rx="20"/></clipPath>')
    a('<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
      '<stop offset="0" stop-color="#070A18"/>'
      '<stop offset="0.5" stop-color="#0F2C57"><animate attributeName="stop-color" '
      'values="#0F2C57;#0B4A5C;#1B2F6B;#0F2C57" dur="10s" repeatCount="indefinite"/></stop>'
      '<stop offset="1" stop-color="#04382F"/></linearGradient>')
    a('<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="50" y1="0" x2="350" y2="0" spreadMethod="repeat">'
      '<stop offset="0" stop-color="#FFFFFF"/><stop offset="0.35" stop-color="#7CF2D8"/>'
      '<stop offset="0.7" stop-color="#6FA8FF"/><stop offset="1" stop-color="#FFFFFF"/>'
      '<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="300 0" dur="4s" repeatCount="indefinite"/>'
      '</linearGradient>')
    a('<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#00D4AA"/>'
      '<stop offset="0.6" stop-color="#4C8DFF"/><stop offset="1" stop-color="#B783FF"/></linearGradient>')
    a('<pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse">'
      '<path d="M36 0H0V36" fill="none" stroke="#7FB4FF" stroke-opacity="0.07"/>'
      '<animateTransform attributeName="patternTransform" type="translate" from="0 0" to="36 36" dur="6s" repeatCount="indefinite"/>'
      '</pattern>')
    a('<radialGradient id="orbT"><stop offset="0" stop-color="#00D4AA" stop-opacity="0.35"/>'
      '<stop offset="1" stop-color="#00D4AA" stop-opacity="0"/></radialGradient>')
    a('<radialGradient id="orbB"><stop offset="0" stop-color="#4C8DFF" stop-opacity="0.32"/>'
      '<stop offset="1" stop-color="#4C8DFF" stop-opacity="0"/></radialGradient>')
    a('<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">'
      '<feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')

    tag = "Data Science · Machine Learning · Analytics · Computational Biology"
    n = len(tag)
    cw = 9.0
    vals = ";".join(str(round(j * cw, 1)) for j in range(n + 1))
    a(f'<clipPath id="tg"><rect x="52" y="196" width="0" height="30">'
      f'<animate attributeName="width" calcMode="discrete" values="{vals}" dur="{n * 0.035:.2f}s" begin="1.6s" fill="freeze"/></rect></clipPath>')
    a('</defs>')

    a('<g clip-path="url(#round)">')
    a('<rect width="1000" height="340" fill="url(#bg)"/>')
    a('<rect width="1000" height="340" fill="url(#grid)"/>')
    a('<circle cx="820" cy="80" r="170" fill="url(#orbT)"><animate attributeName="cx" values="820;760;820" dur="9s" repeatCount="indefinite"/></circle>')
    a('<circle cx="180" cy="320" r="190" fill="url(#orbB)"><animate attributeName="cx" values="180;260;180" dur="11s" repeatCount="indefinite"/></circle>')

    # particles
    for _ in range(26):
        x = random.uniform(10, 990)
        y0 = random.uniform(250, 345)
        r = random.uniform(1.0, 2.6)
        dur = random.uniform(6, 14)
        beg = -random.uniform(0, dur)
        a(f'<circle cx="{x:.1f}" cy="{y0:.1f}" r="{r:.1f}" fill="#8FF5E0" opacity="0">'
          f'<animate attributeName="cy" values="{y0:.1f};{y0 - 190:.1f}" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/>'
          f'<animate attributeName="opacity" values="0;0.8;0" dur="{dur:.1f}s" begin="{beg:.1f}s" repeatCount="indefinite"/></circle>')

    # waves
    def wave(y, amp, fill, op, dur):
        d1 = f"M0 {y} C 160 {y - amp}, 340 {y + amp}, 500 {y} S 840 {y - amp}, 1000 {y} V340 H0 Z"
        d2 = f"M0 {y} C 160 {y + amp}, 340 {y - amp}, 500 {y} S 840 {y + amp}, 1000 {y} V340 H0 Z"
        a(f'<path fill="{fill}" fill-opacity="{op}" d="{d1}"><animate attributeName="d" values="{d1};{d2};{d1}" dur="{dur}s" repeatCount="indefinite"/></path>')

    wave(314, 26, "#00D4AA", 0.10, 8)
    wave(326, 22, "#4C8DFF", 0.12, 11)

    # DNA helix
    N, x0, dx, cy0, amp, K = 18, 712, 15, 165, 62, 36
    a('<g filter="url(#glow)">')
    for i in range(N):
        ph = i * 0.5
        ys = [cy0 + amp * math.sin(ph + 2 * math.pi * k / K) for k in range(K + 1)]
        ya = ";".join(f"{y:.1f}" for y in ys)
        yb = ";".join(f"{2 * cy0 - y:.1f}" for y in ys)
        ra = ";".join(f"{4.5 + 2.2 * math.cos(ph + 2 * math.pi * k / K):.2f}" for k in range(K + 1))
        rb = ";".join(f"{4.5 - 2.2 * math.cos(ph + 2 * math.pi * k / K):.2f}" for k in range(K + 1))
        x = x0 + i * dx
        a(f'<line x1="{x}" x2="{x}" y1="{ys[0]:.1f}" y2="{2 * cy0 - ys[0]:.1f}" stroke="#BFE9FF" stroke-opacity="0.28" stroke-width="1.6">'
          f'<animate attributeName="y1" values="{ya}" dur="4s" repeatCount="indefinite"/>'
          f'<animate attributeName="y2" values="{yb}" dur="4s" repeatCount="indefinite"/></line>')
        a(f'<circle cx="{x}" cy="{ys[0]:.1f}" r="4.5" fill="{TEAL}">'
          f'<animate attributeName="cy" values="{ya}" dur="4s" repeatCount="indefinite"/>'
          f'<animate attributeName="r" values="{ra}" dur="4s" repeatCount="indefinite"/></circle>')
        a(f'<circle cx="{x}" cy="{2 * cy0 - ys[0]:.1f}" r="4.5" fill="{BLUE}">'
          f'<animate attributeName="cy" values="{yb}" dur="4s" repeatCount="indefinite"/>'
          f'<animate attributeName="r" values="{rb}" dur="4s" repeatCount="indefinite"/></circle>')
    a('</g>')

    # text
    a('<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.2s" dur="0.8s" fill="freeze"/>'
      f'<text x="52" y="92" font-family="{MONO}" font-size="15" fill="{TEAL}" letter-spacing="1">// hello, world — I am</text></g>')
    a('<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="0.5s" dur="0.9s" fill="freeze"/>'
      '<animateTransform attributeName="transform" type="translate" from="0 16" to="0 0" begin="0.5s" dur="0.9s" fill="freeze"/>'
      f'<text x="50" y="160" font-family="{SANS}" font-weight="800" font-size="52" fill="url(#shine)" '
      'textLength="610" lengthAdjust="spacingAndGlyphs" filter="url(#glow)">SANCHIT KUMAR RAI</text></g>')
    a('<rect x="52" y="178" width="0" height="3" rx="1.5" fill="url(#bar)">'
      '<animate attributeName="width" from="0" to="610" begin="1s" dur="1s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .2 1"/></rect>')
    a(f'<text x="52" y="218" font-family="{MONO}" font-size="15" fill="#9FE8D8" clip-path="url(#tg)" '
      f'textLength="{n * cw}" lengthAdjust="spacing">{escape(tag)}</text>')
    a('<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="4.2s" dur="0.8s" fill="freeze"/>'
      f'<text x="52" y="252" font-family="{SANS}" font-size="14" fill="#7FA3C9">'
      'B.Sc. Life Sciences · Sri Aurobindo College, University of Delhi</text></g>')

    chips = ["Python", "SQL", "Power BI", "scikit-learn", "SHAP", "Streamlit"]
    x = 52
    for i, c in enumerate(chips):
        w = len(c) * 7.4 + 24
        a(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{4.6 + i * 0.18:.2f}s" dur="0.5s" fill="freeze"/>'
          f'<rect x="{x:.1f}" y="268" width="{w:.1f}" height="26" rx="13" fill="#00D4AA" fill-opacity="0.10" stroke="#00D4AA" stroke-opacity="0.55"/>'
          f'<text x="{x + w / 2:.1f}" y="285" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#CFFFF3">{escape(c)}</text></g>')
        x += w + 10

    a('</g>')
    a('</svg>')
    save("header.svg", "".join(s))


# --------------------------------------------------------------------------- terminal
def terminal():
    W, H = 900, 350
    cw, fs, lh = 9.0, 15, 28
    left, top = 34, 86
    prompt = [("sanchit@bioedge", TEAL), (":", "#8B9BB4"), ("~", BLUE), ("$ ", "#8B9BB4")]
    plen = sum(len(t) for t, _ in prompt)
    script = [
        ("cmd", "whoami"),
        ("out", "Sanchit · B.Sc. Life Sciences · Sri Aurobindo College, DU"),
        ("cmd", "cat mission.txt"),
        ("out", "turn messy data into useful decisions"),
        ("cmd", "ls projects/"),
        ("out", "airbnb-predictor  diabetes-twin  ev-forecasting  docklens  genescope  nextup"),
        ("cmd", "./ship --real-projects"),
        ("out", "✔ learning by shipping, one dataset at a time"),
        ("cmd", ""),
    ]
    # timing
    t = 0.8
    plan = []
    for kind, text in script:
        n = plen + len(text) if kind == "cmd" else 2 + len(text)
        dur = n * (0.045 if kind == "cmd" else 0.012)
        plan.append((kind, text, n, t, dur))
        t += dur + (0.5 if kind == "cmd" else 0.9)
    T = t + 4.0

    defs, body = [], []
    for i, (kind, text, n, start, dur) in enumerate(plan):
        y = top + i * lh
        cid = f"c{i}"
        defs.append(typed_clip(cid, left, y - 18, 24, n, cw, start, dur, T))
        if kind == "cmd":
            spans = "".join(f'<tspan fill="{c}">{escape(tx)}</tspan>' for tx, c in prompt)
            spans += f'<tspan fill="#E6EDF3">{escape(text)}</tspan>'
        else:
            col = "#7EE787" if text.startswith("✔") else "#C9D1D9"
            spans = f'<tspan fill="{TEAL}">▸ </tspan><tspan fill="{col}">{escape(text)}</tspan>'
        body.append(f'<text x="{left}" y="{y}" font-family="{MONO}" font-size="{fs}" xml:space="preserve" clip-path="url(#{cid})">{spans}</text>')

    last = plan[-1]
    cy = top + (len(plan) - 1) * lh
    cx = left + plen * cw
    kt = (last[3] + last[4]) / T

    s = [f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Animated terminal introducing Sanchit">']
    s.append("<defs>" + "".join(defs) + "</defs>")
    s.append('<rect x="1" y="1" width="898" height="348" rx="14" fill="#0D1117" stroke="#30363D" stroke-width="2"/>')
    s.append('<path d="M1 15a14 14 0 0 1 14-14h870a14 14 0 0 1 14 14v26H1z" fill="#161B22"/>')
    for i, c in enumerate(["#FF5F56", "#FFBD2E", "#27C93F"]):
        s.append(f'<circle cx="{28 + i * 22}" cy="21" r="6" fill="{c}"/>')
    s.append(f'<text x="450" y="26" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#8B949E">sanchit@bioedge: ~/profile</text>')
    s.extend(body)
    s.append(f'<g opacity="0"><animate attributeName="opacity" calcMode="discrete" values="0;1" keyTimes="0;{kt:.5f}" dur="{T:.2f}s" repeatCount="indefinite"/>'
             f'<rect x="{cx}" y="{cy - 15}" width="9" height="19" fill="{TEAL}"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect></g>')
    s.append('<rect x="1" y="1" width="898" height="348" rx="14" fill="none" stroke="#00D4AA" stroke-width="2" stroke-linecap="round" '
             'pathLength="1000" stroke-dasharray="120 880"><animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="7s" repeatCount="indefinite"/></rect>')
    s.append("</svg>")
    save("terminal.svg", "".join(s))


# --------------------------------------------------------------------------- focus
def focus():
    W, H = 900, 200
    segs = [
        (50, TEAL, "Data Science & ML", ["Predictive modelling · feature engineering", "time series · explainability"]),
        (30, BLUE, "Data Analytics", ["SQL · Python · Excel · Power BI", "KPI design · dashboards"]),
        (20, VIOLET, "Biotech & Comp. Bio", ["Healthcare data ·", "bioinformatics · docking"]),
    ]
    x0, total, gap = 40, 820, 6
    avail = total - gap * 2
    s = [f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Portfolio mix: 50% data science and machine learning, 30% data analytics, 20% biotechnology and computational biology">']
    s.append('<defs>'
             f'<clipPath id="grow"><rect x="{x0}" y="60" width="0" height="30"><animate attributeName="width" values="0;{total};{total}" '
             'keyTimes="0;0.18;1" calcMode="spline" keySplines=".2 .8 .2 1;0 0 1 1" dur="9s" repeatCount="indefinite"/></rect></clipPath>'
             '<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             '<stop offset="0.5" stop-color="#fff" stop-opacity="0.35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
             '</defs>')
    s.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="#0D1117" stroke="#30363D" stroke-width="2"/>')
    s.append(f'<g clip-path="url(#grow)">')
    x = x0
    bars = []
    for pct, col, title, desc in segs:
        w = avail * pct / 100
        s.append(f'<rect x="{x:.1f}" y="68" width="{w:.1f}" height="22" rx="11" fill="{col}"/>')
        bars.append((x, w, pct, col, title, desc))
        x += w + gap
    s.append('<rect x="-100" y="68" width="90" height="22" fill="url(#sh)"><animate attributeName="x" values="-100;900" dur="3s" repeatCount="indefinite"/></rect>')
    s.append('</g>')
    for x, w, pct, col, title, desc in bars:
        s.append('<g opacity="0"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.2;1" dur="9s" repeatCount="indefinite"/>'
                 f'<text x="{x:.1f}" y="50" font-family="{SANS}" font-weight="800" font-size="30" fill="{col}">{pct}%</text>'
                 f'<text x="{x:.1f}" y="122" font-family="{SANS}" font-weight="700" font-size="13" fill="#F0F6FC">{escape(title)}</text>'
                 f'<text x="{x:.1f}" y="143" font-family="{SANS}" font-size="12" fill="#8FA6C2">{escape(desc[0])}</text>'
                 f'<text x="{x:.1f}" y="161" font-family="{SANS}" font-size="12" fill="#8FA6C2">{escape(desc[1])}</text></g>')
    s.append('</svg>')
    save("focus.svg", "".join(s))


# --------------------------------------------------------------------------- pipeline
def pipeline():
    W, H = 900, 175
    nodes = [("DATA", TEAL, "clean · explore"), ("MODELS", SKY, "baseline · test honestly"),
             ("INSIGHTS", BLUE, "dashboards · stories"), ("IMPACT", VIOLET, "useful decisions")]
    xs = [130, 343.3, 556.7, 770]
    s = [f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Data to models to insights to impact">']
    s.append('<defs><linearGradient id="ln" gradientUnits="userSpaceOnUse" x1="130" y1="0" x2="770" y2="0">'
             f'<stop offset="0" stop-color="{TEAL}"/><stop offset="0.5" stop-color="{BLUE}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>'
             '<filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/>'
             '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>')
    s.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="16" fill="#0D1117" stroke="#30363D" stroke-width="2"/>')
    s.append(f'<text x="450" y="34" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#8FA6C2" letter-spacing="2">THE LOOP</text>')
    s.append('<path d="M130 78 H770" stroke="url(#ln)" stroke-width="3" stroke-opacity="0.35" fill="none"/>')
    s.append('<path d="M130 78 H770" stroke="url(#ln)" stroke-width="3" fill="none" stroke-dasharray="6 10">'
             '<animate attributeName="stroke-dashoffset" from="32" to="0" dur="1.2s" repeatCount="indefinite"/></path>')
    for (label, col, sub), cx in zip(nodes, xs):
        t = (cx - 130) / 640 * 6
        s.append(f'<rect x="{cx - 75:.1f}" y="55" width="150" height="46" rx="12" fill="#101A30" stroke="{col}" stroke-width="2"/>')
        s.append(f'<rect x="{cx - 79:.1f}" y="51" width="158" height="54" rx="15" fill="none" stroke="{col}" stroke-width="3" opacity="0" filter="url(#g)">'
                 f'<animate attributeName="opacity" values="0;0.95;0;0" keyTimes="0;0.06;0.3;1" dur="6s" begin="{t:.2f}s" repeatCount="indefinite"/></rect>')
        s.append(f'<text x="{cx:.1f}" y="84" text-anchor="middle" font-family="{MONO}" font-weight="700" font-size="15" fill="#F0F6FC" letter-spacing="1">{label}</text>')
        s.append(f'<text x="{cx:.1f}" y="124" text-anchor="middle" font-family="{SANS}" font-size="12" fill="#8FA6C2">{escape(sub)}</text>')
    s.append('<circle r="11" fill="#fff" opacity="0.25"><animateMotion dur="6s" repeatCount="indefinite" path="M130 78 H770"/></circle>')
    s.append('<circle r="5" fill="#fff" filter="url(#g)"><animateMotion dur="6s" repeatCount="indefinite" path="M130 78 H770"/></circle>')
    s.append(f'<text x="450" y="154" text-anchor="middle" font-family="{SANS}" font-size="12" fill="#6E86A3">'
             'understand the problem → inspect the data → build a baseline → test honestly → communicate what it means</text>')
    s.append('</svg>')
    save("pipeline.svg", "".join(s))


# --------------------------------------------------------------------------- divider
def divider():
    s = [f'<svg {XMLNS} viewBox="0 0 900 28" width="900" height="28" role="presentation">']
    s.append('<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="900" y2="0">'
             f'<stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset="0.5" stop-color="{BLUE}"/>'
             f'<stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient></defs>')
    s.append('<line x1="0" y1="14" x2="900" y2="14" stroke="url(#g)" stroke-width="2"/>')
    s.append('<circle r="3.5" cy="14" fill="#7CF2D8"><animate attributeName="cx" values="60;840;60" dur="6s" repeatCount="indefinite"/></circle>')
    s.append(f'<rect x="441" y="5" width="18" height="18" rx="3" transform="rotate(45 450 14)" fill="#0D1117" stroke="{TEAL}" stroke-width="2"/>')
    s.append(f'<circle cx="450" cy="14" r="3" fill="{TEAL}"><animate attributeName="r" values="2;4.5;2" dur="2s" repeatCount="indefinite"/></circle>')
    s.append('</svg>')
    save("divider.svg", "".join(s))


# --------------------------------------------------------------------------- cards
def card(fname, emoji, tag, title, sub, desc, tech, accent, cta=None, metric=None):
    W, H = 460, 210
    s = [f'<svg {XMLNS} viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(title)}">']
    s.append('<defs><clipPath id="r"><rect width="460" height="210" rx="16"/></clipPath>'
             '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0D1117"/><stop offset="1" stop-color="#12203A"/></linearGradient>'
             f'<radialGradient id="glow" cx="1" cy="0" r="1"><stop offset="0" stop-color="{accent}" stop-opacity="0.28"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>'
             '<linearGradient id="sw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
             '<stop offset="0.5" stop-color="#fff" stop-opacity="0.09"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>')
    s.append('<g clip-path="url(#r)">')
    s.append('<rect width="460" height="210" fill="url(#bg)"/><rect width="460" height="210" fill="url(#glow)"/>')
    s.append('<rect x="-140" y="-20" width="110" height="260" fill="url(#sw)" transform="skewX(-18)">'
             '<animate attributeName="x" values="-140;520;520" keyTimes="0;0.5;1" dur="6s" repeatCount="indefinite"/></rect>')
    s.append('</g>')
    s.append(f'<rect x="1" y="1" width="458" height="208" rx="15" fill="none" stroke="{accent}" stroke-opacity="0.28" stroke-width="1.5"/>')
    s.append(f'<rect x="1" y="1" width="458" height="208" rx="15" fill="none" stroke="{accent}" stroke-width="2.5" stroke-linecap="round" '
             'pathLength="1000" stroke-dasharray="130 870"><animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="6s" repeatCount="indefinite"/></rect>')
    tw = len(tag) * 7.6 + 22
    s.append(f'<rect x="24" y="22" width="{tw:.1f}" height="22" rx="11" fill="{accent}" fill-opacity="0.14" stroke="{accent}" stroke-opacity="0.6"/>')
    s.append(f'<text x="{24 + tw / 2:.1f}" y="37" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="700" fill="{accent}" letter-spacing="1">{escape(tag)}</text>')
    s.append(f'<text x="436" y="56" font-size="30" text-anchor="end" font-family="{EMOJI}">{emoji}'
             '<animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" dur="3.2s" repeatCount="indefinite"/></text>')
    s.append(f'<text x="24" y="90" font-family="{SANS}" font-weight="800" font-size="22" fill="#F0F6FC">{escape(title)}</text>')
    y = 114
    if sub:
        s.append(f'<text x="24" y="112" font-family="{SANS}" font-weight="600" font-size="13" fill="{accent}">{escape(sub)}</text>')
        y = 134
    for line in desc:
        s.append(f'<text x="24" y="{y}" font-family="{SANS}" font-size="13" fill="#9FB4CC">{escape(line)}</text>')
        y += 18
    s.append(f'<text x="24" y="178" font-family="{MONO}" font-size="11.5" fill="{accent}" fill-opacity="0.95">{escape(tech)}</text>')
    if metric:
        s.append(f'<text x="24" y="198" font-family="{MONO}" font-size="11" fill="#FFD27A">{escape(metric)}</text>')
    if cta:
        s.append(f'<text x="436" y="198" text-anchor="end" font-family="{MONO}" font-size="11" font-weight="700" fill="{accent}" letter-spacing="1">{escape(cta)}'
                 '<animate attributeName="opacity" values="1;0.55;1" dur="2.4s" repeatCount="indefinite"/></text>')
    s.append('</svg>')
    save(fname, "".join(s))


header()
terminal()
focus()
pipeline()
divider()
card("card-airbnb.svg", "🏙️", "LIVE APP", "NYC Airbnb Predictor", None,
     ["Machine-learning web app that predicts an Airbnb room-type", "category from listing features."],
     "Python · pandas · scikit-learn · FastAPI", TEAL, "OPEN LIVE APP ↗")
card("card-diabetes.svg", "🩺", "PROOF OF CONCEPT", "Type 2 Diabetes Digital Twin", None,
     ["Explores glucose-spike prediction from synthetic CGM,", "wearable, and EHR-style signals."],
     "Python · pandas · XGBoost · SHAP", SKY, "OPEN STREAMLIT APP ↗")
card("card-ev.svg", "⚡", "CASE STUDY", "EV Charging Demand Forecasting", None,
     ["End-to-end forecasting: clean charging-session data, analyse", "usage patterns, compare approaches, produce 30/90/365-day",
      "forecasts and present the results in Power BI."],
     "Python · time series · Prophet · Power BI", AMBER, None, "RMSE 3,782.32 kWh · MAPE 16.57%")
card("card-nextup.svg", "🧭", "WEB APP", "NextUp", "From Confused to Career-Proof",
     ["A career-path exploration project that helps users move", "from uncertainty toward a clearer next step."],
     "Web app · career exploration", BLUE, "EXPLORE PROJECT ↗")
card("card-datalens.svg", "📈", "DATA APP", "DataLens Insights", None,
     ["An interactive data-insights project focused on making", "information easier to explore and interpret."],
     "Data insights · visualisation · web app", "#3CE0C8", "OPEN PROJECT ↗")
card("card-docklens.svg", "🧪", "COMP. BIOLOGY", "DockLens", None,
     ["Computational drug-discovery prototype combining docking", "workflows with ML-based affinity estimation and", "model explainability."],
     "Python · AutoDock Vina · XGBoost/RF · SHAP", VIOLET, "OPEN STREAMLIT APP ↗")
print("done:", sorted(os.listdir("assets")))
