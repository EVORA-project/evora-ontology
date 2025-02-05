

# Slot: contact point (contactPoint)


_An information that allows someone to establish communication_





URI: [EVORAO:contactPoint](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#contactPoint)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [RI](RI.md) | A research infrastructure |  no  |
| [Service](Service.md) | A service |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Product](Product.md) | A product |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Person](Person.md) | An individual |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |







## Properties

* Range: [ContactPoint](ContactPoint.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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