
# Class: SyntheticPartOrigin

Information on the origin of a synthetic part that composes the biological material

URI: [EVORA:SyntheticPartOrigin](https://evora-project.eu/SyntheticPartOrigin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BiologicalPartOrigin]^-[SyntheticPartOrigin&#124;modificationsFromTheReferenceSequences:boolean;descriptionOfModificationsMadeFromTheReferenceSequences:string%20%3F;accessToPhysicalGeneticResource(i):boolean],[RecombinantPartIdentification],[BiologicalPartOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[BiologicalPartOrigin]^-[SyntheticPartOrigin&#124;modificationsFromTheReferenceSequences:boolean;descriptionOfModificationsMadeFromTheReferenceSequences:string%20%3F;accessToPhysicalGeneticResource(i):boolean],[RecombinantPartIdentification],[BiologicalPartOrigin])

## Parents

 *  is_a: [BiologicalPartOrigin](BiologicalPartOrigin.md) - Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material

## Referenced by Class


## Attributes


### Own

 * [SyntheticPartOrigin➞modificationsFromTheReferenceSequences](SyntheticPartOrigin_modificationsFromTheReferenceSequences.md)  <sub>1..1</sub>
     * Description: Set to TRUE if there was is any modification made from the reference sequence
     * Range: [Boolean](types/Boolean.md)
 * [SyntheticPartOrigin➞descriptionOfModificationsMadeFromTheReferenceSequences](SyntheticPartOrigin_descriptionOfModificationsMadeFromTheReferenceSequences.md)  <sub>0..1</sub>
     * Description: List the modifications mades from the reference sequence if any
     * Range: [String](types/String.md)

### Inherited from BiologicalPartOrigin:

 * [BiologicalPartOrigin➞recombinantPartIdentification](BiologicalPartOrigin_recombinantPartIdentification.md)  <sub>0..1</sub>
     * Description: Identification of a recombinant part
     * Range: [RecombinantPartIdentification](RecombinantPartIdentification.md)
 * [BiologicalPartOrigin➞accessToPhysicalGeneticResource](BiologicalPartOrigin_accessToPhysicalGeneticResource.md)  <sub>1..1</sub>
     * Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
     * Range: [Boolean](types/Boolean.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Synthetic part origin |