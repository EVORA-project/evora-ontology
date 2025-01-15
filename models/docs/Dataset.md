

# Class: Dataset (Dataset)


_A collection of data, published or curated by a single agent, and available for access_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [EVORAO:Dataset](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Dataset)






```mermaid
 classDiagram
    class Dataset
    click Dataset href "../Dataset"
      Dataset <|-- Version
        click Version href "../Version"
      Dataset <|-- PathogenIdentification
        click PathogenIdentification href "../PathogenIdentification"
      Dataset <|-- Publication
        click Publication href "../Publication"
      Dataset <|-- ExternalRelatedReference
        click ExternalRelatedReference href "../ExternalRelatedReference"
      Dataset <|-- Sequence
        click Sequence href "../Sequence"
      Dataset <|-- SequenceReference
        click SequenceReference href "../SequenceReference"
      Dataset <|-- BiologicalMaterialOrigin
        click BiologicalMaterialOrigin href "../BiologicalMaterialOrigin"
      Dataset <|-- BiologicalPartOrigin
        click BiologicalPartOrigin href "../BiologicalPartOrigin"
      Dataset <|-- MSDS
        click MSDS href "../MSDS"
      
      
```





## Inheritance
* **Dataset**
    * [Version](Version.md)
    * [PathogenIdentification](PathogenIdentification.md)
    * [Publication](Publication.md)
    * [ExternalRelatedReference](ExternalRelatedReference.md)
    * [Sequence](Sequence.md)
    * [SequenceReference](SequenceReference.md)
    * [BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)
    * [BiologicalPartOrigin](BiologicalPartOrigin.md)
    * [MSDS](MSDS.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Dataset |
| native | EVORAO:Dataset |
| exact | dcat:Dataset |
| close | wd:Q1172284, schema:DataCatalog |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Dataset
description: A collection of data, published or curated by a single agent, and available
  for access
title: Dataset
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:Dataset
close_mappings:
- wd:Q1172284
- schema:DataCatalog
abstract: true

```
</details>

### Induced

<details>
```yaml
name: Dataset
description: A collection of data, published or curated by a single agent, and available
  for access
title: Dataset
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:Dataset
close_mappings:
- wd:Q1172284
- schema:DataCatalog
abstract: true

```
</details>