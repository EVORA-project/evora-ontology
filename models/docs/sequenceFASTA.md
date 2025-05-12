

# Slot: sequence FASTA (sequenceFASTA) 


_In case no sequence reference exists in public repositories, the corresponding FASTA sequence is required_





URI: [EVORAO:sequenceFASTA](https://w3id.org/evorao/sequenceFASTA)
Alias: sequenceFASTA

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sequence](Sequence.md) | A nucleic acid or protein sequence information |  yes  |







## Properties

* Range: [String](String.md)





## Comments

* In FASTA format the line before the nucleotide sequence, called the FASTA definition line, must begin with a charater ('>'), followed by a unique SeqID (sequence identifier). In case the sequence is made of multiple parts several fasta sequences can be provided

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequenceFASTA |
| native | EVORAO:sequenceFASTA |




## LinkML Source

<details>
```yaml
name: sequenceFASTA
description: In case no sequence reference exists in public repositories, the corresponding
  FASTA sequence is required
title: sequence FASTA
comments:
- In FASTA format the line before the nucleotide sequence, called the FASTA definition
  line, must begin with a charater ('>'), followed by a unique SeqID (sequence identifier).
  In case the sequence is made of multiple parts several fasta sequences can be provided
from_schema: https://w3id.org/evorao/
rank: 1000
alias: sequenceFASTA
domain_of:
- Sequence
range: string
required: false
multivalued: false

```
</details>