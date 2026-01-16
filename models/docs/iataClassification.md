

# Slot: IATA classification (iataClassification) 


_The corresponding International Air Transport Association (IATA)'s category for this Product._





URI: [EVORAO:iataClassification](https://w3id.org/evorao/iataClassification)
Alias: iataClassification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  yes  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |







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
  for this Product.
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