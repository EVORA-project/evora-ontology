

# Slot: product picture (productPicture) 


_A picture that can represent the item_





URI: [EVORAO:productPicture](https://w3id.org/evorao/productPicture)
Alias: productPicture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Service](Service.md) | A service |  no  |







## Properties

* Range: [Image](Image.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:productPicture |
| native | EVORAO:productPicture |




## LinkML Source

<details>
```yaml
name: productPicture
description: A picture that can represent the item
title: product picture
from_schema: https://w3id.org/evorao/
rank: 1000
alias: productPicture
domain_of:
- ProductOrService
range: Image
required: false
multivalued: true

```
</details>