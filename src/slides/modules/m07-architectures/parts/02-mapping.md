---
minutes: 3
---

# Getting data in

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>RML · YARRRML</h3>
    <p>Declarative mappings from CSV, JSON, XML and databases to triples.</p>
    <p class="pro"><b>Pro</b> Mapping files can be reviewed, versioned and rerun.</p>
    <p class="con"><b>Con</b> One more language; messy sources still need cleaning first.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Ontop</h3>
    <p>A virtual graph: SPARQL is rewritten to SQL, nothing is copied.</p>
    <p class="pro"><b>Pro</b> Always as fresh as the database; no second copy to keep in sync.</p>
    <p class="con"><b>Con</b> SQL sources only, and only as fast as the SQL it generates.</p>
  </div>
  <div class="sdsc-feature">
    <h3>JSON-LD</h3>
    <p>Add a context to JSON you already publish.</p>
    <p class="pro"><b>Pro</b> Developers keep working with plain JSON.</p>
    <p class="con"><b>Con</b> Keys missing from the context are silently dropped.</p>
  </div>
  <div class="sdsc-feature">
    <h3>LLM extraction</h3>
    <p>For free text, always followed by validation.</p>
    <p class="pro"><b>Pro</b> Reaches facts locked in PDFs and prose.</p>
    <p class="con"><b>Con</b> Invents and mislinks facts; costs money per document.</p>
  </div>
</div>

<p class="fine">Sources: W3C KGC RML · Heyvaert et al. 2018 · Calvanese et al. 2017 · W3C JSON-LD 1.1 · Pan et al. 2024</p>

<!--
RML is specified by the W3C Knowledge Graph Construction Community Group; YARRRML is a friendlier YAML syntax for it.
R2RML (W3C, 2012) is the relational-database-only predecessor.
JSON-LD: during expansion, keys that the context doesn't map to an IRI are dropped without an error. Check with the JSON-LD Playground.
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
