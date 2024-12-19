
# Class: Certification

Assurance given by an independent certification body that a product, service or system meets the requirements of a standard

URI: [EVORA:Certification](https://evora-project.eu/Certification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[Nameable],[Image],[Document],[Document]<certificationDocument%200..*-++[Certification&#124;resourceURL:uri%20%3F;name(i):string;description(i):string%20%3F],[Image]<logo%200..1-++[Certification],[ProductOrService]++-%20certification%200..*>[Certification],[Nameable]^-[Certification])](https://yuml.me/diagram/nofunky;dir:TB/class/[ProductOrService],[Nameable],[Image],[Document],[Document]<certificationDocument%200..*-++[Certification&#124;resourceURL:uri%20%3F;name(i):string;description(i):string%20%3F],[Image]<logo%200..1-++[Certification],[ProductOrService]++-%20certification%200..*>[Certification],[Nameable]^-[Certification])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Referenced by Class

 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞certification](ProductOrService_certification.md)*  <sub>0..\*</sub>  **[Certification](Certification.md)**

## Attributes


### Own

 * [Certification➞logo](Certification_logo.md)  <sub>0..1</sub>
     * Description: A path or URL to the related logo
     * Range: [Image](Image.md)
 * [Certification➞certificationDocument](Certification_certificationDocument.md)  <sub>0..\*</sub>
     * Description: The document(s) issued by an authority certifying the conformity of the subject to the applicable scheme, including, as the case may be, the documents attesting the equivalence to another certification scheme.
     * Range: [Document](Document.md)
 * [Certification➞resourceURL](Certification_resourceURL.md)  <sub>0..1</sub>
     * Description: The web address or location where the details or content is stored and can be accessed or downloaded.
     * Range: [Uri](types/Uri.md)

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
| **Aliases:** | | Certification |
| **Close Mappings:** | | wd:Q374814 |
|  | | schema:Certification |