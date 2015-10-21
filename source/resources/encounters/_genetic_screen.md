## Genetic Screens
This is an object representing a genetic screen.

### Get a specific genetic screen
> Example request:

```shell
curl "https://api.picnichealth.com/v1/genetic-screens/2c5f5800-6bda-4018-9c11-f4275880495b \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "GeneticScreen",
  "id": "2c5f5800-6bda-4018-9c11-f4275880495b",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "location": {
    "object": "MedicalFacility",
    "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
  },
  "notes": [
    {
      "object": "TextSection",
      "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
    }
  ]
}
```

Return a genetic screen

#### HTTP Request
`GET https://api.picnichealth.com/v1/genetic-screens/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the genetic screen to be retrieved.


### List genetic screens
> Example request:

```shell
curl "https://api.picnichealth.com/v1/genetic-screens" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "List",
  "length": 20,
  "hasMore": true,
  "data": [
    {
      "object": "GeneticScreen",
      "id": "2c5f5800-6bda-4018-9c11-f4275880495b",
      "effectiveDate": "2015-10-17",
      "patient": {
        "object": "Patient",
        "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
      },
      "location": {
        "object": "MedicalFacility",
        "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
      },
      "notes": [
        {
          "object": "TextSection",
          "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
        }
      ]
    }, {
      "...": "..."
    }
  ]
}
```

Return a list of genetic screens

### Create a genetic screen
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/genetic-screens" \
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Genetic Screen",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "participant": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/genetic-screens`

Create a new genetic screen object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the genetic screen
patient | [Patient](#patients) | The patient of the genetic screen
location | [MedicalFacility](#medical-facilities) | The location of the genetic screen
notes | Array of [TextSection](#text-sections) | The notes for the genetic screen

### Update a genetic screen
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/genetic-screens/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "GeneticScreen",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "effectiveDate": "2015-10-19",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "participant": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/genetic-screens/:id`

Update an existing genetic screen object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the genetic screen
patient | [Patient](#patients) | The patient of the genetic screen
location | [MedicalFacility](#medical-facilities) | The location of the genetic screen
notes | Array of [TextSection](#text-sections) | The notes for the genetic screen

### Delete an genetic screen
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/genetic-screens/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "deleted": true
}
```

Permanently delete a genetic screen.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/genetic-screens/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the genetic screen to delete
