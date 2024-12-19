
# Class: VirusName

A virus vernacular name or a name that describes a group of viruses

URI: [EVORA:VirusName](https://evora-project.eu/VirusName)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Virus]++-%20coInfectingViruses%200..*>[VirusName&#124;sourceOfInformation(i):string%20*;weight(i):integer;name(i):string;description(i):string%20%3F],[CommonName]^-[VirusName],[Virus],[CommonName],[AlternateName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Virus]++-%20coInfectingViruses%200..*>[VirusName&#124;sourceOfInformation(i):string%20*;weight(i):integer;name(i):string;description(i):string%20%3F],[CommonName]^-[VirusName],[Virus],[CommonName],[AlternateName])

## Parents

 *  is_a: [CommonName](CommonName.md) - Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name

## Referenced by Class

 *  **[Virus](Virus.md)** *[Virus➞coInfectingViruses](Virus_coInfectingViruses.md)*  <sub>0..\*</sub>  **[VirusName](VirusName.md)**

## Attributes


### Inherited from CommonName:

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
 * [CommonName➞alternateName](CommonName_alternateName.md)  <sub>0..\*</sub>
     * Description: Any known alternate name related to this name
     * Range: [AlternateName](AlternateName.md)
 * [CommonName➞sourceOfInformation](CommonName_sourceOfInformation.md)  <sub>0..\*</sub>
     * Description: The name of the origin from which knowledge is obtained. This can include any entity that provides information
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Virus Name |
| **Close Mappings:** | | wd:Q125481078 |