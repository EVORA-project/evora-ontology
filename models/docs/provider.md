

# Slot: provider (provider) 


_A provider of this product or service, as a specific organization_





URI: [EVORAO:provider](https://w3id.org/evorao/provider)
Alias: provider

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Product](Product.md) | A tangible, physical item made available by a provider for use, consumption, ... |  no  |
| [Bundle](Bundle.md) | A grouping of products and/or services intentionally combined into a single o... |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Service](Service.md) | An intangible offering characterized by an activity, performance, or facilita... |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | An offering provided by a provider, which may be tangible (a product) or inta... |  yes  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |







## Properties

* Range: [Provider](Provider.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:provider |
| native | EVORAO:provider |
| exact | sio:000066 |
| close | schema:provider, dct:publisher |




## LinkML Source

<details>
```yaml
name: provider
description: A provider of this product or service, as a specific organization
title: provider
from_schema: https://w3id.org/evorao/
exact_mappings:
- sio:000066
close_mappings:
- schema:provider
- dct:publisher
rank: 1000
alias: provider
domain_of:
- ProductOrService
range: Provider
required: true
multivalued: false

```
</details>