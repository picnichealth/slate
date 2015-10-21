## Imaging Studies

This is an object representing an imaging study.

### Get a specific imaging study
> Example request:

```shell
curl "https://api.picnichealth.com/v1/imaging-studies/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Observation",
  "id": "ad37701d-7228-4904-9945-7c537b2c7848",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "fa316bf8-6d58-4971-8de2-5d003c582540"
  },
  "doctorList": [
    {
      "role": "referrer",
      "doctor": {
        "object": "MedicalPractitioner",
        "referenceId": "6f821cab-b345-46db-ba1e-e5b7db2e16ed"
      }
    },
    {
      "role": "performer",
      "doctor": {
        "object": "MedicalPractitoner",
        "referenceId": "1e04e410-2e68-4241-b3e4-c4181af199a4"
      }
    }
  ],
  "medicalFacility": {
    "object": "MedicalFacility",
    "referenceId": "d670e59d-b0cf-4ac3-830b-892735301748"
  },
  "dicom": [
    {
      "studyUid": "2.16.840.1.113786.1.661.8.594745134.757",
      "viewerUrl": "https://cloud.app.box.com/dicom_viewer/27705542820/manifest.boxdicom?sharedName=onsnmi460st8qlf9q55huv71kre7cxoa"
    }
  ]
}
```
Return an imaging study object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/imaging-studies/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the imaging study to be retrieved.

### List imaging studies
> Example request:

```shell
curl "https://api.picnichealth.com/v1/imaging-studies" \
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
      "object": "Observation",
      "id": "ad37701d-7228-4904-9945-7c537b2c7848",
      "effectiveDate": "2015-10-17",
      "patient": {
        "object": "Patient",
        "referenceId": "fa316bf8-6d58-4971-8de2-5d003c582540"
      },
      "doctorList": [
        {
          "role": "referrer",
          "doctor": {
            "object": "MedicalPractitioner",
            "referenceId": "6f821cab-b345-46db-ba1e-e5b7db2e16ed"
          }
        },
        {
          "role": "performer",
          "doctor": {
            "object": "MedicalPractitoner",
            "referenceId": "1e04e410-2e68-4241-b3e4-c4181af199a4"
          }
        }
      ],
      "medicalFacility": {
        "object": "MedicalFacility",
        "referenceId": "d670e59d-b0cf-4ac3-830b-892735301748"
      },
      "dicom": [
        {
          "studyUid": "2.16.840.1.113786.1.661.8.594745134.757",
          "viewerUrl": "https://cloud.app.box.com/dicom_viewer/27705542820/manifest.boxdicom?sharedName=onsnmi460st8qlf9q55huv71kre7cxoa"
        }
      ]
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of imaging study objects

### Create an imaging study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/imaging-studies" \
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -d dicom='[{ "viewerUrl": "https://www.medxt.com/docs/pathology_test" }]' \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "ImagingStudy",
  "id": "1871ebca-d7f2-47e3-bbaf-72e87e022cdb",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "doctorList": null,
  "medicalFacility": null,
  "description": null,
  "dicom": [
    {
      "studyUid": null,
      "viewerUrl": "https://www.medxt.com/docs/pathology_test"
    }
  ]
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/imaging-studies`

Create a new imaging study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the imaging study
patient | [Patient](#patients) | The patient for whom the imaging study was made
doctorList | Array of Objects | The list of doctors involved
medicalFaciltiy | [MedicalFacility](#medical-facilities) | The medical facility where the imaging study was made
description | String | The description of the imaging study
dicom | Array of Objects | The array of objects for dicom

### Update an imaging study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/imaging-studies/1871ebca-d7f2-47e3-bbaf-72e87e022cdb" \
  -d effectiveDate="2015-10-19" \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "ImagingStudy",
  "id": "1871ebca-d7f2-47e3-bbaf-72e87e022cdb",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "doctorList": null,
  "medicalFacility": null,
  "description": null,
  "dicom": [
    {
      "studyUid": null,
      "viewerUrl": "https://www.medxt.com/docs/pathology_test"
    }
  ]
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/imaging-studies`

Update an existing imaging study object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the imaging study
patient | [Patient](#patients) | The patient for whom the imaging study was made
doctorList | Array of Objects | The list of doctors involved
medicalFaciltiy | [MedicalFacility](#medical-facilities) | The medical facility where the imaging study was made
description | String | The description of the imaging study
dicom | Array of Objects | The array of objects for dicom

### Delete an imaging study
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/imaging-studies/1871ebca-d7f2-47e3-bbaf-72e87e022cdb" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "1871ebca-d7f2-47e3-bbaf-72e87e022cdb",
  "deleted": true
}
```

Permanently delete an imaging study

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/imaging-studies/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the imaging study to delete
