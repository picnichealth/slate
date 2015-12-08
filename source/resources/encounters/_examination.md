## Examinations
This is an object representing an examination.

### Get a specific examination
> Example request:

```shell
curl "https://api.picnichealth.com/v1/examinations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Examination",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "date": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "doctorList": [
    {
      "role": "performer",
      "doctor": {
        "object": "MedicalPractitioner",
        "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
      }
    }
  ],
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

Return an examination

#### HTTP Request
`GET https://api.picnichealth.com/v1/examinations/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the examination to be retrieved.


### List examinations
> Example request:

```shell
curl "https://api.picnichealth.com/v1/examinations" \
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
      "object": "Examination",
      "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
      "date": "2015-10-17",
      "patient": {
        "object": "Patient",
        "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
      },
      "doctorList": [
        {
          "role": "performer",
          "doctor": {
            "object": "MedicalPractitioner",
            "referenceId": "532b9e57-18ba-4024-8440-1abe5ba17c39"
          }
        }
      ],
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
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of examinations

### Create an examination
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/examinations" \
  -u YOUR_API_KEY" \
  -d date="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" }
```

> Example response:

```json
{
  "object": "Examination",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
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
`POST https://api.picnichealth.com/v1/examinations`

Create a new imaging study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the examination
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the examination
notes | Array of [TextSection](#text-sections) | The notes for the examination

### Update an examination
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/examinations/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -u YOUR_API_KEY \
  -d date="2015-10-19"
```

> Example response:

```json
{
  "object": "Examination",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "date": "2015-10-19",
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
`POST https://api.picnichealth.com/v1/examinations/:id`

Update an existing examination object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the examination
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the examination
notes | Array of [TextSection](#text-sections) | The notes for the examination

### Delete an examination
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/examinations/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "deleted": true
}
```

Permanently delete an examination.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/examinations/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the examination to delete
