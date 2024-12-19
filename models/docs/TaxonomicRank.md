
# Class: TaxonomicRank

The possible taxonomic ranks and their description

URI: [EVORA:TaxonomicRank](https://evora-project.eu/TaxonomicRank)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Taxonomy],[Taxonomy]<taxonomy%200..*-++[TaxonomicRank&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Taxon]++-%20rank%201..1>[TaxonomicRank],[Taxonomy]++-%20rank%200..*>[TaxonomicRank],[Term]^-[TaxonomicRank],[Taxon])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Taxonomy],[Taxonomy]<taxonomy%200..*-++[TaxonomicRank&#124;weight(i):integer;name(i):string;description(i):string%20%3F],[Taxon]++-%20rank%201..1>[TaxonomicRank],[Taxonomy]++-%20rank%200..*>[TaxonomicRank],[Term]^-[TaxonomicRank],[Taxon])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[Taxon](Taxon.md)** *[Taxon➞rank](Taxon_rank.md)*  <sub>1..1</sub>  **[TaxonomicRank](TaxonomicRank.md)**
 *  **[Taxonomy](Taxonomy.md)** *[Taxonomy➞rank](Taxonomy_rank.md)*  <sub>0..\*</sub>  **[TaxonomicRank](TaxonomicRank.md)**

## Attributes


### Own

 * [TaxonomicRank➞taxonomy](TaxonomicRank_taxonomy.md)  <sub>0..\*</sub>
     * Description: The taxonomy release(s) in which this entity exists
     * Range: [Taxonomy](Taxonomy.md)

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
| **Aliases:** | | Taxonomic rank |
| **Comments:** | | Use of Data provider recommended |
| **Close Mappings:** | | wd:Q427626 |