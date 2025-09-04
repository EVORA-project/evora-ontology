

# Slot: DOI (doi) 


_A Digital Object Identifier (DOI) that can be related_





URI: [EVORAO:doi](https://w3id.org/evorao/doi)
Alias: doi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Publication](Publication.md) | A scientific publication |  yes  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [Doi](Doi.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:doi |
| native | EVORAO:doi |
| close | wdp:P356 |




## LinkML Source

<details>
```yaml
name: doi
description: A Digital Object Identifier (DOI) that can be related
title: DOI
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P356
rank: 1000
alias: doi
domain_of:
- Publication
- ProductOrService
range: Doi
required: false
multivalued: true

```
</details>