
# Class: Taxonomy

Science of naming, defining and classifying organisms

URI: [EVORA:Taxonomy](https://evora-project.eu/Taxonomy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Version],[DataProvider]<rankDataProvider%200..1-++[Taxonomy&#124;name(i):string;description(i):string%20%3F],[TaxonomicRank]<rank%200..*-++[Taxonomy],[DataProvider]<versionDataProvider%201..1-++[Taxonomy],[Version]<version%201..1-++[Taxonomy],[DataProvider]<taxonDataProvider%200..1-++[Taxonomy],[Taxon]<taxon%200..*-++[Taxonomy],[Taxon]++-%20taxonomy%200..*>[Taxonomy],[TaxonomicRank]++-%20taxonomy%200..*>[Taxonomy],[Catalogue]^-[Taxonomy],[TaxonomicRank],[Taxon],[DataProvider],[Catalogue])](https://yuml.me/diagram/nofunky;dir:TB/class/[Version],[DataProvider]<rankDataProvider%200..1-++[Taxonomy&#124;name(i):string;description(i):string%20%3F],[TaxonomicRank]<rank%200..*-++[Taxonomy],[DataProvider]<versionDataProvider%201..1-++[Taxonomy],[Version]<version%201..1-++[Taxonomy],[DataProvider]<taxonDataProvider%200..1-++[Taxonomy],[Taxon]<taxon%200..*-++[Taxonomy],[Taxon]++-%20taxonomy%200..*>[Taxonomy],[TaxonomicRank]++-%20taxonomy%200..*>[Taxonomy],[Catalogue]^-[Taxonomy],[TaxonomicRank],[Taxon],[DataProvider],[Catalogue])

## Parents

 *  is_a: [Catalogue](Catalogue.md) - A curated collection of metadata about resources

## Referenced by Class

 *  **[Taxon](Taxon.md)** *[Taxon➞taxonomy](Taxon_taxonomy.md)*  <sub>0..\*</sub>  **[Taxonomy](Taxonomy.md)**
 *  **[TaxonomicRank](TaxonomicRank.md)** *[TaxonomicRank➞taxonomy](TaxonomicRank_taxonomy.md)*  <sub>0..\*</sub>  **[Taxonomy](Taxonomy.md)**

## Attributes


### Own

 * [Taxonomy➞taxon](Taxonomy_taxon.md)  <sub>0..\*</sub>
     * Description: Scientifically classified group or entity within the reference taxonomy
     * Range: [Taxon](Taxon.md)
 * [Taxonomy➞taxonDataProvider](Taxonomy_taxonDataProvider.md)  <sub>0..1</sub>
     * Description: The data provider for the taxons of the taxonomy
     * Range: [DataProvider](DataProvider.md)
 * [Taxonomy➞version](Taxonomy_version.md)  <sub>1..1</sub>
     * Description: The version of this instance of entity
     * Range: [Version](Version.md)
 * [Taxonomy➞versionDataProvider](Taxonomy_versionDataProvider.md)  <sub>1..1</sub>
     * Description: The data provider for the Version ID of this taxonomy
     * Range: [DataProvider](DataProvider.md)
 * [Taxonomy➞rank](Taxonomy_rank.md)  <sub>0..\*</sub>
     * Description: Relative level or position of the identified taxon in the taxonomy
     * Range: [TaxonomicRank](TaxonomicRank.md)
 * [Taxonomy➞rankDataProvider](Taxonomy_rankDataProvider.md)  <sub>0..1</sub>
     * Description: The data provider for the description of the taxonomic ranks used in this taxonomy
     * Range: [DataProvider](DataProvider.md)

### Inherited from Catalogue:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Taxonomy |
| **Close Mappings:** | | wd:Q8269924 |
|  | | skos:Collection |