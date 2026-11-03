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

- Quick to write, fine for small details
- Nobody else can point to them, and merging graphs can duplicate them
- Validation reports name them `_:b0`, which is hard to trace

<div class="sdsc-takeaway">Give things an IRI if anyone might need to refer to them.</div>

<!--
Compare with recipe:rosti-u1 on the previous slide. The old SHACL deck showed how blank nodes make
reports unreadable; that is why our usages have IRIs.
-->
