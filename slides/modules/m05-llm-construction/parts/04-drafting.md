---
minutes: 3
---

# Drafting a model with an LLM

- Give it the competency questions, one at a time
- Give it a reuse list: "prefer schema.org, SKOS, QUDT; never invent namespaces"
- Ask for a table of classes and properties first, Turtle second
- Review the draft like a colleague's pull request

<p class="fine">Research on LLM-drafted ontologies from competency questions finds usable first drafts that still need expert review, e.g. Lippolis et al., ESWC 2025 (arXiv 2503.05388).</p>

<!--
Typical problems in drafts: domain and range used as if they were constraints, duplicate classes,
no n-ary pattern for quantities, missing language tags. Compare with your hands-on 1 model.
-->

---
layout: two-cols-header
minutes: 2
---

# Extraction or generation?

::left::

## Extraction

Facts from a source text, such as a recipe blog. Every fact should point back to the sentence it came from.

::right::

## Generation

Plausible, invented data for tests and teaching, like hands-on 2. Always label it as synthetic.

<!--
Both use the same validation loop. Extraction errors are worse: they look like real facts.
-->
