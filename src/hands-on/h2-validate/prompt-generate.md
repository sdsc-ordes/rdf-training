You help build a recipe knowledge graph in RDF.

Write 5 recipes from this cuisine: CUISINE. Output only Turtle, no explanation.

Start with exactly these prefixes:

@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix schema:  <https://schema.org/> .
@prefix rec:     <https://sdsc-ordes.github.io/rdf-training/vocab/recipes#> .
@prefix recipe:  <https://sdsc-ordes.github.io/rdf-training/id/recipe/> .
@prefix food:    <https://sdsc-ordes.github.io/rdf-training/id/food/> .
@prefix cuisine: <https://sdsc-ordes.github.io/rdf-training/id/cuisine/> .
@prefix course:  <https://sdsc-ordes.github.io/rdf-training/id/course/> .
@prefix person:  <https://sdsc-ordes.github.io/rdf-training/id/person/> .

Follow this example exactly:

recipe:rosti a schema:Recipe ;
    schema:name "Rösti"@de, "Rösti"@en ;
    schema:description "Crispy grated potato cake from German-speaking Switzerland."@en ;
    schema:author person:anna-keller ;
    schema:totalTime "PT40M"^^xsd:dayTimeDuration ;
    rec:cuisine cuisine:swiss ;
    rec:course course:side ;
    schema:suitableForDiet schema:VegetarianDiet, schema:GlutenFreeDiet ;
    rec:hasIngredient food:potato, food:butter, food:salt .

Rules:
- schema:name: at most one per language, tagged en, de, fr or it.
- schema:totalTime: exactly one, typed xsd:dayTimeDuration.
- rec:cuisine: one of {{cuisines}}.
- rec:course: one of {{courses}}.
- schema:author: one of {{people}}.
- schema:suitableForDiet: only schema:VeganDiet, schema:VegetarianDiet or schema:GlutenFreeDiet, and only if true for every ingredient.
- rec:hasIngredient: only these foods: {{foods}}.
- Use no other properties, prefixes or IRIs.
