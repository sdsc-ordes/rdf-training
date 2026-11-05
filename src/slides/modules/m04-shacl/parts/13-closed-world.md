---
class: code-small
minutes: 1
---

# Closed world: SHACL reports it

The same data, checked with a shape instead of an OWL restriction.

<div class="grid grid-cols-2 gap-6">
<div class="min-w-0">

```turtle
@prefix ex: <http://example.org/> .

ex:TownShape a sh:NodeShape ;
    sh:targetClass ex:Town ;
    sh:property [
        sh:path ex:officialLanguage ;
        sh:maxCount 1
    ] .

ex:biel-bienne a ex:Town ;
    ex:officialLanguage ex:german, ex:french .
```

</div>
<div class="min-w-0">

```turtle
@prefix ex: <http://example.org/> .

# Validation report
[] a sh:ValidationResult ;
    sh:resultSeverity sh:Violation ;
    sh:focusNode ex:biel-bienne ;
    sh:resultPath ex:officialLanguage ;
    sh:sourceConstraintComponent
        sh:MaxCountConstraintComponent ;
    sh:resultMessage "More than 1 values" .
```

</div>
</div>

<p class="fine">Sources: W3C SHACL · pySHACL</p>

<!--
OWL concluded that German and French are one language; SHACL judges only the data in front of it and reports a violation.
Here the shape is what is wrong: Biel/Bienne really has two official languages. A violation is a prompt to check the data or the rule.
Which one you want depends on the job: OWL to infer new facts, SHACL to check data before you use it.
Report checked with pySHACL; the message text is pySHACL's ("More than 1 values on ex:biel-bienne->ex:officialLanguage").
-->
