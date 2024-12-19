
# Class: ProteinTag

Peptide sequence genetically grafted onto a recombinant protein

URI: [EVORA:ProteinTag](https://evora-project.eu/ProteinTag)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[NucleicAcid]++-%20hasTAG%201..1>[ProteinTag&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Protein]++-%20proteinTAG%200..*>[ProteinTag],[Term]^-[ProteinTag],[Protein],[NucleicAcid])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[NucleicAcid]++-%20hasTAG%201..1>[ProteinTag&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Protein]++-%20proteinTAG%200..*>[ProteinTag],[Term]^-[ProteinTag],[Protein],[NucleicAcid])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[NucleicAcid](NucleicAcid.md)** *[Nucleic Acid➞hasTAG](Nucleic_Acid_hasTAG.md)*  <sub>1..1</sub>  **[ProteinTag](ProteinTag.md)**
 *  **[Protein](Protein.md)** *[Protein➞proteinTAG](Protein_proteinTAG.md)*  <sub>0..\*</sub>  **[ProteinTag](ProteinTag.md)**

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
| **Aliases:** | | Protein tag |
| **Close Mappings:** | | wd:Q645590 |