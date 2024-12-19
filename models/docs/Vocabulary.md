
# Class: Vocabulary

A subset of words or phrases specific to a particular subject or field

URI: [EVORA:Vocabulary](https://evora-project.eu/Vocabulary)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term]<term%200..*-++[Vocabulary&#124;name(i):string;description(i):string%20%3F],[DataProvider]<termDataProvider%200..1-++[Vocabulary],[Term]++-%20inVocabulary%201..1>[Vocabulary],[Catalogue]^-[Vocabulary],[Term],[DataProvider],[Catalogue])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term]<term%200..*-++[Vocabulary&#124;name(i):string;description(i):string%20%3F],[DataProvider]<termDataProvider%200..1-++[Vocabulary],[Term]++-%20inVocabulary%201..1>[Vocabulary],[Catalogue]^-[Vocabulary],[Term],[DataProvider],[Catalogue])

## Parents

 *  is_a: [Catalogue](Catalogue.md) - A curated collection of metadata about resources

## Referenced by Class

 *  **[Term](Term.md)** *[Term➞inVocabulary](Term_inVocabulary.md)*  <sub>1..1</sub>  **[Vocabulary](Vocabulary.md)**

## Attributes


### Own

 * [Vocabulary➞termDataProvider](Vocabulary_termDataProvider.md)  <sub>0..1</sub>
     * Description: An external API or Endpoint that permits to retrieve the terms of this vocabulary
     * Range: [DataProvider](DataProvider.md)
 * [Vocabulary➞term](Vocabulary_term.md)  <sub>0..\*</sub>
     * Description: The terms related to this vocabulary
     * Range: [Term](Term.md)

### Inherited from Catalogue:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Vocabulary |
| **Close Mappings:** | | wd:Q6499736 |
|  | | skos:Collection |