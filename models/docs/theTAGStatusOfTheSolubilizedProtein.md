

# Slot: TAG status of the solubilized protein (theTAGStatusOfTheSolubilizedProtein) 


_Indicates the presence and condition of a tag on the protein after solubilization. Possible values include 'Uncleaved Tag' (the tag is still attached to the protein), 'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein does not have a tag)_





URI: [EVORAO:theTAGStatusOfTheSolubilizedProtein](https://w3id.org/evorao/theTAGStatusOfTheSolubilizedProtein)
Alias: theTAGStatusOfTheSolubilizedProtein

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:theTAGStatusOfTheSolubilizedProtein |
| native | EVORAO:theTAGStatusOfTheSolubilizedProtein |




## LinkML Source

<details>
```yaml
name: theTAGStatusOfTheSolubilizedProtein
description: Indicates the presence and condition of a tag on the protein after solubilization.
  Possible values include 'Uncleaved Tag' (the tag is still attached to the protein),
  'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein
  does not have a tag)
title: TAG status of the solubilized protein
from_schema: https://w3id.org/evorao/
rank: 1000
alias: theTAGStatusOfTheSolubilizedProtein
domain_of:
- Protein
range: string
required: false
multivalued: true

```
</details>