

# Class: Taxon (Taxon) 


_Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit_





URI: [EVORAO:Taxon](https://w3id.org/evorao/Taxon)






```mermaid
 classDiagram
    class Taxon
    click Taxon href "../Taxon"
      Term <|-- Taxon
        click Term href "../Term"
      
      Taxon : description
        
      Taxon : externalEquivalentTaxon
        
          
    
    
    Taxon --> "*" Taxon : externalEquivalentTaxon
    click Taxon href "../Taxon"

        
      Taxon : inVocabulary
        
          
    
    
    Taxon --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Taxon : parentTaxon
        
          
    
    
    Taxon --> "1" Taxon : parentTaxon
    click Taxon href "../Taxon"

        
      Taxon : previouslyKnownAs
        
          
    
    
    Taxon --> "*" Taxon : previouslyKnownAs
    click Taxon href "../Taxon"

        
      Taxon : rank
        
          
    
    
    Taxon --> "1" TaxonomicRank : rank
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
| [parentTaxon](parentTaxon.md) | 1 <br/> [Taxon](Taxon.md) | The parent taxon of the current taxon | direct |
| [rank](rank.md) | 1 <br/> [TaxonomicRank](TaxonomicRank.md) | Relative level or position of the identified taxon in the taxonomy | direct |
| [previouslyKnownAs](previouslyKnownAs.md) | * <br/> [Taxon](Taxon.md) | Any historic version of this taxon having a different name | direct |
| [externalEquivalentTaxon](externalEquivalentTaxon.md) | * <br/> [Taxon](Taxon.md) | Any equivalent taxon in a different taxonomy if exists/known to serve as a br... | direct |
| [taxonomicId](taxonomicId.md) | 1 <br/> [String](String.md) | The taxonomic identifier as a persistent identifier accross releases | direct |
| [taxonomicNodeId](taxonomicNodeId.md) | 0..1 _recommended_ <br/> [String](String.md) | The taxonomic_Node Identifier as an identifier specific the current taxon in ... | direct |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Taxonomy](Taxonomy.md) | [taxon](taxon.md) | range | [Taxon](Taxon.md) |
| [PathogenIdentification](PathogenIdentification.md) | [taxon](taxon.md) | range | [Taxon](Taxon.md) |
| [Taxon](Taxon.md) | [parentTaxon](parentTaxon.md) | range | [Taxon](Taxon.md) |
| [Taxon](Taxon.md) | [previouslyKnownAs](previouslyKnownAs.md) | range | [Taxon](Taxon.md) |
| [Taxon](Taxon.md) | [externalEquivalentTaxon](externalEquivalentTaxon.md) | range | [Taxon](Taxon.md) |






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
- previouslyKnownAs
- externalEquivalentTaxon
- taxonomicId
- taxonomicNodeId
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
    required: true
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
    required: true
    multivalued: false
  previouslyKnownAs:
    name: previouslyKnownAs
    description: Any historic version of this taxon having a different name
    title: previously known as
    related_mappings:
    - schema:alternateName
    broad_mappings:
    - dwc:Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    multivalued: true
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
    domain_of:
    - Taxon
    range: string
    required: false
    recommended: true
    multivalued: false

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
    required: true
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
    required: true
    multivalued: false
  previouslyKnownAs:
    name: previouslyKnownAs
    description: Any historic version of this taxon having a different name
    title: previously known as
    related_mappings:
    - schema:alternateName
    broad_mappings:
    - dwc:Taxon
    domain_of:
    - Taxon
    range: Taxon
    required: false
    multivalued: true
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
    domain_of:
    - Taxon
    range: string
    required: false
    recommended: true
    multivalued: false
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
    required: true
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
    required: true
    multivalued: false
  previouslyKnownAs:
    name: previouslyKnownAs
    description: Any historic version of this taxon having a different name
    title: previously known as
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
    alias: taxonomicNodeId
    owner: Taxon
    domain_of:
    - Taxon
    range: string
    required: false
    recommended: true
    multivalued: false
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

```
</details>