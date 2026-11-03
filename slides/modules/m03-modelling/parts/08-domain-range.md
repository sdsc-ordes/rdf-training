---
minutes: 3
---

# Domain and range infer, they don't check

From our old project data:

```turtle
@prefix ui: <http://example.org/underground_infra#> .

ui:name rdfs:domain ui:Borehole .
ui:Zurich ui:name "Zurich" .

# An RDFS reasoner concludes: ui:Zurich a ui:Borehole .
```

- `rdfs:domain` and `rdfs:range` add types, they never reject data
- To say what values a property may have, write a SHACL shape

<!--
A classic surprise for people coming from databases or object-oriented code.
The full example is in legacy/bedretto/simple-taxonomy.ttl.
-->
