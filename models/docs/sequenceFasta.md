

# Slot: sequence FASTA (sequenceFasta) 


_Textual encoding of a biological sequence information in FASTA format_





URI: [EVORAO:sequenceFasta](https://w3id.org/evorao/sequenceFasta)
Alias: sequenceFasta

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sequence](Sequence.md) | A nucleic acid or protein sequence information |  yes  |







## Properties

* Range: [String](String.md)





## Comments

* In cases where no reference sequence exists in public repositories, the corresponding FASTA sequence is expected; otherwise, the reference sequence is sufficient. In FASTA format the line before the nucleotide sequence, called the FASTA definition line, must begin with a charater ('>'), followed by a unique SeqID (sequence identifier). In case the sequence is made of multiple parts several fasta sequences can be provided

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:sequenceFasta |
| native | EVORAO:sequenceFasta |




## LinkML Source

<details>
```yaml
name: sequenceFasta
description: Textual encoding of a biological sequence information in FASTA format
title: sequence FASTA
comments:
- In cases where no reference sequence exists in public repositories, the corresponding
  FASTA sequence is expected; otherwise, the reference sequence is sufficient. In
  FASTA format the line before the nucleotide sequence, called the FASTA definition
  line, must begin with a charater ('>'), followed by a unique SeqID (sequence identifier).
  In case the sequence is made of multiple parts several fasta sequences can be provided
from_schema: https://w3id.org/evorao/
rank: 1000
alias: sequenceFasta
domain_of:
- Sequence
range: string
required: false
multivalued: false

```
</details>