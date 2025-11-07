

# Slot: tag status of the solubilized protein (tagStatusOfTheSolubilizedProtein) 


_Indicates the presence and condition of a tag on the protein after solubilization. Possible values include 'Uncleaved Tag' (the tag is still attached to the protein), 'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein does not have a tag)._





URI: [EVORAO:tagStatusOfTheSolubilizedProtein](https://w3id.org/evorao/tagStatusOfTheSolubilizedProtein)
Alias: tagStatusOfTheSolubilizedProtein

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
| self | EVORAO:tagStatusOfTheSolubilizedProtein |
| native | EVORAO:tagStatusOfTheSolubilizedProtein |




## LinkML Source

<details>
```yaml
name: tagStatusOfTheSolubilizedProtein
description: Indicates the presence and condition of a tag on the protein after solubilization.
  Possible values include 'Uncleaved Tag' (the tag is still attached to the protein),
  'Cleaved Tag' (the tag has been removed from the protein), and 'No Tag' (the protein
  does not have a tag).
title: tag status of the solubilized protein
from_schema: https://w3id.org/evorao/
rank: 1000
alias: tagStatusOfTheSolubilizedProtein
domain_of:
- Protein
range: string
required: false
multivalued: true

```
</details>