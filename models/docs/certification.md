

# Slot: certification (certification) 


_Any certification related to the current product or service; e.g., ISO certification_





URI: [EVORAO:certification](https://w3id.org/evorao/certification)
Alias: certification

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
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Product](Product.md) | A product |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |







## Properties

* Range: [Certification](Certification.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:certification |
| native | EVORAO:certification |
| close | dct:conformsTo |




## LinkML Source

<details>
```yaml
name: certification
description: Any certification related to the current product or service; e.g., ISO
  certification
title: certification
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:conformsTo
rank: 1000
alias: certification
domain_of:
- ProductOrService
range: Certification
required: false
multivalued: true

```
</details>