

# Slot: related PDB (relatedPdb) 


_Identifier for 3D structural data as per the PDB (Protein Data Bank) database_





URI: [EVORAO:relatedPdb](https://w3id.org/evorao/relatedPdb)
Alias: relatedPdb

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Protein](Protein.md) | A protein as a derived product from a pathogen |  yes  |







## Properties

* Range: [PdbReference](PdbReference.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:relatedPdb |
| native | EVORAO:relatedPdb |
| close | wdp:P638 |




## LinkML Source

<details>
```yaml
name: relatedPdb
description: Identifier for 3D structural data as per the PDB (Protein Data Bank)
  database
title: related PDB
from_schema: https://w3id.org/evorao/
close_mappings:
- wdp:P638
rank: 1000
alias: relatedPdb
domain_of:
- Protein
range: PdbReference
required: false
multivalued: true

```
</details>