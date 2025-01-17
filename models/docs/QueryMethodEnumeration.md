# Enum: QueryMethodEnumeration



URI: [QueryMethodEnumeration](QueryMethodEnumeration.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| GET | wd:Q3504817 | GET http method, used to send information, such as a query string, directly i... |
| POST | wd:Q2764521 | POST http method, used to send information to a server by storing it in the r... |




## Slots

| Name | Description |
| ---  | --- |
| [loginRequestMethod](loginRequestMethod.md) | The http request method used to acces the login request url |
| [queryMethod](queryMethod.md) | The http request method used to access the requested query url |






## Identifier and Mapping Information







### Schema Source


* from schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#






## LinkML Source

<details>
```yaml
name: queryMethodEnumeration
from_schema: https://raw.githubusercontent.com/EVORA-project/evora-ontology/refs/heads/main/models/owl/evora_ontology.owl.ttl#
rank: 1000
permissible_values:
  GET:
    text: GET
    description: GET http method, used to send information, such as a query string,
      directly in the URL
    meaning: wd:Q3504817
  POST:
    text: POST
    description: POST http method, used to send information to a server by storing
      it in the request body of the http request
    meaning: wd:Q2764521

```
</details>
