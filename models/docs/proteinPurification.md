

# Slot: protein purification (proteinPurification) 


_Refers to the degree of purity achieved for a protein sample. Possible values include '>95%' (the protein is highly purified, with more than 95% purity) and 'Unpurified expression host lysate or partly purified protein' (the protein is either unpurified and present in the host cell lysate or only partially purified)._





URI: [EVORAO:proteinPurification](https://w3id.org/evorao/proteinPurification)
Alias: proteinPurification

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
| self | EVORAO:proteinPurification |
| native | EVORAO:proteinPurification |




## LinkML Source

<details>
```yaml
name: proteinPurification
description: Refers to the degree of purity achieved for a protein sample. Possible
  values include '>95%' (the protein is highly purified, with more than 95% purity)
  and 'Unpurified expression host lysate or partly purified protein' (the protein
  is either unpurified and present in the host cell lysate or only partially purified).
title: protein purification
from_schema: https://w3id.org/evorao/
rank: 1000
alias: proteinPurification
domain_of:
- Protein
range: string
required: false
multivalued: true
equals_string_in:
- Greater than 95 percent
- Unpurified expression host lysate or partly purified protein

```
</details>