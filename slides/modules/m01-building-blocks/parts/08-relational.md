---
class: code-small
minutes: 2
---

# The same sentences as tables

```sql
CREATE TABLE person   (id, name, job_title, favourite_food);  -- only one favourite?
CREATE TABLE food     (id, name, kind);                        -- Fuji: a row, a kind, a subtype table?
CREATE TABLE country  (id, name, continent);                   -- continent: text or another table?
CREATE TABLE grown_in (food_id, country_id);                   -- many-to-many needs a join table
CREATE TABLE course   (id, topic, city, start_date, instructor_id);
```

- Every table, column and key is decided **before** the first row is loaded
- "Also likes pears": `favourite_food` must become a join table
- "Grown in Valais": a canton is not a country, so `grown_in` needs rework
- Each change means `ALTER TABLE`, migrating data and fixing queries

<div class="sdsc-takeaway">With triples you add facts and the schema grows with the data. You still have to agree on names and meaning.</div>

<!--
Relational databases are excellent at fixed, well-understood structures and transactions.
The point is not "SQL is bad" but when the modelling decisions have to be made, and what changing them costs.
In RDF the new sentence is two or three new triples; old data and old queries keep working.
-->
