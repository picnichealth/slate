## Hospitalizations
This is an object representing a hospitalization.

### Get a specific hospitalization
> Example request:

```shell
curl "https://api.picnichealth.com/v1/hospitalizations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Hospitalization",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "date": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "doctorList": [
    {
      "role": "consultant",
      "doctor": {
        "object": "MedicalPractitioner",
        "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
      }
    },
    {
      "role": "referrer",
      "doctor": {
        "object": "MedicalPractitoner",
        "referenceId": "0aeb1158-66d6-4e46-9ef6-e614bb6cc34a"
      }
    }
  ],
  "location": {
    "object": "MedicalFacility",
    "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
  },
  "notes": [
    {
      "object": "Note",
      "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
    }
  ]
}
```

Return an hospitalization

#### HTTP Request
`GET https://api.picnichealth.com/v1/hospitalizations/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the hospitalization to be retrieved.


### List hospitalizations
> Example request:

```shell
curl "https://api.picnichealth.com/v1/hospitalizations" \
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
      "object": "Hospitalization",
      "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
      "date": "2015-10-17",
      "patient": {
        "object": "Patient",
        "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
      },
      "doctorList": [
        {
          "role": "consultant",
          "doctor": {
            "object": "MedicalPractitioner",
            "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
          }
        },
        {
          "role": "referrer",
          "doctor": {
            "object": "MedicalPractitoner",
            "referenceId": "0aeb1158-66d6-4e46-9ef6-e614bb6cc34a"
          }
        }
      ],
      "location": {
        "object": "MedicalFacility",
        "referenceId": "00993db8-fc4e-4276-9e41-dbeb3e72fbfd"
      },
      "notes": [
        {
          "object": "Note",
          "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
        }
      ]
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of hospitalizations

### Create a hospitalization
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/hospitalizations" \
  -d date="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Hospitalization",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "date": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "doctorList": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/hospitalizations`

Create a new hospitalization object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the hospitalization
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the hospitalization
notes | Array of [TextSection](#text-sections) | The notes for the hospitalization


### Update a hospitalization
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/hospitalizations/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -d date="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Hospitalization",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "date": "2015-10-19",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "referrer": null,
  "hospitalizationant": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/hospitalizations/:id`

Update an existing hospitalization object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the hospitalization
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the hospitalization
notes | Array of [TextSection](#text-sections) | The notes for the hospitalization


### Delete an hospitalization
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/hospitalizations/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "deleted": true
}
```

Permanently delete an hospitalization.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/hospitalizations/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the hospitalization to delete
