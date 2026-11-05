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
- Named graphs group whole sets of triples, e.g. one graph per source

<div class="caveat"><b>Drawback:</b> this pattern is not standardized. Each project invents its own terms (here <code>ex:Rating</code>, <code>ex:by</code>, <code>ex:of</code>), so tools cannot tell which triple the node describes. RDF 1.2 (a Candidate Recommendation) adds a standard link for this, <code>rdf:reifies</code>.</div>

<p class="fine">Sources: Noy & Rector 2006 · W3C RDF 1.2</p>

<!--
This "n-ary relation" pattern is also how we model quantities of ingredients (rec:IngredientUsage).
In RDF 1.2 Turtle the same node gets a standard link to the triple it describes:
<< person:alice ex:rated recipe:rosti ~ ex:rating-1 >> ex:stars 5 .
which means ex:rating-1 rdf:reifies <<( person:alice ex:rated recipe:rosti )>> (RDF 1.2 Concepts, section 1.5).
Named graphs need a quad format (TriG, N-Quads) and are the usual way to track provenance per batch.
-->
