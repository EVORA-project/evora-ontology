

# Class: DOI (Doi) 


_A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard_





URI: [EVORAO:Doi](https://w3id.org/evorao/Doi)






```mermaid
 classDiagram
    class Doi
    click Doi href "../Doi"
      Term <|-- Doi
        click Term href "../Term"
      
      Doi : description
        
      Doi : inVocabulary
        
          
    
    
    Doi --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Doi : title
        
      Doi : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **Doi**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Publication](Publication.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [ProductOrService](ProductOrService.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Service](Service.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Product](Product.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Antibody](Antibody.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Hybridoma](Hybridoma.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Protein](Protein.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [NucleicAcid](NucleicAcid.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [DetectionKit](DetectionKit.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Bundle](Bundle.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Pathogen](Pathogen.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Virus](Virus.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Bacterium](Bacterium.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Fungus](Fungus.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Protozoan](Protozoan.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Viroid](Viroid.md) | [doi](doi.md) | range | [Doi](Doi.md) |
| [Prion](Prion.md) | [doi](doi.md) | range | [Doi](Doi.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Doi |
| native | EVORAO:Doi |
| close | wd:Q25670, wd:Q25670 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Doi
description: A unique string identifier assigned to a digital object, providing a
  permanent link for reliable citation and access.  The Digital Object Identifier
  (DOI) is a persistent identifier that is an ISO standard
title: DOI
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q25670
- wd:Q25670
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: Doi
description: A unique string identifier assigned to a digital object, providing a
  permanent link for reliable citation and access.  The Digital Object Identifier
  (DOI) is a persistent identifier that is an ISO standard
title: DOI
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q25670
- wd:Q25670
is_a: Term
attributes:
  title:
    name: title
    description: A name given to the resource
    title: title
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - rdfs:label
    - schema:name
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: Doi
    domain_of:
    - Term
    - Dataset
    - DataService
    - Publication
    - License
    - Certification
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
      present the resource.

      '
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:description
    close_mappings:
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: Doi
    domain_of:
    - Term
    - Dataset
    - DataService
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  weight:
    name: weight
    description: A numerical value indicating relative importance or priority, generally
      processed in ascending order. This weight helps prioritize content when organizing
      or processing data. Its value can be negative, with a default set to 0
    title: weight
    comments:
    - The lowest weighted Data providers are triggered first, this may be usefull
      to populate at first entities that are referenced by others (e.g. Version ahead
      of Rank ahead of Taxon)
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: Doi
    domain_of:
    - Term
    - DataProvider
    range: integer
    required: true
    multivalued: false
  inVocabulary:
    name: inVocabulary
    description: Terms belong to a specific vocabulary
    title: in Vocabulary
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - wdp:P972
    rank: 1000
    alias: inVocabulary
    owner: Doi
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>