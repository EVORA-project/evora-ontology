

# Class: Country


_The country as of ISO3166_





URI: [EVORA:Country](https://evora-project.eu/Country)






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

        
      Country : name
        
      Country : weight
        
      
```





## Inheritance
* [Nameable](Nameable.md)
    * [NamedDataset](NamedDataset.md)
        * [Term](Term.md)
            * **Country**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [alpha2Code](alpha2Code.md) | 1 <br/> [String](String.md) | Two-letter country codes from ISO 3166-1 alpha-2 | direct |
| [weight](weight.md) | 1 <br/> [Integer](Integer.md) | A numerical value indicating relative importance or priority, generally proce... | [Term](Term.md) |
| [inVocabulary](inVocabulary.md) | 1 <br/> [Vocabulary](Vocabulary.md) | Terms belong to a specific vocabulary | [Term](Term.md) |
| [name](name.md) | 1 <br/> [String](String.md) | The label that allows humans to identify the current item | [Nameable](Nameable.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A short explanation of the characteristics, features, or nature of the curren... | [Nameable](Nameable.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Organization](Organization.md) | [country](country.md) | range | [Country](Country.md) |
| [RI](RI.md) | [country](country.md) | range | [Country](Country.md) |
| [Provider](Provider.md) | [country](country.md) | range | [Country](Country.md) |
| [NaturalPartOrigin](NaturalPartOrigin.md) | [countryOfCollection](countryOfCollection.md) | range | [Country](Country.md) |
| [ContactPoint](ContactPoint.md) | [addressCountry](addressCountry.md) | range | [Country](Country.md) |




## Aliases


* Country



## Comments

* Use of Data provider recommended... serve as a local cache for ISO3166

## Identifier and Mapping Information







### Schema Source


* from schema: https://evora-project.eu/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | EVORA:Country |
| native | EVORA:Country |
| close | wd:Q6256 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Country
description: The country as of ISO3166
comments:
- Use of Data provider recommended... serve as a local cache for ISO3166
from_schema: https://evora-project.eu/
aliases:
- Country
close_mappings:
- wd:Q6256
is_a: Term
slots:
- alpha2Code
slot_usage:
  alpha2Code:
    name: alpha2Code
    description: Two-letter country codes from ISO 3166-1 alpha-2
    aliases:
    - alpha-2 code
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
comments:
- Use of Data provider recommended... serve as a local cache for ISO3166
from_schema: https://evora-project.eu/
aliases:
- Country
close_mappings:
- wd:Q6256
is_a: Term
slot_usage:
  alpha2Code:
    name: alpha2Code
    description: Two-letter country codes from ISO 3166-1 alpha-2
    aliases:
    - alpha-2 code
    range: string
    required: true
    multivalued: false
attributes:
  alpha2Code:
    name: alpha2Code
    description: Two-letter country codes from ISO 3166-1 alpha-2
    from_schema: https://evora-project.eu/
    aliases:
    - alpha-2 code
    rank: 1000
    alias: alpha2Code
    owner: Country
    domain_of:
    - Country
    range: string
    required: true
    multivalued: false
  weight:
    name: weight
    description: A numerical value indicating relative importance or priority, generally
      processed in ascending order. This weight helps prioritize content when organizing
      or processing data. Its value can be negative, with a default set to 0
    from_schema: https://evora-project.eu/
    aliases:
    - weight
    close_mappings:
    - adms:status
    rank: 1000
    ifabsent: int(0)
    alias: weight
    owner: Country
    domain_of:
    - DataProvider
    - Term
    range: integer
    required: true
    multivalued: false
  inVocabulary:
    name: inVocabulary
    description: Terms belong to a specific vocabulary
    from_schema: https://evora-project.eu/
    aliases:
    - in Vocabulary
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
    owner: Country
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
    owner: Country
    domain_of:
    - Nameable
    range: string
    required: false
    multivalued: false

```
</details>