

# Class: License


_The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions_





URI: [EVORA:License](https://evora-project.eu/License)






```mermaid
 classDiagram
    class License
    click License href "../License"
      Nameable <|-- License
        click Nameable href "../Nameable"
      
      License : description
        
      License : licensingOrAttribution
        
      License : logo
        
          
    
    
    License --> "0..1" Image : logo
    click Image href "../Image"

        
      License : name
        
      License : resourceURL
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * **License**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [resourceURL](resourceURL.md) | 0..1 <br/> [Uri](Uri.md) | The web address or location where the details or content is stored and can be... | direct |
| [licensingOrAttribution](licensingOrAttribution.md) | 0..1 <br/> [String](String.md) | A text or html code that provides any related data sharing licence and/or att... | direct |
| [logo](logo.md) | 0..1 <br/> [Image](Image.md) | A path or URL to the related logo | direct |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DataProvider](DataProvider.md) | [license](license.md) | range | [License](License.md) |
| [File](File.md) | [license](license.md) | range | [License](License.md) |
| [Data](Data.md) | [license](license.md) | range | [License](License.md) |
| [Document](Document.md) | [license](license.md) | range | [License](License.md) |
| [Audio](Audio.md) | [license](license.md) | range | [License](License.md) |
| [Video](Video.md) | [license](license.md) | range | [License](License.md) |
| [Image](Image.md) | [license](license.md) | range | [License](License.md) |




## Aliases


* License



## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:License |
| native | EVORA:License |
| exact | dct:RightsStatement |
| close | wd:Q79719, dct:LicenseDocument |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: License
description: The legal terms and conditions under which the subject can be used, shared,
  or distributed, indicating any restrictions or permissions
from_schema: https://evora-project.eu/
aliases:
- License
exact_mappings:
- dct:RightsStatement
close_mappings:
- wd:Q79719
- dct:LicenseDocument
is_a: Nameable
slots:
- resourceURL
- licensingOrAttribution
- logo
slot_usage:
  resourceURL:
    name: resourceURL
    description: The web address or location where the details or content is stored
      and can be accessed or downloaded.
    aliases:
    - resource URL
    exact_mappings:
    - dct:license
    close_mappings:
    - schema:url
    range: uri
    required: false
    multivalued: false
  licensingOrAttribution:
    name: licensingOrAttribution
    description: A text or html code that provides any related data sharing licence
      and/or attribution
    aliases:
    - licensing or attribution
    exact_mappings:
    - dct:rights
    close_mappings:
    - schema:license
    range: string
    required: false
    multivalued: false
  logo:
    name: logo
    description: A path or URL to the related logo
    aliases:
    - logo
    range: Image
    required: false
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: License
description: The legal terms and conditions under which the subject can be used, shared,
  or distributed, indicating any restrictions or permissions
from_schema: https://evora-project.eu/
aliases:
- License
exact_mappings:
- dct:RightsStatement
close_mappings:
- wd:Q79719
- dct:LicenseDocument
is_a: Nameable
slot_usage:
  resourceURL:
    name: resourceURL
    description: The web address or location where the details or content is stored
      and can be accessed or downloaded.
    aliases:
    - resource URL
    exact_mappings:
    - dct:license
    close_mappings:
    - schema:url
    range: uri
    required: false
    multivalued: false
  licensingOrAttribution:
    name: licensingOrAttribution
    description: A text or html code that provides any related data sharing licence
      and/or attribution
    aliases:
    - licensing or attribution
    exact_mappings:
    - dct:rights
    close_mappings:
    - schema:license
    range: string
    required: false
    multivalued: false
  logo:
    name: logo
    description: A path or URL to the related logo
    aliases:
    - logo
    range: Image
    required: false
    multivalued: false
attributes:
  resourceURL:
    name: resourceURL
    description: The web address or location where the details or content is stored
      and can be accessed or downloaded.
    from_schema: https://evora-project.eu/
    aliases:
    - resource URL
    exact_mappings:
    - dct:license
    close_mappings:
    - schema:url
    rank: 1000
    alias: resourceURL
    owner: License
    domain_of:
    - License
    - Certification
    range: uri
    required: false
    multivalued: false
  licensingOrAttribution:
    name: licensingOrAttribution
    description: A text or html code that provides any related data sharing licence
      and/or attribution
    from_schema: https://evora-project.eu/
    aliases:
    - licensing or attribution
    exact_mappings:
    - dct:rights
    close_mappings:
    - schema:license
    rank: 1000
    alias: licensingOrAttribution
    owner: License
    domain_of:
    - License
    range: string
    required: false
    multivalued: false
  logo:
    name: logo
    description: A path or URL to the related logo
    from_schema: https://evora-project.eu/
    aliases:
    - logo
    rank: 1000
    alias: logo
    owner: License
    domain_of:
    - PersonOrOrganization
    - License
    - Certification
    range: Image
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
    owner: License
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
    owner: License
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>