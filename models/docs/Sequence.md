

# Class: Sequence (Sequence)


_A nucleic acid or protein sequence information_





URI: [EVORAO:Sequence](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Sequence)






```mermaid
 classDiagram
    class Sequence
    click Sequence href "../Sequence"
      Resource <|-- Sequence
        click Resource href "../Resource"
      
      Sequence : sequenceFASTA
        
      Sequence : sequenceReference
        
          
    
    
    Sequence --> "* _recommended_" SequenceReference : sequenceReference
    click SequenceReference href "../SequenceReference"

        
      
```





## Inheritance
* [Resource](Resource.md)
    * **Sequence**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sequenceReference](sequenceReference.md) | * _recommended_ <br/> [SequenceReference](SequenceReference.md) | A reference that permits to retrieve the sequence information from a sequence... | direct |
| [sequenceFASTA](sequenceFASTA.md) | 0..1 <br/> [String](String.md) | In case no sequence reference exists in public repositories, the correspondin... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [RecombinantPartIdentification](RecombinantPartIdentification.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Protein](Protein.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [NucleicAcid](NucleicAcid.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Pathogen](Pathogen.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Virus](Virus.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Bacterium](Bacterium.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Fungus](Fungus.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Protozoan](Protozoan.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Viroid](Viroid.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |
| [Prion](Prion.md) | [sequence](sequence.md) | range | [Sequence](Sequence.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Sequence |
| native | EVORAO:Sequence |
| close | wd:Q3511065, wd:Q3511065 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sequence
description: A nucleic acid or protein sequence information
title: Sequence
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q3511065
- wd:Q3511065
is_a: Resource
slots:
- sequenceReference
- sequenceFASTA
slot_usage:
  sequenceReference:
    name: sequenceReference
    description: A reference that permits to retrieve the sequence information from
      a sequence provider
    title: sequence reference
    domain_of:
    - Sequence
    - Antibody
    range: SequenceReference
    required: false
    recommended: true
    multivalued: true
  sequenceFASTA:
    name: sequenceFASTA
    description: In case no sequence reference exists in public repositories, the
      corresponding FASTA sequence is required
    title: sequence FASTA
    comments:
    - In FASTA format the line before the nucleotide sequence, called the FASTA definition
      line, must begin with a charater ('>'), followed by a unique SeqID (sequence
      identifier). In case the sequence is made of multiple parts several fasta sequences
      can be provided
    domain_of:
    - Sequence
    range: string
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Sequence
description: A nucleic acid or protein sequence information
title: Sequence
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q3511065
- wd:Q3511065
is_a: Resource
slot_usage:
  sequenceReference:
    name: sequenceReference
    description: A reference that permits to retrieve the sequence information from
      a sequence provider
    title: sequence reference
    domain_of:
    - Sequence
    - Antibody
    range: SequenceReference
    required: false
    recommended: true
    multivalued: true
  sequenceFASTA:
    name: sequenceFASTA
    description: In case no sequence reference exists in public repositories, the
      corresponding FASTA sequence is required
    title: sequence FASTA
    comments:
    - In FASTA format the line before the nucleotide sequence, called the FASTA definition
      line, must begin with a charater ('>'), followed by a unique SeqID (sequence
      identifier). In case the sequence is made of multiple parts several fasta sequences
      can be provided
    domain_of:
    - Sequence
    range: string
    required: false
    multivalued: false
attributes:
  sequenceReference:
    name: sequenceReference
    description: A reference that permits to retrieve the sequence information from
      a sequence provider
    title: sequence reference
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: sequenceReference
    owner: Sequence
    domain_of:
    - Sequence
    - Antibody
    range: SequenceReference
    required: false
    recommended: true
    multivalued: true
  sequenceFASTA:
    name: sequenceFASTA
    description: In case no sequence reference exists in public repositories, the
      corresponding FASTA sequence is required
    title: sequence FASTA
    comments:
    - In FASTA format the line before the nucleotide sequence, called the FASTA definition
      line, must begin with a charater ('>'), followed by a unique SeqID (sequence
      identifier). In case the sequence is made of multiple parts several fasta sequences
      can be provided
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: sequenceFASTA
    owner: Sequence
    domain_of:
    - Sequence
    range: string
    required: false
    multivalued: false

```
</details>