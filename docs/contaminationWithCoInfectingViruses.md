

# Slot: contamination with co-infecting viruses (contaminationWithCoInfectingViruses) 


_Indicates whether the sample contains contamination with co-infecting viruses. Possible values are ‘Not tested’, ‘Contaminated’, and ‘No contamination detected’._





URI: [EVORAO:contaminationWithCoInfectingViruses](https://w3id.org/evorao/contaminationWithCoInfectingViruses)
Alias: contaminationWithCoInfectingViruses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Comments

* When it can be assessed, it is recommended to indicate whether contamination with co-infecting viruses was detected or if the test was not performed.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:contaminationWithCoInfectingViruses |
| native | EVORAO:contaminationWithCoInfectingViruses |




## LinkML Source

<details>
```yaml
name: contaminationWithCoInfectingViruses
description: Indicates whether the sample contains contamination with co-infecting
  viruses. Possible values are ‘Not tested’, ‘Contaminated’, and ‘No contamination
  detected’.
title: contamination with co-infecting viruses
comments:
- When it can be assessed, it is recommended to indicate whether contamination with
  co-infecting viruses was detected or if the test was not performed.
from_schema: https://w3id.org/evorao/
rank: 1000
alias: contaminationWithCoInfectingViruses
domain_of:
- Virus
range: string
required: false
recommended: true
multivalued: false
equals_string_in:
- Not tested
- Contaminated
- No contamination detected

```
</details>