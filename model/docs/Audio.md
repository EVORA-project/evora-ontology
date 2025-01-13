

# Class: Audio


_Subclass of File representing sound recordings or audio tracks_





URI: [EVORA:Audio](https://evora-project.eu/Audio)






```mermaid
 classDiagram
    class Audio
    click Audio href "../Audio"
      File <|-- Audio
        click File href "../File"
      
      Audio : contentURL
        
      Audio : description
        
      Audio : format
        
      Audio : license
        
          
    
    
    Audio --> "0..1" License : license
    click License href "../License"

        
      Audio : name
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [File](File.md)
        * **Audio**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [contentURL](contentURL.md) | 1 <br/> [Uri](Uri.md) | The web address or location where the file content is stored and can be acces... | [File](File.md) |
| [format](format.md) | 1 <br/> [String](String.md) | The file type or format that indicates how the data within the file is struct... | [File](File.md) |
| [license](license.md) | 0..1 <br/> [License](License.md) | The legal terms and conditions under which the file can be used, shared, or d... | [File](File.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |







## Aliases


* Audio



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Audio |
| native | EVORA:Audio |
| close | wd:Q26987229 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Audio
description: Subclass of File representing sound recordings or audio tracks
from_schema: https://evora-project.eu/
aliases:
- Audio
close_mappings:
- wd:Q26987229
is_a: File

```
</details>

### Induced

<details>
```yaml
name: Audio
description: Subclass of File representing sound recordings or audio tracks
from_schema: https://evora-project.eu/
aliases:
- Audio
close_mappings:
- wd:Q26987229
is_a: File
attributes:
  contentURL:
    name: contentURL
    description: The web address or location where the file content is stored and
      can be accessed or downloaded.
    from_schema: https://evora-project.eu/
    aliases:
    - content URL
    rank: 1000
    alias: contentURL
    owner: Audio
    domain_of:
    - File
    range: uri
    required: true
    multivalued: false
  format:
    name: format
    description: The file type or format that indicates how the data within the file
      is structured
    from_schema: https://evora-project.eu/
    aliases:
    - format
    rank: 1000
    alias: format
    owner: Audio
    domain_of:
    - File
    range: string
    required: true
    multivalued: false
  license:
    name: license
    description: The legal terms and conditions under which the file can be used,
      shared, or distributed, indicating any restrictions or permissions.
    from_schema: https://evora-project.eu/
    aliases:
    - license
    rank: 1000
    alias: license
    owner: Audio
    domain_of:
    - DataProvider
    - File
    range: License
    required: false
    multivalued: false
  name:
    name: name
    description: The label that allows humans to identify the current item
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      "Virus name", "virus host type", "collection year", "country of collection"
      ex "suspected epidemiological origin", "genotype", "strain", "variant name or
      specific feature"'
    from_schema: https://evora-project.eu/
    aliases:
    - name
    exact_mappings:
    - dct:title
    close_mappings:
    - rdfs:label
    rank: 1000
    alias: name
    owner: Audio
    domain_of:
    - Nameable
    range: string
    required: true
    multivalued: false
  description:
    name: description
    description: A short explanation of the characteristics, features, or nature of
      the current item
    comments:
    - 'Describe this item in few lines. This description will serve as a summary to
      present the item.

      '
    from_schema: https://evora-project.eu/
    aliases:
    - description
    exact_mappings:
    - dct:description
    rank: 1000
    alias: description
    owner: Audio
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>