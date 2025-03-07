

# Slot: ORCID iD (oRCIDiD)


_Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation_





URI: [EVORAO:oRCIDiD](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#oRCIDiD)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | An individual |  yes  |
| [ContactPoint](ContactPoint.md) | Entity serving as focal point of information |  yes  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:oRCIDiD |
| native | EVORAO:oRCIDiD |
| exact | wdp:P496, IAO:0000708 |




## LinkML Source

<details>
```yaml
name: oRCIDiD
description: Unique persistent identifier for a person, provided by the Open Researcher
  and Contributor ID (ORCID) organisation
title: ORCID iD
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- wdp:P496
- IAO:0000708
rank: 1000
alias: oRCIDiD
domain_of:
- Person
- ContactPoint
range: string
required: false
recommended: true
multivalued: false

```
</details>