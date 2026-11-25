---
layout: two-cols-header
layoutClass: code-small no-prefixes
minutes: 3
---

# Modelling with SKOS

::left::

```turtle
# Concept scheme: the allowed values
cuisine:swiss a skos:Concept ;
    skos:inScheme cuisine:scheme ;
    skos:broader cuisine:european ;
    skos:prefLabel "Swiss"@en, "Schweizerisch"@de .

# Ontology: what the property points to
rec:cuisine rdfs:domain schema:Recipe ;
    rdfs:range skos:Concept .

# Shape: the value must come from the cuisine scheme
recsh:Recipe-cuisine sh:path rec:cuisine ;
    sh:node recsh:CuisineConcept .
recsh:CuisineConcept sh:property [
    sh:path skos:inScheme ;
    sh:hasValue cuisine:scheme ] .
```

::right::

- Concepts are individuals. Recipes point to `cuisine:swiss` with `rec:cuisine`; nothing has the type `cuisine:swiss`
- `skos:broader` is not `rdfs:subClassOf` and is not transitive. A Swiss recipe does not get the cuisine European; a query follows `skos:broader*`
- `rdfs:range` rejects nothing, so the shape checks that the value is in the cuisine scheme
- Use a class instead when the members need their own properties or should inherit rules, as food types do (`rec:HardCheese`)
- Link to concepts in other schemes with `skos:exactMatch` or `skos:closeMatch`

::bottom::

<p class="fine">Sources: W3C SKOS · W3C SHACL</p>

<!--
Cut down from the three ontology modules: src/data/ontology/enumerations.ttl, ontology.ttl and shapes.ttl.
SKOS (W3C, 2009) writes thesauri, classification schemes and code lists as data. skos:Concept is a class; each cuisine is one instance of it.
If cuisines were classes, every recipe would need a type such as recipe:rosti a cuisine:Swiss, and with cuisine:Swiss rdfs:subClassOf cuisine:European a reasoner would also make it a European recipe. With SKOS the recipe points to a concept and the hierarchy stays between the concepts.
skos:broader is not transitive; skos:broaderTransitive is its transitive super-property. In SPARQL, ?recipe rec:cuisine/skos:broader* cuisine:european finds the Swiss, Italian and French recipes.
Labels: the SKOS Reference allows at most one skos:prefLabel per language tag. SHACL can check this with sh:uniqueLang true on skos:prefLabel; our shapes do not.
Why food types are classes and allergens are concepts: the vegan rule uses sh:class rec:AnimalProduct, which follows rdfs:subClassOf. The gluten-free rule only needs rec:hasAllergen with sh:hasValue allergen:gluten.
Mappings: skos:exactMatch is transitive, skos:closeMatch is not, so chains of close matches do not spread. owl:sameAs would merge every statement about both IRIs.
Editors for SKOS: VocBench (EuroVoc, AGROVOC) and PoolParty, on the tools slide.
-->
