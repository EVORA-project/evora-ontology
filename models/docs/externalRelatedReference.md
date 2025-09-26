

# Slot: external related reference (externalRelatedReference) 


_A reference that permits to retrieve another related item from an external provider_





URI: [EVORAO:externalRelatedReference](https://w3id.org/evorao/externalRelatedReference)
Alias: externalRelatedReference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [ExternalRelatedReference](ExternalRelatedReference.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:externalRelatedReference |
| native | EVORAO:externalRelatedReference |
| broad | dct:references |




## LinkML Source

<details>
```yaml
name: externalRelatedReference
description: A reference that permits to retrieve another related item from an external
  provider
title: external related reference
from_schema: https://w3id.org/evorao/
broad_mappings:
- dct:references
rank: 1000
alias: externalRelatedReference
domain_of:
- ProductOrService
range: ExternalRelatedReference
required: false
multivalued: true

```
</details>