

# Slot: collection (collection) 


_The collection(s) to which belongs this item_





URI: [EVORAO:collection](https://w3id.org/evorao/collection)
Alias: collection

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [Collection](Collection.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:collection |
| native | EVORAO:collection |




## LinkML Source

<details>
```yaml
name: collection
description: The collection(s) to which belongs this item
title: collection
from_schema: https://w3id.org/evorao/
rank: 1000
alias: collection
domain_of:
- ProductOrService
range: Collection
required: true
multivalued: true

```
</details>