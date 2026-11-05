---
minutes: 3
---

# Choosing IRIs

- **Unique:** one IRI, one thing
- **Resolvable:** a domain you control, or a redirect service like w3id.org
- **Stable:** no versions, file names or status in IRIs
- **Readable or opaque?** `food:potato` helps people; `wd:Q29` survives renames
- **Separate namespaces:** vocabulary (`…/vocab/recipes#`) apart from data (`…/id/food/`)

<p class="fine">Sources: Berners-Lee 1998 · W3C Cool URIs 2008 · w3id.org</p>

<!--
Where does meaning live? Not in the IRI string: an opaque IRI with good labels is as meaningful as a readable one.
Dates: Berners-Lee (1998) writes "After the creation date, putting any information in the name is asking for trouble one way or another."
The date an IRI is issued never changes, so W3C namespaces start with one: rdf 1999/02/22, rdfs 2000/01, owl 2002/07, skos 2004/02.
RDF 1.1 and 1.2 still use the 1999 rdf namespace. Links break when the date or version changes with each release (…/2024/recipes, then …/2025/recipes).
This course uses https://sdsc-ordes.github.io/rdf-training/ so IRIs resolve to documentation.
-->
