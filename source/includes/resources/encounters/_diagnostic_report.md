## Diagnostic Reports
This is an object representing a diagnostic report. A `DiagnosticReport` object includes

* Laborary (Clinical Chemistry, Hematology, Migrobiology, etc.)
* Other diagnostics - Cardiology, Gastroenterology etc.

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
    "object": "MedicalPractitioner",
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
  "conclusion": null,
  "presentedForm": {
    "object": "MedicalRecordPdf",
    "referenceId": "06aa180e-f3ba-4614-a4a6-2a11debad0e0"
  }
}
```
Return a diagnostic report object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/diagnostic-reports/:id`

#### URL Parameters
Parameter | Description
--------- | -----------
id | The ID of the diagnostic report to be retrieved.


### List diagnostic reports
> Example request:

```shell
curl "https://api.picnichealth.com/v1/diagnostic-reports" \
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
      "object": "MedicalPractitioner",
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
    "presentedForm": {
      "object": "DataSource",
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
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/diagnostic-reports" \
  -d effectiveDate="2015-10-17" \
  -d performer='{ "object": "MedicalPractitioner", "referenceId": "b034557d-5dbe-4812-ab13-4678c1ef8daf" }' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "DiagnosticReport",
  "id": "b08c2faf-8cde-4075-b25f-aed2ebe0f657",
  "effectiveDate": "2015-10-17",
  "performer": {
    "object": "MedicalPractitioner",
    "referenceId": "b034557d-5dbe-4812-ab13-4678c1ef8daf"
  },
  "result": null,
  "conclusion": null,
  "presentedForm": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/diagnostic-reports`

Create a new diagnostic report object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the observation
performer | [MedicalPractitioner](#medical-practitioners) | The medical practitioner who performed the diagnostics
result | Array of [Observation](#observations) | The lab test panels for the diagnostic report
conclusion | String | The conclusion or narrative of the diagnostic report
presentedForm | [DataSource](#data-sources) | The data source of the diagnostic report

### Update diagnostic report
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/diagnostic-reports/b08c2faf-8cde-4075-b25f-aed2ebe0f657" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "DiagnosticReport",
  "id": "b08c2faf-8cde-4075-b25f-aed2ebe0f657",
  "effectiveDate": "2015-10-19",
  "performer": {
    "object": "MedicalPractitioner",
    "referenceId": "b034557d-5dbe-4812-ab13-4678c1ef8daf"
  },
  "result": null,
  "conclusion": null,
  "presentedForm": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/diagnostic-reports/:id`

Update an existing diagnostic report object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the diagnostic report
performer | [MedicalPractitioner](#medical-practitioners) | The medical practitioner who performed the diagnostics
result | Array of [Observation](#observations) | The lab test panels for the diagnostic report
conclusion | String | The conclusion or narrative of the diagnostic report
presentedForm | [DataSource](#data-sources) | The data source of the diagnostic report

### Delete diagnostic report
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/diagnostic-reports/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "deleted": true
}
```

Permanently delete a diagnostic report

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/diagnostic-reports/:id`

#### URL Parameters
Parameter | DataType | Description
--------- | -------- | -----------
id | String | The ID of the diagnostic report to delete
