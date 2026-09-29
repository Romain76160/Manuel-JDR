#!/usr/bin/env python3
from pathlib import Path
import re
import sys

try:
    import markdown
    from weasyprint import HTML
except ImportError as exc:
    raise SystemExit(f"Missing dependency: {exc}")

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "homebrewery" / "prologue-complet.md"
STYLE = ROOT / "homebrewery" / "style.css"
OUTDIR = ROOT / "dist"
OUTPUT = OUTDIR / "la-seconde-guerre-darkin-prologue.pdf"

BLOCKS = {
    "note": "note",
    "descriptive": "descriptive",
    "wuju": "wuju",
    "darkin": "darkin",
    "encounter": "encounter",
    "mapSlot": "mapSlot",
    "chapter": "chapter",
    "coverPage": "coverPage",
}

def preprocess_blocks(text: str) -> str:
    out = []
    stack = []
    for line in text.splitlines():
        stripped = line.strip()

        if stripped == "{{pageNumber,auto}}":
            continue

        m = re.fullmatch(r"\{\{footnote\s+(.+)\}\}", stripped)
        if m:
            out.append(f'<div class="source-footnote">{m.group(1)}</div>')
            continue

        opened = False
        for token, cls in BLOCKS.items():
            if stripped == "{{" + token:
                out.append(f'<div class="{cls}" markdown="1">')
                stack.append(cls)
                opened = True
                break
        if opened:
            continue

        if stripped == "}}" and stack:
            stack.pop()
            out.append("</div>")
            continue

        # Homebrewery spacer line.
        if stripped == ":":
            out.append('<div class="spacer"></div>')
            continue

        out.append(line)

    while stack:
        stack.pop()
        out.append("</div>")

    return "\n".join(out)

def page_class(segment: str) -> str:
    if "{{coverPage" in segment:
        return "page cover-sheet"
    if "{{chapter" in segment:
        return "page chapter-sheet"
    return "page content-sheet"

