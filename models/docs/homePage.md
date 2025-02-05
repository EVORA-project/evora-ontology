

# Slot: home page (homePage)


_A web page that serves as the main or introductory page_





URI: [EVORAO:homePage](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#homePage)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [RI](RI.md) | A research infrastructure |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Person](Person.md) | An individual |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |







## Properties

* Range: [Uri](Uri.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:homePage |
| native | EVORAO:homePage |




## LinkML Source

<details>
```yaml
name: homePage
description: A web page that serves as the main or introductory page
title: home page
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: homePage
domain_of:
- PersonOrOrganization
range: uri
required: false
multivalued: false

```
</details>