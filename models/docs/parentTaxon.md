

# Slot: parent taxon (parentTaxon)


_The parent taxon of the current taxon_





URI: [EVORAO:parentTaxon](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#parentTaxon)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [Taxon](Taxon.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:parentTaxon |
| native | EVORAO:parentTaxon |
| close | dwc:Taxon |




## LinkML Source

<details>
```yaml
name: parentTaxon
description: The parent taxon of the current taxon
title: parent taxon
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dwc:Taxon
rank: 1000
alias: parentTaxon
domain_of:
- Taxon
range: Taxon
required: true
multivalued: false

```
</details>