
# Class: RecombinantPartIdentification

Identification of a recombinant part

URI: [EVORA:RecombinantPartIdentification](https://evora-project.eu/RecombinantPartIdentification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence],[Sequence]<sequence%201..*-++[RecombinantPartIdentification&#124;partIdentification:string],[BiologicalPartOrigin]++-%20recombinantPartIdentification%200..1>[RecombinantPartIdentification],[BiologicalPartOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sequence],[Sequence]<sequence%201..*-++[RecombinantPartIdentification&#124;partIdentification:string],[BiologicalPartOrigin]++-%20recombinantPartIdentification%200..1>[RecombinantPartIdentification],[BiologicalPartOrigin])

## Referenced by Class

 *  **[BiologicalPartOrigin](BiologicalPartOrigin.md)** *[BiologicalPartOrigin➞recombinantPartIdentification](BiologicalPartOrigin_recombinantPartIdentification.md)*  <sub>0..1</sub>  **[RecombinantPartIdentification](RecombinantPartIdentification.md)**

## Attributes


### Own

 * [RecombinantPartIdentification➞partIdentification](RecombinantPartIdentification_partIdentification.md)  <sub>1..1</sub>
     * Description: A short designation of this recombinant part of the related biological material
     * Range: [String](types/String.md)
 * [RecombinantPartIdentification➞sequence](RecombinantPartIdentification_sequence.md)  <sub>1..\*</sub>
     * Description: The related sequence information from a sequence provider or in fasta format
     * Range: [Sequence](Sequence.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Recombinant part identification |