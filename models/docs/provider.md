

# Slot: provider (provider)


_A provider of this product or service, as a specific organization_





URI: [EVORAO:provider](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#provider)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Product](Product.md) | A product |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Service](Service.md) | A service |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [ProductOrService](ProductOrService.md) | A product or a service |  yes  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







## Properties

* Range: [Provider](Provider.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:provider |
| native | EVORAO:provider |




## LinkML Source

<details>
```yaml
name: provider
description: A provider of this product or service, as a specific organization
title: provider
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: provider
domain_of:
- ProductOrService
range: Provider
required: true
multivalued: false

```
</details>