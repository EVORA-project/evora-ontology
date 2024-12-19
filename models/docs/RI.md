
# Class: RI

A research infrastructure

URI: [EVORA:RI](https://evora-project.eu/RI)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Provider]++-%20memberOfRI%200..*>[RI&#124;homePage(i):string%20%3F;name(i):string;description(i):string%20%3F],[Organization]^-[RI],[Provider],[Organization],[Image],[Country],[ContactPoint],[AlternateName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Provider]++-%20memberOfRI%200..*>[RI&#124;homePage(i):string%20%3F;name(i):string;description(i):string%20%3F],[Organization]^-[RI],[Provider],[Organization],[Image],[Country],[ContactPoint],[AlternateName])

## Parents

 *  is_a: [Organization](Organization.md) - A social entity established to meet needs or pursue specific goals

## Referenced by Class

 *  **[Provider](Provider.md)** *[Provider➞memberOfRI](Provider_memberOfRI.md)*  <sub>0..\*</sub>  **[RI](RI.md)**

## Attributes


### Inherited from Organization:

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
 * [Organization➞alternateName](Organization_alternateName.md)  <sub>0..1</sub>
     * Description: An alternate name or acronym
     * Range: [AlternateName](AlternateName.md)
 * [Organization➞country](Organization_country.md)  <sub>0..1</sub>
     * Description: The country of the organization
     * Range: [Country](Country.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | RI |
| **Close Mappings:** | | wd:Q1438053 |