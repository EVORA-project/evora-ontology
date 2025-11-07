

# Slot: biosafety level (biosafetyLevel) 


_The level of biocontainment required or applied in the facility where the biological agent is manipulated._





URI: [EVORAO:biosafetyLevel](https://w3id.org/evorao/biosafetyLevel)
Alias: biosafetyLevel

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |







## Properties

* Range: [BiosafetyLevel](BiosafetyLevel.md)





## Comments

* The Biosafety Level (BSL) reflects the operational safety measures implemented, which may differ from the intrinsic risk defined by the agent’s Risk Group (RG).

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:biosafetyLevel |
| native | EVORAO:biosafetyLevel |
| exact | wdp:P1604, bao:0002826 |




## LinkML Source

<details>
```yaml
name: biosafetyLevel
description: The level of biocontainment required or applied in the facility where
  the biological agent is manipulated.
title: biosafety level
comments:
- The Biosafety Level (BSL) reflects the operational safety measures implemented,
  which may differ from the intrinsic risk defined by the agent’s Risk Group (RG).
from_schema: https://w3id.org/evorao/
exact_mappings:
- wdp:P1604
- bao:0002826
rank: 1000
alias: biosafetyLevel
domain_of:
- ProductOrService
range: BiosafetyLevel
required: false
multivalued: false

```
</details>