

# Class: Document (Document)


_Subclass of File representing textual or written files such as reports, manuals, or forms_





URI: [EVORAO:Document](https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#Document)






```mermaid
 classDiagram
    class Document
    click Document href "../Document"
      File <|-- Document
        click File href "../File"
      
      Document : contentURL
        
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
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [File](File.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [File](File.md) |
| [contentURL](contentURL.md) | 1 <br/> [Uri](Uri.md) | The web address or location where the file content is stored and can be acces... | [File](File.md) |
| [format](format.md) | 1 <br/> [String](String.md) | The file type or format that indicates how the data within the file is struct... | [File](File.md) |
| [license](license.md) | 0..1 <br/> [License](License.md) | The legal terms and conditions under which the file can be used, shared, or d... | [File](File.md) |





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


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Document |
| native | EVORAO:Document |
| close | wd:Q49848 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Document
description: Subclass of File representing textual or written files such as reports,
  manuals, or forms
title: Document
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
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
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
close_mappings:
- wd:Q49848
is_a: File
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
    owner: Document
    domain_of:
    - File
    - DataService
    - Catalogue
    - Term
    - PersonOrOrganization
    - ProductOrService
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
    owner: Document
    domain_of:
    - File
    - DataService
    - Catalogue
    - Term
    - PersonOrOrganization
    - ProductOrService
    - ContactPoint
    - License
    - Certification
    range: string
    required: false
    recommended: true
    multivalued: false
  contentURL:
    name: contentURL
    description: The web address or location where the file content is stored and
      can be accessed or downloaded.
    title: content URL
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
    rank: 1000
    alias: contentURL
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
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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
    description: The legal terms and conditions under which the file can be used,
      shared, or distributed, indicating any restrictions or permissions.
    title: license
    from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
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