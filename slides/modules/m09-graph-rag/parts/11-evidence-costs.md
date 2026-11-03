---
minutes: 3
---

# What the evidence says, and what it costs

> Graph-based RAG does better on multi-hop and aggregation questions; vector RAG stays strong on single-hop detail. The two are complementary.
>
> <span class="sdsc-quote-cite">Paraphrasing Han et al., RAG vs. GraphRAG: A Systematic Evaluation and Key Insights (arXiv 2502.11371)</span>

- **LLM-built graphs:** LLM calls for every chunk to index, and again when text changes
- **Text-to-SPARQL:** a schema description, examples and a retry loop
- **Agents:** several LLM calls per question, so more latency
- **Curated KG:** the modelling and data work up front: this course

<!--
Fill in figures from your own run of notebook 03 (tokens to index, calls and seconds per answer).
Benchmarks also exist (e.g. GraphRAG-Bench); results depend heavily on the question mix.
-->
