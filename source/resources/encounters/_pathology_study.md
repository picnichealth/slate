## Pathology Studies
This is an object representing an pathology study.

### Get a specific pathology study
> Example request:

```shell
curl "https://api.picnichealth.com/v1/pathology-studies/79689692-b639-4c56-b57e-1528d2550b5e" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "PathologyStudy",
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
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
  "title": "Pathology",
  "subtitle": "GI Biopsy",
  "notes": [
    {
      "object": "TextSection",
      "referenceId": "df6f12d9-be67-4644-8a73-6ac9843684df"
    }
  ]
}
```

Return a pathology study.

#### HTTP Request
`GET https://api.picnichealth.com/v1/pathology-studies/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the pathology study to be retrieved.


### List pathology studies
> Example request:

```shell
curl "https://api.picnichealth.com/v1/pathology-studies" \
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
      "object": "PathologyStudy",
      "id": "79689692-b639-4c56-b57e-1528d2550b5e",
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
          "object": "TextSection",
          "referenceId": "df6f12d9-be67-4644-8a73-6ac9843684df"
        }
      ]
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of pathology studies

### Create a pathology study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/pathology-studies" \
  -d date="2015-10-17" \
  -d patient='{ object: "Patient", referenceId: "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca" }' \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "PathologyStudy",
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
  "date": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "doctorList": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/pathology-studies`

Create a new pathology study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the pathology study
patient | [Patient](#patients) | The patient of the pathology study
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the pathology study
notes | Array of [TextSection](#text-sections) | The notes for the pathology study


### Update a pathology study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/pathology-studies/79689692-b639-4c56-b57e-1528d2550b5e" \
  -d date="2015-10-19" \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "PathologyStudy",
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
  "date": "2015-10-19",
  "patient": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
  "doctorList": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/pathology-studies/:id`

Update an existing pathology study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the pathology study
patient | [Patient](#patients) | The patient of the pathology study
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the pathology study
notes | Array of [TextSection](#text-sections) | The notes for the pathology study

### Delete an pathology study
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/pathology-studies/79689692-b639-4c56-b57e-1528d2550b5e" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
  "deleted": true
}
```

Permanently delete a pathology study.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/pathology-studies/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the pathology study to delete
