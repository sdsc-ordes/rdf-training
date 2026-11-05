---
minutes: 2
---

# Why LLMs need grounding

- They **hallucinate**: fluent answers with no source
- Their knowledge is **frozen** at training time and misses your private data
- They **can't show where** an answer came from
- They **can't count** over a collection they have never seen

<div class="sdsc-takeaway">Retrieval-augmented generation (RAG): fetch relevant facts first, then let the LLM answer from them.</div>

<p class="fine">Sources: Ji et al. 2023 · Lewis et al. 2020</p>

<!--
RAG: Lewis et al. 2020 (arXiv 2005.11401). Everything in this module is a variant of "what do we retrieve, and how?"
-->
