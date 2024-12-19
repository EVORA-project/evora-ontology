
# Class: CommonName

Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name

URI: [EVORA:CommonName](https://evora-project.eu/CommonName)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[VirusName],[Variant],[Term],[PathogenIdentification],[AlternateName]<alternateName%200..*-++[CommonName&#124;sourceOfInformation:string%20*;weight(i):integer;name(i):string;description(i):string%20%3F],[PathogenIdentification]++-%20pathogenName%201..1>[CommonName],[CommonName]^-[VirusName],[CommonName]^-[Variant],[Term]^-[CommonName],[AlternateName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[VirusName],[Variant],[Term],[PathogenIdentification],[AlternateName]<alternateName%200..*-++[CommonName&#124;sourceOfInformation:string%20*;weight(i):integer;name(i):string;description(i):string%20%3F],[PathogenIdentification]++-%20pathogenName%201..1>[CommonName],[CommonName]^-[VirusName],[CommonName]^-[Variant],[Term]^-[CommonName],[AlternateName])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Children

 * [Variant](Variant.md) - An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain
 * [VirusName](VirusName.md) - A virus vernacular name or a name that describes a group of viruses

## Referenced by Class

 *  **[PathogenIdentification](PathogenIdentification.md)** *[PathogenIdentification➞pathogenName](PathogenIdentification_pathogenName.md)*  <sub>1..1</sub>  **[CommonName](CommonName.md)**

## Attributes


### Own

 * [CommonName➞alternateName](CommonName_alternateName.md)  <sub>0..\*</sub>
     * Description: Any known alternate name related to this name
     * Range: [AlternateName](AlternateName.md)
 * [CommonName➞sourceOfInformation](CommonName_sourceOfInformation.md)  <sub>0..\*</sub>
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
| **Aliases:** | | Common Name |
| **Exact Mappings:** | | dwc:vernacularName |
| **Close Mappings:** | | wd:Q502895 |