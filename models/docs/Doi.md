

# Class: DOI (Doi) 


_A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard_





URI: [EVORAO:Doi](https://w3id.org/evorao/Doi)






```mermaid
 classDiagram
    class Doi
    click Doi href "../Doi"
      Term <|-- Doi
        click Term href "../Term"
      
      Doi : dateIssued
        
      Doi : dateModified
        
      Doi : description
        
      Doi : identifier
        
      Doi : inVocabulary
        
          
    
    
    Doi --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Doi : iri
        
      Doi : keyword
        
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
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |
| [dateIssued](dateIssued.md) | 0..1 <br/> [Datetime](Datetime.md) | Date of formal issuance (e | [Resource](Resource.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Datetime](Datetime.md) | Most recent date on which the resource was changed, updated or modified | [Resource](Resource.md) |
| [identifier](identifier.md) | * <br/> [String](String.md) | A unique identifier of the resource being described or cataloged | [Resource](Resource.md) |
| [iri](iri.md) | * <br/> [Uri](Uri.md) | International Resource Identifier (IRI) that uniquely identifies or refers to... | [Resource](Resource.md) |





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
| exact | wd:Q25670, ncit:C71462, t4fs:0000434, obi:0002110, wd:Q25670, ncit:C71462, t4fs:0000434, obi:0002110 |







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
exact_mappings:
- wd:Q25670
- ncit:C71462
- t4fs:0000434
- obi:0002110
- wd:Q25670
- ncit:C71462
- t4fs:0000434
- obi:0002110
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
exact_mappings:
- wd:Q25670
- ncit:C71462
- t4fs:0000434
- obi:0002110
- wd:Q25670
- ncit:C71462
- t4fs:0000434
- obi:0002110
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
    related_mappings:
    - dct:isReferencedBy
    broad_mappings:
    - dct:isPartOf
    rank: 1000
    alias: inVocabulary
    owner: Doi
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
    owner: Doi
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
    owner: Doi
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
    owner: Doi
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
    owner: Doi
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
    rank: 1000
    is_a: identifier
    alias: iri
    owner: Doi
    domain_of:
    - Resource
    range: uri
    required: false
    multivalued: true

```
</details>