---
minutes: 3
---

# Domain and range add types

Someone records an allergen on a recipe instead of on a food:

```turtle
rec:hasAllergen rdfs:domain rec:Food .
recipe:caesar-salad rec:hasAllergen allergen:fish .

# An RDFS reasoner concludes: recipe:caesar-salad a rec:Food .
```

- `rdfs:domain` and `rdfs:range` add types, they never reject data
- To say what values a property may have, write a SHACL shape

<p class="fine">Sources: W3C RDF Schema 1.1</p>

<!--
A classic surprise for people coming from databases or object-oriented code.
-->
