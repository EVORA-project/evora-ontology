
# Class: Version

Numeric code assigned to identify a particular historical version of a work (e.g. software or technical standards)

URI: [EVORA:Version](https://evora-project.eu/Version)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Taxonomy]++-%20version%201..1>[Version&#124;ID:string;versionOf:uri],[Dataset]^-[Version],[Taxonomy],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Taxonomy]++-%20version%201..1>[Version&#124;ID:string;versionOf:uri],[Dataset]^-[Version],[Taxonomy],[Dataset])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[Taxonomy](Taxonomy.md)** *[Taxonomy➞version](Taxonomy_version.md)*  <sub>1..1</sub>  **[Version](Version.md)**

## Attributes


### Own

 * [Version➞ID](Version_ID.md)  <sub>1..1</sub>
     * Description: The version identifier
     * Range: [String](types/String.md)
 * [Version➞versionOf](Version_versionOf.md)  <sub>1..1</sub>
     * Description: Identifier of what the version qualifies
     * Range: [Uri](types/Uri.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Version |
| **Close Mappings:** | | wd:Q114469879 |