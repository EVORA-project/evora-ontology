

# Slot: additional category (additionalCategory) 


_Any category apart from its main category in which this product or service can fit_





URI: [EVORAO:additionalCategory](https://w3id.org/evorao/additionalCategory)
Alias: additionalCategory

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Service](Service.md) | A service |  no  |
| [Product](Product.md) | A product |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |







## Properties

* Range: [ProductCategory](ProductCategory.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:additionalCategory |
| native | EVORAO:additionalCategory |
| exact | dcat:theme |




## LinkML Source

<details>
```yaml
name: additionalCategory
description: Any category apart from its main category in which this product or service
  can fit
title: additional category
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:theme
rank: 1000
alias: additionalCategory
domain_of:
- ProductOrService
range: ProductCategory
required: false
recommended: true
multivalued: true

```
</details>