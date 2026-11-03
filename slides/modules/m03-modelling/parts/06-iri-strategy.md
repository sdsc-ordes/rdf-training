---
minutes: 3
---

# Choosing IRIs

- **Unique:** one IRI, one thing
- **Resolvable:** a domain you control, or a redirect service like w3id.org
- **Stable:** no versions, file names or dates in the IRIs of things
- **Readable or opaque?** `food:potato` helps people; `wd:Q29` survives renames
- **Separate namespaces:** vocabulary (`…/vocab/recipes#`) apart from data (`…/id/food/`)

<div class="sdsc-takeaway">Decide your IRI pattern before you publish data. Changing it later breaks every link.</div>

<!--
Where does meaning live? Not in the IRI string: an opaque IRI with good labels is as meaningful as a readable one.
This course uses https://sdsc-ordes.github.io/rdf-training/ so IRIs resolve to documentation.
-->
