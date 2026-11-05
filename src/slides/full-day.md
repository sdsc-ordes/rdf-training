---
theme: default
title: Knowledge Graphs in a Day
info: One-day course on RDF knowledge graphs, modelling, validation, SPARQL, architectures and graph RAG.
footer: Knowledge graphs · 1-day course
layout: cover
colorSchema: light
routerMode: hash
fonts:
  sans: Switzer
  serif: Switzer
  mono: Fira Code
  provider: none
exportFilename: kg-full-day
---

<img class="sdsc-cover-logo" src="/SDSC_logo_horizontal_rgb_white.png" alt="Swiss Data Science Center" />

# Knowledge Graphs in a Day

RDF, SHACL, SPARQL and graph RAG

<div class="sdsc-meta">Robin Franken · Swiss Data Science Center · 1-day course</div>

---
minutes: 5
---

# Today

<table class="compact">
  <tbody>
    <tr><td>09:00</td><td>Welcome</td></tr>
    <tr><td>09:10</td><td>Building blocks · RDF and property graphs · Modelling</td></tr>
    <tr><td>10:20</td><td><i>Break</i></td></tr>
    <tr><td>10:35</td><td>Hands-on 1: model · Validating data · LLMs build graphs</td></tr>
    <tr><td>12:00</td><td><i>Lunch</i></td></tr>
    <tr><td>13:00</td><td>Hands-on 2: generate and validate · SPARQL · Hands-on 3: query</td></tr>
    <tr><td>14:30</td><td><i>Break</i></td></tr>
    <tr><td>14:45</td><td>Architectures · Use cases and tools · Graph RAG</td></tr>
    <tr><td>15:55</td><td>Wrap-up</td></tr>
  </tbody>
</table>

<!--
Adjust the times per event. One running example all day: a recipe knowledge graph.
Everything hands-on runs in the browser; the worksheets are on the course site.
-->

---
minutes: 5
---

# Who's here?

Hands up if you have…

- written a SQL query
- used an LLM this week
- heard of RDF before today
- had to combine data from multiple sources

<!--
Use the answers to pitch the day: many SQL users → lean on comparisons; many LLM users → tease module 5 and 9.
-->

---
src: ./modules/m00-why-now/full.md
---

---
layout: section
---

<div class="sdsc-section-num">01</div>

# Building blocks

Nodes, edges, triples and IRIs

---
src: ./modules/m01-building-blocks/full.md
---

---
layout: section
---

<div class="sdsc-section-num">02</div>

# RDF and property graphs

The W3C stack and labelled property graphs

---
src: ./modules/m02-stack-vs-lpg/full.md
---

---
layout: section
---

<div class="sdsc-section-num">03</div>

# Modelling a domain

Competency questions, classes and properties

---
src: ./modules/m03-modelling/full.md
---

---
layout: section
minutes: 15
---

# Coffee break

Back at 10:35 for hands-on 1

---
src: ./modules/h1-model/full.md
---

---
layout: section
---

<div class="sdsc-section-num">04</div>

# Validating data

SHACL

---
src: ./modules/m04-shacl/full.md
---

---
layout: section
---

<div class="sdsc-section-num">05</div>

# LLMs build graphs

Generate, validate, repair

---
src: ./modules/m05-llm-construction/full.md
---

---
layout: section
---

# Lunch

Back at 13:00 for hands-on 2

---
src: ./modules/h2-generate-validate/full.md
---

---
layout: section
---

<div class="sdsc-section-num">06</div>

# Asking questions

SPARQL

---
src: ./modules/m06-sparql/full.md
---

---
src: ./modules/h3-query/full.md
---

---
layout: section
minutes: 15
---

# Coffee break

Back at 14:45

---
layout: section
---

<div class="sdsc-section-num">07</div>

# Architectures

Mapping, storage and access

---
src: ./modules/m07-architectures/full.md
---

---
layout: section
---

<div class="sdsc-section-num">08</div>

# Use cases and tools

Industry, health and public-sector cases; tools

---
src: ./modules/m08-use-cases/full.md
---

---
layout: section
---

<div class="sdsc-section-num">09</div>

# Graphs ground LLMs

Graph RAG

---
src: ./modules/m09-graph-rag/full.md
---

---
minutes: 5
---

# What you can do now

- Read and write triples in Turtle
- Model a domain from questions, and validate data with SHACL
- Let an LLM build data, and keep it in check
- Ask a knowledge graph questions with SPARQL
- Judge when a graph helps an LLM, and when it doesn't

<div class="exercise-meta">
  <img src="/qr/site.svg" alt="QR code to the course site" />
  <span>Slides, worksheets and data<br /><b>sdsc-ordes.github.io/rdf-training</b></span>
</div>

---
layout: cover
---

<img class="sdsc-cover-logo" src="/SDSC_logo_horizontal_rgb_white.png" alt="Swiss Data Science Center" />

# Questions?

<div class="sdsc-contact">
  <p class="sdsc-contact-name">Robin Franken</p>
  <p>datascience.ch</p>
  <p>github.com/sdsc-ordes/rdf-training</p>
</div>

<div class="sdsc-partners">
  <img src="/partners/ETH_Zurich_logo_white.png" alt="ETH Zürich" />
  <img src="/partners/EPFL_logo_white.png" alt="EPFL" />
  <img src="/partners/PSI_logo_white.png" alt="PSI" />
</div>

---
src: ./references/full-day.md
---
