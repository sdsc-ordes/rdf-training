# SDSC Slide Layouts

These layouts cover almost every deck. Each is themed from `tokens.toml` and is
available in **both** renderers — a `Deck` method in `build_pptx.py` and a Slidev
`layout:` (plus a few helper classes) — and in **both themes** (light / dark, see
`tokens.toml` `[dark]`). Pick by the slide's job; keep the brand rules from
`DESIGN.md`: the title/closing slides are full-bleed brand-blue gradient, section
dividers are a pale lavender panel, content slides follow the theme background,
and green is reserved for the KPI top rule and the key-takeaway edge.

| # | Layout | Use for | Background | python-pptx | Slidev |
|---|--------|---------|------------|-------------|--------|
| 1 | Title | Deck opener | Brand-blue gradient | `deck.title()` | `layout: cover` |
| 2 | Section | Divider between parts | Lavender `#DDDEEC` | `deck.section()` | `layout: section` |
| 3 | Content | Bullets / prose / takeaway | Theme bg | `deck.content()` | `layout: default` |
| 4 | Two-column | Compare / pair / code | Theme bg | `deck.two_column()` | `layout: two-cols-header` |
| 5 | Feature grid | 2–4 capabilities | Theme bg | `deck.feature_grid()` | `.sdsc-features` cards |
| 6 | Key numbers | Headline stats | Theme bg | `deck.key_numbers()` | `.sdsc-kpis` blocks |
| 7 | Code | A code listing | Theme bg | `deck.code()` | fenced code block |
| 8 | Quote / findings | Pull-quote + narrative | Theme bg | `deck.findings()` | `>` blockquote band |
| 9 | CTA banner | One emphasised message | Theme bg | `deck.banner()` | `.sdsc-banner` |
| 10 | Closing | Thanks / questions / contact | Brand-blue gradient | `deck.closing()` | `layout: cover` |

There is no green accent rule under headings any more, and no text eyebrow above
them — the heading stands on its own.

## 1 · Title

Cover slide. Brand-blue **gradient** background, the white **horizontal** SDSC
logo pinned top-left, the title in Space Grotesk, a periwinkle Switzer tagline,
then a muted meta line (`Author · ISO-date · Event`). No text eyebrow — the logo
already carries the "Swiss Data Science Center" wordmark.

- **python-pptx:** `deck.title("Presentation Title", "Subtitle or tagline goes here", "Author Name · 2026-06-16 · Event or Venue")`
- **Slidev:**
  ```md
  ---
  layout: cover
  # footer: My Event   # optional centred footer text (read by global-bottom.vue)
  ---
  <img class="sdsc-cover-logo" src="/SDSC_logo_horizontal_rgb_white.png" alt="Swiss Data Science Center" />

  # Presentation Title

  Subtitle or tagline goes here

  <div class="sdsc-meta">Author Name · 2026-06-16 · Event or Venue</div>
  ```

## 2 · Section divider

Marks a new part. A **pale lavender panel** (`#DDDEEC`) with a big lavender
two-digit number, the section title in Secondary, and a one-line grey
description. No footer.

- **python-pptx:** `deck.section(1, "Introduction & Context", "A brief description …")`
- **Slidev:**
  ```md
  ---
  layout: section
  ---
  <div class="sdsc-section-num">01</div>

  # Introduction & Context

  A brief description of what this section covers and why it matters.
  ```

## 3 · Content

The workhorse. Theme background; Secondary heading (lavender in dark mode); an
optional intro paragraph; bullets with a **hollow Primary ring** marker; and an
optional **key-takeaway band** — a pale `#F4F3F8` strip with a thin green left
edge for the one statement you want remembered. Use inline `` `code` `` for
literals (dates, flags). The footer (logo · event · page) is automatic.

- **Keep to ~5 bullets**, one line each where possible. Split rather than shrink.
- **python-pptx:** `deck.content(title, body="…", bullets=[…], takeaway="…")`
- **Slidev:** Markdown under an `#` heading; wrap the takeaway in
  `<div class="sdsc-takeaway">…</div>`.

## 4 · Two-column

A full-width title (the `two-cols-header` layout) over two equal columns, each a
Secondary sub-head with body text and either bullets or a code block. Use for
explanation-plus-visual or paired themes.

- **python-pptx:** `deck.two_column(title, left, right)` where `left`/`right` are
  dicts with optional `head`, `body`, `items`, `code`.
- **Slidev:**
  ```md
  ---
  layout: two-cols-header
  ---
  # Two-Column Layout

  ::left::
  ## Left Column
  Use this column for the main explanation.

  - Point one
  - Point two

  ::right::
  ## Right Column
  A supporting visual or code goes here.

  ```python
  SDSC_CATEGORICAL = ["#26245c", "#73a235"]
  ```
  ```

