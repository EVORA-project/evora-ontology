

# Slot: funding source (fundingSource) 


_A program, grant, or project providing financial support for the access or use of the product or service, either fully or partially._





URI: [EVORAO:fundingSource](https://w3id.org/evorao/fundingSource)
Alias: fundingSource

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |







## Properties

* Range: [FundingSource](FundingSource.md)

* Multivalued: True





## Comments

* Links a product or service to one or more financial mechanisms, initiatives, or grants that enable or support its provision or access.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:fundingSource |
| native | EVORAO:fundingSource |
| exact | schema:funding |




## LinkML Source

<details>
```yaml
name: fundingSource
description: A program, grant, or project providing financial support for the access
  or use of the product or service, either fully or partially.
title: funding source
comments:
- Links a product or service to one or more financial mechanisms, initiatives, or
  grants that enable or support its provision or access.
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:funding
rank: 1000
alias: fundingSource
domain_of:
- ProductOrService
range: FundingSource
required: false
multivalued: true

```
</details>