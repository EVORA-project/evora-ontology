
# Class: SequenceReference

A reference that permits to retrieve the sequence information from a sequence provider

URI: [EVORA:SequenceReference](https://evora-project.eu/SequenceReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Antibody]++-%20sequenceReference%200..*>[SequenceReference&#124;accessionNumber:string;sequenceProvider:string],[Sequence]++-%20sequenceReference%200..*>[SequenceReference],[Dataset]^-[SequenceReference],[Sequence],[Dataset],[Antibody])](https://yuml.me/diagram/nofunky;dir:TB/class/[Antibody]++-%20sequenceReference%200..*>[SequenceReference&#124;accessionNumber:string;sequenceProvider:string],[Sequence]++-%20sequenceReference%200..*>[SequenceReference],[Dataset]^-[SequenceReference],[Sequence],[Dataset],[Antibody])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[Antibody](Antibody.md)** *[Antibody➞sequenceReference](Antibody_sequenceReference.md)*  <sub>0..\*</sub>  **[SequenceReference](SequenceReference.md)**
 *  **[Sequence](Sequence.md)** *[Sequence➞sequenceReference](Sequence_sequenceReference.md)*  <sub>0..\*</sub>  **[SequenceReference](SequenceReference.md)**

## Attributes


### Own

 * [SequenceReference➞accessionNumber](SequenceReference_accessionNumber.md)  <sub>1..1</sub>
     * Description: The sequence ID that permits to retrieve the sequence information from the sequence provider
     * Range: [String](types/String.md)
 * [SequenceReference➞sequenceProvider](SequenceReference_sequenceProvider.md)  <sub>1..1</sub>
     * Description: The name of the sequence provider within the list of accepted sequence providers
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Sequence reference |
| **Comments:** | | A work on making it a subclass of External related reference might be consistent and beneficial for data structuration but special attention will have to be take to ensure it remains consistent with the actual the use cases for users |