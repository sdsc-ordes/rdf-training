---
minutes: 3
---

# Statements about statements today

Until RDF 1.2 is widely supported, give the rating its own node:

```turtle
@prefix ex: <http://example.org/> .

ex:rating-1 a ex:Rating ;
    ex:by person:alice ;
    ex:of recipe:rosti ;
    ex:stars 5 ;
    ex:confidence 0.8 .
```

- Works in every RDF tool today
- RDF 1.2 triple terms let you annotate the triple directly
- Named graphs group whole sets of triples, e.g. one graph per source

<!--
This "n-ary relation" pattern is also how we model quantities of ingredients (rec:IngredientUsage).
Named graphs need a quad format (TriG, N-Quads) and are the usual way to track provenance per batch.
-->
