
# Class: PersonOrOrganization

A person or an organization

URI: [EVORA:PersonOrOrganization](https://evora-project.eu/PersonOrOrganization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Image]<logo%200..1-++[PersonOrOrganization&#124;homePage:string%20%3F;name(i):string;description(i):string%20%3F],[ContactPoint]<contactPoint%200..1-++[PersonOrOrganization],[PersonOrOrganization]^-[Person],[PersonOrOrganization]^-[Originator],[PersonOrOrganization]^-[Organization],[Nameable]^-[PersonOrOrganization],[Person],[Originator],[Organization],[Nameable],[Image],[ContactPoint])](https://yuml.me/diagram/nofunky;dir:TB/class/[Image]<logo%200..1-++[PersonOrOrganization&#124;homePage:string%20%3F;name(i):string;description(i):string%20%3F],[ContactPoint]<contactPoint%200..1-++[PersonOrOrganization],[PersonOrOrganization]^-[Person],[PersonOrOrganization]^-[Originator],[PersonOrOrganization]^-[Organization],[Nameable]^-[PersonOrOrganization],[Person],[Originator],[Organization],[Nameable],[Image],[ContactPoint])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Children

 * [Organization](Organization.md) - A social entity established to meet needs or pursue specific goals
 * [Originator](Originator.md) - The individual or organization responsible for the original discovery, isolation, or creation of an item, providing information about the source or origin of the sample
 * [Person](Person.md) - An individual

## Referenced by Class


## Attributes


### Own

 * [PersonOrOrganization➞homePage](PersonOrOrganization_homePage.md)  <sub>0..1</sub>
     * Description: Refers to the degree of purity achieved for a protein sample. Possible values include ">95%" (the protein is highly purified, with more than 95% purity) and "Unpurified expression host lysate or partly purified protein" (the protein is either unpurified and present in the host cell lysate or only partially purified).
     * Range: [String](types/String.md)
 * [PersonOrOrganization➞contactPoint](PersonOrOrganization_contactPoint.md)  <sub>0..1</sub>
     * Description: An information that allows someone to establish communication
     * Range: [ContactPoint](ContactPoint.md)
 * [PersonOrOrganization➞logo](PersonOrOrganization_logo.md)  <sub>0..1</sub>
     * Description: A path or URL to the related logo
     * Range: [Image](Image.md)

### Inherited from Nameable:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Person Or Organization |
| **Exact Mappings:** | | dct:Agent |
| **Close Mappings:** | | foaf:Agent |