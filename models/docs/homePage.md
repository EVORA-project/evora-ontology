

# Slot: home page (homePage) 


_A web page that serves as the main or introductory page_





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
Alias: homePage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Person](Person.md) | An individual |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [RI](RI.md) | A research infrastructure |  no  |







## Properties

* Range: [Uri](Uri.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:homepage |
| native | EVORAO:homePage |




## LinkML Source

<details>
```yaml
name: homePage
description: A web page that serves as the main or introductory page
title: home page
from_schema: https://w3id.org/evorao/
rank: 1000
slot_uri: foaf:homepage
alias: homePage
domain_of:
- PersonOrOrganization
range: uri
required: false
multivalued: false

```
</details>