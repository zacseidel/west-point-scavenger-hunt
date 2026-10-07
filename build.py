"""Build the West Point Scavenger Hunt web page and phone-sized PDFs.

Usage: python3 build.py https://zacseidel.github.io/west-point-scavenger-hunt/
Outputs: index.html (GitHub Pages), west-point-hunt.html (Claude artifact), west-point-hunt-short.pdf, west-point-hunt-long.pdf
"""
import json
import math
import sys
from pathlib import Path

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (Flowable, KeepTogether, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer)

import hunt_data as D

HERE = Path(__file__).parent
WEB_URL = sys.argv[1] if len(sys.argv) > 1 else None
KID_PACE_M_PER_MIN = 55   # about 2 mph with kids
PATH_FACTOR = 1.35        # straight line -> walking path
MIN_PER_STOP = 2


def meters(a, b):
    r = 6371000
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dp, dl = p2 - p1, math.radians(b["lng"] - a["lng"])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h)) * PATH_FACTOR


def build_routes():
    out = {}
    for key, r in D.ROUTES.items():
        prev_id, prev = "ike_hall", D.START
        legs, total_m = [], 0
        for sid in r["stops"]:
            s = D.STOPS[sid]
            m = meters(prev, s)
            if sid == "chapel":
                m *= 1.4  # switchbacks and stairs up the hill
            total_m += m
            walk = s["walk"].get(prev_id)
            if walk is None:
                raise SystemExit(f"{key}: stop '{sid}' has no walking directions from '{prev_id}'")
            legs.append({
                "id": sid, "name": s["name"], "clue": s["clue"], "walk": walk,
                "walkMin": max(1, round(m / KID_PACE_M_PER_MIN)),
                "activity": s["activity"], "question": s["question"], "answer": s["answer"],
                "facts": s["facts"], "grownup_tip": s.get("grownup_tip"),
                "lat": s["lat"], "lng": s["lng"],
                "gmaps": D.gmaps(s["lat"], s["lng"]), "amaps": D.amaps(s["lat"], s["lng"]),
            })
            prev_id, prev = sid, s
        minutes = total_m / KID_PACE_M_PER_MIN + MIN_PER_STOP * len(legs)
        out[key] = {"name": r["name"], "tagline": r["tagline"], "terrain": r["terrain"],
                    "legs": legs, "meters": round(total_m), "minutes": round(minutes)}
    return out


ROUTES = build_routes()
START = dict(D.START, gmaps=D.gmaps(D.START["lat"], D.START["lng"]),
             amaps=D.amaps(D.START["lat"], D.START["lng"]))


# ---------- Web page ----------
def build_html():
    data = {"edition": D.EDITION, "start": START, "routes": ROUTES, "notes": D.ADULT_NOTES}
    links = " ".join(f'<a href="west-point-hunt-{k}.pdf" target="_blank" rel="noopener">{r["name"]} (PDF)</a>'
                     for k, r in ROUTES.items())
    html = (HERE / "template.html").read_text()
    html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__PDF_LINKS__", links)
    (HERE / "west-point-hunt.html").write_text(html)
    # Standalone page for GitHub Pages: add the document skeleton the artifact host normally provides.
    (HERE / "index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        f'</head>\n<body>\n{html}\n</body>\n</html>\n')


# ---------- PDF ----------
PAGE = (4.5 * inch, 8 * inch)
INK = colors.HexColor("#17191b")
GOLD = colors.HexColor("#8a6714")
GOLD_FILL = colors.HexColor("#d3a93a")
MUTED = colors.HexColor("#565d63")

ss = {
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=22, leading=25, textColor=INK, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=GOLD, spaceAfter=6),
    "eyebrow": ParagraphStyle("eb", fontName="Helvetica-Bold", fontSize=7.5, leading=10, textColor=MUTED, spaceAfter=4),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=13.5, textColor=INK, spaceAfter=6),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8.5, leading=11.5, textColor=MUTED, spaceAfter=4),
    "clue": ParagraphStyle("clue", fontName="Helvetica-Oblique", fontSize=12.5, leading=17, textColor=INK,
                           leftIndent=10, borderPadding=(0, 0, 0, 0), spaceAfter=10),
    "links": ParagraphStyle("links", fontName="Helvetica-Bold", fontSize=11, leading=14, alignment=TA_CENTER, textColor=GOLD),
    "fact": ParagraphStyle("fact", fontName="Helvetica", fontSize=9.5, leading=12.5, textColor=INK,
                           leftIndent=10, bulletIndent=0, spaceAfter=4),
    "center": ParagraphStyle("center", fontName="Helvetica", fontSize=10, leading=13.5, alignment=TA_CENTER, textColor=INK),
}


