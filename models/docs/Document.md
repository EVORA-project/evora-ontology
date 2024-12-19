
# Class: Document

Subclass of File representing textual or written files such as reports, manuals, or forms

URI: [EVORA:Document](https://evora-project.eu/Document)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[License],[File],[Certification]++-%20certificationDocument%200..*>[Document&#124;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[ProductOrService]++-%20complementaryDocument%200..*>[Document],[File]^-[Document],[Certification])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[License],[File],[Certification]++-%20certificationDocument%200..*>[Document&#124;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[ProductOrService]++-%20complementaryDocument%200..*>[Document],[File]^-[Document],[Certification])

## Parents

 *  is_a: [File](File.md) - Digital document or record stored in a specific format that contains data or information

## Referenced by Class

 *  **[Certification](Certification.md)** *[Certification➞certificationDocument](Certification_certificationDocument.md)*  <sub>0..\*</sub>  **[Document](Document.md)**
 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞complementaryDocument](ProductOrService_complementaryDocument.md)*  <sub>0..\*</sub>  **[Document](Document.md)**

## Attributes


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
| **Aliases:** | | Document |
| **Close Mappings:** | | wd:Q49848 |