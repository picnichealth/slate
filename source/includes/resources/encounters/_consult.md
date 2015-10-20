## Consults
This is an object representing an consult.

### Get a specific consult
> Example request:

```shell
curl "https://api.picnichealth.com/v1/consults/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Consult",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "effectiveDate": "2015-10-17",
  "subject": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "consultant": {
    "object": "MedicalPractitioner",
    "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
  },
  "referrer": {
    "object": "MedicalPractitoner",
    "referenceId": "0aeb1158-66d6-4e46-9ef6-e614bb6cc34a"
  },
  "location": {
    "object": "MedicalFacility",
    "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
  },
  "title": "Consult Note",
  "subtitle": null,
  "notes": [
    {
      "object": "TextSection",
      "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
    }
  ]
}
```

Return an consult

#### HTTP Request
`GET https://api.picnichealth.com/v1/consults/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the consult to be retrieved.


### List consults
> Example request:

```shell
curl "https://api.picnichealth.com/v1/consults" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "Consult",
    "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
    "effectiveDate": "2015-10-17",
    "subject": {
      "object": "Patient",
      "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
    },
    "consultant": {
      "object": "MedicalPractitioner",
      "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
    },
    "referrer": {
      "object": "MedicalPractitoner",
      "referenceId": "0aeb1158-66d6-4e46-9ef6-e614bb6cc34a"
    },
    "location": {
      "object": "MedicalFacility",
      "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
    },
    "title": "Consult Note",
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

Return a list of consults

### Create a consult
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/consults" \
  -d effectiveDate="2015-10-17" \
  -d subject='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -d title="Consult Note" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Consult",
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
`POST https://api.picnichealth.com/v1/consults`

Create a new imaging study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the consult
subject | [Patient](#patients) | The subject of the consult
referrer | [MedicalPractitioner](#medical-practitioners) | The referring doctor
consultant | [MedicalPractioner](#medical-practitioners) | THe consulting doctor
location | [MedicalFacility](#medical-facilities) | The location of the consult
title | String | The title of the consult
subtitle | String | The subtitle of the consult
notes | Array of [TextSection](#text-sections) | The notes for the consult


### Update a consult
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/consults/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Consult",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "effectiveDate": "2015-10-19",
  "subject": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "referrer": null,
  "consultant": null,
  "location": null,
  "title": "Office Visit",
  "subtitle": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/consults/:id`

Update an existing consult object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the consult
subject | [Patient](#patients) | The subject of the consult
referrer | [MedicalPractitioner](#medical-practitioners) | The referring doctor
consultant | [MedicalPractioner](#medical-practitioners) | THe consulting doctor
location | [MedicalFacility](#medical-facilities) | The location of the consult
title | String | The title of the consult
subtitle | String | The subtitle of the consult
notes | Array of [TextSection](#text-sections) | The notes for the consult


### Delete an consult
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/consults/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "deleted": true
}
```

Permanently delete an consult.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/consults/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the consult to delete
