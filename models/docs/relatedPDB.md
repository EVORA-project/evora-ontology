

# Slot: related PDB (relatedPDB)


_Identifier for 3D structural data as per the PDB (Protein Data Bank) database_





URI: [EVORAO:relatedPDB](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#relatedPDB)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [PDBReference](PDBReference.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:relatedPDB |
| native | EVORAO:relatedPDB |
| close | wdp:P638 |




## LinkML Source

<details>
```yaml
name: relatedPDB
description: Identifier for 3D structural data as per the PDB (Protein Data Bank)
  database
title: related PDB
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wdp:P638
rank: 1000
alias: relatedPDB
domain_of:
- Protein
range: PDBReference
required: false
multivalued: true

```
</details>