## 5 · Feature grid

Two to four equal cards, each with a Secondary top rule, a Primary outline icon,
a bold title, and a two-sentence description. Use for capabilities, pillars, or
steps.

- **python-pptx:** `deck.feature_grid(title, [{"icon": "hexagon", "title": …, "desc": …}, …])`
  (`icon` ∈ `hexagon` / `diamond` / `target`).
- **Slidev:** a `.sdsc-features` grid of `.sdsc-feature` cards, each with a
  `.sdsc-feature-icon` (inline SVG), an `<h3>`, and a `<p>`.

## 6 · Key numbers

Headline statistics: equal columns, each a **green top rule**, a large Secondary
number, and a grey label. Three or four read best. Numbers are not decoration —
each must mean something.

- **python-pptx:** `deck.key_numbers(title, [("250+", "Projects completed"), …])`
- **Slidev:**
  ```md
  <div class="sdsc-kpis">
    <div class="sdsc-kpi"><b>250+</b><span>Projects completed</span></div>
    <div class="sdsc-kpi"><b>42</b><span>Partner institutions</span></div>
  </div>
  ```

## 7 · Code

A code listing under a heading and one explanatory line. The block sits on the
pale `#F4F3F8` fill in Fira Code. In Slidev, syntax highlighting comes from
Shiki's light theme; this skill only owns the container fill/padding.

- **python-pptx:** `deck.code(title, body, code_string)`
- **Slidev:** a normal fenced ```` ```python ```` block.

## 8 · Quote / findings

A heading, then the quote in a band — pale `#F4F3F8` fill with a thick Secondary
left edge, the quote in Space Grotesk / Secondary, a grey attribution line — then
a short supporting narrative below.

- **python-pptx:** `deck.findings(title, quote, attribution, narrative)`
- **Slidev:**
  ```md
  # Findings

  > "Model B converges 2× faster on all five benchmark datasets."
  >
  > <span class="sdsc-quote-cite">— Smith et al. (2026), ICML proceedings</span>

  Supporting narrative that contextualises the quote.
  ```

## 9 · CTA banner

One emphasised message on an otherwise normal content slide: a lavender band with
a Secondary left edge, a centred title and supporting line, with body copy
continuing below. Use sparingly — one banner per deck.

- **python-pptx:** `deck.banner(banner_title, banner_text, body)`
- **Slidev:**
  ```md
  <div class="sdsc-banner">
    <h2>Call to Action or Key Message</h2>
    <p>Use this banner to emphasise a single important takeaway or next step.</p>
  </div>

  Additional body copy continues below the banner as normal.
  ```

## 10 · Closing

The mirror of the title: brand-blue gradient, the horizontal white logo top-left,
a "Questions?" / "Thank you" title, a stacked contact block (name + email + URL),
and the **partner logos** (ETH Zürich, EPFL, PSI) as **white silhouettes** along
the bottom-left — straight on the gradient, no backing band. Use the
`*_white.png` partner assets so the marks stay visible on the dark gradient.

- **python-pptx:** `deck.closing("Questions?", ["Author Name", "author@datascience.ch", "datascience.ch"])`
  (the white partner logos are added automatically from `assets/logos/partners/`).
- **Slidev:** `layout: cover` with `.sdsc-contact` and:
  ```md
  <div class="sdsc-partners">
    <img src="/partners/ETH_Zurich_logo_white.png" alt="ETH Zürich" />
    <img src="/partners/EPFL_logo_white.png" alt="EPFL" />
    <img src="/partners/PSI_logo_white.png" alt="PSI" />
  </div>
  ```

## Bonus · Chart-palette slide

The example deck includes a **Chart Color Palette** slide (`deck.palette(...)` /
`.sdsc-swatches`). Its swatch colours are the **sdsc-plotting** data palette, not
brand tokens — it shows how to *present* that palette on a deck. Colour any real
chart on a slide with sdsc-plotting, never with these brand colours.

## Composition rules

- **One idea per slide.** If a slide needs two headings, it is two slides.
- **Whitespace over density** — respect the margins; never run text edge to edge.
- **Green is a rule, not a fill.** The only green on a slide is the KPI top rule
  and the key-takeaway band's left edge.
- **No labels/eyebrows above headings, and no accent rule under them** — the
  heading stands on its own.
- **Bullets never rely on colour alone** — the ring marker is shape + colour.
- **Charts** placed on a content slide are coloured by `sdsc-plotting`, not by
  the brand tokens here. Leave the slide chrome (heading, footer) in brand
  colours and let the figure own its data palette.
- **Footers** carry the SDSC logo and the page number `n / total` (no divider
  line), plus an optional centred deck/event name (the headmatter `footer:`
  field); the title, section, and closing slides have no footer.
