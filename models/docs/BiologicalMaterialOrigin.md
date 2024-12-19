
# Class: BiologicalMaterialOrigin

Information about the origin of the biological material, compulsory for access, utilization, and benefit-sharing of genetic resources in compliance with the Nagoya Protocol

URI: [EVORA:BiologicalMaterialOrigin](https://evora-project.eu/BiologicalMaterialOrigin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Protein],[Pathogen],[NucleicAcid],[Dataset],[BiologicalPartOrigin],[BiologicalPartOrigin]<biologicalPartOrigin%201..*-++[BiologicalMaterialOrigin&#124;recombinantMaterial:boolean;biologicalSourceType:boolean;thirdPartyDistributionConsent:boolean%20%3F;usageRestrictions:string%20%3F],[NucleicAcid]++-%20biologicalMaterialOrigin%201..1>[BiologicalMaterialOrigin],[Pathogen]++-%20biologicalMaterialOrigin%201..1>[BiologicalMaterialOrigin],[Protein]++-%20biologicalMaterialOrigin%201..1>[BiologicalMaterialOrigin],[Dataset]^-[BiologicalMaterialOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Protein],[Pathogen],[NucleicAcid],[Dataset],[BiologicalPartOrigin],[BiologicalPartOrigin]<biologicalPartOrigin%201..*-++[BiologicalMaterialOrigin&#124;recombinantMaterial:boolean;biologicalSourceType:boolean;thirdPartyDistributionConsent:boolean%20%3F;usageRestrictions:string%20%3F],[NucleicAcid]++-%20biologicalMaterialOrigin%201..1>[BiologicalMaterialOrigin],[Pathogen]++-%20biologicalMaterialOrigin%201..1>[BiologicalMaterialOrigin],[Protein]++-%20biologicalMaterialOrigin%201..1>[BiologicalMaterialOrigin],[Dataset]^-[BiologicalMaterialOrigin])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[NucleicAcid](NucleicAcid.md)** *[Nucleic Acid➞biologicalMaterialOrigin](Nucleic_Acid_biologicalMaterialOrigin.md)*  <sub>1..1</sub>  **[BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)**
 *  **[Pathogen](Pathogen.md)** *[Pathogen➞biologicalMaterialOrigin](Pathogen_biologicalMaterialOrigin.md)*  <sub>1..1</sub>  **[BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)**
 *  **[Protein](Protein.md)** *[Protein➞biologicalMaterialOrigin](Protein_biologicalMaterialOrigin.md)*  <sub>1..1</sub>  **[BiologicalMaterialOrigin](BiologicalMaterialOrigin.md)**

## Attributes


### Own

 * [BiologicalMaterialOrigin➞recombinantMaterial](BiologicalMaterialOrigin_recombinantMaterial.md)  <sub>1..1</sub>
     * Description: Indicates if this biological material is a recombinant biological material.
     * Range: [Boolean](types/Boolean.md)
 * [BiologicalMaterialOrigin➞biologicalSourceType](BiologicalMaterialOrigin_biologicalSourceType.md)  <sub>1..1</sub>
     * Description: Defines if the current biological material is natural and was collected or if it is a synthetic biological material. It makes sense that only recombinant biological materials can have a mixed material origin!
     * Range: [Boolean](types/Boolean.md)
 * [BiologicalMaterialOrigin➞biologicalPartOrigin](BiologicalMaterialOrigin_biologicalPartOrigin.md)  <sub>1..\*</sub>
     * Description: Details the origin of one or more unitary parts that make up the biological material. In the case of recombinant biological material, multiple parts may be involved.
     * Range: [BiologicalPartOrigin](BiologicalPartOrigin.md)
 * [BiologicalMaterialOrigin➞thirdPartyDistributionConsent](BiologicalMaterialOrigin_thirdPartyDistributionConsent.md)  <sub>0..1</sub>
     * Description: Indicates whether the biological material can be distributed to third parties, considering any potential concerns about to the related genetic material as indicated by the ABS permit, if one exists
     * Range: [Boolean](types/Boolean.md)
 * [BiologicalMaterialOrigin➞usageRestrictions](BiologicalMaterialOrigin_usageRestrictions.md)  <sub>0..1</sub>
     * Description: Specifies any limitations or conditions on the use of the biological material, including restrictions on research, commercial use, or distribution, considering any potential concerns about the related genetic material
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Biological material origin |