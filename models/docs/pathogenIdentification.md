

# Slot: pathogen identification (pathogenIdentification) 


_The identification of the pathogen or group of pathogens (e.g; name, taxon identification, etc.) related to the current item._





URI: [EVORAO:pathogenIdentification](https://w3id.org/evorao/pathogenIdentification)
Alias: pathogenIdentification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |







## Properties

* Range: [PathogenIdentification](PathogenIdentification.md)

* Multivalued: True

* Required: True





## Comments

* The pathogen identification contains information about name and taxon but in some cases(e.g: FAIRSHARING) there may have no direct pathogen related but simply a taxonomic information .... the default value should be the root of virology: Viruses

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:pathogenIdentification |
| native | EVORAO:pathogenIdentification |




## LinkML Source

<details>
```yaml
name: pathogenIdentification
description: The identification of the pathogen or group of pathogens (e.g; name,
  taxon identification, etc.) related to the current item.
title: pathogen identification
comments:
- 'The pathogen identification contains information about name and taxon but in some
  cases(e.g: FAIRSHARING) there may have no direct pathogen related but simply a taxonomic
  information .... the default value should be the root of virology: Viruses'
from_schema: https://w3id.org/evorao/
rank: 1000
alias: pathogenIdentification
domain_of:
- ProductOrService
range: PathogenIdentification
required: true
multivalued: true

```
</details>