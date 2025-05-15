

# Slot: availability (availability) 


_The state or condition in which this item is accessible and ready for use or can be obtained_





URI: [EVORAO:availability](https://w3id.org/evorao/availability)
Alias: availability

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Product](Product.md) | A product |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Service](Service.md) | A service |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* Possible availabilities may differ from a project to another

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:availability |
| native | EVORAO:availability |




## LinkML Source

<details>
```yaml
name: availability
description: The state or condition in which this item is accessible and ready for
  use or can be obtained
title: availability
comments:
- Possible availabilities may differ from a project to another
from_schema: https://w3id.org/evorao/
rank: 1000
ifabsent: string(on request)
alias: availability
domain_of:
- ProductOrService
range: string
required: true
multivalued: false

```
</details>