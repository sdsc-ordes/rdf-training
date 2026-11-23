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
minutes: 2
---

# Agenda — morning

<table class="agenda">
  <thead><tr><th>Time</th><th>Session</th><th>Format</th></tr></thead>
  <tbody>
    <tr class="pause"><td>09:00–09:10</td><td>Welcome and introduction</td><td></td></tr>
    <tr><td>09:10–09:30</td><td><b>Building blocks: nodes, edges, triples and IRIs</b><small>How facts become subject–predicate–object statements, and why global identifiers matter.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr><td>09:30–10:00</td><td><b>RDF and property graphs</b><small>The W3C stack (RDF, RDFS, OWL, SKOS, SHACL, SPARQL) and when a property graph suits the data better.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr><td>10:00–10:25</td><td><b>Modelling a domain: from questions to classes and properties</b><small>Competency questions, schema design, SKOS lists and reuse of existing vocabularies.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr class="pause"><td>10:25–10:40</td><td>Coffee break</td><td></td></tr>
    <tr><td>10:40–11:15</td><td><b>Hands-on 1: model the recipe domain</b><small>Turn five competency questions into classes and properties, then compare the groups' models.</small></td><td><span class="fmt fmt-hands-on">Hands-on</span></td></tr>
    <tr><td>11:15–11:50</td><td><b>Validating data with SHACL</b><small>Shapes and constraints that catch inconsistent data before it reaches applications.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr><td>11:50–12:15</td><td><b>How LLMs can help build knowledge graphs</b><small>Ontology drafting, entity and relation extraction, triple generation and validation in the loop.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr class="pause"><td>12:15–13:15</td><td>Lunch</td><td></td></tr>
  </tbody>
</table>

<!--
Times are rough estimates per session; adjust them per event.
One running example all day: a recipe knowledge graph.
Everything hands-on runs in the browser; the worksheets are on the course site.
-->

---
minutes: 1
---

# Agenda — afternoon

<table class="agenda">
  <thead><tr><th>Time</th><th>Session</th><th>Format</th></tr></thead>
  <tbody>
    <tr><td>13:15–13:50</td><td><b>Hands-on 2: generate, validate, repair</b><small>Validate LLM-written recipe data with SHACL and send the report back, at most three rounds.</small></td><td><span class="fmt fmt-hands-on">Hands-on</span></td></tr>
    <tr><td>13:50–14:10</td><td><b>Asking questions with SPARQL</b><small>Graph patterns, filters, aggregates and queries across federated endpoints.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr><td>14:10–14:40</td><td><b>Hands-on 3: query the recipe graph</b><small>Run and change the SPARQL queries that answer the competency questions.</small></td><td><span class="fmt fmt-hands-on">Hands-on</span></td></tr>
    <tr class="pause"><td>14:40–14:55</td><td>Coffee break</td><td></td></tr>
    <tr><td>14:55–15:15</td><td><b>Knowledge graph architectures: from sources to applications</b><small>Mapping and ETL, triplestores, federated SPARQL endpoints and ways to serve the graph.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr><td>15:15–15:50</td><td><b>Graph RAG: grounding LLMs in knowledge graphs</b><small>Retrieval over entities and relations to give LLM answers context and traceable sources.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr><td>15:50–16:20</td><td><b>Use cases and tools</b><small>How knowledge graphs are used across domains, and the tooling that supports them.</small></td><td><span class="fmt">Lecture &amp; Q&amp;A</span></td></tr>
    <tr class="pause"><td>16:20–16:50</td><td>Wrap-up and questions</td><td></td></tr>
  </tbody>
</table>

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
Use the answers to pitch the day: many SQL users → lean on comparisons; many LLM users → tease module 5 and 8.
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

Back at 10:40 for hands-on 1

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

Back at 13:15 for hands-on 2

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

Back at 14:55

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

# Graphs ground LLMs

Graph RAG

---
src: ./modules/m09-graph-rag/full.md
---

---
layout: section
---

<div class="sdsc-section-num">09</div>

# Use cases and tools

Industry, health and public-sector cases; tools

---
src: ./modules/m08-use-cases/full.md
---

---
minutes: 5
---

# What you can do now

- Read and write triples in Turtle, and choose between RDF and a property graph
- Model a domain from questions, and validate data with SHACL
- Let an LLM build data, and keep it in check
- Ask a knowledge graph questions with SPARQL, and sketch the pipeline that serves it
- Judge when a graph helps an LLM, and when it doesn't

<div class="exercise-meta">
  <span>Slides, worksheets and data: <b>github.com/sdsc-ordes/rdf-training</b></span>
</div>

---
layout: cover
minutes: 25
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
