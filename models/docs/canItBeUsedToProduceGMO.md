

# Slot: can it be used to produce GMO (canItBeUsedToProduceGMO)


_Indicates if the current service or product can be used to produce GMO_





URI: [EVORAO:canItBeUsedToProduceGMO](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#canItBeUsedToProduceGMO)



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

* Range: [Boolean](Boolean.md)

* Required: True





## Comments

* Set to TRUE if it can produce GMO. It is recommended to have a value for this field, no value will be understood as unknown

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:canItBeUsedToProduceGMO |
| native | EVORAO:canItBeUsedToProduceGMO |




## LinkML Source

<details>
```yaml
name: canItBeUsedToProduceGMO
description: Indicates if the current service or product can be used to produce GMO
title: can it be used to produce GMO
comments:
- Set to TRUE if it can produce GMO. It is recommended to have a value for this field,
  no value will be understood as unknown
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: canItBeUsedToProduceGMO
domain_of:
- ProductOrService
range: boolean
required: true
recommended: true
multivalued: false

```
</details>