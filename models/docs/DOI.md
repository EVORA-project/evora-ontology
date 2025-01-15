

# Class: DOI (DOI)


_A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard_





URI: [EVORA:DOI](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#DOI)






```mermaid
 classDiagram
    class DOI
    click DOI href "../DOI"
      Term <|-- DOI
        click Term href "../Term"
      
      DOI : description
        
      DOI : inVocabulary
        
          
    
    
    DOI --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      DOI : name
        
      DOI : weight
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [Term](Term.md)
            * **DOI**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Publication](Publication.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [ProductOrService](ProductOrService.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Service](Service.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Product](Product.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Antibody](Antibody.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Hybridoma](Hybridoma.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Protein](Protein.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [NucleicAcid](NucleicAcid.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [DetectionKit](DetectionKit.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Bundle](Bundle.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Pathogen](Pathogen.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Virus](Virus.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Bacterium](Bacterium.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Fungus](Fungus.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Protozoan](Protozoan.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Viroid](Viroid.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |
| [Prion](Prion.md) | [relatedDOI](relatedDOI.md) | range | [DOI](DOI.md) |




## Aliases


* DOI



## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:DOI |
| native | EVORA:DOI |
| close | wd:Q25670 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DOI
description: A unique string identifier assigned to a digital object, providing a
  permanent link for reliable citation and access.  The Digital Object Identifier
  (DOI) is a persistent identifier that is an ISO standard
title: DOI
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
aliases:
- DOI
close_mappings:
- wd:Q25670
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: DOI
description: A unique string identifier assigned to a digital object, providing a
  permanent link for reliable citation and access.  The Digital Object Identifier
  (DOI) is a persistent identifier that is an ISO standard
title: DOI
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
aliases:
- DOI
close_mappings:
- wd:Q25670
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
    owner: DOI
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
    aliases:
    - catalog
    close_mappings:
    - wdp:P972
    rank: 1000
    alias: inVocabulary
    owner: DOI
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
    owner: DOI
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
    owner: DOI
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>