
# Class: DOI

A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard

URI: [EVORA:DOI](https://evora-project.eu/DOI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Publication],[ProductOrService],[ProductOrService]++-%20relatedDOI%200..*>[DOI&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Publication]++-%20relatedDOI%201..1>[DOI],[Term]^-[DOI])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Publication],[ProductOrService],[ProductOrService]++-%20relatedDOI%200..*>[DOI&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Publication]++-%20relatedDOI%201..1>[DOI],[Term]^-[DOI])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞relatedDOI](ProductOrService_relatedDOI.md)*  <sub>0..\*</sub>  **[DOI](DOI.md)**
 *  **[Publication](Publication.md)** *[Publication➞relatedDOI](Publication_relatedDOI.md)*  <sub>1..1</sub>  **[DOI](DOI.md)**

## Attributes


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
| **Aliases:** | | DOI |
| **Close Mappings:** | | wd:Q25670 |