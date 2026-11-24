---
minutes: 1
---

# IRIs and literals

- A thing is named by an IRI: `https://sdsc-ordes.github.io/rdf-training/id/food/fuji-apple`
- Prefixes keep it short: `food:fuji-apple`
- Values can have a datatype or a language: `"PT1H10M"^^xsd:dayTimeDuration`, `"Apfelwähe"@de`
- Same IRI in two datasets = same thing, so the datasets can merge by default

<div v-click class="uri-sets">
  <div class="tbox tbox-1"><b>IRI</b><small>any Unicode character</small><code>https://de.wikipedia.org/wiki/Zürich</code>
    <div class="tbox tbox-2"><b>URI</b><small>ASCII characters only</small>
      <div class="uri-row">
        <div class="tbox tbox-3"><b>URL</b><small>also says where to fetch it</small><code>https://www.wikidata.org/entity/Q29</code></div>
        <div class="tbox tbox-3"><b>URN</b><small>a name with no location</small><code>urn:isbn:0451450523</code></div>
      </div>
    </div>
  </div>
</div>

<p class="fine">Sources: W3C RDF 1.1 Concepts · Vrandečić & Krötzsch 2014 · RFC 3986 · RFC 3987</p>

<!--
IRI = internationalised URI. Ideally it resolves to a page describing the thing (Linked Data).
Strings are ambiguous ("Spain", "España", "ES"); IRIs are not.
On click, the boxes: every URL is a URI, every URI is an IRI. Berners-Lee's rules (previous slide) say URI; RDF 1.1 uses IRI.
The Zürich address is an IRI but not a URI; percent-encoded (Z%C3%BCrich) it becomes one.
URL: a URI that also says how to reach the thing (here over HTTPS). URN: a URI that only names it (urn:isbn:0451450523 is the book The Last Unicorn).
Linked Data rule 2 asks for HTTP IRIs: those are also URLs, so people can open them.
Browsers follow the WHATWG URL Standard, which calls all of these URLs; RDF specs use the RFC terms.
-->
