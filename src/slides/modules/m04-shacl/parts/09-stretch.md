---
minutes: 2
---

# Stretch: find the bugs

The shapes file `docs/legacy/bedretto/ontology.ttl` in the course repository contains at least four mistakes.

<v-clicks>

- A prefix that was never declared
- A constraint no value can meet: `xsd:string` *and* a class
- A nested shape that mixes up `sh:node` and `sh:path`
- Data written as decimals, shapes expecting doubles

</v-clicks>

<!--
For coders who finish early, or as homework. The list of issues is in docs/legacy/README.md.
-->
