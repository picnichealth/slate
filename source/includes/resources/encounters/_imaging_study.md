## Imaging Studies

This is an object representing an imaging study.

### Get a specific imaging study
> Example request:

```shell
curl "https://api.picnichealth.com/v1/imaging-studies/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY"
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
  "referrer": {
    "object": "MedicalPractitoner",
    "referenceId": "6f821cab-b345-46db-ba1e-e5b7db2e16ed"
  },
  "performer": {
    "object": "MedicalPractitoner",
    "referenceId": "1e04e410-2e68-4241-b3e4-c4181af199a4"
  },
  "medicalFacility": {
    "object": "MedicalFacility",
    "referenceId": "d670e59d-b0cf-4ac3-830b-892735301748"
  },
  "title": "X-Ray",
  "subtitle": "Chest",
  "series": [
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
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "Observation",
    "id": "ad37701d-7228-4904-9945-7c537b2c7848",
    "effectiveDate": "2015-10-17",
    "patient": {
      "object": "Patient",
      "referenceId": "fa316bf8-6d58-4971-8de2-5d003c582540"
    },
    "referrer": {
      "object": "MedicalPractitoner",
      "referenceId": "6f821cab-b345-46db-ba1e-e5b7db2e16ed"
    },
    "performer": {
      "object": "MedicalPractitoner",
      "referenceId": "1e04e410-2e68-4241-b3e4-c4181af199a4"
    },
    "medicalFacility": {
      "object": "MedicalFacility",
      "referenceId": "d670e59d-b0cf-4ac3-830b-892735301748"
    },
    "title": "X-Ray",
    "subtitle": "Chest",
    "description": "Amorphous enhancing tissue just above the vaginal cuff and extending to the pelvic sidewalls with central complex fluid within it. Post-op changes with seroma versus phlegmon with central abscess. Correlate with clinical history and laboratory assessment.",
    "series": [
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
```

Return a list of imaging study objects

### Create an imaging study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/imaging-studies" \
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -d title="CT Scan" \
  -d series='[{ "viewerUrl": "https://www.medxt.com/docs/pathology_test" }]' \
  -H "Authorization: YOUR_API_KEY" \
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
  "referrer": null,
  "performer": null,
  "medicalFacility": null,
  "title": "CT Scan",
  "subtitle": null,
  "description": null,
  "series": [
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
referrer | [MedicalPractitioner](#medical-practitioners) | The referral doctor of the imaging study
performer | [MedicalPractitioner](#medical-practitioners) | The performing doctor of the imaging study
medicalFaciltiy | [MedicalFacility](#medical-facilities) | The medical facility where the imaging study was made
title | String | The title of the imaging study
subtitle | String | The subtitle of the imaging study
description | String | The description of the imaging study
series | Array of objects | The series of the imaging study

### Update an imaging study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/imaging-studies/1871ebca-d7f2-47e3-bbaf-72e87e022cdb" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
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
  "referrer": null,
  "performer": null,
  "medicalFacility": null,
  "title": "CT Scan",
  "subtitle": null,
  "description": null,
  "series": [
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
referrer | [MedicalPractitioner](#medical-practitioners) | The referral doctor of the imaging study
performer | [MedicalPractitioner](#medical-practitioners) | The performing doctor of the imaging study
medicalFaciltiy | [MedicalFacility](#medical-facilities) | The medical facility where the imaging study was made
title | String | The title of the imaging study
subtitle | String | The subtitle of the imaging study
description | String | The description of the imaging study
series | Array of objects | The series of the imaging study

### Delete an imaging study
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/imaging-studies/1871ebca-d7f2-47e3-bbaf-72e87e022cdb" \
  -H "Authorization: YOUR_API_KEY
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