def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Source missing: {SOURCE}")

    source = SOURCE.read_text(encoding="utf-8")
    source = source.replace("https://raw.githubusercontent.com/Romain76160/Manuel-JDR/main/", "")

    source = re.sub(
        r'<img class="mapImage" src="assets/cartes/temple-wuju-niveau-inferieur-joueurs\.jpg"[^>]*>',
        '<div class="mapFallback">Carte du Reliquaire : asset source disponible dans <strong>assets/cartes/temple-wuju-niveau-inferieur-joueurs.jpg</strong>.</div>',
        source,
    )
    project_css = STYLE.read_text(encoding="utf-8") if STYLE.exists() else ""

    segments = re.split(r"(?m)^\s*[\\]page\s*$", source)
    rendered_pages = []

    md = markdown.Markdown(
        extensions=["extra", "tables", "sane_lists", "md_in_html"],
        output_format="html5",
    )

    for index, raw_segment in enumerate(segments, start=1):
        raw_segment = raw_segment.strip()
        if not raw_segment:
            continue
        cls = page_class(raw_segment)
        processed = preprocess_blocks(raw_segment)
        md.reset()
        html = md.convert(processed)
        rendered_pages.append(
            f'<section class="{cls}" data-logical-page="{index}">{html}</section>'
        )

    pdf_css = r"""
@page {
  size: A4;
  margin: 11mm 12mm 12mm 12mm;
  @bottom-center {
    content: counter(page);
    font-family: "DejaVu Sans", sans-serif;
    font-size: 7pt;
    color: #53645e;
  }
}

html, body {
  margin: 0;
  padding: 0;
  background: white;
}

body {
  font-family: "DejaVu Serif", Georgia, serif;
  color: #26332f;
  font-size: 9.15pt;
  line-height: 1.30;
}

.page {
  position: relative;
  box-sizing: border-box;
  min-height: 273mm;
  break-after: page;
  page-break-after: always;
  counter-increment: logicalpage;
}

.page:last-child {
  break-after: auto;
  page-break-after: auto;
}

.content-sheet {
  column-count: 2;
  column-gap: 8mm;
  column-fill: auto;
}

.content-sheet > h1,
.content-sheet > h2 {
  column-span: all;
}

h1, h2, h3, h4, h5 {
  font-family: "DejaVu Sans", sans-serif;
  break-after: avoid;
  page-break-after: avoid;
}

h1 {
  margin: 0 0 4mm 0;
  font-size: 23pt;
  line-height: 1.05;
}

h2 {
  margin: 3mm 0 1.5mm;
  font-size: 15pt;
  border-bottom: 0.5pt solid #819d89;
}

h3 {
  margin: 2.8mm 0 1mm;
  font-size: 11.5pt;
}

h4, h5 {
  margin: 2mm 0 1mm;
  font-size: 9.5pt;
}

p {
  margin: 0 0 2.2mm 0;
}

ul, ol {
  margin-top: 1mm;
  margin-bottom: 2mm;
  padding-left: 5mm;
}

blockquote {
  margin: 2mm 0;
  padding: 1.8mm 2.5mm;
  border-left: 2.5pt solid #819d89;
  background: #f5f7f5;
  font-style: italic;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
  margin: 2mm 0 3mm;
  break-inside: avoid;
}

th, td {
  border-bottom: 0.4pt solid #b7c5bd;
  padding: 1.2mm 1.4mm;
  vertical-align: top;
}

th {
  font-family: "DejaVu Sans", sans-serif;
  background: #e8eee9;
}

.note, .descriptive, .wuju, .darkin, .encounter {
  display: block;
  padding: 2.2mm 2.8mm;
  margin: 2.5mm 0;
  border-radius: 1mm;
  break-inside: avoid;
  page-break-inside: avoid;
}

.note { background: #eef0e5; border-left: 3pt solid #a2a578; }
.descriptive { background: #e8eee9; border-left: 3pt solid #819d89; }
.wuju { background: #edf4ef; border-left: 3pt solid #315f56; }
.darkin { background: #f3e9e6; border-left: 3pt solid #6f2628; }
.encounter { background: #f3eee3; border-left: 3pt solid #9a783d; }

.note > :first-child,
.descriptive > :first-child,
.wuju > :first-child,
.darkin > :first-child,
.encounter > :first-child {
  margin-top: 0;
}

.note > :last-child,
.descriptive > :last-child,
.wuju > :last-child,
.darkin > :last-child,
.encounter > :last-child {
  margin-bottom: 0;
}

.cover-sheet,
.chapter-sheet {
  column-count: 1;
  text-align: center;
  padding-top: 14mm;
  overflow: hidden;
}

.coverPage {
  margin-top: 34mm;
}

.coverPage h1:first-child {
  font-size: 32pt;
  letter-spacing: 0.03em;
}

.coverPage h1:last-of-type {
  font-size: 27pt;
  margin-top: 7mm;
}

.coverPage h2 {
  border: 0;
  font-size: 18pt;
}

.chapter-sheet .chapter {
  position: relative;
  z-index: 3;
  background: rgba(255,255,255,.78);
  padding: 4mm;
  border-radius: 2mm;
}

.chapter-sheet .chapter h1 {
  font-size: 29pt;
  margin: 0 0 4mm;
}

.chapter-sheet .chapterHero {
  position: absolute !important;
  left: -12mm !important;
  right: -12mm !important;
  bottom: -12mm !important;
  width: calc(100% + 24mm) !important;
  height: 72% !important;
  max-height: none !important;
  object-fit: cover !important;
  z-index: 0 !important;
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,.88) 24%, #000 40%, #000 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,.88) 24%, #000 40%, #000 100%);
}

.chapter-sheet .artCredit {
  z-index: 4 !important;
  right: 0 !important;
  bottom: 1mm !important;
}

img {
  max-width: 100%;
  height: auto;
}

.sectionArt,
.mapImage {
  max-height: 120mm !important;
  object-fit: contain !important;
}

.mapFallback {
  padding: 4mm;
  margin: 2mm 0;
  border: 0.6pt dashed #819d89;
  background: #f4f7f5;
  font-family: "DejaVu Sans", sans-serif;
  font-size: 8pt;
  color: #53645e;
  text-align: center;
}

.mapSlot {
  column-span: all;
  break-inside: avoid;
  border: 0.6pt solid #819d89;
  background: #f4f7f5;
  padding: 2mm;
  margin: 2mm 0 3mm;
}

.source-footnote {
  position: absolute;
  left: 0;
  bottom: 1mm;
  font-family: "DejaVu Sans", sans-serif;
  font-size: 6.5pt;
  color: #62716b;
  letter-spacing: .02em;
}

.spacer { height: 4mm; }

.artCredit, .sectionArtCredit, .mapCredit {
  font-family: "DejaVu Sans", sans-serif;
  font-size: 6.5pt;
  color: #62716b;
}

a {
  color: #315f56;
  text-decoration: none;
}

strong {
  color: #223b34;
}
"""

    html_doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>La Seconde Guerre Darkin - Prologue</title>
<style>
{project_css}
{pdf_css}
</style>
</head>
<body>
{''.join(rendered_pages)}
</body>
</html>
"""

    OUTDIR.mkdir(parents=True, exist_ok=True)
    debug_html = OUTDIR / "la-seconde-guerre-darkin-prologue.html"
    debug_html.write_text(html_doc, encoding="utf-8")

    HTML(string=html_doc, base_url=str(ROOT)).write_pdf(str(OUTPUT))
    print(OUTPUT)

if __name__ == "__main__":
    main()
