## Notes
This is an object representing a note.

### Get a specific note
> Example request:

```shell
curl "https://api.picnichealth.com/v1/notes/89460ec2-323a-4f2f-b2d8-bfc8ef535c99" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Note",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": "Assessment",
  "note": "Malignant neoplasm of unspecified site"
}
```
Return a note object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/notes/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the note to be retrieved.


### List notes
> Example request:

```shell
curl "https://api.picnichealth.com/v1/notes" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "List",
  "length": 20,
  "hasMore": true,
  "data": [
    {
      "object": "Note",
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
}
```

Return a list of note objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/notes`

### Create a note
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/notes" \
  -d encounter='{ object: "Examination", referenceId: "a8ddb870-c65c-4b31-ba42-8f7b55f37e96" }' \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Note",
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
`POST https://api.picnichealth.com/v1/notes`

Create a new note object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter with which the note is associated
title | String | The title of the note
note | String | The content of the note

### Update a note
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/notes/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d title="Impression" \
  -d node="Doing well"
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Note",
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
`POST https://api.picnichealth.com/v1/notes/:id`

Update an existing note

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter with which the note is associated
title | String | The title of the note
note | String | The content of the note

### Delete a note
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/notes/89460ec2-323a-4f2f-b2d8-bfc8ef535c99" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "deleted": true
}
```

Permanently delete a note

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/notes/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the note to delete

