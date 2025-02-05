

# Slot: co-infecting viruses (coInfectingViruses)


_Identifies other viruses that may co-infect the host organism along with the primary virus, indicating the presence of multiple viral infections within the same host._





URI: [EVORAO:coInfectingViruses](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#coInfectingViruses)



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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: coInfectingViruses
domain_of:
- Virus
range: VirusName
required: false
multivalued: true

```
</details>