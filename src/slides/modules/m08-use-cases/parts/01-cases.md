---
minutes: 3
---

# Knowledge graphs at work (1/2)

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Life sciences</h3>
    <p>SIB publishes UniProt and other databases as RDF. One SPARQL query joins proteins, reactions and species; an LLM assistant writes such queries.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Health research</h3>
    <p>SPHN gives Swiss university hospitals one RDF schema for clinical data, with SHACL checks before data is shared.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Open knowledge</h3>
    <p>Wikidata: a free, multilingual graph anyone can edit. Statements carry qualifiers and references.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Government</h3>
    <p>LINDAS publishes Swiss federal open data as linked data; its statistical cubes feed visualize.admin.ch.</p>
  </div>
</div>

<p class="fine">Sources: Emonet et al. 2024 · Touré et al. 2023 · Vrandečić & Krötzsch 2014 · LINDAS</p>

<!--
Dot vote: which case is closest to your work? Zoom into the top two.
SIB's assistant: Emonet et al. 2024, LLM-based SPARQL generation over federated KGs (arXiv 2410.06062).
SPHN lessons from the old deck: objectification pays off but costs triples; versioned schemas help.
-->

---
minutes: 3
---

# Knowledge graphs at work (2/2)

<div class="sdsc-features">
  <div class="sdsc-feature">
    <h3>Cultural heritage</h3>
    <p>Europeana aggregates collections from many European institutions; Linked Art is a simpler JSON-LD profile of CIDOC-CRM.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Buildings</h3>
    <p>Brick gives every sensor, valve and air handler a shared type, so one analytics app runs in many buildings.</p>
  </div>
  <div class="sdsc-feature">
    <h3>Finance</h3>
    <p>FIBO, from the EDM Council, defines financial concepts in OWL; banks adopt the parts they need.</p>
  </div>
</div>

<p class="fine">Sources: Europeana · Linked Art · Balaji et al. 2016 · EDM Council FIBO</p>

<!--
Brick: property paths answer "which sensors are downstream of air handler 1?".
-->
