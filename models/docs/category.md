

# Slot: category (category) 


_The main category of the service or product_





URI: [EVORAO:category](https://w3id.org/evorao/category)
Alias: category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Product](Product.md) | A product |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Service](Service.md) | A service |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |







## Properties

* Range: [ProductCategory](ProductCategory.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:category |
| native | EVORAO:category |
| exact | dcat:theme |




## LinkML Source

<details>
```yaml
name: category
description: The main category of the service or product
title: category
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:theme
rank: 1000
alias: category
domain_of:
- ProductOrService
range: ProductCategory
required: true
multivalued: false

```
</details>