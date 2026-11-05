---
class: code-small
minutes: 2
---

# A rule across ingredients

<<< @/../data/shapes/recipes.shapes.ttl#veganRule turtle {3-4|5-6|all}

- A vegan claim is fine only if no ingredient, also inside products, is an animal product
- `sh:class` follows `rdfs:subClassOf` only if the vocabulary is in the **data** graph: validation does not infer

<!--
Hands-on 2 stretch: remove the vocabulary from the data graph and watch the rule stop firing.
That is the difference between inference (adding facts) and validation (checking facts).
-->

---
class: code-small
minutes: 2
---

# The same rule in SHACL-SPARQL

<<< @/../data/shapes/recipes.shapes-sparql.ttl#veganSparql turtle

- More expressive, and readable for anyone who knows SPARQL
- Needs an engine with SHACL-SPARQL support (not the browser playground)

<!--
pySHACL (advanced mode), TopBraid and the EU ITB validator support it.
The SPARQL query follows the class hierarchy itself (a/rdfs:subClassOf*), so it needs no inference either.
-->
