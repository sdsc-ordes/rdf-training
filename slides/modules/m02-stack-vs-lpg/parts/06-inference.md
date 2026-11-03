---
minutes: 3
---

# Inference: facts you didn't write

```turtle
rec:HardCheese rdfs:subClassOf rec:Cheese .
rec:Cheese rdfs:subClassOf rec:DairyProduct .
rec:DairyProduct rdfs:subClassOf rec:AnimalProduct .
food:gruyere a rec:HardCheese .

# An RDFS reasoner adds: food:gruyere a rec:Cheese, rec:DairyProduct, rec:AnimalProduct .
```

- RDFS infers from subclasses, subproperties, domain and range
- OWL adds equivalence, disjointness, cardinality and more
- Reasoners **add** facts, they don't reject data: that is SHACL's job

<!--
You can also follow the hierarchy at query time with a property path (a/rdfs:subClassOf*),
which is what our hands-on queries do: no reasoner needed.
-->
