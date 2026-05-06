

# Slot: taxonomic node ID (taxonomicNodeId) 


_Identifier for the taxonomic node, unique to this taxon within the specific taxonomy release/version._





URI: [EVORAO:taxonomicNodeId](https://w3id.org/evorao/taxonomicNodeId)
Alias: taxonomicNodeId


## Inheritance

* [identifier](identifier.md)
    * **taxonomicNodeId**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) | Conceptual entity that groups one or more populations of an organism or organ... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Recommended: True





## Comments

* NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in ICTV= Key of the taxon node!

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:taxonomicNodeId |
| native | EVORAO:taxonomicNodeId |
| broad | dct:identifier |
| close | dwc:taxonID |




## LinkML Source

<details>
```yaml
name: taxonomicNodeId
description: Identifier for the taxonomic node, unique to this taxon within the specific
  taxonomy release/version.
title: taxonomic node ID
comments:
- NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in
  ICTV= Key of the taxon node!
from_schema: https://w3id.org/evorao/
close_mappings:
- dwc:taxonID
broad_mappings:
- dct:identifier
rank: 1000
is_a: identifier
alias: taxonomicNodeId
domain_of:
- Taxon
range: string
required: false
recommended: true
multivalued: true

```
</details>