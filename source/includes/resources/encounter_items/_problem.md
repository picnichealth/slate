## Conditions
This is an object representing a condition.

### Get a specific condition
> Example request:

```shell
curl "https://api.picnichealth.com/v1/conditions/0507420d-fcf8-4ec9-8bf0-c10bf408e6cd" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Condition",
  "id": "0507420d-fcf8-4ec9-8bf0-c10bf408e6cd",
  "encounter": {
    "object": "Examination",
    "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
  },
  "coding": {
    "object": "Code",
    "referenceId": "f60d40f2-dc3a-49f1-a7e2-a599c2be36dc"
  }
}
```
Return a condition object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/conditions/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | The ID of the condition to be retrieved.


### List conditions
> Example request:

```shell
curl "https://api.picnichealth.com/v1/conditions" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "Condition",
    "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
    "encounter": {
      "object": "Examination",
      "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
    },
    "coding": {
      "object": "Code",
      "referenceId": "f60d40f2-dc3a-49f1-a7e2-a599c2be36dc"
    }
  },
  {
    "...": "..."
  }
]
```

Return a list of problem objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/problems`

### Create a problem
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/problems" \
  -d encounter='{ "object": "Code", "referenceId:": "72314206-32df-4777-9a26-73b37bae9a5a" }' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Condition",
  "id": "0507420d-fcf8-4ec9-8bf0-c10bf408e6cd",
  "encounter": {
    "object": "Examination",
    "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
  },
  "coding": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/conditions`

Create a new condition object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter when the condition was recorded
coding | [Code](#codes) | The coding of the condition

### Update an medication
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/problems/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d coding='{ object: "Code", referenceId: "e04d504c-ab2e-4126-9180-b8384c315590" }' \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Condition",
  "id": "0507420d-fcf8-4ec9-8bf0-c10bf408e6cd",
  "encounter": {
    "object": "Examination",
    "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
  },
  "coding": {
    "object": "Code",
    "referenceId": "e04d504c-ab2e-4126-9180-b8384c315590"
  }
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/problems/:id`

Update a medical practitioner

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter when the condition was recorded
coding | [Code](#codes) | The coding of the condition

### Delete a problem
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/problems/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "deleted": true
}
```

Permanently delete a condition

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/conditions/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the condition to delete
