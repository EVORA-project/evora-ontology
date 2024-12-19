
# Class: Term

Word or phrase from a specialized area of knowledge

URI: [EVORA:Term](https://evora-project.eu/Term)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[TransmissionMethod],[Vocabulary]<inVocabulary%201..1-++[Term&#124;weight:integer;name(i):string;description(i):string%20%3F],[Vocabulary]++-%20term%200..*>[Term],[Term]^-[TransmissionMethod],[Term]^-[TaxonomicRank],[Term]^-[Taxon],[Term]^-[SpecialFeature],[Term]^-[RiskGroup],[Term]^-[ProteinTag],[Term]^-[PropagationHost],[Term]^-[ProductionCellLine],[Term]^-[ProductCategory],[Term]^-[PlasmidSelection],[Term]^-[PDBReference],[Term]^-[Keyword],[Term]^-[Journal],[Term]^-[IsolationHost],[Term]^-[IATAClassification],[Term]^-[GeographicalOrigin],[Term]^-[ExpressionVector],[Term]^-[DOI],[Term]^-[Country],[Term]^-[CommonName],[Term]^-[AlternateName],[NamedDataset]^-[Term],[TaxonomicRank],[Taxon],[SpecialFeature],[RiskGroup],[ProteinTag],[PropagationHost],[ProductionCellLine],[ProductCategory],[PlasmidSelection],[PDBReference],[NamedDataset],[Keyword],[Journal],[IsolationHost],[IATAClassification],[GeographicalOrigin],[ExpressionVector],[DOI],[Country],[CommonName],[AlternateName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[TransmissionMethod],[Vocabulary]<inVocabulary%201..1-++[Term&#124;weight:integer;name(i):string;description(i):string%20%3F],[Vocabulary]++-%20term%200..*>[Term],[Term]^-[TransmissionMethod],[Term]^-[TaxonomicRank],[Term]^-[Taxon],[Term]^-[SpecialFeature],[Term]^-[RiskGroup],[Term]^-[ProteinTag],[Term]^-[PropagationHost],[Term]^-[ProductionCellLine],[Term]^-[ProductCategory],[Term]^-[PlasmidSelection],[Term]^-[PDBReference],[Term]^-[Keyword],[Term]^-[Journal],[Term]^-[IsolationHost],[Term]^-[IATAClassification],[Term]^-[GeographicalOrigin],[Term]^-[ExpressionVector],[Term]^-[DOI],[Term]^-[Country],[Term]^-[CommonName],[Term]^-[AlternateName],[NamedDataset]^-[Term],[TaxonomicRank],[Taxon],[SpecialFeature],[RiskGroup],[ProteinTag],[PropagationHost],[ProductionCellLine],[ProductCategory],[PlasmidSelection],[PDBReference],[NamedDataset],[Keyword],[Journal],[IsolationHost],[IATAClassification],[GeographicalOrigin],[ExpressionVector],[DOI],[Country],[CommonName],[AlternateName])

## Parents

 *  is_a: [NamedDataset](NamedDataset.md) - A collection of data, that has a name and can have a description, published or curated by a single agent, and available for access

## Children

 * [AlternateName](AlternateName.md) - List of alternate names for things
 * [CommonName](CommonName.md) - Vernacular name that is the name used in everyday language to refer to an organism or group of organisms. This name is typically easier to remember and pronounce compared to the scientific name
 * [Country](Country.md) - The country as of ISO3166
 * [DOI](DOI.md) - A unique string identifier assigned to a digital object, providing a permanent link for reliable citation and access.  The Digital Object Identifier (DOI) is a persistent identifier that is an ISO standard
 * [ExpressionVector](ExpressionVector.md) - A reference to an expression vector plasmid, typically embedding a resistance marker for inducible protein expression
 * [GeographicalOrigin](GeographicalOrigin.md) - The specific location or region where a physical item, originates or is naturally found
 * [IATAClassification](IATAClassification.md) - The corresponding International Air Transport Association (IATA)'s category for dangerous goods that are transported by air
 * [IsolationHost](IsolationHost.md) - Host organism from which the pathogen was isolated
 * [Journal](Journal.md) - Periodical journal publishing scientific research
 * [Keyword](Keyword.md) - A term or phrase used to tag and categorize content
 * [PDBReference](PDBReference.md) - Identifier for 3D structural data as per the PDB (Protein Data Bank) database
 * [PlasmidSelection](PlasmidSelection.md) - The process of identifying cells that have successfully incorporated a plasmid, typically using antibiotic resistance markers
 * [ProductCategory](ProductCategory.md) - A term used to classify a group of products that share common characteristics or functions, which helps in their organization
 * [ProductionCellLine](ProductionCellLine.md) - A population of cells that originates from a primary culture, adapted to grow and divide under laboratory conditions. Used in biotechnology to consistently produce biological substances
 * [PropagationHost](PropagationHost.md) - The organism used to grow and multiply the pathogen under controlled conditions
 * [ProteinTag](ProteinTag.md) - Peptide sequence genetically grafted onto a recombinant protein
 * [RiskGroup](RiskGroup.md) - Risk group classification guides initial handling of biological agents in labs but doesn't systematically equate to biosafety levels. Actual risk varies with the agent, procedures, and personnel competence
 * [SpecialFeature](SpecialFeature.md) - Distinctive attributes of a product that set it apart from other similar items e.g., Reference strain, Vaccinal strain, Antiviral resistant strain ...
 * [Taxon](Taxon.md) - Conceptual entity that groups one or more populations of an organism or organisms, as seen by taxonomists, to form a unit
 * [TaxonomicRank](TaxonomicRank.md) - The possible taxonomic ranks and their description
 * [TransmissionMethod](TransmissionMethod.md) - The process by which the pathogen spreads between hosts

## Referenced by Class

 *  **[Vocabulary](Vocabulary.md)** *[Vocabulary➞term](Vocabulary_term.md)*  <sub>0..\*</sub>  **[Term](Term.md)**

## Attributes


### Own

 * [Term➞weight](Term_weight.md)  <sub>1..1</sub>
     * Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
     * Range: [Integer](types/Integer.md)
 * [Term➞inVocabulary](Term_inVocabulary.md)  <sub>1..1</sub>
     * Description: Terms belong to a specific vocabulary
     * Range: [Vocabulary](Vocabulary.md)

### Inherited from NamedDataset:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Term |
| **Close Mappings:** | | wd:Q1969448 |