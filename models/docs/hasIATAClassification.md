

# Slot: IATA classification (hasIATAClassification) 


_The corresponding International Air Transport Association (IATA)'s category for this Product_





URI: [EVORAO:hasIATAClassification](https://w3id.org/evorao/hasIATAClassification)
Alias: hasIATAClassification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Product](Product.md) | A product |  yes  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
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

* Range: [IATAClassification](IATAClassification.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:hasIATAClassification |
| native | EVORAO:hasIATAClassification |




## LinkML Source

<details>
```yaml
name: hasIATAClassification
description: The corresponding International Air Transport Association (IATA)'s category
  for this Product
title: IATA classification
from_schema: https://w3id.org/evorao/
rank: 1000
alias: hasIATAClassification
domain_of:
- Product
range: IATAClassification
required: true
multivalued: false

```
</details>