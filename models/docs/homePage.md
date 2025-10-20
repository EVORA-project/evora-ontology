

# Slot: home page (homePage) 


_A web page that serves as the main or introductory page_





URI: [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)
Alias: homePage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [ReasearchInfrastructure](ReasearchInfrastructure.md) | A research infrastructure (RI) |  no  |
| [Person](Person.md) | An individual |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |







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
| close | swo:0004006 |




## LinkML Source

<details>
```yaml
name: homePage
description: A web page that serves as the main or introductory page
title: home page
from_schema: https://w3id.org/evorao/
close_mappings:
- swo:0004006
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