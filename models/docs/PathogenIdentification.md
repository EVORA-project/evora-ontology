
# Class: PathogenIdentification

A collection of distinguishing information that enables the differentiation of a pathogen from another

URI: [EVORA:PathogenIdentification](https://evora-project.eu/PathogenIdentification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Taxon],[ProductOrService],[Variant]<variant%200..1-++[PathogenIdentification&#124;pathogenType:string;hostType:string%20*;subspecies:string%20%3F;strain:string%20%3F;isolate:string%20%3F;genotype:string%20%3F;serotype:string%20%3F],[CommonName]<pathogenName%201..1-++[PathogenIdentification],[Taxon]<taxon%201..1-++[PathogenIdentification],[ProductOrService]++-%20pathogenIdentification%201..*>[PathogenIdentification],[Dataset]^-[PathogenIdentification],[Dataset],[CommonName])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Taxon],[ProductOrService],[Variant]<variant%200..1-++[PathogenIdentification&#124;pathogenType:string;hostType:string%20*;subspecies:string%20%3F;strain:string%20%3F;isolate:string%20%3F;genotype:string%20%3F;serotype:string%20%3F],[CommonName]<pathogenName%201..1-++[PathogenIdentification],[Taxon]<taxon%201..1-++[PathogenIdentification],[ProductOrService]++-%20pathogenIdentification%201..*>[PathogenIdentification],[Dataset]^-[PathogenIdentification],[Dataset],[CommonName])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class

 *  **[ProductOrService](ProductOrService.md)** *[ProductOrService➞pathogenIdentification](ProductOrService_pathogenIdentification.md)*  <sub>1..\*</sub>  **[PathogenIdentification](PathogenIdentification.md)**

## Attributes


### Own

 * [PathogenIdentification➞taxon](PathogenIdentification_taxon.md)  <sub>1..1</sub>
     * Description: Scientifically classified group or entity within the reference taxonomy
     * Range: [Taxon](Taxon.md)
 * [PathogenIdentification➞pathogenName](PathogenIdentification_pathogenName.md)  <sub>1..1</sub>
     * Description: A pathogen common name or a name that describes a group of pathogens
     * Range: [CommonName](CommonName.md)
 * [PathogenIdentification➞pathogenType](PathogenIdentification_pathogenType.md)  <sub>1..1</sub>
     * Description: Identification of the specific type of pathogen among the listed categories e.g. "Virus","Viroid","Bacterium"...
     * Range: [String](types/String.md)
 * [PathogenIdentification➞hostType](PathogenIdentification_hostType.md)  <sub>0..\*</sub>
     * Description: Indication of the possible host(s) for the identified pathogens among the listed main categories
     * Range: [String](types/String.md)
 * [PathogenIdentification➞subspecies](PathogenIdentification_subspecies.md)  <sub>0..1</sub>
     * Description: The subspecies information differentiates closely related pathogens within a single species
     * Range: [String](types/String.md)
 * [PathogenIdentification➞strain](PathogenIdentification_strain.md)  <sub>0..1</sub>
     * Description: Identifier given to a genetic variant within a single species
     * Range: [String](types/String.md)
 * [PathogenIdentification➞isolate](PathogenIdentification_isolate.md)  <sub>0..1</sub>
     * Description: Identifier given to a pathogen that has been isolated from an infected host and propagated in a laboratory culture. The isolate information may include an internal reference code from the laboratory that took the sample or performed the isolation, as well as details about the specific conditions of isolation, such as the name of the town, hospital, and type of host
     * Range: [String](types/String.md)
 * [PathogenIdentification➞genotype](PathogenIdentification_genotype.md)  <sub>0..1</sub>
     * Description: Genotype information that identifies organisms that cluster in phylogenetic trees, thus different clusters are distinct genotypes
     * Range: [String](types/String.md)
 * [PathogenIdentification➞serotype](PathogenIdentification_serotype.md)  <sub>0..1</sub>
     * Description: Genetically related pathogens that group together based on serological relationships
     * Range: [String](types/String.md)
 * [PathogenIdentification➞variant](PathogenIdentification_variant.md)  <sub>0..1</sub>
     * Description: An organism with one or more new mutations is referred to as a “variant” of the original organism if not sufficiently different to be termed a distinct strain
     * Range: [Variant](Variant.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Pathogen identification |