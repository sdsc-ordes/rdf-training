---
minutes: 2
---

# Blank nodes: things without a name

```turtle
recipe:rosti rec:hasIngredientUsage [
    rec:food food:potato ;
    rec:quantity 800.0 ;
    rec:unit unit:GM
] .
```

- Quick to write, handy while you sketch a model
- Nobody else can point to them, and merging graphs can duplicate them
- Tools relabel them on every load or replace them with generated IRIs, so a report that names `_:b0` is hard to trace
- In production data, give nodes IRIs; blank nodes remain normal inside SHACL shapes and OWL axioms

<p class="fine">Sources: Hogan et al. 2014 · W3C RDF 1.1 Concepts · W3C SPARQL 1.1</p>

<!--
Compare with recipe:rosti-u1 on the previous slide. The old SHACL deck showed how blank nodes make
reports unreadable; that is why our usages have IRIs.
A label like _:b0 only holds within one file or one query result (SPARQL 1.1 Query, section 2.4), so you cannot use it in the next query.
RDF 1.1 Concepts (section 3.5) lets systems replace blank nodes with Skolem IRIs such as http://example.com/.well-known/genid/d26a….
Every sh:property [ … ] in our shapes and every OWL restriction is a blank node. Tools handle those well because nobody needs to point at them.
-->
