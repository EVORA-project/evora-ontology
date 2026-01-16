

# Slot: unit definition (unitDefinition) 


_A short description of what will be delivered by ordering one unit of this item._





URI: [EVORAO:unitDefinition](https://w3id.org/evorao/unitDefinition)
Alias: unitDefinition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Comments

* The description of what will be delivered to the end-user (e.g.: packaging, quantity...).

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:unitDefinition |
| native | EVORAO:unitDefinition |
| related | dct:format |




## LinkML Source

<details>
```yaml
name: unitDefinition
description: A short description of what will be delivered by ordering one unit of
  this item.
title: unit definition
comments:
- 'The description of what will be delivered to the end-user (e.g.: packaging, quantity...).'
from_schema: https://w3id.org/evorao/
related_mappings:
- dct:format
rank: 1000
alias: unitDefinition
domain_of:
- ProductOrService
range: string
required: false
recommended: true
multivalued: false

```
</details>