
# Class: Video

Subclass of File representing moving visual media, such as recordings, presentations, or movies

URI: [EVORA:Video](https://evora-project.eu/Video)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[File]^-[Video&#124;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[License],[File])](https://yuml.me/diagram/nofunky;dir:TB/class/[File]^-[Video&#124;contentURL(i):uri;format(i):string;name(i):string;description(i):string%20%3F],[License],[File])

## Parents

 *  is_a: [File](File.md) - Digital document or record stored in a specific format that contains data or information

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
| **Aliases:** | | Video |
| **Close Mappings:** | | wd:Q98405806 |