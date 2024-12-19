
# Class: Person

An individual

URI: [EVORA:Person](https://evora-project.eu/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PersonOrOrganization],[PersonOrOrganization]^-[Person&#124;oRCIDiD:string%20%3F;homePage(i):string%20%3F;name(i):string;description(i):string%20%3F],[Image],[ContactPoint])](https://yuml.me/diagram/nofunky;dir:TB/class/[PersonOrOrganization],[PersonOrOrganization]^-[Person&#124;oRCIDiD:string%20%3F;homePage(i):string%20%3F;name(i):string;description(i):string%20%3F],[Image],[ContactPoint])

## Parents

 *  is_a: [PersonOrOrganization](PersonOrOrganization.md) - A person or an organization

## Referenced by Class


## Attributes


### Own

 * [Person➞oRCIDiD](Person_oRCIDiD.md)  <sub>0..1</sub>
     * Description: Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation
     * Range: [String](types/String.md)

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
| **Aliases:** | | Person |
| **Close Mappings:** | | wd:Q215627 |
|  | | vcard:Individual |