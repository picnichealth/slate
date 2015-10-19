## Diagnostic Reports
This is an object representing a diagnostic report.

### Get a specific diagnostic report
> Example request:

```shell
curl "https://api.picnichealth.com/v1/diagnostic-reports/a15ad9e5-d96b-4ebf-9781-bccc3707932d" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "DiagnosticReport",
  "id": "a15ad9e5-d96b-4ebf-9781-bccc3707932d",
  "effectiveDate": "2015-10-17",
  "performer": {
    "object": "medicalPractitioner",
    "referenceId": "ad5ea88e-a79a-4431-98ae-45b3ef254f8a"
  },
  "result": [
    {
      "object": "Observation",
      "referenceId": "9899e9d3-be6e-4f83-942d-cd755722c672"
    },
    {
      "object": "Observation",
      "referenceId": "ae8a6262-33d1-46f1-b8d9-ca2dbd42bef6"
    },
    {
      "object": "Observation",
      "referenceId": "5f2eaea8-c2a4-43e1-ba70-44f3b59c7052"
    },
    {
      "object": "Observation",
      "referenceId": "ef45c193-2712-4b0e-b329-3364c19f7233"
    }
  ],
  "imagingStudy": {
    "object": "ImagingStudy",
    "referenceId": "c1c66e17-f31d-481f-81a5-3b8712eda46f"
  },
  "presentedForm": {
    "object": "MedicalRecordPdf",
    "referenceId": "06aa180e-f3ba-4614-a4a6-2a11debad0e0"
  }
}
```
Return a diagnostic report object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/diagnostic reports/:id`

#### URL Parameters
Parameter | Description
--------- | -----------
id | The ID of the diagnostic report to be retrieved.


### List diagnostic reports
> Example request:

```shell
curl "https://api.picnichealth.com/v1/diagnostic reports" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "DiagnosticReport",
    "id": "a15ad9e5-d96b-4ebf-9781-bccc3707932d",
    "effectiveDate": "2015-10-17",
    "performer": {
      "object": "medicalPractitioner",
      "referenceId": "ad5ea88e-a79a-4431-98ae-45b3ef254f8a"
    },
    "result": [
      {
        "object": "Observation",
        "referenceId": "9899e9d3-be6e-4f83-942d-cd755722c672"
      },
      {
        "object": "Observation",
        "referenceId": "ae8a6262-33d1-46f1-b8d9-ca2dbd42bef6"
      },
      {
        "object": "Observation",
        "referenceId": "5f2eaea8-c2a4-43e1-ba70-44f3b59c7052"
      },
      {
        "object": "Observation",
        "referenceId": "ef45c193-2712-4b0e-b329-3364c19f7233"
      }
    ],
    "imagingStudy": {
      "object": "ImagingStudy",
      "referenceId": "c1c66e17-f31d-481f-81a5-3b8712eda46f"
    },
    "presentedForm": {
      "object": "MedicalRecordPdf",
      "referenceId": "06aa180e-f3ba-4614-a4a6-2a11debad0e0"
    }
  },
  {
    "...": "..."
  }
]
```

Return a list of diagnostic report objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/diagnostic-reports`

### Create a diagnostic report
TODO

### Update diagnostic report
TODO

### Delete diagnostic report
Permanently delete a diagnostic report

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/diagnostic-reports/:id`

#### URL Parameters
Parameter | DataType | Description
--------- | -------- | -----------
id | String | The ID of the diagnostic report
