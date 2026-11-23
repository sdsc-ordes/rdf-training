---
minutes: 4
---

# Sentences to triples

> Robin is a data engineer who loves apples, especially Fuji.
>
> Fuji apples are grown in Spain and France, both countries in Europe.
>
> Robin teaches an RDF course in Zurich on 12 March 2025.

<div class="mini-example">Example: "Rösti comes from Switzerland." <Triple s="Rösti" p="comes from" o="Switzerland" /></div>

<div class="exercise-meta">
  <span><b>Pairs · 4 min</b> · write your triples in any text editor</span>
</div>

<div v-click class="sdsc-takeaway"><b>New sentence:</b> Robin also likes pears, grown in Valais. What changes in your triples? What would change in a traditional relational database?</div>

<!--
Reveal the new sentence after about 3 minutes.
Longer formats: let half the pairs design database tables instead of triples, then reveal the new sentence.
Table designs typically break twice: a favourite_food column can't hold a second food,
and a grown_in table that points to countries can't hold a canton.
Debrief: Is "Fuji" a thing or a value? Is "loves" the same relation as "favourite"?
How do you write the date so a computer can compare it?
-->

---

# One possible answer

```turtle
@prefix ex: <http://example.org/> .

person:robin a schema:Person ;
    schema:jobTitle "Data engineer"@en ;
    ex:likes food:apple, food:fuji-apple .

food:fuji-apple rec:grownIn wd:Q29, wd:Q142 .    # Spain, France
wd:Q29 schema:containedInPlace wd:Q46 .          # Spain is in Europe
wd:Q142 schema:containedInPlace wd:Q46 .

ex:rdf-course a schema:Course ;
    schema:instructor person:robin ;
    schema:location wd:Q72 ;                      # Zurich
    schema:startDate "2025-03-12"^^xsd:date .
```

<div v-click class="popup side-quest">

<b>Side quest</b>

Link the two foods with <code>rdfs:subClassOf</code> and drop <code>food:apple</code> from the likes list:

```turtle
food:fuji-apple rdfs:subClassOf food:apple .
food:apple rdfs:subClassOf rec:Fruit .
```

Which fruits does Robin like?

```sparql
PREFIX ex: <http://example.org/>
SELECT ?food WHERE {
  person:robin ex:likes ?food .
  ?food rdfs:subClassOf* rec:Fruit .
}
```

Answer: <code>food:fuji-apple</code>, two subclass steps below <code>rec:Fruit</code>.

</div>

<!--
No single right answer. Note what we reused (schema.org, Wikidata) and what we invented (ex:likes).
Side quest (click): rdfs:subClassOf* follows the hierarchy any number of steps, so the same query also finds pears or lemons once they sit under rec:Fruit.
Discussion point: liking Fuji apples does not mean liking every apple. Keep ex:likes food:apple if the sentence ("loves apples") matters.
In the course graph food:fuji-apple is one food item typed rec:Fruit, so the hands-on queries use a/rdfs:subClassOf*. Both readings work: a variety can be a class of apples or a single food item.
-->
