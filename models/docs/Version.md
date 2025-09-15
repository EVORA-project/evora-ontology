

# Class: Version (Version) 


_Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)_





URI: [EVORAO:Version](https://w3id.org/evorao/Version)






```mermaid
 classDiagram
    class Version
    click Version href "../Version"
      Resource <|-- Version
        click Resource href "../Resource"
      
      Version : keyword
        
      Version : resource
        
          
    
    
    Version --> "* _recommended_" Resource : resource
    click Resource href "../Resource"

        
      Version : version
        
      Version : versionOf
        
      
```





## Inheritance
* [Resource](Resource.md)
    * **Version**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [version](version.md) | 1 _recommended_ <br/> [String](String.md) | The version indicator (name or identifier) of a resource | direct |
| [versionOf](versionOf.md) | 1 <br/> [String](String.md) | Identifier of what type of entities the version qualifies | direct |
| [resource](resource.md) | * _recommended_ <br/> [Resource](Resource.md) | Resource published or curated by a single agent | direct |
| [keyword](keyword.md) | * <br/> [String](String.md) | A keyword or tag describing the resource | [Resource](Resource.md) |









## Comments

* Represents a specific snapshot/release of a resource (e.g., a dataset). It enables managing multiple versions as first-class nodes and linking each version to its subject via evorao:versionOf and to the using resource via evorao:version (e.g., as nodes in a graph database).

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Version |
| native | EVORAO:Version |
| related | wd:Q114469879, wd:Q114469879 |
| close | reproduceme:Version, reproduceme:Version |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Version
description: Numeric code assigned to identify a particular historical version of
  a work (e.g. software or technical standards)
title: Version
comments:
- Represents a specific snapshot/release of a resource (e.g., a dataset). It enables
  managing multiple versions as first-class nodes and linking each version to its
  subject via evorao:versionOf and to the using resource via evorao:version (e.g.,
  as nodes in a graph database).
from_schema: https://w3id.org/evorao/
close_mappings:
- reproduceme:Version
- reproduceme:Version
related_mappings:
- wd:Q114469879
- wd:Q114469879
is_a: Resource
slots:
- version
- versionOf
- resource
slot_usage:
  version:
    name: version
    description: The version indicator (name or identifier) of a resource
    title: version
    exact_mappings:
    - pav:version
    close_mappings:
    - wdp:P393
    - schema:version
    related_mappings:
    - schema:identifier
    slot_uri: dcat:version
    domain_of:
    - Version
    - Dataset
    - Taxonomy
    range: string
    required: true
    multivalued: false
  versionOf:
    name: versionOf
    description: Identifier of what type of entities the version qualifies
    title: version Of
    related_mappings:
    - dct:isVersionOf
    domain_of:
    - Version
    range: string
    required: true
    multivalued: false
  resource:
    name: resource
    description: Resource published or curated by a single agent
    title: resource
    domain_of:
    - Version
    range: Resource
    required: false
    recommended: true
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: Version
description: Numeric code assigned to identify a particular historical version of
  a work (e.g. software or technical standards)
title: Version
comments:
- Represents a specific snapshot/release of a resource (e.g., a dataset). It enables
  managing multiple versions as first-class nodes and linking each version to its
  subject via evorao:versionOf and to the using resource via evorao:version (e.g.,
  as nodes in a graph database).
from_schema: https://w3id.org/evorao/
close_mappings:
- reproduceme:Version
- reproduceme:Version
related_mappings:
- wd:Q114469879
- wd:Q114469879
is_a: Resource
slot_usage:
  version:
    name: version
    description: The version indicator (name or identifier) of a resource
    title: version
    exact_mappings:
    - pav:version
    close_mappings:
    - wdp:P393
    - schema:version
    related_mappings:
    - schema:identifier
    slot_uri: dcat:version
    domain_of:
    - Version
    - Dataset
    - Taxonomy
    range: string
    required: true
    multivalued: false
  versionOf:
    name: versionOf
    description: Identifier of what type of entities the version qualifies
    title: version Of
    related_mappings:
    - dct:isVersionOf
    domain_of:
    - Version
    range: string
    required: true
    multivalued: false
  resource:
    name: resource
    description: Resource published or curated by a single agent
    title: resource
    domain_of:
    - Version
    range: Resource
    required: false
    recommended: true
    multivalued: true
attributes:
  version:
    name: version
    description: The version indicator (name or identifier) of a resource
    title: version
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - pav:version
    close_mappings:
    - wdp:P393
    - schema:version
    related_mappings:
    - schema:identifier
    rank: 1000
    slot_uri: dcat:version
    alias: version
    owner: Version
    domain_of:
    - Version
    - Dataset
    - Taxonomy
    range: string
    required: true
    recommended: true
    multivalued: false
  versionOf:
    name: versionOf
    description: Identifier of what type of entities the version qualifies
    title: version Of
    from_schema: https://w3id.org/evorao/
    related_mappings:
    - dct:isVersionOf
    rank: 1000
    alias: versionOf
    owner: Version
    domain_of:
    - Version
    range: string
    required: true
    multivalued: false
  resource:
    name: resource
    description: Resource published or curated by a single agent
    title: resource
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: resource
    owner: Version
    domain_of:
    - Version
    range: Resource
    required: false
    recommended: true
    multivalued: true
  keyword:
    name: keyword
    description: A keyword or tag describing the resource
    title: keyword
    from_schema: https://w3id.org/evorao/
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: Version
    domain_of:
    - Resource
    range: string
    required: false
    multivalued: true

```
</details>