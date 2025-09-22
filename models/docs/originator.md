

# Slot: originator (originator) 


_The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample_





URI: [EVORAO:originator](https://w3id.org/evorao/originator)
Alias: originator

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

* Range: [Originator](Originator.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:originator |
| native | EVORAO:originator |
| close | dct:provenance |




## LinkML Source

<details>
```yaml
name: originator
description: The individual or organization responsible for the original discovery,
  isolation, or creation of an item, providing information about the source or origin
  of the sample
title: originator
from_schema: https://w3id.org/evorao/
close_mappings:
- dct:provenance
rank: 1000
alias: originator
domain_of:
- Product
range: Originator
required: false
multivalued: false

```
</details>