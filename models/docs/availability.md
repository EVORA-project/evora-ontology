

# Slot: availability (availability) 


_The state or condition in which this item is accessible and ready for use or can be obtained._





URI: [EVORAO:availability](https://w3id.org/evorao/availability)
Alias: availability

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* Possible availabilities may differ from a project to another.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:availability |
| native | EVORAO:availability |
| close | schema:availability, dct:available |




## LinkML Source

<details>
```yaml
name: availability
description: The state or condition in which this item is accessible and ready for
  use or can be obtained.
title: availability
comments:
- Possible availabilities may differ from a project to another.
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:availability
- dct:available
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