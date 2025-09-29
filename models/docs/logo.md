

# Slot: logo (logo) 


_A path or URL to the related logo_





URI: [EVORAO:logo](https://w3id.org/evorao/logo)
Alias: logo

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |
| [Person](Person.md) | An individual |  no  |
| [ReasearchInfrastructure](ReasearchInfrastructure.md) | A research infrastructure (RI) |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |







## Properties

* Range: [Image](Image.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:logo |
| native | EVORAO:logo |
| exact | schema:logo |




## LinkML Source

<details>
```yaml
name: logo
description: A path or URL to the related logo
title: logo
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:logo
rank: 1000
alias: logo
domain_of:
- PersonOrOrganization
- License
- Certification
range: Image
required: false
multivalued: false

```
</details>