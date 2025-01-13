

# Class: Variant


_An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain_





URI: [EVORA:Variant](https://evora-project.eu/Variant)






```mermaid
 classDiagram
    class Variant
    click Variant href "../Variant"
      CommonName <|-- Variant
        click CommonName href "../CommonName"
      
      Variant : alternateName
        
          
    
    
    Variant --> "*" AlternateName : alternateName
    click AlternateName href "../AlternateName"

        
      Variant : description
        
      Variant : inVocabulary
        
          
    
    
    Variant --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Variant : name
        
      Variant : sourceOfInformation
        
      Variant : weight
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [Term](Term.md)
            * [CommonName](CommonName.md)
                * **Variant**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any known alternate name related to this name | [CommonName](CommonName.md) |
| [sourceOfInformation](sourceOfInformation.md) | * <br/> [String](String.md) | The name of the origin from which knowledge is obtained | [CommonName](CommonName.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PathogenIdentification](PathogenIdentification.md) | [variant](variant.md) | range | [Variant](Variant.md) |




## Aliases


* Variant



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Variant |
| native | EVORA:Variant |
| close | wd:Q104795308 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Variant
description: An organism with one or more new mutations is referred to as a “variant”
  of the original organism if not sufficiently different to be termed a distinct strain
from_schema: https://evora-project.eu/
aliases:
- Variant
close_mappings:
- wd:Q104795308
is_a: CommonName

```
</details>

### Induced

<details>
```yaml
name: Variant
description: An organism with one or more new mutations is referred to as a “variant”
  of the original organism if not sufficiently different to be termed a distinct strain
from_schema: https://evora-project.eu/
aliases:
- Variant
close_mappings:
- wd:Q104795308
is_a: CommonName
attributes:
  alternateName:
    name: alternateName
    description: Any known alternate name related to this name
    comments:
    - including previous names and former taxonomic terms, this information can also
      serve as keywords arround the pathogen name for search and as a bridge with
      other projects that are still using other naming systems or taxonomies e.g.
      the NCBI taxonomy
    from_schema: https://evora-project.eu/
    aliases:
    - alternate name
    close_mappings:
    - wdp:P4970
    rank: 1000
    alias: alternateName
    owner: Variant
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
    from_schema: https://evora-project.eu/
    aliases:
    - source of information
    close_mappings:
    - wdp:P248
    rank: 1000
    alias: sourceOfInformation
    owner: Variant
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
    from_schema: https://evora-project.eu/
    aliases:
    - weight
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: Variant
    domain_of:
    - DataProvider
    - Term
    range: integer
    required: true
    multivalued: false
  inVocabulary:
    name: inVocabulary
    description: Terms belong to a specific vocabulary
    from_schema: https://evora-project.eu/
    aliases:
    - in Vocabulary
    close_mappings:
    - wdp:P972
    rank: 1000
    alias: inVocabulary
    owner: Variant
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false
  name:
    name: name
    description: The label that allows humans to identify the current item
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://evora-project.eu/
    aliases:
    - name
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Variant
    domain_of:
    - Nameable
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    comments:
    - 'Describe this item in few lines. This description will serve as a summary to
      present the item.

      '
    from_schema: https://evora-project.eu/
    aliases:
    - description
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Variant
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>