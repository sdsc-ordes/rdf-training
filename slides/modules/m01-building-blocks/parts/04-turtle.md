---
minutes: 3
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

<!--
Turtle is one of several formats for the same triples; JSON-LD is another, popular on the web.
Count the triples on this slide: 1 type + 2 names + 2 ingredients = 5.
-->
