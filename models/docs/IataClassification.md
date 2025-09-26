

# Class: IATA classification (IataClassification) 


_The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air_





URI: [EVORAO:IataClassification](https://w3id.org/evorao/IataClassification)






```mermaid
 classDiagram
    class IataClassification
    click IataClassification href "../IataClassification"
      Term <|-- IataClassification
        click Term href "../Term"
      
      IataClassification : dateIssued
        
      IataClassification : dateModified
        
      IataClassification : description
        
      IataClassification : identifier
        
      IataClassification : inVocabulary
        
          
    
    
    IataClassification --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      IataClassification : iri
        
      IataClassification : keyword
        
      IataClassification : title
        
      IataClassification : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **IataClassification**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |
| [dateIssued](dateIssued.md) | 0..1 <br/> [Datetime](Datetime.md) | Date of formal issuance (e | [Resource](Resource.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Datetime](Datetime.md) | Most recent date on which the resource was changed, updated or modified | [Resource](Resource.md) |
| [identifier](identifier.md) | * <br/> [String](String.md) | A unique identifier of the resource being described or cataloged | [Resource](Resource.md) |
| [iri](iri.md) | * <br/> [Uri](Uri.md) | International Resource Identifier (IRI) that uniquely identifies or refers to... | [Resource](Resource.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Product](Product.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Antibody](Antibody.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Hybridoma](Hybridoma.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Protein](Protein.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [NucleicAcid](NucleicAcid.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [DetectionKit](DetectionKit.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Bundle](Bundle.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Pathogen](Pathogen.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Virus](Virus.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Bacterium](Bacterium.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Fungus](Fungus.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Protozoan](Protozoan.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Viroid](Viroid.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |
| [Prion](Prion.md) | [iataClassification](iataClassification.md) | range | [IataClassification](IataClassification.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:IataClassification |
| native | EVORAO:IataClassification |
| related | wd:Q19755, wd:Q19755 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IataClassification
description: The corresponding International Air Transport Association (IATA)'s category
  for dangerous goods that are transported by air
title: IATA classification
from_schema: https://w3id.org/evorao/
related_mappings:
- wd:Q19755
- wd:Q19755
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: IataClassification
description: The corresponding International Air Transport Association (IATA)'s category
  for dangerous goods that are transported by air
title: IATA classification
from_schema: https://w3id.org/evorao/
related_mappings:
- wd:Q19755
- wd:Q19755
is_a: Term
attributes:
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
    owner: IataClassification
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
    owner: IataClassification
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
    owner: IataClassification
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
    owner: IataClassification
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
    owner: IataClassification
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
    owner: IataClassification
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
    owner: IataClassification
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  identifier:
    name: identifier
    description: A unique identifier of the resource being described or cataloged
    title: identifier
    comments:
    - The identifier is a text string which is assigned to the resource to provide
      an unambiguous reference within a particular context. Persistent identifiers
      should be provided as HTTP URIs
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:identifier
    rank: 1000
    slot_uri: dct:identifier
    alias: identifier
    owner: IataClassification
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  iri:
    name: iri
    description: International Resource Identifier (IRI) that uniquely identifies
      or refers to the resource. IRIs include URIs, and URIs include URLs
    title: IRI
    comments:
    - An IRI is a global identifier standardized by IETF RFC 3987. It may or may not
      be resolvable on the web. IRIs include URIs, and URIs include URLs
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - biolink:iri
    related_mappings:
    - mi:url
    narrow_mappings:
    - schema:url
    rank: 1000
    is_a: identifier
    alias: iri
    owner: IataClassification
    domain_of:
    - Resource
    range: uri
    required: false
    multivalued: true

```
</details>