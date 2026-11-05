---
minutes: 3
---

# Triples

<Triple s="Apple tart" p="has ingredient" o="Fuji apple" />
<Triple s="Fuji apple" p="grown in" o="Spain" />
<Triple s="Apple tart" p="total time" o="70 minutes" literal />

- **Subject** → **predicate** → **object**
- The object is a thing (pill) or a value (dashed box)

<p class="fine">Sources: W3C RDF 1.1 Concepts</p>

<!--
A triple is the smallest unit of data in RDF. A graph is just a set of triples.
Values are called literals: text, numbers, dates.
-->

---

# IRIs and literals

- A thing is named by an IRI: `https://sdsc-ordes.github.io/rdf-training/id/food/fuji-apple`
- Prefixes keep it short: `food:fuji-apple`
- Values carry a datatype or a language: `"PT1H10M"^^xsd:dayTimeDuration`, `"Apfelwähe"@de`
- Same IRI in two datasets = same thing, so the datasets merge without join keys

<p class="fine">Sources: W3C RDF 1.1 Concepts · Vrandečić & Krötzsch 2014</p>

<!--
IRI = internationalised URI. Ideally it resolves to a page describing the thing (Linked Data).
Strings are ambiguous ("Spain", "España", "ES"); IRIs are not.
-->
