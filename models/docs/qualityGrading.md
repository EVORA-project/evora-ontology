

# Slot: quality grading (qualityGrading) 


_Information that permits to assess the quality level of what will be provided_





URI: [EVORAO:qualityGrading](https://w3id.org/evorao/qualityGrading)
Alias: qualityGrading

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | A service |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A product |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:qualityGrading |
| native | EVORAO:qualityGrading |




## LinkML Source

<details>
```yaml
name: qualityGrading
description: Information that permits to assess the quality level of what will be
  provided
title: quality grading
from_schema: https://w3id.org/evorao/
rank: 1000
alias: qualityGrading
domain_of:
- ProductOrService
range: string
required: false
multivalued: false

```
</details>