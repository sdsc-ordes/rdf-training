---
class: code-small
minutes: 1
---

# Open world: this is fine

What happens when you encounter data that doesn't match your expectations?

<div class="grid grid-cols-2 gap-6">
<div class="min-w-0">

<img class="comic" src="/img/this-is-fine-1.jpg" alt="Comic panel: a dog sits calmly at a table in a burning room" />

```turtle
@prefix ex: <http://example.org/> .

ex:Town rdfs:subClassOf [
    a owl:Restriction ;
    owl:onProperty ex:officialLanguage ;
    owl:maxCardinality 1
] .
```

</div>
<div class="min-w-0">

<img class="comic" src="/img/this-is-fine-2.jpg" alt="Comic panel: the dog smiles and says: this is fine" />

```turtle
@prefix ex: <http://example.org/> .

ex:biel-bienne a ex:Town ;
    ex:officialLanguage ex:german, ex:french .

# Inferred: ex:german owl:sameAs ex:french .
```

</div>
</div>

<p class="fine">Sources: Green 2013 · W3C OWL 2 Profiles</p>

<!--
The rule says a town has at most one official language. Biel/Bienne is officially bilingual, German and French.
No error: the reasoner concludes that German and French are the same language under two IRIs.
OWL makes no unique name assumption. It only reports a problem if the data also says ex:german owl:differentFrom ex:french.
Checked with owlrl (OWL 2 RL rule cls-maxc2). The next slide checks the same data with SHACL.
-->
