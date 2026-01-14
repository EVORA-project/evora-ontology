

# Slot: biosafety restrictions (biosafetyRestrictions) 


_Information about guidelines and regulations designed to prevent the exposure to or release of potentially harmful biological agents. It thereby contributes to protecting people and the environment from biohazards while accessing this product or service._





URI: [EVORAO:biosafetyRestrictions](https://w3id.org/evorao/biosafetyRestrictions)
Alias: biosafetyRestrictions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:biosafetyRestrictions |
| native | EVORAO:biosafetyRestrictions |
| related | bao:0002826, wdp:P12663, wdp:P1604 |




## LinkML Source

<details>
```yaml
name: biosafetyRestrictions
description: Information about guidelines and regulations designed to prevent the
  exposure to or release of potentially harmful biological agents. It thereby contributes
  to protecting people and the environment from biohazards while accessing this product
  or service.
title: biosafety restrictions
from_schema: https://w3id.org/evorao/
related_mappings:
- bao:0002826
- wdp:P12663
- wdp:P1604
rank: 1000
alias: biosafetyRestrictions
domain_of:
- ProductOrService
range: string
required: false
multivalued: false

```
</details>