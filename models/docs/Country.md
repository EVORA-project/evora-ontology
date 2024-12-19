
# Class: Country

The country as of ISO3166

URI: [EVORA:Country](https://evora-project.eu/Country)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Organization],[NaturalPartOrigin],[ContactPoint]++-%20addressCountry%200..1>[Country&#124;alpha2Code:string;weight(i):integer;name(i):string;description(i):string%20%3F],[NaturalPartOrigin]++-%20countryOfCollection%201..1>[Country],[Organization]++-%20country%200..1>[Country],[Term]^-[Country],[ContactPoint])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Organization],[NaturalPartOrigin],[ContactPoint]++-%20addressCountry%200..1>[Country&#124;alpha2Code:string;weight(i):integer;name(i):string;description(i):string%20%3F],[NaturalPartOrigin]++-%20countryOfCollection%201..1>[Country],[Organization]++-%20country%200..1>[Country],[Term]^-[Country],[ContactPoint])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[ContactPoint](ContactPoint.md)** *[ContactPoint➞addressCountry](ContactPoint_addressCountry.md)*  <sub>0..1</sub>  **[Country](Country.md)**
 *  **[NaturalPartOrigin](NaturalPartOrigin.md)** *[NaturalPartOrigin➞countryOfCollection](NaturalPartOrigin_countryOfCollection.md)*  <sub>1..1</sub>  **[Country](Country.md)**
 *  **[Organization](Organization.md)** *[Organization➞country](Organization_country.md)*  <sub>0..1</sub>  **[Country](Country.md)**

## Attributes


### Own

 * [Country➞alpha2Code](Country_alpha2Code.md)  <sub>1..1</sub>
     * Description: Two-letter country codes from ISO 3166-1 alpha-2
     * Range: [String](types/String.md)

### Inherited from Term:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)
 * [Term➞weight](Term_weight.md)  <sub>1..1</sub>
     * Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
     * Range: [Integer](types/Integer.md)
 * [Term➞inVocabulary](Term_inVocabulary.md)  <sub>1..1</sub>
     * Description: Terms belong to a specific vocabulary
     * Range: [Vocabulary](Vocabulary.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Country |
| **Comments:** | | Use of Data provider recommended... serve as a local cache for ISO3166 |
| **Close Mappings:** | | wd:Q6256 |