
# Class: PlasmidSelection

The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers

URI: [EVORA:PlasmidSelection](https://evora-project.eu/PlasmidSelection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[NucleicAcid]++-%20pasmidSelection%200..*>[PlasmidSelection&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[PlasmidSelection],[NucleicAcid])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[NucleicAcid]++-%20pasmidSelection%200..*>[PlasmidSelection&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Term]^-[PlasmidSelection],[NucleicAcid])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[NucleicAcid](NucleicAcid.md)** *[Nucleic Acid➞pasmidSelection](Nucleic_Acid_pasmidSelection.md)*  <sub>0..\*</sub>  **[PlasmidSelection](PlasmidSelection.md)**

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
| **Aliases:** | | Plasmid selection |