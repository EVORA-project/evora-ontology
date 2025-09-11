

# Slot: pathogen name (pathogenName) 


_A pathogen common name or a name that describes a group of pathogens_





URI: [EVORAO:pathogenName](https://w3id.org/evorao/pathogenName)
Alias: pathogenName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PathogenIdentification](PathogenIdentification.md) | A collection of distinguishing information that enables the differentiation o... |  yes  |







## Properties

* Range: [CommonName](CommonName.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:pathogenName |
| native | EVORAO:pathogenName |
| exact | dwc:organismName |




## LinkML Source

<details>
```yaml
name: pathogenName
description: A pathogen common name or a name that describes a group of pathogens
title: pathogen name
from_schema: https://w3id.org/evorao/
exact_mappings:
- dwc:organismName
rank: 1000
alias: pathogenName
domain_of:
- PathogenIdentification
range: CommonName
required: true
multivalued: false

```
</details>