def eyebrow(t):
    return Paragraph(t.upper(), ss["eyebrow"])


class QR(Flowable):
    """Clickable QR code, centered."""
    def __init__(self, url, size=1.9 * inch):
        super().__init__()
        self.url, self.size = url, size

    def wrap(self, aw, ah):
        self.aw = aw
        return aw, self.size

    def draw(self):
        w = QrCodeWidget(self.url, barLevel="M")
        b = w.getBounds()
        bw, bh = b[2] - b[0], b[3] - b[1]
        d = Drawing(self.size, self.size, transform=[self.size / bw, 0, 0, self.size / bh, 0, 0])
        d.add(w)
        x = (self.aw - self.size) / 2
        renderPDF.draw(d, self.canv, x, 0)
        self.canv.linkURL(self.url, (x, 0, x + self.size, self.size), relative=1)


class UpsideDown(Flowable):
    """An upside-down answer box so kids can't read it at a glance."""
    def __init__(self, text):
        super().__init__()
        self.p = Paragraph(f"<b>Answer:</b> {text}", ss["small"])

    def wrap(self, aw, ah):
        self.aw = aw
        _, self.h = self.p.wrap(aw - 16, ah)
        return aw, self.h + 12

    def draw(self):
        c = self.canv
        c.setStrokeColor(GOLD_FILL)
        c.setDash(3, 2)
        c.roundRect(0, 0, self.aw, self.h + 12, 5)
        c.saveState()
        c.translate(self.aw - 8, self.h + 6)
        c.rotate(180)
        self.p.drawOn(c, 0, 0)
        c.restoreState()


class Stripe(Flowable):
    def wrap(self, aw, ah):
        self.aw = aw
        return aw, 10

    def draw(self):
        c, x = self.canv, 0
        while x < self.aw:
            c.setFillColor(GOLD_FILL)
            c.rect(x, 4, min(34, self.aw - x), 4, stroke=0, fill=1)
            c.setFillColor(INK)
            c.rect(x + 34, 4, 6, 4, stroke=0, fill=1)
            x += 40


def map_block(p):
    return KeepTogether([
        QR(p["gmaps"]), Spacer(1, 6),
        Paragraph(f'<link href="{p["gmaps"]}" color="#8a6714"><u>Google Maps</u></link>'
                  f'&nbsp;&nbsp;|&nbsp;&nbsp;<link href="{p["amaps"]}" color="#8a6714"><u>Apple Maps</u></link>',
                  ss["links"]),
        Paragraph("Scan or tap for walking directions", ParagraphStyle("x", parent=ss["small"], alignment=TA_CENTER)),
    ])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(PAGE[0] / 2, 0.3 * inch, f"West Point Scavenger Hunt  ·  page {doc.page}")
    canvas.restoreState()


