
# Class: File

Digital document or record stored in a specific format that contains data or information

URI: [EVORA:File](https://evora-project.eu/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Video],[Nameable],[License],[Image],[License]<license%200..1-++[File&#124;contentURL:uri;format:string;name(i):string;description(i):string%20%3F],[Bundle]++-%20complementaryDocument(i)%200..*>[File],[DetectionKit]++-%20hasSOPFile%200..*>[File],[File]^-[Video],[File]^-[Image],[File]^-[Document],[File]^-[Data],[File]^-[Audio],[Nameable]^-[File],[Document],[DetectionKit],[Data],[Bundle],[Audio])](https://yuml.me/diagram/nofunky;dir:TB/class/[Video],[Nameable],[License],[Image],[License]<license%200..1-++[File&#124;contentURL:uri;format:string;name(i):string;description(i):string%20%3F],[Bundle]++-%20complementaryDocument(i)%200..*>[File],[DetectionKit]++-%20hasSOPFile%200..*>[File],[File]^-[Video],[File]^-[Image],[File]^-[Document],[File]^-[Data],[File]^-[Audio],[Nameable]^-[File],[Document],[DetectionKit],[Data],[Bundle],[Audio])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Children

 * [Audio](Audio.md) - Subclass of File representing sound recordings or audio tracks
 * [Data](Data.md) - Subclass of File representing structured or unstructured datasets, often used for analysis, storage, or transfer of information
 * [Document](Document.md) - Subclass of File representing textual or written files such as reports, manuals, or forms
 * [Image](Image.md) - Subclass of File representing visual content such as pictures, diagrams, or illustrations
 * [Video](Video.md) - Subclass of File representing moving visual media, such as recordings, presentations, or movies

## Referenced by Class

 *  **[Bundle](Bundle.md)** *[Bundle➞complementaryDocument](Bundle_complementaryDocument.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **[DetectionKit](DetectionKit.md)** *[Detection Kit➞hasSOPFile](Detection_Kit_hasSOPFile.md)*  <sub>0..\*</sub>  **[File](File.md)**

## Attributes


### Own

 * [File➞contentURL](File_contentURL.md)  <sub>1..1</sub>
     * Description: The web address or location where the file content is stored and can be accessed or downloaded.
     * Range: [Uri](types/Uri.md)
 * [File➞format](File_format.md)  <sub>1..1</sub>
     * Description: The file type or format that indicates how the data within the file is structured
     * Range: [String](types/String.md)
 * [File➞license](File_license.md)  <sub>0..1</sub>
     * Description: The legal terms and conditions under which the file can be used, shared, or distributed, indicating any restrictions or permissions.
     * Range: [License](License.md)

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
| **Aliases:** | | File |
| **Exact Mappings:** | | dcat:mediaType |
| **Close Mappings:** | | wd:Q82753 |