

# Class: Image (Image) 


_Subclass of File representing visual content such as pictures, diagrams, or illustrations_





URI: [EVORAO:Image](https://w3id.org/evorao/Image)






```mermaid
 classDiagram
    class Image
    click Image href "../Image"
      File <|-- Image
        click File href "../File"
      
      Image : altText
        
      Image : contentURL
        
      Image : description
        
      Image : format
        
      Image : license
        
          
    
    
    Image --> "0..1" License : license
    click License href "../License"

        
      Image : name
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [File](File.md)
        * **Image**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [altText](altText.md) | 0..1 _recommended_ <br/> [String](String.md) | An alternate text for the image, if the image cannot be displayed | direct |
| [name](name.md) | 1 <br/> [String](String.md) | A word or set of words used to identify and refer to an entity | [File](File.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [File](File.md) |
| [contentURL](contentURL.md) | 1 <br/> [Uri](Uri.md) | The web address or location where the file content is stored and can be acces... | [File](File.md) |
| [format](format.md) | 1 <br/> [String](String.md) | The file type or format that indicates how the data within the file is struct... | [File](File.md) |
| [license](license.md) | 0..1 <br/> [License](License.md) | Information about terms and conditions under which the subject can be used, s... | [File](File.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PersonOrOrganization](PersonOrOrganization.md) | [logo](logo.md) | range | [Image](Image.md) |
| [Person](Person.md) | [logo](logo.md) | range | [Image](Image.md) |
| [Organization](Organization.md) | [logo](logo.md) | range | [Image](Image.md) |
| [RI](RI.md) | [logo](logo.md) | range | [Image](Image.md) |
| [Provider](Provider.md) | [logo](logo.md) | range | [Image](Image.md) |
| [Originator](Originator.md) | [logo](logo.md) | range | [Image](Image.md) |
| [ProductOrService](ProductOrService.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Service](Service.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Product](Product.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Antibody](Antibody.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Hybridoma](Hybridoma.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Protein](Protein.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [NucleicAcid](NucleicAcid.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [DetectionKit](DetectionKit.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Bundle](Bundle.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Pathogen](Pathogen.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Virus](Virus.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Bacterium](Bacterium.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Fungus](Fungus.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Protozoan](Protozoan.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Viroid](Viroid.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [Prion](Prion.md) | [productPicture](productPicture.md) | range | [Image](Image.md) |
| [License](License.md) | [logo](logo.md) | range | [Image](Image.md) |
| [Certification](Certification.md) | [logo](logo.md) | range | [Image](Image.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Image |
| native | EVORAO:Image |
| close | wd:Q860625, wd:Q860625 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Image
description: Subclass of File representing visual content such as pictures, diagrams,
  or illustrations
title: Image
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q860625
- wd:Q860625
is_a: File
slots:
- altText
slot_usage:
  altText:
    name: altText
    description: An alternate text for the image, if the image cannot be displayed
    title: alt text
    domain_of:
    - Image
    range: string
    required: false
    recommended: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Image
description: Subclass of File representing visual content such as pictures, diagrams,
  or illustrations
title: Image
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q860625
- wd:Q860625
is_a: File
slot_usage:
  altText:
    name: altText
    description: An alternate text for the image, if the image cannot be displayed
    title: alt text
    domain_of:
    - Image
    range: string
    required: false
    recommended: true
    multivalued: false
attributes:
  altText:
    name: altText
    description: An alternate text for the image, if the image cannot be displayed
    title: alt text
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: altText
    owner: Image
    domain_of:
    - Image
    range: string
    required: false
    recommended: true
    multivalued: false
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
    owner: Image
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
    owner: Image
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
  contentURL:
    name: contentURL
    description: The web address or location where the file content is stored and
      can be accessed or downloaded.
    title: content URL
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: contentURL
    owner: Image
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
    owner: Image
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
    owner: Image
    domain_of:
    - File
    - DataProvider
    range: License
    required: false
    multivalued: false

```
</details>