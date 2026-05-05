

# Slot: parent taxon (parentTaxon) 


_The parent taxon of the current taxon._





URI: [EVORAO:parentTaxon](https://w3id.org/evorao/parentTaxon)
Alias: parentTaxon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [Taxon](Taxon.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:parentTaxon |
| native | EVORAO:parentTaxon |
| exact | schema:parentTaxon |
| broad | dwc:Taxon |
| close | wdp:P171 |




## LinkML Source

<details>
```yaml
name: parentTaxon
description: The parent taxon of the current taxon.
title: parent taxon
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:parentTaxon
close_mappings:
- wdp:P171
broad_mappings:
- dwc:Taxon
rank: 1000
alias: parentTaxon
domain_of:
- Taxon
range: Taxon
required: false
recommended: true
multivalued: false

```
</details>