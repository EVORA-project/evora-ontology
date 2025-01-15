

# Class: Alternate Name (AlternateName)


_List of alternate names for things_





URI: [EVORA:AlternateName](https://evora-project.eu/AlternateName)






```mermaid
 classDiagram
    class AlternateName
    click AlternateName href "../AlternateName"
      Term <|-- AlternateName
        click Term href "../Term"
      
      AlternateName : alternateName
        
          
    
    
    AlternateName --> "*" AlternateName : alternateName
    click AlternateName href "../AlternateName"

        
      AlternateName : description
        
      AlternateName : inVocabulary
        
          
    
    
    AlternateName --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      AlternateName : name
        
      AlternateName : sourceOfInformation
        
      AlternateName : weight
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [Term](Term.md)
            * **AlternateName**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any known alternate name related to this name | direct |
| [sourceOfInformation](sourceOfInformation.md) | * <br/> [String](String.md) | The name of the origin from which knowledge is obtained | direct |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CommonName](CommonName.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |
| [VirusName](VirusName.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |
| [AlternateName](AlternateName.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |
| [Variant](Variant.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |
| [Organization](Organization.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |
| [RI](RI.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |
| [Provider](Provider.md) | [alternateName](alternateName.md) | range | [AlternateName](AlternateName.md) |




## Aliases


* synonym



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:AlternateName |
| native | EVORA:AlternateName |
| close | wd:Q7662595 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AlternateName
description: List of alternate names for things
title: Alternate Name
from_schema: https://evora-project.eu/
aliases:
- synonym
close_mappings:
- wd:Q7662595
is_a: Term
slots:
- alternateName
- sourceOfInformation
slot_usage:
  alternateName:
    name: alternateName
    description: Any known alternate name related to this name
    title: alternate name
    aliases:
    - alternative name
    close_mappings:
    - wdp:P4970
    range: AlternateName
    required: false
    multivalued: true
  sourceOfInformation:
    name: sourceOfInformation
    description: The name of the origin from which knowledge is obtained. This can
      include any entity that provides information
    title: source of information
    aliases:
    - stated in
    close_mappings:
    - wdp:P248
    range: string
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: AlternateName
description: List of alternate names for things
title: Alternate Name
from_schema: https://evora-project.eu/
aliases:
- synonym
close_mappings:
- wd:Q7662595
is_a: Term
slot_usage:
  alternateName:
    name: alternateName
    description: Any known alternate name related to this name
    title: alternate name
    aliases:
    - alternative name
    close_mappings:
    - wdp:P4970
    range: AlternateName
    required: false
    multivalued: true
  sourceOfInformation:
    name: sourceOfInformation
    description: The name of the origin from which knowledge is obtained. This can
      include any entity that provides information
    title: source of information
    aliases:
    - stated in
    close_mappings:
    - wdp:P248
    range: string
    required: false
    multivalued: true
attributes:
  alternateName:
    name: alternateName
    description: Any known alternate name related to this name
    title: alternate name
    from_schema: https://evora-project.eu/
    aliases:
    - alternative name
    close_mappings:
    - wdp:P4970
    rank: 1000
    alias: alternateName
    owner: AlternateName
    domain_of:
    - CommonName
    - AlternateName
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  sourceOfInformation:
    name: sourceOfInformation
    description: The name of the origin from which knowledge is obtained. This can
      include any entity that provides information
    title: source of information
    from_schema: https://evora-project.eu/
    aliases:
    - stated in
    close_mappings:
    - wdp:P248
    rank: 1000
    alias: sourceOfInformation
    owner: AlternateName
    domain_of:
    - CommonName
    - AlternateName
    range: string
    required: false
    multivalued: true
  weight:
    name: weight
    description: A numerical value indicating relative importance or priority, generally
      processed in ascending order. This weight helps prioritize content when organizing
      or processing data. Its value can be negative, with a default set to 0
    title: weight
    from_schema: https://evora-project.eu/
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: AlternateName
    domain_of:
    - DataProvider
    - Term
    range: integer
    required: true
    multivalued: false
  inVocabulary:
    name: inVocabulary
    description: Terms belong to a specific vocabulary
    title: in Vocabulary
    from_schema: https://evora-project.eu/
    aliases:
    - catalog
    close_mappings:
    - wdp:P972
    rank: 1000
    alias: inVocabulary
    owner: AlternateName
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false
  name:
    name: name
    description: The label that allows humans to identify the current item
    title: name
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: AlternateName
    domain_of:
    - Nameable
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    title: description
    comments:
    - 'Describe this item in few lines. This description will serve as a summary to
      present the item.

      '
    from_schema: https://evora-project.eu/
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: AlternateName
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>