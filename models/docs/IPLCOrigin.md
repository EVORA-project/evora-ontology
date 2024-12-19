
# Class: IPLCOrigin

The IPLC area (Indigenous People and Local Communities) from which a physical item, originates or is naturally found

URI: [EVORA:IPLCOrigin](https://evora-project.eu/IPLCOrigin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[NaturalPartOrigin],[NaturalPartOrigin]++-%20indigenousPoepleAndLocalCommunityOrigin%200..1>[IPLCOrigin&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[GeographicalOrigin]^-[IPLCOrigin],[GeographicalOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[NaturalPartOrigin],[NaturalPartOrigin]++-%20indigenousPoepleAndLocalCommunityOrigin%200..1>[IPLCOrigin&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[GeographicalOrigin]^-[IPLCOrigin],[GeographicalOrigin])

## Parents

 *  is_a: [GeographicalOrigin](GeographicalOrigin.md) - The specific location or region where a physical item, originates or is naturally found

## Referenced by Class

 *  **[NaturalPartOrigin](NaturalPartOrigin.md)** *[NaturalPartOrigin➞indigenousPoepleAndLocalCommunityOrigin](NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin.md)*  <sub>0..1</sub>  **[IPLCOrigin](IPLCOrigin.md)**

## Attributes


### Inherited from GeographicalOrigin:

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
| **Aliases:** | | IPLC origin |