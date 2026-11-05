---
layout: two-cols-header
class: code-small
minutes: 3
---

# Demo · counting and themes

::left::

## How many recipes use Spanish ingredients?

Vector RAG can only count the chunks it retrieved. The graph counts everything:

<<< @/../hands-on/h3-query/queries/q06-grown-in-spain.rq#query sparql

::right::

## What are this cookbook's main themes?

No single document answers this. An LLM-built graph with community summaries (Family A) does better than vector RAG here.

A curated KG gives counts and statistics, not themes.

::bottom::

<p class="fine">Sources: Edge et al. 2024</p>

<!--
Run in notebook 03 (replay mode). Keep the comparison fair: a vector RAG with metadata filters or a
reranker fixes some failures; say so.
-->
