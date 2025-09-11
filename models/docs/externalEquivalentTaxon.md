

# Slot: external equivalent taxon (externalEquivalentTaxon) 


_Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI)_





URI: [EVORAO:externalEquivalentTaxon](https://w3id.org/evorao/externalEquivalentTaxon)
Alias: externalEquivalentTaxon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [Taxon](Taxon.md)

* Multivalued: True





## Comments

* Could serve as a bridge between ICTV and NCBI as several providers currently uses NCBI Taxonomy

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:externalEquivalentTaxon |
| native | EVORAO:externalEquivalentTaxon |
| related | dct:references |
| close | dwc:taxonID |




## LinkML Source

<details>
```yaml
name: externalEquivalentTaxon
description: Any equivalent taxon in a different taxonomy if exists/known to serve
  as a bridge (e.g, ICTV towards NCBI)
title: external equivalent taxon
comments:
- Could serve as a bridge between ICTV and NCBI as several providers currently uses
  NCBI Taxonomy
from_schema: https://w3id.org/evorao/
close_mappings:
- dwc:taxonID
related_mappings:
- dct:references
rank: 1000
alias: externalEquivalentTaxon
domain_of:
- Taxon
range: Taxon
required: false
multivalued: true

```
</details>