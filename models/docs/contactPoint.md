

# Slot: contactPoint



URI: [EVORA:contactPoint](https://evora-project.eu/contactPoint)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Organization](Organization.md) | A social entity established to meet needs or pursue specific goals |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [PersonOrOrganization](PersonOrOrganization.md) | A person or an organization |  yes  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Person](Person.md) | An individual |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Provider](Provider.md) | A provider of products or services, as a specific organization |  no  |
| [Service](Service.md) | A service |  no  |
| [Originator](Originator.md) | The individual or organization responsible for the original discovery, isolat... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [RI](RI.md) | A research infrastructure |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:contactPoint |
| native | EVORA:contactPoint |




## LinkML Source

<details>
```yaml
name: contactPoint
from_schema: https://evora-project.eu/
rank: 1000
alias: contactPoint
domain_of:
- PersonOrOrganization
- ProductOrService
range: string

```
</details>