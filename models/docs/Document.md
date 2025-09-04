

# Class: Document (Document) 


_Subclass of File representing textual or written files such as reports, manuals, or forms_





URI: [EVORAO:Document](https://w3id.org/evorao/Document)






```mermaid
 classDiagram
    class Document
    click Document href "../Document"
      File <|-- Document
        click File href "../File"
      
      Document : contentUrl
        
      Document : description
        
      Document : format
        
      Document : license
        
          
    
    
    Document --> "0..1" License : license
    click License href "../License"

        
      Document : name
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [File](File.md)
        * **Document**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | A word or set of words used to identify and refer to an entity | [File](File.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [File](File.md) |
| [contentUrl](contentUrl.md) | 1 <br/> [Uri](Uri.md) | The web address or location where the file content is stored and can be acces... | [File](File.md) |
| [format](format.md) | 1 <br/> [String](String.md) | The file type or format that indicates how the data within the file is struct... | [File](File.md) |
| [license](license.md) | 0..1 <br/> [License](License.md) | Information about terms and conditions under which the subject can be used, s... | [File](File.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProductOrService](ProductOrService.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Service](Service.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Product](Product.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Antibody](Antibody.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Hybridoma](Hybridoma.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Protein](Protein.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [NucleicAcid](NucleicAcid.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [DetectionKit](DetectionKit.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Bundle](Bundle.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Pathogen](Pathogen.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Virus](Virus.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Bacterium](Bacterium.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Fungus](Fungus.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Protozoan](Protozoan.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Viroid](Viroid.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Prion](Prion.md) | [complementaryDocument](complementaryDocument.md) | range | [Document](Document.md) |
| [Certification](Certification.md) | [certificationDocument](certificationDocument.md) | range | [Document](Document.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Document |
| native | EVORAO:Document |
| close | wd:Q49848, wd:Q49848 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Document
description: Subclass of File representing textual or written files such as reports,
  manuals, or forms
title: Document
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q49848
- wd:Q49848
is_a: File

```
</details>

### Induced

<details>
```yaml
name: Document
description: Subclass of File representing textual or written files such as reports,
  manuals, or forms
title: Document
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q49848
- wd:Q49848
is_a: File
attributes:
  name:
    name: name
    description: A word or set of words used to identify and refer to an entity
    title: name
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:name
    close_mappings:
    - foaf:name
    - dct:title
    rank: 1000
    slot_uri: foaf:name
    alias: name
    owner: Document
    domain_of:
    - File
    - PersonOrOrganization
    - ContactPoint
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
      present the resource.

      '
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - schema:description
    close_mappings:
    - schema:description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: Document
    domain_of:
    - File
    - Dataset
    - DataService
    - Term
    - PersonOrOrganization
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  contentUrl:
    name: contentUrl
    description: The web address or location where the file content is stored and
      can be accessed or downloaded.
    title: content URL
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: contentUrl
    owner: Document
    domain_of:
    - File
    range: uri
    required: true
    multivalued: false
  format:
    name: format
    description: The file type or format that indicates how the data within the file
      is structured
    title: format
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: format
    owner: Document
    domain_of:
    - File
    range: string
    required: true
    multivalued: false
  license:
    name: license
    description: Information about terms and conditions under which the subject can
      be used, shared, or distributed, indicating any restrictions or permissions
    title: license
    from_schema: https://w3id.org/evorao/
    exact_mappings:
    - dct:license
    rank: 1000
    alias: license
    owner: Document
    domain_of:
    - File
    - DataProvider
    range: License
    required: false
    multivalued: false

```
</details>