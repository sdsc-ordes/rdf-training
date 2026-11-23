---
minutes: 1
---

# IRIs and literals

- A thing is named by an IRI: `https://sdsc-ordes.github.io/rdf-training/id/food/fuji-apple`
- Prefixes keep it short: `food:fuji-apple`
- Values can have a datatype or a language: `"PT1H10M"^^xsd:dayTimeDuration`, `"Apfelwähe"@de`
- Same IRI in two datasets = same thing, so the datasets can merge by default

<p class="fine">Sources: W3C RDF 1.1 Concepts · Vrandečić & Krötzsch 2014</p>

<!--
IRI = internationalised URI. Ideally it resolves to a page describing the thing (Linked Data).
Strings are ambiguous ("Spain", "España", "ES"); IRIs are not.
-->
