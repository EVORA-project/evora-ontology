

# Class: Clinical group (ClinicalGroup) 


_A syndromic grouping of pathogens, based on typical disease manifestation, clinical syndrome, or primary system affected. Examples include Respiratory viruses, Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic categories but practical classifications used in medicine, epidemiology, and public health._





URI: [EVORAO:ClinicalGroup](https://w3id.org/evorao/ClinicalGroup)






```mermaid
 classDiagram
    class ClinicalGroup
    click ClinicalGroup href "../ClinicalGroup"
      Term <|-- ClinicalGroup
        click Term href "../Term"
      
      ClinicalGroup : alternateName
        
          
    
    
    ClinicalGroup --> "*" AlternateName : alternateName
    click AlternateName href "../AlternateName"

        
      ClinicalGroup : dateIssued
        
      ClinicalGroup : dateModified
        
      ClinicalGroup : description
        
      ClinicalGroup : identifier
        
      ClinicalGroup : inVocabulary
        
          
    
    
    ClinicalGroup --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      ClinicalGroup : iri
        
      ClinicalGroup : keyword
        
      ClinicalGroup : publisher
        
          
    
    
    ClinicalGroup --> "0..1" PersonOrOrganization : publisher
    click PersonOrOrganization href "../PersonOrOrganization"

        
      ClinicalGroup : taxon
        
          
    
    
    ClinicalGroup --> "*" Taxon : taxon
    click Taxon href "../Taxon"

        
      ClinicalGroup : title
        
      ClinicalGroup : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **ClinicalGroup**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any other name under which the entity can be known | direct |
| [taxon](taxon.md) | * <br/> [Taxon](Taxon.md) | Scientifically classified group or entity within the reference taxonomy | direct |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |
| [dateIssued](dateIssued.md) | 0..1 <br/> [Datetime](Datetime.md) | Date of formal issuance (e | [Resource](Resource.md) |
| [dateModified](dateModified.md) | 0..1 <br/> [Datetime](Datetime.md) | Most recent date on which the resource was changed, updated or modified | [Resource](Resource.md) |
| [identifier](identifier.md) | * <br/> [String](String.md) | A unique identifier of the resource being described or cataloged | [Resource](Resource.md) |
| [iri](iri.md) | * <br/> [Uri](Uri.md) | International Resource Identifier (IRI) that uniquely identifies or refers to... | [Resource](Resource.md) |
| [publisher](publisher.md) | 0..1 <br/> [PersonOrOrganization](PersonOrOrganization.md) | The entity responsible for making the resource available | [Resource](Resource.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:ClinicalGroup |
| native | EVORAO:ClinicalGroup |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClinicalGroup
description: A syndromic grouping of pathogens, based on typical disease manifestation,
  clinical syndrome, or primary system affected. Examples include Respiratory viruses,
  Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic
  categories but practical classifications used in medicine, epidemiology, and public
  health.
title: Clinical group
from_schema: https://w3id.org/evorao/
is_a: Term
slots:
- alternateName
- taxon
slot_usage:
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known.
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
    - This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies.
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    domain_of:
    - ClinicalGroup
    - CommonName
    - AlternateName
    - Taxon
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  taxon:
    name: taxon
    description: Scientifically classified group or entity within the reference taxonomy.
    title: taxon
    close_mappings:
    - schema:taxonomicRange
    - dwc:taxonID
    - dwc:toTaxon
    related_mappings:
    - dwc:Taxon
    domain_of:
    - ClinicalGroup
    - Taxonomy
    - PathogenIdentification
    range: Taxon
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ClinicalGroup
description: A syndromic grouping of pathogens, based on typical disease manifestation,
  clinical syndrome, or primary system affected. Examples include Respiratory viruses,
  Hemorrhagic viruses, and Gastroenteritis viruses. Clinical groups are not taxonomic
  categories but practical classifications used in medicine, epidemiology, and public
  health.
title: Clinical group
from_schema: https://w3id.org/evorao/
is_a: Term
slot_usage:
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known.
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
    - This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies.
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    domain_of:
    - ClinicalGroup
    - CommonName
    - AlternateName
    - Taxon
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  taxon:
    name: taxon
    description: Scientifically classified group or entity within the reference taxonomy.
    title: taxon
    close_mappings:
    - schema:taxonomicRange
    - dwc:taxonID
    - dwc:toTaxon
    related_mappings:
    - dwc:Taxon
    domain_of:
    - ClinicalGroup
    - Taxonomy
    - PathogenIdentification
    range: Taxon
    required: false
    multivalued: true
attributes:
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known.
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
    - This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies.
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    rank: 1000
    alias: alternateName
    owner: ClinicalGroup
    domain_of:
    - ClinicalGroup
    - CommonName
    - AlternateName
    - Taxon
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  taxon:
    name: taxon
    description: Scientifically classified group or entity within the reference taxonomy.
    title: taxon
    comments:
    - The taxon of the highest rank known that can be used to classify a pathogen
      or group of pathogens (e.g viruses) in the reference taxonomy.
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - schema:taxonomicRange
    - dwc:taxonID
    - dwc:toTaxon
    related_mappings:
    - dwc:Taxon
    rank: 1000
    alias: taxon
    owner: ClinicalGroup
    domain_of:
    - ClinicalGroup
    - Taxonomy
    - PathogenIdentification
    range: Taxon
    required: false
    multivalued: true
  title:
    name: title
    description: A name given to the resource.
    title: title
    comments:
    - The title of the item should be as short and descriptive as possible.
    - 'E.g. for virus products it should basically be based on the following Pattern:
      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature.'
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:name
    - rdfs:label
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: ClinicalGroup
    domain_of:
    - Term
    - Dataset
    - DataService
    - Publication
    - License
    - Certification
    - FundingSource
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item.
    title: description
    comments:
    - Describe this item in few lines. This description will serve as a summary to
      present the resource.
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: ClinicalGroup
    domain_of:
    - Term
    - Dataset
    - DataService
    - PersonOrOrganization
    - File
    - ContactPoint
    - License
    - Certification
    - FundingSource
    range: string
    required: false
    recommended: true
    multivalued: false
  weight:
    name: weight
    description: A numerical value indicating relative importance or priority, generally
      processed in ascending order. This weight helps prioritize content when organizing
      or processing data. Its value can be negative, with a default set to 0.
    title: weight
    comments:
    - The lowest weighted Data providers are triggered first.
    - This property may be usefull to populate at first entities that are referenced
      by others (e.g. Version ahead of Rank ahead of Taxon).
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: ClinicalGroup
    domain_of:
    - Term
    - DataProvider
    range: integer
    required: true
    multivalued: false
  inVocabulary:
    name: inVocabulary
    description: Terms belong to a specific vocabulary.
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
    owner: ClinicalGroup
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false
  keyword:
    name: keyword
    description: A keyword or tag describing the resource.
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: ClinicalGroup
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  dateIssued:
    name: dateIssued
    description: Date of formal issuance (e.g., publication) of the resource.
    title: date issued
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME].
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000051
    close_mappings:
    - schema:datePublished
    - schema:dateCreated
    rank: 1000
    slot_uri: dct:issued
    alias: dateIssued
    owner: ClinicalGroup
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  dateModified:
    name: dateModified
    description: Most recent date on which the resource was changed, updated or modified.
    title: date modified
    comments:
    - encoded using the relevant ISO 8601 Date and Time compliant string [DATETIME].
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - sepio:0000036
    close_mappings:
    - schema:dateModified
    rank: 1000
    slot_uri: dct:modified
    alias: dateModified
    owner: ClinicalGroup
    domain_of:
    - Resource
    range: datetime
    required: false
    multivalued: false
  identifier:
    name: identifier
    description: A unique identifier of the resource being described or cataloged.
    title: identifier
    comments:
    - The identifier is a text string which is assigned to the resource to provide
      an unambiguous reference within a particular context. Persistent identifiers
      should be provided as HTTP URIs.
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:identifier
    rank: 1000
    slot_uri: dct:identifier
    alias: identifier
    owner: ClinicalGroup
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true
  iri:
    name: iri
    description: International Resource Identifier (IRI) that uniquely identifies
      or refers to the resource. IRIs include URIs, and URIs include URLs.
    title: IRI
    comments:
    - An IRI is a global identifier standardized by IETF RFC 3987. It may or may not
      be resolvable on the web. IRIs include URIs, and URIs include URLs.
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
    owner: ClinicalGroup
    domain_of:
    - Resource
    range: uri
    required: false
    multivalued: true
  publisher:
    name: publisher
    description: The entity responsible for making the resource available.
    title: publisher
    comments:
    - Resources of type foaf:Agent like EVORAO:PersonOrOrganization are recommended
      as values for this property.
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dct:publisher
    alias: publisher
    owner: ClinicalGroup
    domain_of:
    - Resource
    range: PersonOrOrganization
    required: false
    multivalued: false

```
</details>