

# Slot: material safety data sheet (materialSafetyDataSheet)


_A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized document that contains crucial occupational safety and health information related to the product_





URI: [EVORAO:materialSafetyDataSheet](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#materialSafetyDataSheet)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Fungus](Fungus.md) | The fungus as a biological material |  no  |
| [Virus](Virus.md) | The virus as a biological material |  no  |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  no  |
| [Viroid](Viroid.md) | The viroid as a biological material |  no  |
| [Product](Product.md) | A product |  yes  |
| [Hybridoma](Hybridoma.md) | An hybridoma that provides antibodies that can be related to a pathogen |  no  |
| [DetectionKit](DetectionKit.md) | A detection kit for specific pathogens |  no  |
| [Pathogen](Pathogen.md) | Biological entity that causes disease in its host, which is typically an infe... |  no  |
| [Bundle](Bundle.md) | A group of products |  no  |
| [Protozoan](Protozoan.md) | The protozoan as a biological material |  no  |
| [Antibody](Antibody.md) | Protein that can bind to certain types of foreign bodies, such as pathogens |  no  |
| [Prion](Prion.md) | The prion as a biological material |  no  |
| [NucleicAcid](NucleicAcid.md) | Nucleic acid related to a pathogen |  no  |
| [Bacterium](Bacterium.md) | The bacterium as a biological material |  no  |







## Properties

* Range: [MSDS](MSDS.md)





## Comments

* The MSD  is a document that provides detailed information about the properties, hazards, handling, storage, and emergency procedures related to the use of a chemical or substance

## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:materialSafetyDataSheet |
| native | EVORAO:materialSafetyDataSheet |




## LinkML Source

<details>
```yaml
name: materialSafetyDataSheet
description: A Material Safety Data Sheet (MSDS) or Safety Data Sheet (SDS) is a standardized
  document that contains crucial occupational safety and health information related
  to the product
title: material safety data sheet
comments:
- The MSD  is a document that provides detailed information about the properties,
  hazards, handling, storage, and emergency procedures related to the use of a chemical
  or substance
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
alias: materialSafetyDataSheet
domain_of:
- Product
range: MSDS
required: false
multivalued: false

```
</details>