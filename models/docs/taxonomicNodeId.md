

# Slot: taxonomic node ID (taxonomicNodeId) 


_The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy_





URI: [EVORAO:taxonomicNodeId](https://w3id.org/evorao/taxonomicNodeId)
Alias: taxonomicNodeId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Comments

* NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in ICTV= Key of the taxon node !! Could be replaced by a composite key made of 'taxonomic ID' + 'has version'

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxonomicNodeId |
| native | EVORAO:taxonomicNodeId |
| close | dwc:taxonID |




## LinkML Source

<details>
```yaml
name: taxonomicNodeId
description: The taxonomic_Node Identifier as an identifier specific the current taxon
  in the corresponding release/version of the taxonomy
title: taxonomic node ID
comments:
- NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in
  ICTV= Key of the taxon node !! Could be replaced by a composite key made of 'taxonomic
  ID' + 'has version'
from_schema: https://w3id.org/evorao/
close_mappings:
- dwc:taxonID
rank: 1000
alias: taxonomicNodeId
domain_of:
- Taxon
range: string
required: false
recommended: true
multivalued: false

```
</details>