

# Slot: additional category (additionalCategory) 


_Any category apart from its main category in which this product or service can fit_





URI: [EVORAO:additionalCategory](https://w3id.org/evorao/additionalCategory)
Alias: additionalCategory


## Inheritance

* [category](category.md)
    * **additionalCategory**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [ProductCategory](ProductCategory.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:additionalCategory |
| native | EVORAO:additionalCategory |
| close | schema:additionalType |




## LinkML Source

<details>
```yaml
name: additionalCategory
description: Any category apart from its main category in which this product or service
  can fit
title: additional category
from_schema: https://w3id.org/evorao/
close_mappings:
- schema:additionalType
rank: 1000
is_a: category
alias: additionalCategory
domain_of:
- ProductOrService
range: ProductCategory
required: true
recommended: true
multivalued: true

```
</details>