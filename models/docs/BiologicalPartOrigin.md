
# Class: BiologicalPartOrigin

Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material

URI: [EVORA:BiologicalPartOrigin](https://evora-project.eu/BiologicalPartOrigin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SyntheticPartOrigin],[RecombinantPartIdentification],[NaturalPartOrigin],[Dataset],[RecombinantPartIdentification]<recombinantPartIdentification%200..1-++[BiologicalPartOrigin&#124;accessToPhysicalGeneticResource:boolean],[BiologicalMaterialOrigin]++-%20biologicalPartOrigin%201..*>[BiologicalPartOrigin],[BiologicalPartOrigin]^-[SyntheticPartOrigin],[BiologicalPartOrigin]^-[NaturalPartOrigin],[Dataset]^-[BiologicalPartOrigin],[BiologicalMaterialOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SyntheticPartOrigin],[RecombinantPartIdentification],[NaturalPartOrigin],[Dataset],[RecombinantPartIdentification]<recombinantPartIdentification%200..1-++[BiologicalPartOrigin&#124;accessToPhysicalGeneticResource:boolean],[BiologicalMaterialOrigin]++-%20biologicalPartOrigin%201..*>[BiologicalPartOrigin],[BiologicalPartOrigin]^-[SyntheticPartOrigin],[BiologicalPartOrigin]^-[NaturalPartOrigin],[Dataset]^-[BiologicalPartOrigin],[BiologicalMaterialOrigin])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Children

 * [NaturalPartOrigin](NaturalPartOrigin.md) - Information on the origin of a natural part that composes the biological material
 * [SyntheticPartOrigin](SyntheticPartOrigin.md) - Information on the origin of a synthetic part that composes the biological material

## Referenced by Class

 *  **[BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)** *[BiologicalMaterialOrigin➞biologicalPartOrigin](BiologicalMaterialOrigin_biologicalPartOrigin.md)*  <sub>1..\*</sub>  **[BiologicalPartOrigin](BiologicalPartOrigin.md)**

## Attributes


### Own

 * [BiologicalPartOrigin➞recombinantPartIdentification](BiologicalPartOrigin_recombinantPartIdentification.md)  <sub>0..1</sub>
     * Description: Identification of a recombinant part
     * Range: [RecombinantPartIdentification](RecombinantPartIdentification.md)
 * [BiologicalPartOrigin➞accessToPhysicalGeneticResource](BiologicalPartOrigin_accessToPhysicalGeneticResource.md)  <sub>1..1</sub>
     * Description: Reference of the permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
     * Range: [Boolean](types/Boolean.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Biological part origin |