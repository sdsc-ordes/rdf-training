---
class: code-small
minutes: 2
---

# A rule across ingredients

<<< @/../data/ontology/shapes.ttl#veganRule turtle {3-4|5|all}

- A vegan claim is fine only if no ingredient is an animal product
- `sh:class` follows `rdfs:subClassOf` only if the vocabulary is in the **data** graph: validation does not infer

<!--
Hands-on 2 stretch: remove the vocabulary from the data graph and watch the rule stop firing.
That is the difference between inference (adding facts) and validation (checking facts).
-->

---
class: code-small
minutes: 2
---

# The vegan rule in SHACL-SPARQL

<<< @/../data/shacl-advanced.ttl#veganSparql turtle

- Also looks inside products: `rec:containsIngredient*` reaches the Parmesan in pesto
- Needs an engine with SHACL-SPARQL support (not the browser playground)

<!--
pySHACL (advanced mode), TopBraid and the EU ITB validator support it.
More expressive than Core, and readable for anyone who knows SPARQL.
The SPARQL query follows the class hierarchy itself (a/rdfs:subClassOf*), so it needs no inference either.
SHACL Core can look inside products too, with sh:zeroOrMorePath in the path; the course shapes leave that out to stay readable.
-->
