---
layout: two-cols-header
class: code-small
minutes: 3
---

# Inference with RDFS and OWL

::left::

## RDFS: subclasses

```turtle
rec:HardCheese rdfs:subClassOf rec:Cheese .
rec:Cheese rdfs:subClassOf rec:DairyProduct .
rec:DairyProduct rdfs:subClassOf rec:AnimalProduct .
food:gruyere a rec:HardCheese .

# Inferred: food:gruyere a rec:Cheese ,
#     rec:DairyProduct , rec:AnimalProduct .
```

::right::

## OWL: property chains

```turtle
rec:grownIn owl:propertyChainAxiom
    ( rec:grownIn schema:containedInPlace ) .
food:fuji-apple rec:grownIn wd:Q29 .      # Spain
wd:Q29 schema:containedInPlace wd:Q46 .   # Europe

# Inferred: food:fuji-apple rec:grownIn wd:Q46 .
```

::bottom::

- RDFS also infers from subproperties, domain and range
- OWL adds inverse and transitive properties, equivalence, disjointness and cardinality
- A reasoner adds facts and rejects no data; SHACL checks data, and SHACL rules can infer many of the same facts (module 4)

<p class="fine">Sources: W3C RDF 1.1 Semantics · W3C OWL 2 Overview</p>

<!--
The chain reads: if X is grown in Y, and Y is contained in Z, then X is grown in Z. Applied again, it climbs any depth of places.
"Which ingredients are grown in Europe?" then needs no knowledge of which countries are in Europe at query time.
Checked with the owlrl reasoner (OWL 2 RL rule prp-spo2).
You can also follow the hierarchy at query time with a property path (a/rdfs:subClassOf*),
which is what our hands-on queries do: no reasoner needed.
-->
