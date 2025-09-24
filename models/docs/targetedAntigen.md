

# Slot: targeted antigen (targetedAntigen) 


_Specific molecular structure or epitope recognized and bound by an antibody_





URI: [EVORAO:targetedAntigen](https://w3id.org/evorao/targetedAntigen)
Alias: targetedAntigen

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:targetedAntigen |
| native | EVORAO:targetedAntigen |




## LinkML Source

<details>
```yaml
name: targetedAntigen
description: Specific molecular structure or epitope recognized and bound by an antibody
title: targeted antigen
from_schema: https://w3id.org/evorao/
rank: 1000
alias: targetedAntigen
domain_of:
- Antibody
range: string
required: true
multivalued: false

```
</details>