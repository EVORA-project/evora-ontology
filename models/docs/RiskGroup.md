

# Class: Risk group (RiskGroup)


_Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence_





URI: [EVORAO:RiskGroup](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#RiskGroup)






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

        
      RiskGroup : name
        
      RiskGroup : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **RiskGroup**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Term](Term.md) |
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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:RiskGroup |
| native | EVORAO:RiskGroup |
| close | wd:Q125449255 |







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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q125449255
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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q125449255
is_a: Term
attributes:
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
    owner: RiskGroup
    domain_of:
    - Term
    - DataService
    - Catalogue
    - PersonOrOrganization
    - ProductOrService
    - File
    - ContactPoint
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
      present the item.

      '
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: RiskGroup
    domain_of:
    - Term
    - DataService
    - Catalogue
    - PersonOrOrganization
    - ProductOrService
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    close_mappings:
    - wdp:P972
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