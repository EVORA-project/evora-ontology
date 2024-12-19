
# Class: Publication

A scientific publication

URI: [EVORA:Publication](https://evora-project.eu/Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Journal]<journal%200..1-++[Publication&#124;title:string;authors:string;abstract:string],[DOI]<relatedDOI%201..1-++[Publication],[Dataset]^-[Publication],[Journal],[Dataset],[DOI])](https://yuml.me/diagram/nofunky;dir:TB/class/[Journal]<journal%200..1-++[Publication&#124;title:string;authors:string;abstract:string],[DOI]<relatedDOI%201..1-++[Publication],[Dataset]^-[Publication],[Journal],[Dataset],[DOI])

## Parents

 *  is_a: [Dataset](Dataset.md) - A collection of data, published or curated by a single agent, and available for access

## Referenced by Class


## Attributes


### Own

 * [Publication➞title](Publication_title.md)  <sub>1..1</sub>
     * Description: The descriptive word or phrase that identifies the current piece of work
     * Range: [String](types/String.md)
 * [Publication➞authors](Publication_authors.md)  <sub>1..1</sub>
     * Description: The list of authors
     * Range: [String](types/String.md)
 * [Publication➞abstract](Publication_abstract.md)  <sub>1..1</sub>
     * Description: Concise summary of the publication
     * Range: [String](types/String.md)
 * [Publication➞relatedDOI](Publication_relatedDOI.md)  <sub>1..1</sub>
     * Description: Any Digital Object Identifier that can be related
     * Range: [DOI](DOI.md)
 * [Publication➞journal](Publication_journal.md)  <sub>0..1</sub>
     * Description: The scientific journal in which the publication was published
     * Range: [Journal](Journal.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Publication |
| **Close Mappings:** | | wd:Q591041 |