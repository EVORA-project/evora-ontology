

# Slot: member of RI (memberOfRi) 


_The research infrastructure of which this organization is a member._





URI: [EVORAO:memberOfRi](https://w3id.org/evorao/memberOfRi)
Alias: memberOfRi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  yes  |







## Properties

* Range: [ReasearchInfrastructure](ReasearchInfrastructure.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:memberOfRi |
| native | EVORAO:memberOfRi |
| broad | schema:memberOf |




## LinkML Source

<details>
```yaml
name: memberOfRi
description: The research infrastructure of which this organization is a member.
title: member of RI
from_schema: https://w3id.org/evorao/
broad_mappings:
- schema:memberOf
rank: 1000
alias: memberOfRi
domain_of:
- Provider
range: ReasearchInfrastructure
required: false
multivalued: true

```
</details>