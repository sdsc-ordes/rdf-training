---
class: code-small
minutes: 1
---

# Open world: this is fine

Alice may have at most one mother, and the data names two.

<div class="grid grid-cols-2 gap-6">
<div class="min-w-0">

<img class="comic" src="/img/this-is-fine-1.jpg" alt="Comic panel: a dog sits calmly at a table in a burning room" />

```turtle
@prefix ex: <http://example.org/> .

ex:Person rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty ex:mother ;
    owl:maxCardinality 1
] .
```

</div>
<div class="min-w-0">

<img class="comic" src="/img/this-is-fine-2.jpg" alt="Comic panel: the dog smiles and says: this is fine" />

```turtle
@prefix ex: <http://example.org/> .

ex:alice a ex:Person ;
    ex:mother ex:carol, ex:diane .

# Inferred: ex:carol owl:sameAs ex:diane .
```

</div>
</div>

<p class="fine">Sources: Green 2013 · W3C OWL 2 Profiles</p>

<!--
No error: with at most one mother and two names for her, the reasoner concludes that Carol and Diane are the same person under two IRIs.
OWL makes no unique name assumption. It only reports a problem if the data also says ex:carol owl:differentFrom ex:diane.
Checked with owlrl (OWL 2 RL rule cls-maxc2). A SHACL shape with sh:maxCount 1 on ex:mother reports a violation instead.
-->
