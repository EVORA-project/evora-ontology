
# Class: AlternateName

List of alternate names for things

URI: [EVORA:AlternateName](https://evora-project.eu/AlternateName)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Organization],[CommonName],[AlternateName]<alternateName%200..*-++[AlternateName&#124;sourceOfInformation:string%20*;weight(i):integer;name(i):string;description(i):string%20%3F],[CommonName]++-%20alternateName%200..*>[AlternateName],[Organization]++-%20alternateName%200..1>[AlternateName],[Term]^-[AlternateName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Organization],[CommonName],[AlternateName]<alternateName%200..*-++[AlternateName&#124;sourceOfInformation:string%20*;weight(i):integer;name(i):string;description(i):string%20%3F],[CommonName]++-%20alternateName%200..*>[AlternateName],[Organization]++-%20alternateName%200..1>[AlternateName],[Term]^-[AlternateName])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[AlternateName](AlternateName.md)** *[AlternateName➞alternateName](AlternateName_alternateName.md)*  <sub>0..\*</sub>  **[AlternateName](AlternateName.md)**
 *  **[CommonName](CommonName.md)** *[CommonName➞alternateName](CommonName_alternateName.md)*  <sub>0..\*</sub>  **[AlternateName](AlternateName.md)**
 *  **[Organization](Organization.md)** *[Organization➞alternateName](Organization_alternateName.md)*  <sub>0..1</sub>  **[AlternateName](AlternateName.md)**

## Attributes


### Own

 * [AlternateName➞alternateName](AlternateName_alternateName.md)  <sub>0..\*</sub>
     * Description: Any known alternate name related to this name
     * Range: [AlternateName](AlternateName.md)
 * [AlternateName➞sourceOfInformation](AlternateName_sourceOfInformation.md)  <sub>0..\*</sub>
     * Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information
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
| **Aliases:** | | Alternate Name |
| **Close Mappings:** | | wd:Q7662595 |