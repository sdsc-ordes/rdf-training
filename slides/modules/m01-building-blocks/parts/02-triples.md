---
minutes: 4
---

# One fact, one triple

<Triple s="Apple tart" p="has ingredient" o="Fuji apple" />
<Triple s="Fuji apple" p="grown in" o="Spain" />
<Triple s="Apple tart" p="total time" o="70 minutes" literal />

- **Subject** → **predicate** → **object**
- The object is a thing (pill) or a value (dashed box)

<!--
A triple is the smallest unit of data in RDF. A graph is just a set of triples.
Values are called literals: text, numbers, dates.
-->

---

# Things get IRIs, values get types

- A thing is named by an IRI: `https://sdsc-ordes.github.io/rdf-training/id/food/fuji-apple`
- Prefixes keep it short: `food:fuji-apple`
- Values carry a datatype or a language: `"PT1H10M"^^xsd:dayTimeDuration`, `"Apfelwähe"@de`
- Same IRI in two datasets = same thing: merging is free

<div class="sdsc-takeaway">Reuse IRIs others already use, like Wikidata's <code>wd:Q29</code> for Spain.</div>

<!--
IRI = internationalised URI. Ideally it resolves to a page describing the thing (Linked Data).
Strings are ambiguous ("Spain", "España", "ES"); IRIs are not.
-->
