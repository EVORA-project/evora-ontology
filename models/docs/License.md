
# Class: License

The legal terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions

URI: [EVORA:License](https://evora-project.eu/License)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Nameable],[Image]<logo%200..1-++[License&#124;resourceURL:uri%20%3F;licensingOrAttribution:string%20%3F;name(i):string;description(i):string%20%3F],[DataProvider]++-%20license%200..1>[License],[File]++-%20license%200..1>[License],[Nameable]^-[License],[Image],[File],[DataProvider])](https://yuml.me/diagram/nofunky;dir:TB/class/[Nameable],[Image]<logo%200..1-++[License&#124;resourceURL:uri%20%3F;licensingOrAttribution:string%20%3F;name(i):string;description(i):string%20%3F],[DataProvider]++-%20license%200..1>[License],[File]++-%20license%200..1>[License],[Nameable]^-[License],[Image],[File],[DataProvider])

## Parents

 *  is_a: [Nameable](Nameable.md) - Any entity that has a name and can have a textual description

## Referenced by Class

 *  **[DataProvider](DataProvider.md)** *[DataProvider➞license](DataProvider_license.md)*  <sub>0..1</sub>  **[License](License.md)**
 *  **[File](File.md)** *[File➞license](File_license.md)*  <sub>0..1</sub>  **[License](License.md)**

## Attributes


### Own

 * [License➞resourceURL](License_resourceURL.md)  <sub>0..1</sub>
     * Description: The web address or location where the details or content is stored and can be accessed or downloaded.
     * Range: [Uri](types/Uri.md)
 * [License➞licensingOrAttribution](License_licensingOrAttribution.md)  <sub>0..1</sub>
     * Description: A text or html code that provides any related data sharing licence and/or attribution
     * Range: [String](types/String.md)
 * [License➞logo](License_logo.md)  <sub>0..1</sub>
     * Description: A path or URL to the related logo
     * Range: [Image](Image.md)

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
| **Aliases:** | | License |
| **Exact Mappings:** | | dct:RightsStatement |
| **Close Mappings:** | | wd:Q79719 |
|  | | dct:LicenseDocument |