
# Class: GeographicalOrigin

The specific location or region where a physical item, originates or is naturally found

URI: [EVORA:GeographicalOrigin](https://evora-project.eu/GeographicalOrigin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Pathogen],[IPLCOrigin],[Pathogen]++-%20suspectedEpidemiologicalOrigin%200..*>[GeographicalOrigin&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[GeographicalOrigin]^-[IPLCOrigin],[Term]^-[GeographicalOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Pathogen],[IPLCOrigin],[Pathogen]++-%20suspectedEpidemiologicalOrigin%200..*>[GeographicalOrigin&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[GeographicalOrigin]^-[IPLCOrigin],[Term]^-[GeographicalOrigin])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Children

 * [IPLCOrigin](IPLCOrigin.md) - The IPLC area (Indigenous People and Local Communities) from which a physical item, originates or is naturally found

## Referenced by Class

 *  **[Pathogen](Pathogen.md)** *[Pathogen➞suspectedEpidemiologicalOrigin](Pathogen_suspectedEpidemiologicalOrigin.md)*  <sub>0..\*</sub>  **[GeographicalOrigin](GeographicalOrigin.md)**

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
| **Aliases:** | | Geographical origin |
| **Comments:** | | geonames.org API could be a good service data provider as suggested by DCAT-AP |
| **Exact Mappings:** | | dct:Location |
| **Close Mappings:** | | wd:Q3885844 |