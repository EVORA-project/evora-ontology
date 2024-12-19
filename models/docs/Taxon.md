
# Class: Taxon

Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit

URI: [EVORA:Taxon](https://evora-project.eu/Taxon)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Taxonomy],[TaxonomicRank],[Taxon]<externalEquivalentTaxon%200..*-++[Taxon&#124;taxonomicID:string;taxonomicNodeID:string%20%3F;weight(i):integer;name(i):string;description(i):string%20%3F],[Taxon]<previouslyKnownAs%200..*-++[Taxon],[TaxonomicRank]<rank%201..1-++[Taxon],[Taxon]<parentTaxon%201..1-++[Taxon],[Taxonomy]<taxonomy%200..*-++[Taxon],[PathogenIdentification]++-%20taxon%201..1>[Taxon],[Taxonomy]++-%20taxon%200..*>[Taxon],[Term]^-[Taxon],[PathogenIdentification])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Term],[Taxonomy],[TaxonomicRank],[Taxon]<externalEquivalentTaxon%200..*-++[Taxon&#124;taxonomicID:string;taxonomicNodeID:string%20%3F;weight(i):integer;name(i):string;description(i):string%20%3F],[Taxon]<previouslyKnownAs%200..*-++[Taxon],[TaxonomicRank]<rank%201..1-++[Taxon],[Taxon]<parentTaxon%201..1-++[Taxon],[Taxonomy]<taxonomy%200..*-++[Taxon],[PathogenIdentification]++-%20taxon%201..1>[Taxon],[Taxonomy]++-%20taxon%200..*>[Taxon],[Term]^-[Taxon],[PathogenIdentification])

## Parents

 *  is_a: [Term](Term.md) - Word or phrase from a specialized area of knowledge

## Referenced by Class

 *  **[PathogenIdentification](PathogenIdentification.md)** *[PathogenIdentification➞taxon](PathogenIdentification_taxon.md)*  <sub>1..1</sub>  **[Taxon](Taxon.md)**
 *  **[Taxon](Taxon.md)** *[Taxon➞externalEquivalentTaxon](Taxon_externalEquivalentTaxon.md)*  <sub>0..\*</sub>  **[Taxon](Taxon.md)**
 *  **[Taxon](Taxon.md)** *[Taxon➞parentTaxon](Taxon_parentTaxon.md)*  <sub>1..1</sub>  **[Taxon](Taxon.md)**
 *  **[Taxon](Taxon.md)** *[Taxon➞previouslyKnownAs](Taxon_previouslyKnownAs.md)*  <sub>0..\*</sub>  **[Taxon](Taxon.md)**
 *  **[Taxonomy](Taxonomy.md)** *[Taxonomy➞taxon](Taxonomy_taxon.md)*  <sub>0..\*</sub>  **[Taxon](Taxon.md)**

## Attributes


### Own

 * [Taxon➞taxonomy](Taxon_taxonomy.md)  <sub>0..\*</sub>
     * Description: The taxonomy release(s) in which this entity exists
     * Range: [Taxonomy](Taxonomy.md)
 * [Taxon➞parentTaxon](Taxon_parentTaxon.md)  <sub>1..1</sub>
     * Description: The parent taxon of the current taxon
     * Range: [Taxon](Taxon.md)
 * [Taxon➞rank](Taxon_rank.md)  <sub>1..1</sub>
     * Description: Relative level or position of the identified taxon in the taxonomy
     * Range: [TaxonomicRank](TaxonomicRank.md)
 * [Taxon➞previouslyKnownAs](Taxon_previouslyKnownAs.md)  <sub>0..\*</sub>
     * Description: Any historic version of this taxon having a different name
     * Range: [Taxon](Taxon.md)
 * [Taxon➞externalEquivalentTaxon](Taxon_externalEquivalentTaxon.md)  <sub>0..\*</sub>
     * Description: Any equivalent taxon in a different taxonomy if exists/known to serve as a bridge (e.g, ICTV towards NCBI)
     * Range: [Taxon](Taxon.md)
 * [Taxon➞taxonomicID](Taxon_taxonomicID.md)  <sub>1..1</sub>
     * Description: The taxonomic identifier as a persistent identifier accross releases
     * Range: [String](types/String.md)
 * [Taxon➞taxonomicNodeID](Taxon_taxonomicNodeID.md)  <sub>0..1</sub>
     * Description: The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy
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
| **Aliases:** | | Taxon |
| **Comments:** | | The taxonomic taxons connected to their parent so that a full lienage can be rebuild. Use of Data provider recommended |
| **Exact Mappings:** | | dwc:Taxon |
| **Close Mappings:** | | wd:Q16521 |