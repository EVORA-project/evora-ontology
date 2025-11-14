

# Slot: keywords (keywords) 


_List of terms used to tag and categorize this Item._





URI: [EVORAO:keywords](https://w3id.org/evorao/keywords)
Alias: keywords

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |







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
| exact | schema:keywords |
| close | dcat:keyword |




## LinkML Source

<details>
```yaml
name: keywords
description: List of terms used to tag and categorize this Item.
title: keywords
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:keywords
close_mappings:
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