

# Class: Taxonomic rank (TaxonomicRank) 


_The possible taxonomic ranks and their description_





URI: [EVORAO:TaxonomicRank](https://w3id.org/evorao/TaxonomicRank)






```mermaid
 classDiagram
    class TaxonomicRank
    click TaxonomicRank href "../TaxonomicRank"
      Term <|-- TaxonomicRank
        click Term href "../Term"
      
      TaxonomicRank : dateIssued
        
      TaxonomicRank : dateModified
        
      TaxonomicRank : description
        
      TaxonomicRank : inVocabulary
        
          
    
    
    TaxonomicRank --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      TaxonomicRank : keyword
        
      TaxonomicRank : taxonomy
        
          
    
    
    TaxonomicRank --> "* _recommended_" Taxonomy : taxonomy
    click Taxonomy href "../Taxonomy"

        
      TaxonomicRank : title
        
      TaxonomicRank : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **TaxonomicRank**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [taxonomy](taxonomy.md) | * _recommended_ <br/> [Taxonomy](Taxonomy.md) | The taxonomy release(s) in which this entity exists | direct |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |
| [dateIssued](dateIssued.md) | 0..1 <br/> [Datetime](Datetime.md) | Date of formal issuance (e | [Resource](Resource.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Datetime](Datetime.md) | Most recent date on which the resource was changed, updated or modified | [Resource](Resource.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Taxonomy](Taxonomy.md) | [rank](rank.md) | range | [TaxonomicRank](TaxonomicRank.md) |
| [Taxon](Taxon.md) | [rank](rank.md) | range | [TaxonomicRank](TaxonomicRank.md) |






## Comments

* Use of Data provider recommended

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:TaxonomicRank |
| native | EVORAO:TaxonomicRank |
| exact | taxrank:0000000, uniprotrdfs:Rank, wd:Q427626, taxrank:0000000, uniprotrdfs:Rank, wd:Q427626 |
| related | dwc:taxonRank, dwc:taxonRank |
| close | biolink:TaxonomicRank, biolink:TaxonomicRank |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TaxonomicRank
description: The possible taxonomic ranks and their description
title: Taxonomic rank
comments:
- Use of Data provider recommended
from_schema: https://w3id.org/evorao/
exact_mappings:
- taxrank:0000000
- uniprotrdfs:Rank
- wd:Q427626
- taxrank:0000000
- uniprotrdfs:Rank
- wd:Q427626
close_mappings:
- biolink:TaxonomicRank
- biolink:TaxonomicRank
related_mappings:
- dwc:taxonRank
- dwc:taxonRank
is_a: Term
slots:
- taxonomy
slot_usage:
  taxonomy:
    name: taxonomy
    description: The taxonomy release(s) in which this entity exists
    title: taxonomy
    broad_mappings:
    - dct:isPartOf
    domain_of:
    - TaxonomicRank
    - Taxon
    range: Taxonomy
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: TaxonomicRank
description: The possible taxonomic ranks and their description
title: Taxonomic rank
comments:
- Use of Data provider recommended
from_schema: https://w3id.org/evorao/
exact_mappings:
- taxrank:0000000
- uniprotrdfs:Rank
- wd:Q427626
- taxrank:0000000
- uniprotrdfs:Rank
- wd:Q427626
close_mappings:
- biolink:TaxonomicRank
- biolink:TaxonomicRank
related_mappings:
- dwc:taxonRank
- dwc:taxonRank
is_a: Term
slot_usage:
  taxonomy:
    name: taxonomy
    description: The taxonomy release(s) in which this entity exists
    title: taxonomy
    broad_mappings:
    - dct:isPartOf
    domain_of:
    - TaxonomicRank
    - Taxon
    range: Taxonomy
    required: false
    multivalued: true
attributes:
  taxonomy:
    name: taxonomy
    description: The taxonomy release(s) in which this entity exists
    title: taxonomy
    from_schema: https://w3id.org/evorao/
    broad_mappings:
    - dct:isPartOf
    rank: 1000
    alias: taxonomy
    owner: TaxonomicRank
    domain_of:
    - TaxonomicRank
    - Taxon
    range: Taxonomy
    required: false
    recommended: true
    multivalued: true
  title:
    name: title
    description: A name given to the resource
    title: title
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern: ''Virus
      name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:name
    - rdfs:label
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: TaxonomicRank
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
    - Describe this item in few lines. This description will serve as a summary to
      present the resource.
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:description
    close_mappings:
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: TaxonomicRank
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
    owner: TaxonomicRank
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
    related_mappings:
    - dct:isReferencedBy
    broad_mappings:
    - dct:isPartOf
    rank: 1000
    alias: inVocabulary
    owner: TaxonomicRank
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false
  keyword:
    name: keyword
    description: A keyword or tag describing the resource
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: TaxonomicRank
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  dateIssued:
    name: dateIssued
    description: Date of formal issuance (e.g., publication) of the resource
    title: date issued
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME]
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000051
    close_mappings:
    - schema:datePublished
    - schema:dateCreated
    rank: 1000
    slot_uri: dct:issued
    alias: dateIssued
    owner: TaxonomicRank
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  dateModified:
    name: dateModified
    description: Most recent date on which the resource was changed, updated or modified
    title: date modified
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME]
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000036
    close_mappings:
    - schema:dateModified
    rank: 1000
    slot_uri: dct:modified
    alias: dateModified
    owner: TaxonomicRank
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false

```
</details>