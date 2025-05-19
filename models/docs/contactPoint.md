

# Slot: contact point (contactPoint) 


_An information that allows someone to establish communication_





URI: [EVORAO:contactPoint](https://w3id.org/evorao/contactPoint)
Alias: contactPoint

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RI](RI.md) | A research infrastructure |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Service](Service.md) | A service |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Person](Person.md) | An individual |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Virus](Virus.md) | The virus as a biological material |  no  |







## Properties

* Range: [ContactPoint](ContactPoint.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:contactPoint |
| native | EVORAO:contactPoint |
| exact | dcat:contactPoint |




## LinkML Source

<details>
```yaml
name: contactPoint
description: An information that allows someone to establish communication
title: contact point
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:contactPoint
rank: 1000
alias: contactPoint
domain_of:
- PersonOrOrganization
- ProductOrService
range: ContactPoint
required: false
recommended: true
multivalued: false

```
</details>