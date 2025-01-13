

# Class: SequenceReference


_A reference that permits to retrieve the sequence information from a sequence provider_





URI: [EVORA:SequenceReference](https://evora-project.eu/SequenceReference)






```mermaid
 classDiagram
    class SequenceReference
    click SequenceReference href "../SequenceReference"
      Dataset <|-- SequenceReference
        click Dataset href "../Dataset"
      
      SequenceReference : accessionNumber
        
      SequenceReference : sequenceProvider
        
      
```





## Inheritance
* [Dataset](Dataset.md)
    * **SequenceReference**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [accessionNumber](accessionNumber.md) | 1 <br/> [String](String.md) | The sequence ID that permits to retrieve the sequence information from the se... | direct |
| [sequenceProvider](sequenceProvider.md) | 1 <br/> [String](String.md) | The name of the sequence provider within the list of accepted sequence provid... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Sequence](Sequence.md) | [sequenceReference](sequenceReference.md) | range | [SequenceReference](SequenceReference.md) |
| [Antibody](Antibody.md) | [sequenceReference](sequenceReference.md) | range | [SequenceReference](SequenceReference.md) |
| [Hybridoma](Hybridoma.md) | [sequenceReference](sequenceReference.md) | range | [SequenceReference](SequenceReference.md) |




## Aliases


* Sequence reference



## Comments

* A work on making it a subclass of External related reference might be consistent and beneficial for data structuration but special attention will have to be take to ensure it remains consistent with the actual the use cases for users

## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:SequenceReference |
| native | EVORA:SequenceReference |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SequenceReference
description: A reference that permits to retrieve the sequence information from a
  sequence provider
comments:
- A work on making it a subclass of External related reference might be consistent
  and beneficial for data structuration but special attention will have to be take
  to ensure it remains consistent with the actual the use cases for users
from_schema: https://evora-project.eu/
aliases:
- Sequence reference
is_a: Dataset
slots:
- accessionNumber
- sequenceProvider
slot_usage:
  accessionNumber:
    name: accessionNumber
    description: The sequence ID that permits to retrieve the sequence information
      from the sequence provider
    aliases:
    - accession number
    close_mappings:
    - dct:identifier
    range: string
    required: true
    multivalued: false
  sequenceProvider:
    name: sequenceProvider
    description: The name of the sequence provider within the list of accepted sequence
      providers
    aliases:
    - sequence provider
    close_mappings:
    - dct:publisher
    range: string
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: SequenceReference
description: A reference that permits to retrieve the sequence information from a
  sequence provider
comments:
- A work on making it a subclass of External related reference might be consistent
  and beneficial for data structuration but special attention will have to be take
  to ensure it remains consistent with the actual the use cases for users
from_schema: https://evora-project.eu/
aliases:
- Sequence reference
is_a: Dataset
slot_usage:
  accessionNumber:
    name: accessionNumber
    description: The sequence ID that permits to retrieve the sequence information
      from the sequence provider
    aliases:
    - accession number
    close_mappings:
    - dct:identifier
    range: string
    required: true
    multivalued: false
  sequenceProvider:
    name: sequenceProvider
    description: The name of the sequence provider within the list of accepted sequence
      providers
    aliases:
    - sequence provider
    close_mappings:
    - dct:publisher
    range: string
    required: true
    multivalued: false
attributes:
  accessionNumber:
    name: accessionNumber
    description: The sequence ID that permits to retrieve the sequence information
      from the sequence provider
    from_schema: https://evora-project.eu/
    aliases:
    - accession number
    close_mappings:
    - dct:identifier
    rank: 1000
    alias: accessionNumber
    owner: SequenceReference
    domain_of:
    - SequenceReference
    range: string
    required: true
    multivalued: false
  sequenceProvider:
    name: sequenceProvider
    description: The name of the sequence provider within the list of accepted sequence
      providers
    from_schema: https://evora-project.eu/
    aliases:
    - sequence provider
    close_mappings:
    - dct:publisher
    rank: 1000
    alias: sequenceProvider
    owner: SequenceReference
    domain_of:
    - SequenceReference
    range: string
    required: true
    multivalued: false

```
</details>