## Text Sections
This is an object representing a text section.

### Get a specific text section
> Example request:

```shell
curl "https://api.picnichealth.com/v1/text-sections/89460ec2-323a-4f2f-b2d8-bfc8ef535c99" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "TextSection",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": "Assessment",
  "note": "Malignant neoplasm of unspecified site"
}
```
Return a text section object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/text-sections/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the text section to be retrieved.


### List text sections
> Example request:

```shell
curl "https://api.picnichealth.com/v1/text-sections" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "TextSection",
    "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
    "encounter": {
      "object": "Examination",
      "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
    },
    "title": "Assessment",
    "note": "Malignant neoplasm of unspecified site"
  },
  {
    "...": "..."
  }
]
```

Return a list of text section objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/text-sections`

### Create a text section
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/text-sections" \
  -d encounter='{ object: "Examination", referenceId: "a8ddb870-c65c-4b31-ba42-8f7b55f37e96" }' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "TextSection",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": null,
  "note": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/text-sections`

Create a new text section object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | String | The encounter with which the text section is associated
title | String | The title of the text section
note | String | The content of the text section

### Update a text section
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/text-sections/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d title="Impression" \
  -d node="Doing well"
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "TextSection",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": "Impression",
  "note": "Doing well"
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/text-sections/:id`

Update an existing text section

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | String | The encounter with which the text section is associated
title | String | The title of the text section
note | String | The content of the text section

### Delete a text section
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/text-sections/89460ec2-323a-4f2f-b2d8-bfc8ef535c99" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "deleted": true
}
```

Permanently delete a text section

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/text-sections/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the text section to delete

