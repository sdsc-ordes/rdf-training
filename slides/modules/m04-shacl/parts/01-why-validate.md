---
layout: two-cols-header
minutes: 3
---

# Open world, closed world

A recipe has no total time. Is that a problem?

::left::

## Ontology (RDFS, OWL)

*Open world*: the time may be stated somewhere else. Missing means **unknown**.

Good for describing and inferring.

::right::

## Shapes (SHACL)

*Closed world*: judge only the data in front of you. Missing means **error**.

Good for checking data before you use it.

<div class="sdsc-takeaway">Ontologies say what may be true; shapes say what your data must contain.</div>

<!--
Data arrives from people, scripts and now LLMs. SHACL (W3C, 2017) checks it; shapes are RDF too.
Unique names are a separate question: in OWL, two IRIs may still mean the same thing.
-->
