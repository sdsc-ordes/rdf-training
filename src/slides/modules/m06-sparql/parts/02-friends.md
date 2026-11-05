---
layout: two-cols-header
minutes: 3
---

# Predict the rows

Who has a friend older than 30?

::left::

```turtle
@prefix ex: <http://example.com/> .

ex:alice a ex:Person ; ex:name "Alice" ;
    ex:age 25 ; ex:hasFriend ex:bob .
ex:bob a ex:Person ; ex:name "Bob" ;
    ex:age 30 ; ex:hasFriend ex:alice, ex:charlie .
ex:charlie a ex:Person ; ex:name "Charlie" ;
    ex:age 35 ; ex:hasFriend ex:bob .
```

::right::

```sparql
PREFIX ex: <http://example.com/>

SELECT DISTINCT ?name WHERE {
  ?person a ex:Person ;
          ex:name ?name ;
          ex:hasFriend ?friend .
  ?friend ex:age ?age .
  FILTER(?age > 30)
}
```

<div v-click class="sdsc-takeaway">Only <b>Bob</b>: Bob's friend Charlie is 35. Without DISTINCT, a person with several matching friends would appear several times.</div>

<!--
Common mistake (it was in the old slides): filtering on the person's own age instead of the friend's.
Ask the room to predict before revealing.
-->
