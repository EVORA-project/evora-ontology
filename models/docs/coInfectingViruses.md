

# Slot: co-infecting viruses (coInfectingViruses) 


_Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host._





URI: [EVORAO:coInfectingViruses](https://w3id.org/evorao/coInfectingViruses)
Alias: coInfectingViruses

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  yes  |







## Properties

* Range: [VirusName](VirusName.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:coInfectingViruses |
| native | EVORAO:coInfectingViruses |




## LinkML Source

<details>
```yaml
name: coInfectingViruses
description: Identifies other viruses that may co-infect the host organism along with
  the primary virus, indicating the presence of multiple viral infections within the
  same host.
title: co-infecting viruses
from_schema: https://w3id.org/evorao/
rank: 1000
alias: coInfectingViruses
domain_of:
- Virus
range: VirusName
required: false
multivalued: true

```
</details>