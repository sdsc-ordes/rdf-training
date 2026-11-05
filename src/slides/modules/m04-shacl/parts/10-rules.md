---
class: code-small
minutes: 3
---

# SHACL rules

A recipe with a cheese ingredient is a cheese dish.

<div class="grid grid-cols-[2fr_3fr] gap-6">
<div class="min-w-0">

## OWL definition

```turtle
rec:CheeseDish owl:equivalentClass [
    a owl:Restriction ;
    owl:onProperty rec:hasIngredient ;
    owl:someValuesFrom rec:Cheese
] .
```

Both versions classify 2 of our 7 recipes as cheese dishes: the fondue and the Caesar salad.

</div>
<div class="min-w-0">

## SHACL rule

<<< @/../data/shapes/recipes.rules.ttl#cheeseDishRule turtle

</div>
</div>

<p class="fine">Sources: W3C OWL 2 Overview · W3C SHACL-AF · pySHACL</p>

<!--
The rule runs for each focus node of the shape (every schema:Recipe) and adds the triple when the condition conforms.
The condition is an ordinary shape, written with the same constraints as validation.
sh:class rec:Cheese follows rdfs:subClassOf in the data graph, so Gruyère (a rec:HardCheese) counts, as in the vegan rule.
Run it in Python: pyshacl.shacl_rules(data, shacl_graph=rules, advanced=True).
Tested: tests/test_shapes.py compares the rule's output with a SPARQL query. The OWL version was checked with owlrl.
The SHACL 1.2 Inference Rules draft keeps sh:TripleRule but changes the syntax of node expressions.
-->

---
minutes: 3
---

# OWL and SHACL compared

Many inferences that OWL is used for can also be written as SHACL rules.

<table class="compact tight">
  <thead><tr><th>Task</th><th>OWL</th><th>SHACL</th></tr></thead>
  <tbody>
    <tr><td>Class defined by its properties</td><td><code>owl:equivalentClass</code></td><td>Rule with <code>sh:condition</code></td></tr>
    <tr><td>Inverse property</td><td><code>owl:inverseOf</code></td><td>Rule with <code>sh:inversePath</code></td></tr>
    <tr><td>Property chain</td><td><code>owl:propertyChainAxiom</code></td><td>Rule with a sequence path</td></tr>
    <tr><td>Transitive property</td><td><code>owl:TransitiveProperty</code></td><td>Rule with <code>sh:oneOrMorePath</code></td></tr>
    <tr><td>Infer from missing data, count</td><td>Not possible (open world)</td><td>SPARQL rule</td></tr>
    <tr><td>Consistency of the ontology</td><td>OWL DL reasoner</td><td>Not covered</td></tr>
    <tr><td>Check the schema file itself</td><td>Tools such as ROBOT</td><td>SHACL-SHACL shapes graph</td></tr>
  </tbody>
</table>

<p class="fine">OWL 2 RL, the subset of OWL for rule engines, is itself specified as rules. SHACL 1.2 Inference Rules and SPARQL 1.2 RL are W3C Working Drafts (October 2026).</p>

<p class="fine">Sources: W3C OWL 2 Profiles · W3C OWL 2 Conformance · ROBOT · W3C SHACL · W3C SHACL-AF · W3C SHACL 1.2 Inference Rules · W3C SPARQL 1.2 RL</p>

<!--
Examples. Inverse: rec:usedIn as the inverse of rec:hasIngredient. Property chain: a food grown in a country in Europe is grown in Europe.
Missing data: a recipe with no meat or fish ingredient is vegetarian. OWL cannot infer this, because another ingredient may exist somewhere.
OWL also has no arithmetic: a SPARQL rule can count ingredients or add up cooking times.
OWL is still the tool for checking that an ontology is consistent and for reasoning about things the data mentions but does not name.
SHACL-SHACL (appendix C of the SHACL spec, prefix shsh:) is a shapes graph that checks shapes graphs, so any SHACL engine can check your shapes. In pySHACL: pyshacl -m (--metashacl).
It checks the values of SHACL's own properties, e.g. sh:minCount "1" (a string) or sh:datatype "xsd:string" (a literal). A misspelled property such as sh:mincount passes unnoticed.
Our three shapes files pass (tests/test_shapes.py).
OWL has no such check written in OWL. The OWL 2 Conformance spec defines when a file is an OWL 2 DL, EL, QL or RL ontology, and tools check this: robot validate-profile --profile DL --input onto.owl --output report.txt.
OWL could not express these checks itself: in an open world, a missing value is not an error.
OWL 2 RL rules have names like prp-inv1 (inverse), prp-trp (transitive) and prp-spo2 (property chains).
SPARQL 1.2 RL is a compact rule syntax: RULE { ?x :dependsOn ?y } WHERE { ?x :callsService ?y }
pySHACL implements the 2017 rules. Rules that create new blank nodes can repeat forever; the 1.2 draft lets engines stop after a maximum number of rounds.
-->
