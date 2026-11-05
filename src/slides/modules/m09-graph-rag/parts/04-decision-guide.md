---
minutes: 2
---

# Which approach when?

- Single facts in documents → **vector RAG**
- Joins, counts, hard constraints over data you curate → **KG + SPARQL or MCP tools**
- Themes across a big pile of text → **LLM-built graph** (GraphRAG, LightRAG)
- Answers you must audit → **KG with provenance**
- In practice: a **hybrid**

<p class="fine">Sources: Han et al. 2025</p>

<!--
Evidence: Han et al. 2025 (arXiv 2502.11371) find graph-based RAG helps multi-hop and
aggregation, while vector RAG stays strong on single-hop detail. Costs: LLM-built graphs need
many LLM calls to index; text-to-SPARQL needs a schema description and a repair loop.
-->
