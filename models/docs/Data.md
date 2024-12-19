
# Class: Data

Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information

URI: [EVORA:Data](https://evora-project.eu/Data)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NucleicAcid],[License],[File],[NucleicAcid]++-%20hasGbFileOfTheConstruct%200..*>[Data&#124;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[File]^-[Data])](https://yuml.me/diagram/nofunky;dir:TB/class/[NucleicAcid],[License],[File],[NucleicAcid]++-%20hasGbFileOfTheConstruct%200..*>[Data&#124;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[File]^-[Data])

## Parents

 *  is_a: [File](File.md) - Digital document or record stored in a specific format that contains data or information

## Referenced by Class

 *  **[NucleicAcid](NucleicAcid.md)** *[Nucleic Acid➞hasGbFileOfTheConstruct](Nucleic_Acid_hasGbFileOfTheConstruct.md)*  <sub>0..\*</sub>  **[Data](Data.md)**

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
| **Aliases:** | | Data |
| **Close Mappings:** | | wd:Q42848 |