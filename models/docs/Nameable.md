
# Class: Nameable

Any entity that has a name and can have a textual description

URI: [EVORA:Nameable](https://evora-project.eu/Nameable)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PersonOrOrganization],[NamedDataset],[Nameable&#124;name:string;description:string%20%3F]^-[PersonOrOrganization],[Nameable]^-[NamedDataset],[Nameable]^-[License],[Nameable]^-[File],[Nameable]^-[DataService],[Nameable]^-[ContactPoint],[Nameable]^-[Certification],[Nameable]^-[Catalogue],[License],[File],[DataService],[ContactPoint],[Certification],[Catalogue])](https://yuml.me/diagram/nofunky;dir:TB/class/[PersonOrOrganization],[NamedDataset],[Nameable&#124;name:string;description:string%20%3F]^-[PersonOrOrganization],[Nameable]^-[NamedDataset],[Nameable]^-[License],[Nameable]^-[File],[Nameable]^-[DataService],[Nameable]^-[ContactPoint],[Nameable]^-[Certification],[Nameable]^-[Catalogue],[License],[File],[DataService],[ContactPoint],[Certification],[Catalogue])

## Children

 * [Catalogue](Catalogue.md) - A curated collection of metadata about resources
 * [Certification](Certification.md) - Assurance given by an independent certification body that a product, service or system meets the requirements of a standard
 * [ContactPoint](ContactPoint.md) - Entity serving as focal point of information
 * [DataService](DataService.md) - A collection of operations that provides access to one or more datasets or data processing functions
 * [File](File.md) - Digital document or record stored in a specific format that contains data or information
 * [License](License.md) - The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
 * [NamedDataset](NamedDataset.md) - A collection of data, that has a name and can have a description, published or curated by a single agent, and available for access
 * [PersonOrOrganization](PersonOrOrganization.md) - A person or an organization

## Referenced by Class


## Attributes


### Own

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Nameable |