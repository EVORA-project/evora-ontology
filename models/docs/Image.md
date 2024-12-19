
# Class: Image

Subclass of File representing visual content such as pictures, diagrams, or illustrations

URI: [EVORA:Image](https://evora-project.eu/Image)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[PersonOrOrganization],[License],[Certification]++-%20logo%200..1>[Image&#124;altText:string%20%3F;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[License]++-%20logo%200..1>[Image],[PersonOrOrganization]++-%20logo%200..1>[Image],[ProductOrService]++-%20productPicture%200..*>[Image],[File]^-[Image],[File],[Certification])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[PersonOrOrganization],[License],[Certification]++-%20logo%200..1>[Image&#124;altText:string%20%3F;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[License]++-%20logo%200..1>[Image],[PersonOrOrganization]++-%20logo%200..1>[Image],[ProductOrService]++-%20productPicture%200..*>[Image],[File]^-[Image],[File],[Certification])

## Parents

 *  is_a: [File](File.md) - Digital document or record stored in a specific format that contains data or information

## Referenced by Class

 *  **[Certification](Certification.md)** *[Certification➞logo](Certification_logo.md)*  <sub>0..1</sub>  **[Image](Image.md)**
 *  **[License](License.md)** *[License➞logo](License_logo.md)*  <sub>0..1</sub>  **[Image](Image.md)**
 *  **[PersonOrOrganization](PersonOrOrganization.md)** *[PersonOrOrganization➞logo](PersonOrOrganization_logo.md)*  <sub>0..1</sub>  **[Image](Image.md)**
 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞productPicture](ProductOrService_productPicture.md)*  <sub>0..\*</sub>  **[Image](Image.md)**

## Attributes


### Own

 * [Image➞altText](Image_altText.md)  <sub>0..1</sub>
     * Description: An alternate text for the image, if the image cannot be displayed
     * Range: [String](types/String.md)

### Inherited from File:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)
 * [File➞contentURL](File_contentURL.md)  <sub>1..1</sub>
     * Description: The web address or location where the file content is stored and can be accessed or downloaded.
     * Range: [Uri](types/Uri.md)
 * [File➞format](File_format.md)  <sub>1..1</sub>
     * Description: The file type or format that indicates how the data within the file is structured
     * Range: [String](types/String.md)
 * [File➞license](File_license.md)  <sub>0..1</sub>
     * Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
     * Range: [License](License.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Image |
| **Close Mappings:** | | wd:Q860625 |