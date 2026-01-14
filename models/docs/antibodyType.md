

# Slot: antibody type (antibodyType) 


_The specification of the class of antibody based on its production method or biological origin. Expected values are "Polyclonal", "Monoclonal" or "Serum"_





URI: [EVORAO:antibodyType](https://w3id.org/evorao/antibodyType)
Alias: antibodyType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:antibodyType |
| native | EVORAO:antibodyType |
| related | bao:0000503, bao:0000507 |




## LinkML Source

<details>
```yaml
name: antibodyType
description: The specification of the class of antibody based on its production method
  or biological origin. Expected values are "Polyclonal", "Monoclonal" or "Serum"
title: antibody type
from_schema: https://w3id.org/evorao/
related_mappings:
- bao:0000503
- bao:0000507
rank: 1000
alias: antibodyType
domain_of:
- Antibody
range: string
required: false
recommended: true
multivalued: false
equals_string_in:
- Monoclonal
- Polyclonal
- Serum

```
</details>