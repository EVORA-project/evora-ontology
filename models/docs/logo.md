

# Slot: logo (logo) 


_A path or URL to the related logo._





URI: [EVORAO:logo](https://w3id.org/evorao/logo)
Alias: logo

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ResearchInfrastructure](ResearchInfrastructure.md) | A research infrastructure (RI) |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [FundingSource](FundingSource.md) | A program, grant, or project providing financial support for the access or us... |  yes  |
| [Person](Person.md) | An individual |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |







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
description: A path or URL to the related logo.
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
- FundingSource
range: Image
required: false
multivalued: false

```
</details>