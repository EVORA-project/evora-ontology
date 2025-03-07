

# Slot: storage conditions (storageConditions)


_Specifies the conditions under which the product has to be stored to maintain stability and integrity, such as temperature, buffer, and other environmental factors._





URI: [EVORAO:storageConditions](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#storageConditions)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Product](Product.md) | A product |  yes  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |







## Properties

* Range: [String](String.md)

* Required: True





## Comments

* e.g, could be a xsd:string in enumeration ('Freeze Dried', 'Liquid Nitrogen', 'Viral Storage Medium -20C', 'Viral Storage Medium -80C', 'Living plant material (>= +4°C)', 'Gas Phase', 'Ethanol -20C', 'Ethanol -80C', 'Dried')

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:storageConditions |
| native | EVORAO:storageConditions |




## LinkML Source

<details>
```yaml
name: storageConditions
description: Specifies the conditions under which the product has to be stored to
  maintain stability and integrity, such as temperature, buffer, and other environmental
  factors.
title: storage conditions
comments:
- e.g, could be a xsd:string in enumeration ('Freeze Dried', 'Liquid Nitrogen', 'Viral
  Storage Medium -20C', 'Viral Storage Medium -80C', 'Living plant material (>= +4°C)',
  'Gas Phase', 'Ethanol -20C', 'Ethanol -80C', 'Dried')
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: storageConditions
domain_of:
- Product
range: string
required: true
multivalued: false

```
</details>