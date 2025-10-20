

# Class: Taxon (Taxon) 


_Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit_





URI: [EVORAO:Taxon](https://w3id.org/evorao/Taxon)






```mermaid
 classDiagram
    class Taxon
    click Taxon href "../Taxon"
      Term <|-- Taxon
        click Term href "../Term"
      
      Taxon : alternateName
        
          
    
    
    Taxon --> "*" AlternateName : alternateName
    click AlternateName href "../AlternateName"

        
      Taxon : dateIssued
        
      Taxon : dateModified
        
      Taxon : description
        
      Taxon : externalEquivalentTaxon
        
          
    
    
    Taxon --> "*" Taxon : externalEquivalentTaxon
    click Taxon href "../Taxon"

        
      Taxon : identifier
        
      Taxon : inVocabulary
        
          
    
    
    Taxon --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Taxon : iri
        
      Taxon : keyword
        
      Taxon : parentTaxon
        
          
    
    
    Taxon --> "0..1 _recommended_" Taxon : parentTaxon
    click Taxon href "../Taxon"

        
      Taxon : previouslyKnownAs
        
          
    
    
    Taxon --> "*" Taxon : previouslyKnownAs
    click Taxon href "../Taxon"

        
      Taxon : rank
        
          
    
    
    Taxon --> "0..1 _recommended_" TaxonomicRank : rank
    click TaxonomicRank href "../TaxonomicRank"

        
      Taxon : taxonomicId
        
      Taxon : taxonomicNodeId
        
      Taxon : taxonomy
        
          
    
    
    Taxon --> "* _recommended_" Taxonomy : taxonomy
    click Taxonomy href "../Taxonomy"

        
      Taxon : title
        
      Taxon : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **Taxon**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [taxonomy](taxonomy.md) | * _recommended_ <br/> [Taxonomy](Taxonomy.md) | The taxonomy release(s) in which this entity exists | direct |
| [parentTaxon](parentTaxon.md) | 0..1 _recommended_ <br/> [Taxon](Taxon.md) | The parent taxon of the current taxon | direct |
| [rank](rank.md) | 0..1 _recommended_ <br/> [TaxonomicRank](TaxonomicRank.md) | Relative level or position of the identified taxon in the taxonomy | direct |
| [externalEquivalentTaxon](externalEquivalentTaxon.md) | * <br/> [Taxon](Taxon.md) | Any equivalent taxon in a different taxonomy if exists/known to serve as a br... | direct |
| [taxonomicId](taxonomicId.md) | 1 <br/> [String](String.md) | The taxonomic identifier as a persistent identifier accross releases | direct |
| [taxonomicNodeId](taxonomicNodeId.md) | 0..1 _recommended_ <br/> [String](String.md) | The taxonomic_Node Identifier as an identifier specific the current taxon in ... | direct |
| [alternateName](alternateName.md) | * <br/> [AlternateName](AlternateName.md) | Any other name under which the entity can be known | direct |
| [previouslyKnownAs](previouslyKnownAs.md) | * <br/> [Taxon](Taxon.md) | Any historic version of this taxon having a different name | direct |
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
| [Taxonomy](Taxonomy.md) | [taxon](taxon.md) | range | [Taxon](Taxon.md) |
| [PathogenIdentification](PathogenIdentification.md) | [taxon](taxon.md) | range | [Taxon](Taxon.md) |
| [Taxon](Taxon.md) | [parentTaxon](parentTaxon.md) | range | [Taxon](Taxon.md) |
| [Taxon](Taxon.md) | [externalEquivalentTaxon](externalEquivalentTaxon.md) | range | [Taxon](Taxon.md) |
| [Taxon](Taxon.md) | [previouslyKnownAs](previouslyKnownAs.md) | range | [Taxon](Taxon.md) |
| [ClinicalGroup](ClinicalGroup.md) | [taxon](taxon.md) | range | [Taxon](Taxon.md) |






## Comments

* The taxonomic taxons connected to their parent so that a full lienage can be rebuild. Use of Data provider recommended

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Taxon |
| native | EVORAO:Taxon |
| exact | schema:Taxon, schema:Taxon |
| close | wd:Q16521, dwc:Taxon, uniprotrdfs:Taxon, wd:Q16521, dwc:Taxon, uniprotrdfs:Taxon |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Taxon
description: Conceptual entity that groups one or more populations of an organism
  or organisms, as seen by taxonomists, to form a unit
title: Taxon
comments:
- The taxonomic taxons connected to their parent so that a full lienage can be rebuild.
  Use of Data provider recommended
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:Taxon
- schema:Taxon
close_mappings:
- wd:Q16521
- dwc:Taxon
- uniprotrdfs:Taxon
- wd:Q16521
- dwc:Taxon
- uniprotrdfs:Taxon
is_a: Term
slots:
- taxonomy
- parentTaxon
- rank
- externalEquivalentTaxon
- taxonomicId
- taxonomicNodeId
- alternateName
- previouslyKnownAs
slot_usage:
  taxonomy:
    name: taxonomy
    description: The taxonomy release(s) in which this entity exists
    title: taxonomy
    broad_mappings:
    - dct:isPartOf
    domain_of:
    - Taxon
    - TaxonomicRank
    range: Taxonomy
    required: false
    recommended: true
    multivalued: true
  parentTaxon:
    name: parentTaxon
    description: The parent taxon of the current taxon
    title: parent taxon
    exact_mappings:
    - schema:parentTaxon
    close_mappings:
    - wdp:P171
    broad_mappings:
    - dwc:Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    recommended: true
    multivalued: false
  rank:
    name: rank
    description: Relative level or position of the identified taxon in the taxonomy
    title: rank
    exact_mappings:
    - wdp:P105
    close_mappings:
    - dwc:taxonRank
    - schema:taxonRank
    - biolink:has_taxonomic_rank
    related_mappings:
    - taxrank:1000000
    - ncbitaxon:has_rank
    domain_of:
    - Taxon
    - Taxonomy
    range: TaxonomicRank
    required: false
    recommended: true
    multivalued: false
  externalEquivalentTaxon:
    name: externalEquivalentTaxon
    description: Any equivalent taxon in a different taxonomy if exists/known to serve
      as a bridge (e.g, ICTV towards NCBI)
    title: external equivalent taxon
    comments:
    - Could serve as a bridge between ICTV and NCBI as several providers currently
      uses NCBI Taxonomy
    close_mappings:
    - dwc:taxonID
    related_mappings:
    - dct:references
    domain_of:
    - Taxon
    range: Taxon
    required: false
    multivalued: true
  taxonomicId:
    name: taxonomicId
    description: The taxonomic identifier as a persistent identifier accross releases
    title: taxonomic ID
    exact_mappings:
    - dwc:taxonID
    narrow_mappings:
    - ncit:P331
    broad_mappings:
    - schema:identifier
    - dct:identifier
    is_a: identifier
    domain_of:
    - Taxon
    range: string
    required: true
    multivalued: false
  taxonomicNodeId:
    name: taxonomicNodeId
    description: The taxonomic_Node Identifier as an identifier specific the current
      taxon in the corresponding release/version of the taxonomy
    title: taxonomic node ID
    comments:
    - NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in
      ICTV= Key of the taxon node !! Could be replaced by a composite key made of
      'taxonomic ID' + 'has version'
    close_mappings:
    - dwc:taxonID
    broad_mappings:
    - dct:identifier
    is_a: identifier
    domain_of:
    - Taxon
    range: string
    required: false
    recommended: true
    multivalued: false
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    domain_of:
    - Taxon
    - CommonName
    - AlternateName
    - ClinicalGroup
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  previouslyKnownAs:
    name: previouslyKnownAs
    description: Any historic version of this taxon having a different name
    title: previously known as
    deprecated: EVORAO:previouslyKnownAs is deprecated in favor of alternateName.
      The property required complementary information linked to a Taxon, which limited
      its applicability. alternateName provides broader support for historical and
      non-historical alternative names without requiring taxonomic context
    related_mappings:
    - schema:alternateName
    broad_mappings:
    - dwc:Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Taxon
description: Conceptual entity that groups one or more populations of an organism
  or organisms, as seen by taxonomists, to form a unit
title: Taxon
comments:
- The taxonomic taxons connected to their parent so that a full lienage can be rebuild.
  Use of Data provider recommended
from_schema: https://w3id.org/evorao/
exact_mappings:
- schema:Taxon
- schema:Taxon
close_mappings:
- wd:Q16521
- dwc:Taxon
- uniprotrdfs:Taxon
- wd:Q16521
- dwc:Taxon
- uniprotrdfs:Taxon
is_a: Term
slot_usage:
  taxonomy:
    name: taxonomy
    description: The taxonomy release(s) in which this entity exists
    title: taxonomy
    broad_mappings:
    - dct:isPartOf
    domain_of:
    - Taxon
    - TaxonomicRank
    range: Taxonomy
    required: false
    recommended: true
    multivalued: true
  parentTaxon:
    name: parentTaxon
    description: The parent taxon of the current taxon
    title: parent taxon
    exact_mappings:
    - schema:parentTaxon
    close_mappings:
    - wdp:P171
    broad_mappings:
    - dwc:Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    recommended: true
    multivalued: false
  rank:
    name: rank
    description: Relative level or position of the identified taxon in the taxonomy
    title: rank
    exact_mappings:
    - wdp:P105
    close_mappings:
    - dwc:taxonRank
    - schema:taxonRank
    - biolink:has_taxonomic_rank
    related_mappings:
    - taxrank:1000000
    - ncbitaxon:has_rank
    domain_of:
    - Taxon
    - Taxonomy
    range: TaxonomicRank
    required: false
    recommended: true
    multivalued: false
  externalEquivalentTaxon:
    name: externalEquivalentTaxon
    description: Any equivalent taxon in a different taxonomy if exists/known to serve
      as a bridge (e.g, ICTV towards NCBI)
    title: external equivalent taxon
    comments:
    - Could serve as a bridge between ICTV and NCBI as several providers currently
      uses NCBI Taxonomy
    close_mappings:
    - dwc:taxonID
    related_mappings:
    - dct:references
    domain_of:
    - Taxon
    range: Taxon
    required: false
    multivalued: true
  taxonomicId:
    name: taxonomicId
    description: The taxonomic identifier as a persistent identifier accross releases
    title: taxonomic ID
    exact_mappings:
    - dwc:taxonID
    narrow_mappings:
    - ncit:P331
    broad_mappings:
    - schema:identifier
    - dct:identifier
    is_a: identifier
    domain_of:
    - Taxon
    range: string
    required: true
    multivalued: false
  taxonomicNodeId:
    name: taxonomicNodeId
    description: The taxonomic_Node Identifier as an identifier specific the current
      taxon in the corresponding release/version of the taxonomy
    title: taxonomic node ID
    comments:
    - NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in
      ICTV= Key of the taxon node !! Could be replaced by a composite key made of
      'taxonomic ID' + 'has version'
    close_mappings:
    - dwc:taxonID
    broad_mappings:
    - dct:identifier
    is_a: identifier
    domain_of:
    - Taxon
    range: string
    required: false
    recommended: true
    multivalued: false
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    domain_of:
    - Taxon
    - CommonName
    - AlternateName
    - ClinicalGroup
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  previouslyKnownAs:
    name: previouslyKnownAs
    description: Any historic version of this taxon having a different name
    title: previously known as
    deprecated: EVORAO:previouslyKnownAs is deprecated in favor of alternateName.
      The property required complementary information linked to a Taxon, which limited
      its applicability. alternateName provides broader support for historical and
      non-historical alternative names without requiring taxonomic context
    related_mappings:
    - schema:alternateName
    broad_mappings:
    - dwc:Taxon
    domain_of:
    - Taxon
    range: Taxon
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
    owner: Taxon
    domain_of:
    - Taxon
    - TaxonomicRank
    range: Taxonomy
    required: false
    recommended: true
    multivalued: true
  parentTaxon:
    name: parentTaxon
    description: The parent taxon of the current taxon
    title: parent taxon
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:parentTaxon
    close_mappings:
    - wdp:P171
    broad_mappings:
    - dwc:Taxon
    rank: 1000
    alias: parentTaxon
    owner: Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    recommended: true
    multivalued: false
  rank:
    name: rank
    description: Relative level or position of the identified taxon in the taxonomy
    title: rank
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - wdp:P105
    close_mappings:
    - dwc:taxonRank
    - schema:taxonRank
    - biolink:has_taxonomic_rank
    related_mappings:
    - taxrank:1000000
    - ncbitaxon:has_rank
    rank: 1000
    alias: rank
    owner: Taxon
    domain_of:
    - Taxon
    - Taxonomy
    range: TaxonomicRank
    required: false
    recommended: true
    multivalued: false
  externalEquivalentTaxon:
    name: externalEquivalentTaxon
    description: Any equivalent taxon in a different taxonomy if exists/known to serve
      as a bridge (e.g, ICTV towards NCBI)
    title: external equivalent taxon
    comments:
    - Could serve as a bridge between ICTV and NCBI as several providers currently
      uses NCBI Taxonomy
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - dwc:taxonID
    related_mappings:
    - dct:references
    rank: 1000
    alias: externalEquivalentTaxon
    owner: Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    multivalued: true
  taxonomicId:
    name: taxonomicId
    description: The taxonomic identifier as a persistent identifier accross releases
    title: taxonomic ID
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - dwc:taxonID
    narrow_mappings:
    - ncit:P331
    broad_mappings:
    - schema:identifier
    - dct:identifier
    rank: 1000
    is_a: identifier
    alias: taxonomicId
    owner: Taxon
    domain_of:
    - Taxon
    range: string
    required: true
    multivalued: false
  taxonomicNodeId:
    name: taxonomicNodeId
    description: The taxonomic_Node Identifier as an identifier specific the current
      taxon in the corresponding release/version of the taxonomy
    title: taxonomic node ID
    comments:
    - NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in
      ICTV= Key of the taxon node !! Could be replaced by a composite key made of
      'taxonomic ID' + 'has version'
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - dwc:taxonID
    broad_mappings:
    - dct:identifier
    rank: 1000
    is_a: identifier
    alias: taxonomicNodeId
    owner: Taxon
    domain_of:
    - Taxon
    range: string
    required: false
    recommended: true
    multivalued: false
  alternateName:
    name: alternateName
    description: Any other name under which the entity can be known
    title: alternate name
    comments:
    - This includes previous names, acronyms, former taxonomic terms, and other variations.
      This information can serve as keywords for search purposes and as a bridge with
      other projects that use different naming systems or taxonomies
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:alternateName
    - dct:alternative
    - iao:0000118
    close_mappings:
    - wdp:P4970
    rank: 1000
    alias: alternateName
    owner: Taxon
    domain_of:
    - Taxon
    - CommonName
    - AlternateName
    - ClinicalGroup
    - Organization
    range: AlternateName
    required: false
    multivalued: true
  previouslyKnownAs:
    name: previouslyKnownAs
    description: Any historic version of this taxon having a different name
    title: previously known as
    deprecated: EVORAO:previouslyKnownAs is deprecated in favor of alternateName.
      The property required complementary information linked to a Taxon, which limited
      its applicability. alternateName provides broader support for historical and
      non-historical alternative names without requiring taxonomic context
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - schema:alternateName
    broad_mappings:
    - dwc:Taxon
    rank: 1000
    alias: previouslyKnownAs
    owner: Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
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
    owner: Taxon
    domain_of:
    - Resource
    range: uri
    required: false
    multivalued: true

```
</details>