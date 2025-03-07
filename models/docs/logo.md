

# Slot: logo (logo)


_A path or URL to the related logo_





URI: [EVORAO:logo](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#logo)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Certification](Certification.md) | Assurance given by an independent certification body that a product, service ... |  yes  |
| [RI](RI.md) | A research infrastructure |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [License](License.md) | The legal terms and conditions under which the subject can be used, shared, o... |  yes  |
| [Person](Person.md) | An individual |  no  |







## Properties

* Range: [Image](Image.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:logo |
| native | EVORAO:logo |




## LinkML Source

<details>
```yaml
name: logo
description: A path or URL to the related logo
title: logo
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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