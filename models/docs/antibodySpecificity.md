

# Slot: antibody specificity (antibodySpecificity) 


_Information describing the molecular or antigenic specificity of the antibody, including its recognized target(s), cross-reactivity with related antigens, and any contextual information supporting its selectivity._





URI: [EVORAO:antibodySpecificity](https://w3id.org/evorao/antibodySpecificity)
Alias: antibodySpecificity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:antibodySpecificity |
| native | EVORAO:antibodySpecificity |




## LinkML Source

<details>
```yaml
name: antibodySpecificity
description: Information describing the molecular or antigenic specificity of the
  antibody, including its recognized target(s), cross-reactivity with related antigens,
  and any contextual information supporting its selectivity.
title: antibody specificity
from_schema: https://w3id.org/evorao/
rank: 1000
alias: antibodySpecificity
domain_of:
- Antibody
range: string
required: false
multivalued: false

```
</details>