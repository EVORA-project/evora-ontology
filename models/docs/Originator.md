
# Class: Originator

The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample

URI: [EVORA:Originator](https://evora-project.eu/Originator)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Product],[PersonOrOrganization],[Product]++-%20originator%200..1>[Originator&#124;homePage(i):string%20%3F;name(i):string;description(i):string%20%3F],[PersonOrOrganization]^-[Originator],[Image],[ContactPoint])](https://yuml.me/diagram/nofunky;dir:TB/class/[Product],[PersonOrOrganization],[Product]++-%20originator%200..1>[Originator&#124;homePage(i):string%20%3F;name(i):string;description(i):string%20%3F],[PersonOrOrganization]^-[Originator],[Image],[ContactPoint])

## Parents

 *  is_a: [PersonOrOrganization](PersonOrOrganization.md) - A person or an organization

## Referenced by Class

 *  **[Product](Product.md)** *[Product➞originator](Product_originator.md)*  <sub>0..1</sub>  **[Originator](Originator.md)**

## Attributes


### Inherited from PersonOrOrganization:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)
 * [PersonOrOrganization➞homePage](PersonOrOrganization_homePage.md)  <sub>0..1</sub>
     * Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
     * Range: [String](types/String.md)
 * [PersonOrOrganization➞contactPoint](PersonOrOrganization_contactPoint.md)  <sub>0..1</sub>
     * Description: An information that allows someone to establish communication
     * Range: [ContactPoint](ContactPoint.md)
 * [PersonOrOrganization➞logo](PersonOrOrganization_logo.md)  <sub>0..1</sub>
     * Description: A path or URL to the related logo
     * Range: [Image](Image.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Originator |
| **Close Mappings:** | | dct:ProvenanceStatement |