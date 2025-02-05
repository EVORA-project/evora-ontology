

# Slot: external equivalent taxon (externalEquivalentTaxon)


_Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI)_





URI: [EVORAO:externalEquivalentTaxon](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#externalEquivalentTaxon)



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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:externalEquivalentTaxon |
| native | EVORAO:externalEquivalentTaxon |
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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dwc:taxonID
rank: 1000
alias: externalEquivalentTaxon
domain_of:
- Taxon
range: Taxon
required: false
multivalued: true

```
</details>