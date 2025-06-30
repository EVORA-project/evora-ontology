

# Class: Country (Country) 


_The country as of ISO3166_





URI: [EVORAO:Country](https://w3id.org/evorao/Country)






```mermaid
 classDiagram
    class Country
    click Country href "../Country"
      Term <|-- Country
        click Term href "../Term"
      
      Country : alpha2Code
        
      Country : description
        
      Country : inVocabulary
        
          
    
    
    Country --> "1" Vocabulary : inVocabulary
    click Vocabulary href "../Vocabulary"

        
      Country : title
        
      Country : weight
        
      
```





## Inheritance
* [Resource](Resource.md)
    * [Term](Term.md)
        * **Country**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alpha2Code](alpha2Code.md) | 1 <br/> [String](String.md) | Two-letter country codes from ISO 3166-1 alpha-2 | direct |
| [title](title.md) | 1 <br/> [String](String.md) | A name given to the resource | [Term](Term.md) |
| [description](description.md) | 0..1 _recommended_ <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Term](Term.md) |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Organization](Organization.md) | [country](country.md) | range | [Country](Country.md) |
| [RI](RI.md) | [country](country.md) | range | [Country](Country.md) |
| [Provider](Provider.md) | [country](country.md) | range | [Country](Country.md) |
| [NaturalPartOrigin](NaturalPartOrigin.md) | [countryOfCollection](countryOfCollection.md) | range | [Country](Country.md) |
| [ContactPoint](ContactPoint.md) | [addressCountry](addressCountry.md) | range | [Country](Country.md) |






## Comments

* Use of Data provider recommended... serve as a local cache for ISO3166

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/evorao/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORAO:Country |
| native | EVORAO:Country |
| close | wd:Q6256, wd:Q6256 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Country
description: The country as of ISO3166
title: Country
comments:
- Use of Data provider recommended... serve as a local cache for ISO3166
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q6256
- wd:Q6256
is_a: Term
slots:
- alpha2Code
slot_usage:
  alpha2Code:
    name: alpha2Code
    description: Two-letter country codes from ISO 3166-1 alpha-2
    title: alpha-2 code
    domain_of:
    - Country
    range: string
    required: true
    multivalued: false

```
</details>

### Induced

<details>
```yaml
name: Country
description: The country as of ISO3166
title: Country
comments:
- Use of Data provider recommended... serve as a local cache for ISO3166
from_schema: https://w3id.org/evorao/
close_mappings:
- wd:Q6256
- wd:Q6256
is_a: Term
slot_usage:
  alpha2Code:
    name: alpha2Code
    description: Two-letter country codes from ISO 3166-1 alpha-2
    title: alpha-2 code
    domain_of:
    - Country
    range: string
    required: true
    multivalued: false
attributes:
  alpha2Code:
    name: alpha2Code
    description: Two-letter country codes from ISO 3166-1 alpha-2
    title: alpha-2 code
    from_schema: https://w3id.org/evorao/
    rank: 1000
    alias: alpha2Code
    owner: Country
    domain_of:
    - Country
    range: string
    required: true
    multivalued: false
  title:
    name: title
    description: A name given to the resource
    title: title
    comments:
    - 'The title of the item should be as short and descriptive as possible. E.g.
      for virus products it should basically be based on the following Pattern:

      ''Virus name'', ''virus host type'', ''collection year'', ''country of collection''
      ex ''suspected epidemiological origin'', ''genotype'', ''strain'', ''variant
      name or specific feature'
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - rdfs:label
    - schema:name
    rank: 1000
    slot_uri: dct:title
    alias: title
    owner: Country
    domain_of:
    - Term
    - Dataset
    - DataService
    - Publication
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
    owner: Country
    domain_of:
    - Term
    - Dataset
    - DataService
    - PersonOrOrganization
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
    comments:
    - The lowest weighted Data providers are triggered first, this may be usefull
      to populate at first entities that are referenced by others (e.g. Version ahead
      of Rank ahead of Taxon)
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: Country
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
    from_schema: https://w3id.org/evorao/
    close_mappings:
    - wdp:P972
    rank: 1000
    alias: inVocabulary
    owner: Country
    domain_of:
    - Term
    range: Vocabulary
    required: true
    multivalued: false

```
</details>