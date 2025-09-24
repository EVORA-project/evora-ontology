

# Slot: contact point (contactPoint) 


_An information that allows someone to establish communication_





URI: [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)
Alias: contactPoint


## Inheritance

* **contactPoint**
    * [materialSafetyContact](materialSafetyContact.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Person](Person.md) | An individual |  no  |
| [ReasearchInfrastructure](ReasearchInfrastructure.md) | A research infrastructure (RI) |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |







## Properties

* Range: [ContactPoint](ContactPoint.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:contactPoint |
| native | EVORAO:contactPoint |
| exact | schema:contactPoint |




## LinkML Source

<details>
```yaml
name: contactPoint
description: An information that allows someone to establish communication
title: contact point
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:contactPoint
rank: 1000
slot_uri: dcat:contactPoint
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