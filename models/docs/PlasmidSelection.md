

# Class: Plasmid selection (PlasmidSelection)


_The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers_





URI: [EVORAO:PlasmidSelection](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#PlasmidSelection)






```mermaid
 classDiagram
    class PlasmidSelection
    click PlasmidSelection href "../PlasmidSelection"
      Term <|-- PlasmidSelection
        click Term href "../Term"
      
      PlasmidSelection : description
        
      PlasmidSelection : inVocabulary
        
          
    
    
    PlasmidSelection --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      PlasmidSelection : name
        
      PlasmidSelection : weight
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [Term](Term.md)
            * **PlasmidSelection**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NucleicAcid](NucleicAcid.md) | [pasmidSelection](pasmidSelection.md) | range | [PlasmidSelection](PlasmidSelection.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:PlasmidSelection |
| native | EVORAO:PlasmidSelection |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PlasmidSelection
description: The process of identifying cells that have successfully incorporated
  a plasmid, typically using antibiotic resistance markers
title: Plasmid selection
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: PlasmidSelection
description: The process of identifying cells that have successfully incorporated
  a plasmid, typically using antibiotic resistance markers
title: Plasmid selection
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
is_a: Term
attributes:
  weight:
    name: weight
    description: A numerical value indicating relative importance or priority, generally
      processed in ascending order. This weight helps prioritize content when organizing
      or processing data. Its value can be negative, with a default set to 0
    title: weight
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: PlasmidSelection
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wdp:P972
    rank: 1000
    alias: inVocabulary
    owner: PlasmidSelection
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: PlasmidSelection
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: PlasmidSelection
    domain_of:
    - Nameable
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>