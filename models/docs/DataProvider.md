
# Class: DataProvider

An external API (Application Programming Interface) or Endpoint that permits to retrieve data from other sources

URI: [EVORA:DataProvider](https://evora-project.eu/DataProvider)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Taxonomy],[License],[DataService],[License]<license%200..1-++[DataProvider&#124;loginRequestMethod:string%20%3F;loginURL:uri%20%3F;loginTokenName:string%20%3F;queryURL:uri;queryMethod:string;contentType:string;providedEntityType:string;weight:integer;name(i):string;description(i):string%20%3F],[Collection]++-%20collectionDataProvider%200..1>[DataProvider],[Taxonomy]++-%20rankDataProvider%200..1>[DataProvider],[Taxonomy]++-%20taxonDataProvider%200..1>[DataProvider],[Taxonomy]++-%20versionDataProvider%201..1>[DataProvider],[Vocabulary]++-%20termDataProvider%200..1>[DataProvider],[DataService]^-[DataProvider],[Collection])](https://yuml.me/diagram/nofunky;dir:TB/class/[Vocabulary],[Taxonomy],[License],[DataService],[License]<license%200..1-++[DataProvider&#124;loginRequestMethod:string%20%3F;loginURL:uri%20%3F;loginTokenName:string%20%3F;queryURL:uri;queryMethod:string;contentType:string;providedEntityType:string;weight:integer;name(i):string;description(i):string%20%3F],[Collection]++-%20collectionDataProvider%200..1>[DataProvider],[Taxonomy]++-%20rankDataProvider%200..1>[DataProvider],[Taxonomy]++-%20taxonDataProvider%200..1>[DataProvider],[Taxonomy]++-%20versionDataProvider%201..1>[DataProvider],[Vocabulary]++-%20termDataProvider%200..1>[DataProvider],[DataService]^-[DataProvider],[Collection])

## Parents

 *  is_a: [DataService](DataService.md) - A collection of operations that provides access to one or more datasets or data processing functions

## Referenced by Class

 *  **[Collection](Collection.md)** *[Collection➞collectionDataProvider](Collection_collectionDataProvider.md)*  <sub>0..1</sub>  **[DataProvider](DataProvider.md)**
 *  **[Taxonomy](Taxonomy.md)** *[Taxonomy➞rankDataProvider](Taxonomy_rankDataProvider.md)*  <sub>0..1</sub>  **[DataProvider](DataProvider.md)**
 *  **[Taxonomy](Taxonomy.md)** *[Taxonomy➞taxonDataProvider](Taxonomy_taxonDataProvider.md)*  <sub>0..1</sub>  **[DataProvider](DataProvider.md)**
 *  **[Taxonomy](Taxonomy.md)** *[Taxonomy➞versionDataProvider](Taxonomy_versionDataProvider.md)*  <sub>1..1</sub>  **[DataProvider](DataProvider.md)**
 *  **[Vocabulary](Vocabulary.md)** *[Vocabulary➞termDataProvider](Vocabulary_termDataProvider.md)*  <sub>0..1</sub>  **[DataProvider](DataProvider.md)**

## Attributes


### Own

 * [DataProvider➞license](DataProvider_license.md)  <sub>0..1</sub>
     * Description: Information about terms and conditions under which the subject can be used, shared, or distributed, indicating any restrictions or permissions
     * Range: [License](License.md)
 * [DataProvider➞loginRequestMethod](DataProvider_loginRequestMethod.md)  <sub>0..1</sub>
     * Description: The http request method used to acces the login request url
     * Range: [String](types/String.md)
 * [DataProvider➞loginURL](DataProvider_loginURL.md)  <sub>0..1</sub>
     * Description: The URL template that allows to log in if required
     * Range: [Uri](types/Uri.md)
 * [DataProvider➞loginTokenName](DataProvider_loginTokenName.md)  <sub>0..1</sub>
     * Description: The name of the token, unique identifier of an interaction session, that will have to be reused as credential in the query
     * Range: [String](types/String.md)
 * [DataProvider➞queryURL](DataProvider_queryURL.md)  <sub>1..1</sub>
     * Description: The URL template that allows to get the content
     * Range: [Uri](types/Uri.md)
 * [DataProvider➞queryMethod](DataProvider_queryMethod.md)  <sub>1..1</sub>
     * Description: The http request method used to access the requested query url
     * Range: [String](types/String.md)
 * [DataProvider➞contentType](DataProvider_contentType.md)  <sub>1..1</sub>
     * Description: The content type of the response to the queries
     * Range: [String](types/String.md)
 * [DataProvider➞providedEntityType](DataProvider_providedEntityType.md)  <sub>1..1</sub>
     * Description: The identification of the entity type (Class) described by the response to the query
     * Range: [String](types/String.md)
 * [DataProvider➞weight](DataProvider_weight.md)  <sub>1..1</sub>
     * Description: A numerical value indicating relative importance or priority, generally processed in ascending order. This weight helps prioritize content when organizing or processing data. Its value can be negative, with a default set to 0
     * Range: [Integer](types/Integer.md)

### Inherited from DataService:

 * [Nameable➞name](Nameable_name.md)  <sub>1..1</sub>
     * Description: The label that allows humans to identify the current item
     * Range: [String](types/String.md)
 * [Nameable➞description](Nameable_description.md)  <sub>0..1</sub>
     * Description: A short explanation of the characteristics, features, or nature of the current item
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | Data provider |
| **Close Mappings:** | | wd:Q122625839 |