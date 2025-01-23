

# Slot: contactPoint



URI: [EVORAO:contactPoint](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#contactPoint)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Service](Service.md) | A service |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [RI](RI.md) | A research infrastructure |  no  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Person](Person.md) | An individual |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:contactPoint |
| native | EVORAO:contactPoint |




## LinkML Source

<details>
```yaml
name: contactPoint
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: contactPoint
domain_of:
- PersonOrOrganization
- ProductOrService
range: string

```
</details>