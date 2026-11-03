---
minutes: 2
---

# Getting data in

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>RML · YARRRML</h3>
    <p>Declarative mappings from CSV, JSON, XML and databases to triples.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Ontop</h3>
    <p>A virtual graph: SPARQL is rewritten to SQL, nothing is copied.</p>
  </div>
  <div class="sdsc-feature">
    <h3>JSON-LD</h3>
    <p>Add a context to JSON you already publish.</p>
  </div>
  <div class="sdsc-feature">
    <h3>LLM extraction</h3>
    <p>For free text, always followed by validation.</p>
  </div>
</div>

<!--
RML is specified by the W3C Knowledge Graph Construction Community Group; YARRRML is a friendlier YAML syntax for it.
R2RML (W3C, 2012) is the relational-database-only predecessor.
-->

---
class: code-small
minutes: 2
---

# A mapping in YARRRML

```yaml
prefixes:
  rec: https://sdsc-ordes.github.io/rdf-training/vocab/recipes#
  food: https://sdsc-ordes.github.io/rdf-training/id/food/
  allergen: https://sdsc-ordes.github.io/rdf-training/id/allergen/
mappings:
  products:
    sources:
      - [supplier.csv~csv]
    s: food:$(id)
    po:
      - [rec:hasAllergen, allergen:$(allergen)~iri]
```

<div class="grid grid-cols-2 gap-6">
<div>

`supplier.csv`

```text
id,allergen
soy-sauce,soybeans
soy-sauce,gluten
```

</div>
<div>

Result

```turtle
food:soy-sauce rec:hasAllergen
    allergen:soybeans, allergen:gluten .
```

</div>
</div>

<!--
Each row becomes a triple; $(column) inserts a value; ~iri makes the object an IRI rather than text.
Run it with the RMLMapper or Morph-KGC, or try it in the Matey browser editor.
-->
