

# Slot: IATA classification (iataClassification) 


_The corresponding International Air Transport Association (IATA)'s category for this Product_





URI: [EVORAO:iataClassification](https://w3id.org/evorao/iataClassification)
Alias: iataClassification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  yes  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |







## Properties

* Range: [IataClassification](IataClassification.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:iataClassification |
| native | EVORAO:iataClassification |
| close | wdp:P238, schema:iataCode |




## LinkML Source

<details>
```yaml
name: iataClassification
description: The corresponding International Air Transport Association (IATA)'s category
  for this Product
title: IATA classification
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P238
- schema:iataCode
rank: 1000
alias: iataClassification
domain_of:
- Product
range: IataClassification
required: true
multivalued: false

```
</details>