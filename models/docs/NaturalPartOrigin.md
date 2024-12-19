
# Class: NaturalPartOrigin

Information on the origin of a natural part that composes the biological material

URI: [EVORA:NaturalPartOrigin](https://evora-project.eu/NaturalPartOrigin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RecombinantPartIdentification],[IPLCOrigin]<indigenousPoepleAndLocalCommunityOrigin%200..1-++[NaturalPartOrigin&#124;collectionDate:datetime;beforeDate:boolean;reportingToAuthorities:string%20%3F],[Country]<countryOfCollection%201..1-++[NaturalPartOrigin],[BiologicalPartOrigin]^-[NaturalPartOrigin],[IPLCOrigin],[Country],[BiologicalPartOrigin])](https://yuml.me/diagram/nofunky;dir:TB/class/[RecombinantPartIdentification],[IPLCOrigin]<indigenousPoepleAndLocalCommunityOrigin%200..1-++[NaturalPartOrigin&#124;collectionDate:datetime;beforeDate:boolean;reportingToAuthorities:string%20%3F],[Country]<countryOfCollection%201..1-++[NaturalPartOrigin],[BiologicalPartOrigin]^-[NaturalPartOrigin],[IPLCOrigin],[Country],[BiologicalPartOrigin])

## Parents

 *  is_a: [BiologicalPartOrigin](BiologicalPartOrigin.md) - Information on the origin of a unitary, cohesive part that is part of, or constitutes the biological material. It can be multiple parts in case of a recombinant biological material

## Referenced by Class


## Attributes


### Own

 * [NaturalPartOrigin➞countryOfCollection](NaturalPartOrigin_countryOfCollection.md)  <sub>1..1</sub>
     * Description: The geographical location where the sample was collected in situ. Used for Nagoya/CBD; equivalent to "country of origin".
     * Range: [Country](Country.md)
 * [NaturalPartOrigin➞indigenousPoepleAndLocalCommunityOrigin](NaturalPartOrigin_indigenousPoepleAndLocalCommunityOrigin.md)  <sub>0..1</sub>
     * Description: The specific IPLC area (Indigenous People and Local Communities) from which this sample/element was sampled, if relevant
     * Range: [IPLCOrigin](IPLCOrigin.md)
 * [NaturalPartOrigin➞collectionDate](NaturalPartOrigin_collectionDate.md)  <sub>1..1</sub>
     * Description: The date when the sample was collected in situ. If unknown/private, use a proxy date such as "date received" and indicate this by setting to true the before date property
     * Range: [Datetime](types/Datetime.md)
 * [NaturalPartOrigin➞beforeDate](NaturalPartOrigin_beforeDate.md)  <sub>1..1</sub>
     * Description: Set to TRUE if a proxy date for the collection date is used
     * Range: [Boolean](types/Boolean.md)
 * [NaturalPartOrigin➞reportingToAuthorities](NaturalPartOrigin_reportingToAuthorities.md)  <sub>0..1</sub>
     * Description: Information about permit identifiers for access to the genetic resource, applicable if the genetic resource falls under Access and Benefit-Sharing (ABS) regulations
     * Range: [String](types/String.md)

### Inherited from BiologicalPartOrigin:

 * [BiologicalPartOrigin➞recombinantPartIdentification](BiologicalPartOrigin_recombinantPartIdentification.md)  <sub>0..1</sub>
     * Description: Identification of a recombinant part
     * Range: [RecombinantPartIdentification](RecombinantPartIdentification.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Natural part origin |