

# Slot: can be used to produce GMO (canBeUsedToProduceGmo) 


_Indicates if the current service or product can be used to produce GMO._





URI: [EVORAO:canBeUsedToProduceGmo](https://w3id.org/evorao/canBeUsedToProduceGmo)
Alias: canBeUsedToProduceGmo

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |







## Properties

* Range: [Boolean](Boolean.md)

* Required: True





## Comments

* Set to TRUE if it can produce GMO.
* It is recommended to have a value for this field, no value will be understood as unknown.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:canBeUsedToProduceGmo |
| native | EVORAO:canBeUsedToProduceGmo |
| broad | schema:potentialUse |




## LinkML Source

<details>
```yaml
name: canBeUsedToProduceGmo
description: Indicates if the current service or product can be used to produce GMO.
title: can be used to produce GMO
comments:
- Set to TRUE if it can produce GMO.
- It is recommended to have a value for this field, no value will be understood as
  unknown.
from_schema: https://w3id.org/evorao/
broad_mappings:
- schema:potentialUse
rank: 1000
alias: canBeUsedToProduceGmo
domain_of:
- ProductOrService
range: boolean
required: true
recommended: true
multivalued: false

```
</details>