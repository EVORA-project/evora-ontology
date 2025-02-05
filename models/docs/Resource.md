

# Class: Resource (Resource)


_Resource published or curated by a single agent._




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [EVORAO:Resource](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Resource)






```mermaid
 classDiagram
    class Resource
    click Resource href "../Resource"
      Resource <|-- Dataset
        click Dataset href "../Dataset"
      Resource <|-- DataService
        click DataService href "../DataService"
      Resource <|-- Version
        click Version href "../Version"
      Resource <|-- Publication
        click Publication href "../Publication"
      Resource <|-- Term
        click Term href "../Term"
      Resource <|-- ExternalRelatedReference
        click ExternalRelatedReference href "../ExternalRelatedReference"
      Resource <|-- SequenceReference
        click SequenceReference href "../SequenceReference"
      Resource <|-- PersonOrOrganization
        click PersonOrOrganization href "../PersonOrOrganization"
      Resource <|-- File
        click File href "../File"
      Resource <|-- ContactPoint
        click ContactPoint href "../ContactPoint"
      Resource <|-- License
        click License href "../License"
      Resource <|-- Certification
        click Certification href "../Certification"
      
      
```





## Inheritance
* **Resource**
    * [Dataset](Dataset.md)
    * [DataService](DataService.md)
    * [Version](Version.md)
    * [Publication](Publication.md)
    * [Term](Term.md)
    * [ExternalRelatedReference](ExternalRelatedReference.md)
    * [SequenceReference](SequenceReference.md)
    * [PersonOrOrganization](PersonOrOrganization.md)
    * [File](File.md)
    * [ContactPoint](ContactPoint.md)
    * [License](License.md)
    * [Certification](Certification.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |









## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Resource |
| native | EVORAO:Resource |
| exact | dcat:Resource, dcat:Resource |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Resource
description: Resource published or curated by a single agent.
title: Resource
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:Resource
- dcat:Resource
abstract: true

```
</details>

### Induced

<details>
```yaml
name: Resource
description: Resource published or curated by a single agent.
title: Resource
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
exact_mappings:
- dcat:Resource
- dcat:Resource
abstract: true

```
</details>