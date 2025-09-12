

# Class: Risk group (RiskGroup) 


_Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence_





URI: [EVORAO:RiskGroup](https://w3id.org/evorao/RiskGroup)






```mermaid
 classDiagram
    class RiskGroup
    click RiskGroup href "../RiskGroup"
      Term <|-- RiskGroup
        click Term href "../Term"
      
      RiskGroup : description
        
      RiskGroup : inVocabulary
        
          
    
    
    RiskGroup --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      RiskGroup : title
        
      RiskGroup : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **RiskGroup**



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
| [ProductOrService](ProductOrService.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Service](Service.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Product](Product.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Antibody](Antibody.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Hybridoma](Hybridoma.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Protein](Protein.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [NucleicAcid](NucleicAcid.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [DetectionKit](DetectionKit.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Bundle](Bundle.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Pathogen](Pathogen.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Virus](Virus.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Bacterium](Bacterium.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Fungus](Fungus.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Protozoan](Protozoan.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Viroid](Viroid.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |
| [Prion](Prion.md) | [riskGroup](riskGroup.md) | range | [RiskGroup](RiskGroup.md) |






## Comments

* Use of Data provider if any or manual import of information from wd:Q125449389, wd:Q125449412, wd:Q125449429, wd:Q125449439

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:RiskGroup |
| native | EVORAO:RiskGroup |
| exact | wd:Q125449255, wd:Q125449255 |
| broad | ncit:C95347, ncit:C95347 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskGroup
description: Risk group classification guides initial handling of biological agents
  in labs but doesn't systematically equate to biosafety levels. Actual risk varies
  with the agent, procedures, and personnel competence
title: Risk group
comments:
- Use of Data provider if any or manual import of information from wd:Q125449389,
  wd:Q125449412, wd:Q125449429, wd:Q125449439
from_schema: https://w3id.org/evorao/
exact_mappings:
- wd:Q125449255
- wd:Q125449255
broad_mappings:
- ncit:C95347
- ncit:C95347
is_a: Term

```
</details>

### Induced

<details>
```yaml
name: RiskGroup
description: Risk group classification guides initial handling of biological agents
  in labs but doesn't systematically equate to biosafety levels. Actual risk varies
  with the agent, procedures, and personnel competence
title: Risk group
comments:
- Use of Data provider if any or manual import of information from wd:Q125449389,
  wd:Q125449412, wd:Q125449429, wd:Q125449439
from_schema: https://w3id.org/evorao/
exact_mappings:
- wd:Q125449255
- wd:Q125449255
broad_mappings:
- ncit:C95347
- ncit:C95347
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
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
    owner: RiskGroup
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>