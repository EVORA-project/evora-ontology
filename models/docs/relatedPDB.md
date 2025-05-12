

# Slot: related PDB (relatedPDB) 


_Identifier for 3D structural data as per the PDB (Protein Data Bank) database_





URI: [EVORAO:relatedPDB](https://w3id.org/evorao/relatedPDB)
Alias: relatedPDB

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


* from schema: https://w3id.org/evorao/




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
from_schema: https://w3id.org/evorao/
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