

# Class: Version (Version) 


_Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)_





URI: [EVORAO:Version](https://w3id.org/evorao/Version)






```mermaid
 classDiagram
    class Version
    click Version href "../Version"
      Resource <|-- Version
        click Resource href "../Resource"
      
      Version : ID
        
      Version : versionOf
        
          
    
    
    Version --> "1" Dataset : versionOf
    click Dataset href "../Dataset"

        
      
```





## Inheritance
* [Resource](Resource.md)
    * **Version**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ID](ID.md) | 1 <br/> [String](String.md) | The version identifier | direct |
| [versionOf](versionOf.md) | 1 <br/> [Dataset](Dataset.md) | Identifier of what the version qualifies | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Taxonomy](Taxonomy.md) | [version](version.md) | range | [Version](Version.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Version |
| native | EVORAO:Version |
| close | wd:Q114469879, wd:Q114469879 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Version
description: Numeric code assigned to identify a particular historical version of
  a work (e.g. software or technical standards)
title: Version
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q114469879
- wd:Q114469879
is_a: Resource
slots:
- ID
- versionOf
slot_usage:
  ID:
    name: ID
    description: The version identifier
    title: ID
    close_mappings:
    - wdp:P393
    - schema:version
    domain_of:
    - Version
    range: string
    required: true
    multivalued: false
  versionOf:
    name: versionOf
    description: Identifier of what the version qualifies
    title: version Of
    domain_of:
    - Version
    range: Dataset
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Version
description: Numeric code assigned to identify a particular historical version of
  a work (e.g. software or technical standards)
title: Version
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q114469879
- wd:Q114469879
is_a: Resource
slot_usage:
  ID:
    name: ID
    description: The version identifier
    title: ID
    close_mappings:
    - wdp:P393
    - schema:version
    domain_of:
    - Version
    range: string
    required: true
    multivalued: false
  versionOf:
    name: versionOf
    description: Identifier of what the version qualifies
    title: version Of
    domain_of:
    - Version
    range: Dataset
    required: true
    multivalued: false
attributes:
  ID:
    name: ID
    description: The version identifier
    title: ID
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - wdp:P393
    - schema:version
    rank: 1000
    alias: ID
    owner: Version
    domain_of:
    - Version
    range: string
    required: true
    multivalued: false
  versionOf:
    name: versionOf
    description: Identifier of what the version qualifies
    title: version Of
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: versionOf
    owner: Version
    domain_of:
    - Version
    range: Dataset
    required: true
    multivalued: false

```
</details>