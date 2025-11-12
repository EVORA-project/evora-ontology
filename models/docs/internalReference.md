

# Slot: internal reference (internalReference) 


_Any reference or indication to be used for local retrieval purpose._





URI: [EVORAO:internalReference](https://w3id.org/evorao/internalReference)
Alias: internalReference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:internalReference |
| native | EVORAO:internalReference |
| broad | dct:references |




## LinkML Source

<details>
```yaml
name: internalReference
description: Any reference or indication to be used for local retrieval purpose.
title: internal reference
from_schema: https://w3id.org/evorao/
broad_mappings:
- dct:references
rank: 1000
alias: internalReference
domain_of:
- ProductOrService
range: string
required: false
multivalued: false

```
</details>