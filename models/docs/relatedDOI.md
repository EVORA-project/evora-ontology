

# Slot: DOI (relatedDOI) 


_Any Digital Object Identifier that can be related_





URI: [EVORAO:relatedDOI](https://w3id.org/evorao/relatedDOI)
Alias: relatedDOI

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Service](Service.md) | A service |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Publication](Publication.md) | A scientific publication |  yes  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Product](Product.md) | A product |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [DOI](DOI.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:relatedDOI |
| native | EVORAO:relatedDOI |
| close | wdp:P356 |




## LinkML Source

<details>
```yaml
name: relatedDOI
description: Any Digital Object Identifier that can be related
title: DOI
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P356
rank: 1000
alias: relatedDOI
domain_of:
- Publication
- ProductOrService
range: DOI
required: false
multivalued: true

```
</details>