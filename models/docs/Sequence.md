
# Class: Sequence

A nucleic acid or protein sequence information

URI: [EVORA:Sequence](https://evora-project.eu/Sequence)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceReference],[SequenceReference]<sequenceReference%200..*-++[Sequence&#124;sequenceFASTA:string%20%3F],[NucleicAcid]++-%20sequence%201..*>[Sequence],[Pathogen]++-%20sequence%201..*>[Sequence],[Protein]++-%20sequence%201..*>[Sequence],[RecombinantPartIdentification]++-%20sequence%201..*>[Sequence],[Dataset]^-[Sequence],[RecombinantPartIdentification],[Protein],[Pathogen],[NucleicAcid],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequenceReference],[SequenceReference]<sequenceReference%200..*-++[Sequence&#124;sequenceFASTA:string%20%3F],[NucleicAcid]++-%20sequence%201..*>[Sequence],[Pathogen]++-%20sequence%201..*>[Sequence],[Protein]++-%20sequence%201..*>[Sequence],[RecombinantPartIdentification]++-%20sequence%201..*>[Sequence],[Dataset]^-[Sequence],[RecombinantPartIdentification],[Protein],[Pathogen],[NucleicAcid],[Dataset])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[NucleicAcid](NucleicAcid.md)** *[Nucleic Acid➞sequence](Nucleic_Acid_sequence.md)*  <sub>1..\*</sub>  **[Sequence](Sequence.md)**
 *  **[Pathogen](Pathogen.md)** *[Pathogen➞sequence](Pathogen_sequence.md)*  <sub>1..\*</sub>  **[Sequence](Sequence.md)**
 *  **[Protein](Protein.md)** *[Protein➞sequence](Protein_sequence.md)*  <sub>1..\*</sub>  **[Sequence](Sequence.md)**
 *  **[RecombinantPartIdentification](RecombinantPartIdentification.md)** *[RecombinantPartIdentification➞sequence](RecombinantPartIdentification_sequence.md)*  <sub>1..\*</sub>  **[Sequence](Sequence.md)**

## Attributes


### Own

 * [Sequence➞sequenceReference](Sequence_sequenceReference.md)  <sub>0..\*</sub>
     * Description: A reference that permits to retrieve the sequence information from a sequence provider
     * Range: [SequenceReference](SequenceReference.md)
 * [Sequence➞sequenceFASTA](Sequence_sequenceFASTA.md)  <sub>0..1</sub>
     * Description: In case no sequence reference exists in public repositories, the corresponding FASTA sequence is required
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Sequence |
| **Close Mappings:** | | wd:Q3511065 |