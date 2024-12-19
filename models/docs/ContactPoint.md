
# Class: ContactPoint

Entity serving as focal point of information

URI: [EVORA:ContactPoint](https://evora-project.eu/ContactPoint)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[PersonOrOrganization],[Nameable],[MSDS],[Country],[Country]<addressCountry%200..1-++[ContactPoint&#124;email:string%20%3F;telephone:string%20%3F;streetAddress:string%20%3F;addressLocality:string%20%3F;addressRegion:string%20%3F;postalCode:string%20%3F;oRCIDiD:string%20%3F;name(i):string;description(i):string%20%3F],[MSDS]++-%20msdsContact%201..1>[ContactPoint],[PersonOrOrganization]++-%20contactPoint%200..1>[ContactPoint],[ProductOrService]++-%20contactPoint%200..1>[ContactPoint],[Nameable]^-[ContactPoint])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[PersonOrOrganization],[Nameable],[MSDS],[Country],[Country]<addressCountry%200..1-++[ContactPoint&#124;email:string%20%3F;telephone:string%20%3F;streetAddress:string%20%3F;addressLocality:string%20%3F;addressRegion:string%20%3F;postalCode:string%20%3F;oRCIDiD:string%20%3F;name(i):string;description(i):string%20%3F],[MSDS]++-%20msdsContact%201..1>[ContactPoint],[PersonOrOrganization]++-%20contactPoint%200..1>[ContactPoint],[ProductOrService]++-%20contactPoint%200..1>[ContactPoint],[Nameable]^-[ContactPoint])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Referenced by Class

 *  **[MSDS](MSDS.md)** *[MSDS➞msdsContact](MSDS_msdsContact.md)*  <sub>1..1</sub>  **[ContactPoint](ContactPoint.md)**
 *  **[PersonOrOrganization](PersonOrOrganization.md)** *[PersonOrOrganization➞contactPoint](PersonOrOrganization_contactPoint.md)*  <sub>0..1</sub>  **[ContactPoint](ContactPoint.md)**
 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞contactPoint](ProductOrService_contactPoint.md)*  <sub>0..1</sub>  **[ContactPoint](ContactPoint.md)**

## Attributes


### Own

 * [ContactPoint➞email](ContactPoint_email.md)  <sub>0..1</sub>
     * Description: Email address
     * Range: [String](types/String.md)
 * [ContactPoint➞telephone](ContactPoint_telephone.md)  <sub>0..1</sub>
     * Description: The telephone number
     * Range: [String](types/String.md)
 * [ContactPoint➞streetAddress](ContactPoint_streetAddress.md)  <sub>0..1</sub>
     * Description: The building/apartment number and the street name
     * Range: [String](types/String.md)
 * [ContactPoint➞addressLocality](ContactPoint_addressLocality.md)  <sub>0..1</sub>
     * Description: The locality in which the street address is, and which is in the region. e.g, the city
     * Range: [String](types/String.md)
 * [ContactPoint➞addressRegion](ContactPoint_addressRegion.md)  <sub>0..1</sub>
     * Description: The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division
     * Range: [String](types/String.md)
 * [ContactPoint➞postalCode](ContactPoint_postalCode.md)  <sub>0..1</sub>
     * Description: The postal code
     * Range: [String](types/String.md)
 * [ContactPoint➞addressCountry](ContactPoint_addressCountry.md)  <sub>0..1</sub>
     * Description: The country as of  ISO 3166
     * Range: [Country](Country.md)
 * [ContactPoint➞oRCIDiD](ContactPoint_oRCIDiD.md)  <sub>0..1</sub>
     * Description: Unique persistent identifier for a person, provided by the Open Researcher and Contributor ID (ORCID) organisation
     * Range: [String](types/String.md)

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
| **Aliases:** | | Contact Point |
| **Close Mappings:** | | wd:Q30322502 |
|  | | vcard:Contact |