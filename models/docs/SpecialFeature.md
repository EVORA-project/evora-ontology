
# Class: SpecialFeature

Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...

URI: [EVORA:SpecialFeature](https://evora-project.eu/SpecialFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Protein]++-%20specialFeature%200..*>[SpecialFeature&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[SpecialFeature],[Protein])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Protein]++-%20specialFeature%200..*>[SpecialFeature&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[SpecialFeature],[Protein])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[Protein](Protein.md)** *[Protein➞specialFeature](Protein_specialFeature.md)*  <sub>0..\*</sub>  **[SpecialFeature](SpecialFeature.md)**

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
| **Aliases:** | | Special feature |
| **Comments:** | | These special features help researchers and professionals in the field to select appropriate virus strains for their specific research needs and applications. |