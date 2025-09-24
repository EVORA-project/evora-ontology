

# Slot: unit cost note (unitCostNote) 


_A free-text note describing special conditions or cases where the cost cannot be represented by a numerical value (e.g., on request, free for academics, depends on volume)_





URI: [EVORAO:unitCostNote](https://w3id.org/evorao/unitCostNote)
Alias: unitCostNote

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:unitCostNote |
| native | EVORAO:unitCostNote |




## LinkML Source

<details>
```yaml
name: unitCostNote
description: A free-text note describing special conditions or cases where the cost
  cannot be represented by a numerical value (e.g., on request, free for academics,
  depends on volume)
title: unit cost note
from_schema: https://w3id.org/evorao/
rank: 1000
alias: unitCostNote
domain_of:
- ProductOrService
range: string
required: false
multivalued: false

```
</details>