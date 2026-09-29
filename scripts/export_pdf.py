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
    source = source.replace(
        "https://dd.b.pvp.net/latest/set6/en_us/img/cards/06IO008-full.png",
        ".build-assets/master-yi.png",
    )
    source = source.replace(
        "https://dd.b.pvp.net/latest/set6/en_us/img/cards/06IO011-full.png",
        ".build-assets/jun.png",
    )
    source = source.replace(
        "https://dd.b.pvp.net/latest/set6/en_us/img/cards/06RU005-full.png",
        ".build-assets/kayn.png",
    )
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
  margin: 12mm 13mm 13mm 13mm;
  background: #efe7d2;

  @bottom-center {
    content: counter(page);
    font-family: "DejaVu Sans", sans-serif;
    font-size: 7pt;
    color: #5d6e67;
  }
}

html, body {
  margin: 0;
  padding: 0;
  background: #efe7d2;
}

body {
  font-family: "DejaVu Serif", Georgia, serif;
  color: #26332f;
  font-size: 9pt;
  line-height: 1.32;
}

.page {
  position: relative;
  box-sizing: border-box;
  min-height: 271mm;
  padding: 3mm 4mm 5mm 4mm;
  background:
    radial-gradient(circle at 15% 8%, rgba(255,255,255,.34), transparent 26%),
    radial-gradient(circle at 88% 82%, rgba(49,95,86,.08), transparent 24%),
    linear-gradient(180deg, #f6f0df 0%, #efe6cf 100%);
  border: 0.45pt solid rgba(49,95,86,.28);
  box-shadow: inset 0 0 0 1.2mm rgba(255,255,255,.22);
  break-after: page;
  page-break-after: always;
  counter-increment: logicalpage;
}

.page::before,
.page::after {
  content: "";
  position: absolute;
  width: 18mm;
  height: 18mm;
  opacity: .25;
  pointer-events: none;
}

.page::before {
  left: 2.5mm;
  top: 2.5mm;
  border-left: 1.2pt solid #315f56;
  border-top: 1.2pt solid #315f56;
}

.page::after {
  right: 2.5mm;
  bottom: 2.5mm;
  border-right: 1.2pt solid #315f56;
  border-bottom: 1.2pt solid #315f56;
}

.page:last-child {
  break-after: auto;
  page-break-after: auto;
}

.content-sheet {
  column-count: 2;
  column-gap: 8mm;
  column-rule: .35pt solid rgba(49,95,86,.22);
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
  font-size: 22pt;
  line-height: 1.02;
  color: #315f56;
  letter-spacing: .015em;
  text-transform: none;
  border-bottom: 1.2pt solid #7d9a8c;
  padding-bottom: 1.5mm;
}

h2 {
  margin: 3.2mm 0 1.5mm;
  font-size: 14.5pt;
  color: #315f56;
  border-bottom: .7pt solid #9bb1a5;
  padding-bottom: .7mm;
}

h3 {
  margin: 2.6mm 0 1mm;
  font-size: 11.3pt;
  color: #3f6d62;
}

h4, h5 {
  margin: 2mm 0 1mm;
  font-size: 9.5pt;
  color: #4b746a;
}

p {
  margin: 0 0 2.1mm 0;
  orphans: 3;
  widows: 3;
}

ul, ol {
  margin-top: 1mm;
  margin-bottom: 2mm;
  padding-left: 5mm;
}

li::marker {
  color: #4a766b;
}

blockquote {
  margin: 2.4mm 0;
  padding: 2mm 3mm;
  border-left: 2.7pt solid #789d90;
  background: rgba(226,236,230,.78);
  font-style: italic;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
  margin: 2mm 0 3mm;
  break-inside: avoid;
  background: rgba(255,255,255,.16);
}

th, td {
  border-bottom: .45pt solid #aebdb4;
  padding: 1.3mm 1.5mm;
  vertical-align: top;
}

th {
  font-family: "DejaVu Sans", sans-serif;
  background: rgba(49,95,86,.12);
  color: #315f56;
}

.note,
.descriptive,
.wuju,
.darkin,
.encounter,
.mapSlot {
  display: block;
  padding: 2.6mm 3mm;
  margin: 2.7mm 0;
  border-radius: 1.3mm;
  break-inside: avoid;
  page-break-inside: avoid;
}

.note {
  background: linear-gradient(180deg, #f0eedc 0%, #e9e6cf 100%);
  border: .55pt solid #b9b58d;
  border-left: 3.4pt solid #9d9966;
}

.descriptive {
  background: linear-gradient(180deg, #eaf1ed 0%, #dfe9e4 100%);
  border: .55pt solid #9db7ad;
  border-left: 3.4pt solid #6f9689;
  font-style: italic;
}

.wuju {
  background: linear-gradient(135deg, #e8f1ec 0%, #d8e6df 100%);
  border: .55pt solid #8aa79b;
  border-left: 3.8pt solid #315f56;
}

.darkin {
  background: linear-gradient(135deg, #f2e4e1 0%, #ead4d0 100%);
  border: .55pt solid #b68681;
  border-left: 3.8pt solid #6f2628;
}

.darkin h4,
.darkin h5,
.darkin strong {
  color: #6f2628;
}

.encounter {
  background: linear-gradient(180deg, #f5eddc 0%, #eee1c7 100%);
  border: .55pt solid #b99a61;
  border-left: 3.8pt solid #9a783d;
}

.note > :first-child,
.descriptive > :first-child,
.wuju > :first-child,
.darkin > :first-child,
.encounter > :first-child,
.mapSlot > :first-child {
  margin-top: 0;
}

.note > :last-child,
.descriptive > :last-child,
.wuju > :last-child,
.darkin > :last-child,
.encounter > :last-child,
.mapSlot > :last-child {
  margin-bottom: 0;
}

/* Couverture */
.cover-sheet {
  column-count: 1;
  text-align: center;
  padding: 0;
  overflow: hidden;
  background:
    linear-gradient(180deg, rgba(234,241,236,.10), rgba(20,35,31,.18)),
    radial-gradient(circle at 50% 22%, rgba(118,158,143,.24), transparent 34%),
    linear-gradient(180deg, #dce8e1 0%, #b8cfc4 38%, #5c786f 100%);
  border: 0;
}

.cover-sheet::before,
.cover-sheet::after {
  display: none;
}

.coverPage {
  margin: 0;
  min-height: 250mm;
  padding: 27mm 16mm 18mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background:
    linear-gradient(180deg, rgba(244,241,226,.88) 0%, rgba(244,241,226,.76) 46%, rgba(27,44,39,.34) 100%);
  border: 1.2pt solid rgba(255,255,255,.5);
}

.coverPage h1:first-child {
  font-size: 31pt;
  line-height: 1;
  letter-spacing: .04em;
  color: #284f47;
  border: 0;
  margin: 0 0 9mm;
  text-transform: uppercase;
}

.coverPage h1:last-of-type {
  font-size: 27pt;
  color: #315f56;
  border: 0;
  margin: 0 0 8mm;
}

.coverPage h2 {
  border: 0;
  color: #365f56;
  font-size: 17pt;
  margin-bottom: 8mm;
}

.coverPage h3,
.coverPage h4,
.coverPage h5 {
  color: #f3f0e6;
  text-shadow: 0 1px 2px rgba(0,0,0,.35);
}

.coverPage::after {
  content: "☯";
  display: block;
  margin: 14mm auto 0;
  font-family: "DejaVu Sans", sans-serif;
  font-size: 26pt;
  color: rgba(244,240,225,.9);
}

/* Ouverture de chapitre */
.chapter-sheet {
  column-count: 1;
  text-align: center;
  padding: 0;
  overflow: hidden;
  border: 0;
  background: #182723;
}

.chapter-sheet::before,
.chapter-sheet::after {
  display: none;
}

.chapter-sheet .chapter {
  position: relative;
  z-index: 4;
  margin: 11mm 12mm 0;
  padding: 5mm 7mm 4.5mm;
  background: rgba(242,238,220,.90);
  border-top: 1.3pt solid #6b8f82;
  border-bottom: 1.3pt solid #6b8f82;
  box-shadow: 0 2mm 8mm rgba(0,0,0,.22);
}

.chapter-sheet .chapter h1 {
  font-size: 28pt;
  line-height: 1;
  margin: 0 0 2mm;
  border: 0;
  color: #315f56;
}

.chapter-sheet .chapter hr {
  border: 0;
  border-top: .6pt solid #90a99f;
  margin: 2mm 0;
}

.chapter-sheet .chapterHero {
  position: absolute !important;
  left: -13mm !important;
  right: -13mm !important;
  bottom: -13mm !important;
  width: calc(100% + 26mm) !important;
  height: 76% !important;
  max-height: none !important;
  object-fit: cover !important;
  object-position: center !important;
  z-index: 0 !important;
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,.68) 15%, #000 31%, #000 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0,0,0,.68) 15%, #000 31%, #000 100%);
}

.chapter-sheet > p,
.chapter-sheet > blockquote {
  position: relative;
  z-index: 5;
  max-width: 150mm;
  margin-left: auto;
  margin-right: auto;
}

.chapter-sheet blockquote {
  background: rgba(239,232,211,.82);
  border-left: 0;
  border-top: .5pt solid rgba(49,95,86,.45);
  border-bottom: .5pt solid rgba(49,95,86,.45);
  color: #2d4942;
}

.chapter-sheet .artCredit {
  z-index: 5 !important;
  right: 4mm !important;
  bottom: 2mm !important;
  color: rgba(255,255,255,.95);
  background: rgba(20,32,28,.58);
  padding: 1mm 2mm;
  border-radius: 1mm;
}

img {
  max-width: 100%;
  height: auto;
}

.sectionArt {
  width: 100%;
  max-height: 95mm !important;
  object-fit: cover !important;
  border: .55pt solid rgba(49,95,86,.45);
  box-shadow: 0 1mm 2mm rgba(0,0,0,.12);
}

.mapImage {
  width: 100%;
  max-height: 118mm !important;
  object-fit: contain !important;
  background: #17211e;
  border: .7pt solid #607e74;
}

.mapFallback {
  padding: 4mm;
  margin: 2mm 0;
  border: .8pt dashed #819d89;
  background: rgba(244,247,245,.70);
  font-family: "DejaVu Sans", sans-serif;
  font-size: 8pt;
  color: #53645e;
  text-align: center;
}

.mapSlot {
  column-span: all;
  border: .65pt solid #819d89;
  background: rgba(232,238,233,.62);
}

.source-footnote {
  position: absolute;
  left: 4mm;
  bottom: 1.8mm;
  font-family: "DejaVu Sans", sans-serif;
  font-size: 6.4pt;
  color: #62716b;
  letter-spacing: .025em;
  text-transform: uppercase;
}

.spacer { height: 4mm; }

.artCredit,
.sectionArtCredit,
.mapCredit {
  font-family: "DejaVu Sans", sans-serif;
  font-size: 6.4pt;
  color: #6b786f;
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