def build_pdf(key, r):
    path = HERE / f"west-point-hunt-{key}.pdf"
    doc = SimpleDocTemplate(str(path), pagesize=PAGE, leftMargin=0.35 * inch, rightMargin=0.35 * inch,
                            topMargin=0.4 * inch, bottomMargin=0.5 * inch,
                            title=f"West Point Scavenger Hunt: {r['name']}", author="West Point Scavenger Hunt")
    total = len(r["legs"])
    mi = r["meters"] / 1609.34
    mins = round(r["minutes"] / 5) * 5
    f = [Stripe(), Spacer(1, 6), eyebrow(D.EDITION), Paragraph("West Point Scavenger Hunt", ss["h1"]),
         Paragraph(r["name"], ss["h2"]), Paragraph(r["tagline"], ss["body"]),
         Paragraph(f"<b>{total} stops</b> · about <b>{mi:.1f} miles</b> · about <b>{mins} minutes</b> with stops", ss["body"]),
         Spacer(1, 6),
         Paragraph("Follow rhyming clues from Eisenhower Hall to Trophy Point. Swipe one page at a time: "
                   "read the clue, walk to the next stop, then turn the page to see what you found.", ss["body"])]
    if WEB_URL:
        f += [Spacer(1, 8), Paragraph(f'Prefer tapping? Open the <link href="{WEB_URL}" color="#8a6714"><u>interactive web version</u></link>.', ss["body"])]
    f += [PageBreak()]

    # Grown-up preview
    f += [eyebrow("For grown-ups"), Paragraph("Route preview", ss["h2"]), Paragraph(r["terrain"], ss["body"]),
          Paragraph(f"<b>S.</b> Start: {D.START['name']} (park here)", ss["fact"])]
    for i, l in enumerate(r["legs"], 1):
        f.append(Paragraph(f"<b>{i}.</b> {l['name']} <font color='#565d63'>· {l['walkMin']} min walk</font>", ss["fact"]))
    f += [Spacer(1, 8), eyebrow("Before you go")]
    f += [Paragraph(n, ss["fact"], bulletText="•") for n in D.ADULT_NOTES]
    f += [PageBreak()]

    # Start
    f += [eyebrow("Starting point"), Paragraph(D.START["name"], ss["h2"]), Paragraph(D.START["intro"], ss["body"]),
          Spacer(1, 6), map_block(START), Spacer(1, 10),
          Paragraph("At Eisenhower Hall? Turn the page for your first clue!", ss["center"]), PageBreak()]

    for i, l in enumerate(r["legs"], 1):
        f += [eyebrow(f"Clue {i} of {total}"), Spacer(1, 4),
              Paragraph("<br/>".join(l["clue"]), ss["clue"]), map_block(l), Spacer(1, 8),
              Paragraph(f"<b>Grown-ups:</b> {l['walk']} About {l['walkMin']} min.", ss["small"]),
              Spacer(1, 6), Paragraph("Found it? Turn the page!", ss["center"]), PageBreak()]
        f += [eyebrow(f"Stop {i}: you found"), Paragraph(l["name"], ss["h2"]),
              eyebrow("Activity"), Paragraph(l["activity"], ss["body"]),
              eyebrow("Challenge question"), Paragraph(f"<b>{l['question']}</b>", ss["body"]),
              UpsideDown(l["answer"]), Spacer(1, 8), eyebrow("Fun facts")]
        f += [Paragraph(x, ss["fact"], bulletText="•") for x in l["facts"]]
        if l.get("grownup_tip"):
            f += [Spacer(1, 4), Paragraph(f"<b>Grown-up tip:</b> {l['grownup_tip']}", ss["small"])]
        f += [PageBreak()]

    f += [Spacer(1, 1.5 * inch), Stripe(), Spacer(1, 10),
          Paragraph("Mission complete!", ParagraphStyle("mc", parent=ss["h1"], alignment=TA_CENTER)),
          Paragraph(f"You finished the {r['name']}: {total} stops and about {mi:.1f} miles. "
                    "Every cadet earns an honorary Black Knight salute. Hooah!", ss["center"])]
    doc.build(f, onFirstPage=footer, onLaterPages=footer)
    return path


if __name__ == "__main__":
    build_html()
    for k, r in ROUTES.items():
        p = build_pdf(k, r)
        print(f"{r['name']}: {len(r['legs'])} stops, {r['meters'] / 1609.34:.2f} mi, ~{r['minutes']} min -> {p.name}")
