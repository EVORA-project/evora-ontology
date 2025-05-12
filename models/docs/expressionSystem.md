

# Slot: expression system (expressionSystem) 


_The host organism or cellular environment used to produce a protein from a specific gene. Possible values include 'E. coli' (bacterial system), 'Insect cells' (using baculovirus vectors), and 'Mammalian cells' (mammalian cell lines)._





URI: [EVORAO:expressionSystem](https://w3id.org/evorao/expressionSystem)
Alias: expressionSystem

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
| self | EVORAO:expressionSystem |
| native | EVORAO:expressionSystem |




## LinkML Source

<details>
```yaml
name: expressionSystem
description: The host organism or cellular environment used to produce a protein from
  a specific gene. Possible values include 'E. coli' (bacterial system), 'Insect cells'
  (using baculovirus vectors), and 'Mammalian cells' (mammalian cell lines).
title: expression system
from_schema: https://w3id.org/evorao/
rank: 1000
alias: expressionSystem
domain_of:
- Protein
range: string
required: false
multivalued: true
equals_string_in:
- E. coli
- Insect cells
- Mammalian cells

```
</details>