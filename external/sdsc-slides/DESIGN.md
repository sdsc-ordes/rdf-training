---
version: alpha
name: SDSC Slides
description: >-
  Presentation identity for the Swiss Data Science Center — a 16:9 deck system
  built on the SDSC brand (Space Grotesk + Switzer, Primary #5561A6 / Secondary
  #26235C, green #90CA42 accent) and rendered two ways from one source of truth:
  a python-pptx PowerPoint template and a Slidev Markdown theme. All values come
  from references/tokens.toml; both builders read it, so designers retheme by
  editing a single file. A deck is interface chrome, so colours follow
  sdsc-ui-kit, not the sdsc-plotting data palette. Contrast is verified by
  scripts/verify_tokens.py.
colors:
  primary: "#5561A6"
  primary-light: "#8A94C9"
  secondary: "#26235C"
  background: "#FFFFFF"
  background-alt: "#F4F3F8"
  background-dark: "#101010"
  text: "#000000"
  text-grey: "#848484"
  text-on-dark: "#FFFFFF"
  text-on-dark-muted: "#C2C5E0"
  border: "#C9C9C9"
  accent-green: "#90CA42"
  light-blue-bg: "#DDDEEC"
  content-heading: "#26235C"
gradient:
  start: "#26235C"
  end: "#3B3A7A"
dark:
  background: "#1A1A1A"
  background-alt: "#2D2D2D"
  text: "#FFFFFF"
  text-grey: "#B0B0B0"
  content-heading: "#8A94C9"
  primary: "#8A94C9"
  primary-light: "#A9B1DC"
  light-blue-bg: "#242241"
  gradient: "#101010 -> #26235C"
typography:
  title:
    fontFamily: Space Grotesk
    fontSize: 40pt
    fontWeight: 600
  section-title:
    fontFamily: Space Grotesk
    fontSize: 32pt
    fontWeight: 600
  heading:
    fontFamily: Space Grotesk
    fontSize: 28pt
    fontWeight: 600
  subtitle:
    fontFamily: Switzer
    fontSize: 20pt
    fontWeight: 400
  body:
    fontFamily: Switzer
    fontSize: 18pt
    fontWeight: 400
  section-number:
    fontFamily: Space Grotesk
    fontSize: 72pt
    fontWeight: 600
    color: primary-light
  kpi-number:
    fontFamily: Space Grotesk
    fontSize: 56pt
    fontWeight: 600
    color: content-heading
  kpi-label:
    fontFamily: Switzer
    fontSize: 16pt
    fontWeight: 400
  code:
    fontFamily: Fira Code
    fontSize: 13pt
    fontWeight: 400
  caption:
    fontFamily: Switzer
    fontSize: 12pt
    fontWeight: 400
  footer:
    fontFamily: Switzer
    fontSize: 10pt
    fontWeight: 400
layout:
  aspectRatio: "16:9"
  slideWidth: 13.333in
  slideHeight: 7.5in
  marginX: 0.92in
  marginTop: 0.85in
  footerHeight: 0.55in
  accentBarHeight: 0.06in
components:
  slide-title:
    background: gradient
    backgroundColor: "{gradient.start} -> {gradient.end}"
    titleColor: "{colors.text-on-dark}"
    taglineColor: "{colors.primary-light}"
    metaColor: "{colors.text-on-dark-muted}"
  slide-section:
    backgroundColor: "{colors.light-blue-bg}"
    numberColor: "{colors.primary-light}"
    titleColor: "{colors.content-heading}"
    descColor: "{colors.text-grey}"
  slide-content:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    headingColor: "{colors.content-heading}"
    bulletMarker: "ring, {colors.primary}"
  takeaway:
    backgroundColor: "{colors.background-alt}"
    edge: "{colors.accent-green}"
  feature-card:
    topRule: "{colors.secondary}"
    outline: "{colors.border}"
    iconColor: "{colors.primary}"
  kpi:
    topRule: "{colors.accent-green}"
    numberColor: "{colors.content-heading}"
    labelColor: "{colors.text-grey}"
  banner:
    backgroundColor: "{colors.light-blue-bg}"
    edge: "{colors.secondary}"
  quote:
    backgroundColor: "{colors.background-alt}"
    edge: "{colors.secondary}"
  footer:
    textColor: "{colors.text-grey}"
    layout: "logo · (optional event) · n/total"
    rule: none
  slide-closing:
    background: gradient
    partnerLogos:
      style: white silhouettes on the gradient (no band)
      logos: [ETH Zürich, EPFL, PSI]
---

## Overview

The SDSC presentation identity is the calm, purple-dominant brand of
`sdsc-ui-kit`, recomposed for a 16:9 stage. It pairs **Space Grotesk** (titles,
headings, numbers) with **Switzer** (body, bullets, captions) and **Fira Code**
(code), anchored on **Secondary `#26235C`** — a brand-blue gradient on the
title/closing slides, a pale lavender section divider with a big periwinkle
number, theme-background content slides with Secondary headings,
**Primary `#5561A6`** for links, feature icons, and bullet rings, and **Green
`#90CA42`** reserved for the KPI top rule and the key-takeaway edge. It ships
light + dark themes from one token file. A deck is interface chrome — these are
the brand colours, not the `sdsc-plotting` data palette; colour a chart placed on
a slide with that skill instead.

The normative values live in `references/tokens.toml`, not in this prose.
**Both** renderers — the python-pptx PowerPoint builder and the Slidev CSS
builder — read that one file, so a designer retheme is a single edit plus a
rebuild. The frontmatter above mirrors the TOML for quick reference; the TOML
wins if they ever drift.

## Colors

- **Secondary `#26235C`** — the title/closing gradient anchor; heading colour on
  content slides; KPI numbers; the quote/banner left edge; the feature-card top
  rule. White type sits on it.
- **Primary `#5561A6`** — links, feature icons, the bullet ring marker. Not a
  background. **Primary-light `#8A94C9`** — the big section number and the cover
  tagline (decorative / large only).
- **Lavender `#DDDEEC`** — the section-divider panel, the CTA-banner fill, and
  the inline-code chip. **White `#FFFFFF`** content slides; **`#F4F3F8`** for the
  quote/takeaway/code-block fill.
- **Black `#000000`** body text; **grey `#848484`** captions, footers, and the
  one-line section description only (it is ~3.7:1 on white — keep that text short
  and large, never body copy).
- **Green `#90CA42`** — the KPI top rule and the key-takeaway band's left edge,
  nothing else. Never a fill behind text or a body colour.
- **Border `#C9C9C9`** — feature-card outline, table lines, dividers (the footer
  has no rule).

## Typography

Three families, loaded everywhere: **Space Grotesk** (weight 600) for the title,
section number/title, headings, and KPI numbers; **Switzer** (weight 400) for
subtitles, body, bullets, captions, and footers; **Fira Code** for code. Slide
sizes are in **points** and far larger than the web scale because slides are read
across a room: title 40pt, section number 72pt, section title 36pt, heading
28pt, KPI 56pt, body/bullets 18pt, code 13pt, captions 12pt, footers 10pt.
python-pptx cannot embed fonts — install them locally for PowerPoint; Slidev
pulls Space Grotesk + Fira Code from Google Fonts and Switzer from Fontshare.

## Layout

16:9 (13.333 × 7.5 in). Content slides keep a `0.92in` side margin and `0.7in`
top margin, with a `0.55in` footer band carrying the SDSC logo and the page
number `n / total` (plus an optional centred deck/event name) — **no divider
line**. Headings
stand on their own — no eyebrow above and no accent rule under them — over
generous whitespace, never edge-to-edge text. The layouts (title, section,
content, two-column, feature grid, key numbers, code, quote/findings, CTA banner,
closing) are specified in `references/layouts.md`.

## Themes

One source of truth, two themes. **Light** is default. **Dark** applies the
`tokens.toml` `[dark]` overrides — content slides go to `#1A1A1A` with white body
and a light-lavender `#8A94C9` heading, the footer logo swaps to white, the
section/banner panels become deep indigo `#242241`, and the title/closing
gradient darkens (`#101010 → #26235C`). The title/closing backgrounds stay deep
brand blue in both themes. Build with `--dark` (pptx) or `html.dark` (Slidev);
`verify_tokens.py` checks both.

## Shapes

Restraint, matching the brand: the recurring elements are the **green top rule**
(`~0.04in`) over KPI columns, the **dark / green left edge** on banners / quotes /
takeaways, the thin **feature-card outline**, and a **brand-blue gradient** on the
title and closing backgrounds.
Bullets use a hollow **Primary ring** marker. No drop shadows, no gradients on
type, no rounded photo frames; no footer divider line; no accent rule under
headings.

## Components

- **Title slide** — brand-blue gradient, the white **horizontal** logo top-left
  (no text eyebrow), big Space Grotesk title, periwinkle Switzer tagline, a muted
  meta line (`Author · ISO-date · Event`).
- **Section divider** — pale lavender panel, big periwinkle number, Secondary
  title, one-line grey description. No footer.
- **Content slide** — theme background, Secondary heading (lavender in dark),
  optional intro paragraph, ring bullets, an optional **key-takeaway band** (pale
  fill, green left edge); footer = logo · event · page, no line.
- **Two-column** — full-width title over two equal columns, each a Secondary
  sub-head with body and either bullets or a code block.
- **Feature grid** — 2–4 cards, each a Secondary top rule, a Primary outline
  icon, a bold title, and a two-sentence description.
- **Key numbers** — equal columns, each a green top rule over a large Secondary
  number and a grey label.
- **Code** — a Fira Code listing on the pale `#F4F3F8` fill under a heading.
- **Quote / findings** — a heading, the quote in a band (pale fill, Secondary
  left edge, grey attribution), and a short supporting narrative below.
- **CTA banner** — a lavender band with a Secondary left edge, a centred title
  and line, with body continuing below.
- **Closing** — brand-blue gradient, horizontal white logo, "Questions?", a
  stacked contact block, and the **white partner silhouettes** (ETH Zürich, EPFL,
  PSI) along the bottom-left — straight on the gradient, no backing band.

## Do's and Don'ts

- **Do** edit `references/tokens.toml` and re-run both builders to retheme; never
  hand-edit generated output or hard-code a hex/font in a deck.
- **Do** run `uv run scripts/verify_tokens.py` after any token change.
- **Do** install Space Grotesk + Switzer before exporting a .pptx, or the
  fallbacks (Arial / Calibri) render instead.
- **Don't** add a label/eyebrow above a heading, an accent rule under it, or a
  divider line above the footer — keep the chrome quiet.
- **Don't** use green as a background or body colour — it is the KPI top rule and
  the key-takeaway edge only.
- **Don't** set body copy in the brand grey `#848484` (it fails AA for small
  text); reserve it for short captions, footers, and the section description.
- **Don't** put the coloured partner logos on the dark gradient — use the
  `*_white.png` silhouettes; never recolour or stretch any logo.
- **Don't** colour an on-slide chart with these brand tokens — that is
  `sdsc-plotting`'s job; and don't pull chart colours into slide chrome.
