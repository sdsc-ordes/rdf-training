---
minutes: 2
---

# Turtle in 30 seconds

```turtle {1|3|4|5|all}
@prefix food: <https://sdsc-ordes.github.io/rdf-training/id/food/> .

recipe:apple-tart a schema:Recipe ;
    schema:name "Apfelwähe"@de, "Apple tart"@en ;
    rec:hasIngredient food:fuji-apple, food:butter .
```

- `@prefix` defines a shorthand for an IRI
- `a` means "is of type" (`rdf:type`)
- `;` repeats the subject, `,` repeats subject and predicate
- `.` ends the statement

<div v-click class="popup code-popup">

The same five triples in N-Triples, with full IRIs and one triple per line:

```turtle
<https://sdsc-ordes.github.io/rdf-training/id/recipe/apple-tart> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://schema.org/Recipe> .
<https://sdsc-ordes.github.io/rdf-training/id/recipe/apple-tart> <https://schema.org/name> "Apfelwähe"@de .
<https://sdsc-ordes.github.io/rdf-training/id/recipe/apple-tart> <https://schema.org/name> "Apple tart"@en .
<https://sdsc-ordes.github.io/rdf-training/id/recipe/apple-tart> <https://sdsc-ordes.github.io/rdf-training/vocab/recipes#hasIngredient> <https://sdsc-ordes.github.io/rdf-training/id/food/fuji-apple> .
<https://sdsc-ordes.github.io/rdf-training/id/recipe/apple-tart> <https://sdsc-ordes.github.io/rdf-training/vocab/recipes#hasIngredient> <https://sdsc-ordes.github.io/rdf-training/id/food/butter> .
```

</div>

<p class="fine">Sources: W3C RDF 1.1 Turtle</p>

<!--
Turtle is one of several formats for the same triples; JSON-LD is another, popular on the web.
Count the triples on this slide: 1 type + 2 names + 2 ingredients = 5.
Last click: the same triples in N-Triples, the format without shorthand. Every N-Triples file is also valid Turtle; databases often use it for bulk loading and dumps because each line stands alone.
-->
