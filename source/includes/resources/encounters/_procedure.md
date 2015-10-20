## Procedures
This is an object representing an procedure.

### Get a specific procedure
> Example request:

```shell
curl "https://api.picnichealth.com/v1/procedures/1b26577b-04ea-4fc8-895a-1f466b707e63" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Procedure",
  "id": "1b26577b-04ea-4fc8-895a-1f466b707e63",
  "effectiveDate": "2015-10-17",
  "subject": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "performer": {
    "object": "MedicalPractitioner",
    "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
  },
  "requestFrom": {
    "object": "MedicalPractitoner",
    "referenceId": "0aeb1158-66d6-4e46-9ef6-e614bb6cc34a"
  },
  "location": {
    "object": "MedicalFacility",
    "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
  },
  "title": "Procedure",
  "subtitle": null,
  "notes": [
    {
      "object": "TextSection",
      "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
    }
  ]
}
```

Return an procedure

#### HTTP Request
`GET https://api.picnichealth.com/v1/procedures/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the procedure to be retrieved.


### List procedures
> Example request:

```shell
curl "https://api.picnichealth.com/v1/procedures" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "Procedure",
    "id": "1b26577b-04ea-4fc8-895a-1f466b707e63",
    "effectiveDate": "2015-10-17",
    "subject": {
      "object": "Patient",
      "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
    },
    "performer": {
      "object": "MedicalPractitioner",
      "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
    },
    "requestFrom": {
      "object": "MedicalPractitoner",
      "referenceId": "0aeb1158-66d6-4e46-9ef6-e614bb6cc34a"
    },
    "location": {
      "object": "MedicalFacility",
      "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
    },
    "title": "Procedure",
    "subtitle": null,
    "notes": [
      {
        "object": "TextSection",
        "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
      }
    ]
  },
  {
    "...": "..."
  }
]
```

Return a list of procedures

### Create a procedure
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/procedures" \
  -d effectiveDate="2015-10-17" \
  -d subject='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -d title="Procedure" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Procedure",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "effectiveDate": "2015-10-17",
  "subject": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "participant": null,
  "location": null,
  "title": "Office Visit",
  "subtitle": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/procedures`

Create a new imaging study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the procedure
subject | [Patient](#patients) | The subject of the procedure
performer | [MedicalPractioner](#medical-practitioners) | The performing doctor
requestFrom | [MedicalPractioner](#medical-practitioners) | The requesting doctor
location | [MedicalFacility](#medical-facilities) | The location of the procedure
title | String | The title of the procedure
subtitle | String | The subtitle of the procedure
notes | Array of [TextSection](#text-sections) | The notes for the procedure


### Update a procedure
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/procedures/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Procedure",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "effectiveDate": "2015-10-19",
  "subject": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "referrer": null,
  "procedureant": null,
  "location": null,
  "title": "Office Visit",
  "subtitle": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/procedures/:id`

Update an existing procedure object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the procedure
subject | [Patient](#patients) | The subject of the procedure
performer | [MedicalPractioner](#medical-practitioners) | The performing doctor
requestFrom | [MedicalPractioner](#medical-practitioners) | The requesting doctor
location | [MedicalFacility](#medical-facilities) | The location of the procedure
title | String | The title of the procedure
subtitle | String | The subtitle of the procedure
notes | Array of [TextSection](#text-sections) | The notes for the procedure


### Delete an procedure
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/procedures/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "deleted": true
}
```

Permanently delete an procedure.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/procedures/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the procedure to delete
