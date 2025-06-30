

# Slot: keywords (keywords) 


_List of terms used to tag and categorize this Item_





URI: [EVORAO:keywords](https://w3id.org/evorao/keywords)
Alias: keywords

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | A service |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |







## Properties

* Range: [Keyword](Keyword.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:keywords |
| native | EVORAO:keywords |
| exact | dcat:keyword |




## LinkML Source

<details>
```yaml
name: keywords
description: List of terms used to tag and categorize this Item
title: keywords
from_schema: https://w3id.org/evorao/
exact_mappings:
- dcat:keyword
rank: 1000
alias: keywords
domain_of:
- ProductOrService
range: Keyword
required: true
recommended: true
multivalued: true

```
</details>