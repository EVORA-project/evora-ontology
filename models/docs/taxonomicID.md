

# Slot: taxonomic ID (taxonomicID)


_The taxonomic identifier as a persistent identifier accross releases_





URI: [EVORAO:taxonomicID](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#taxonomicID)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxonomicID |
| native | EVORAO:taxonomicID |
| close | dwc:taxonID |




## LinkML Source

<details>
```yaml
name: taxonomicID
description: The taxonomic identifier as a persistent identifier accross releases
title: taxonomic ID
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- dwc:taxonID
rank: 1000
alias: taxonomicID
domain_of:
- Taxon
range: string
required: true
multivalued: false

```
</details>