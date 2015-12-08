## Laboratory Tests
This is an object representing a laboratory test. A `LaboratoryTest` object includes Clinical Chemistry, Hematology, Migrobiology, etc.

### Get a specific laboratory test
> Example request:

```shell
curl "https://api.picnichealth.com/v1/laboratory-tests/a15ad9e5-d96b-4ebf-9781-bccc3707932d" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "LaboratoryTest",
  "id": "a15ad9e5-d96b-4ebf-9781-bccc3707932d",
  "date": "2015-10-17",
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
Return a laboratory test object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/laboratory-tests/:id`

#### URL Parameters
Parameter | Description
--------- | -----------
id | The ID of the laboratory test to be retrieved.


### List laboratory tests
> Example request:

```shell
curl "https://api.picnichealth.com/v1/laboratory-tests" \
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
      "object": "LaboratoryTest",
      "id": "a15ad9e5-d96b-4ebf-9781-bccc3707932d",
      "date": "2015-10-17",
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
}
```

Return a list of laboratory test objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/laboratory-tests`

### Create a laboratory test
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/laboratory-tests" \
  -u YOUR_API_KEY: \
  -d date="2015-10-17" \
  -d performer='{ "object": "MedicalPractitioner", "referenceId": "b034557d-5dbe-4812-ab13-4678c1ef8daf" }'
```

> Example response:

```json
{
  "object": "LaboratoryTest",
  "id": "b08c2faf-8cde-4075-b25f-aed2ebe0f657",
  "date": "2015-10-17",
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
`POST https://api.picnichealth.com/v1/laboratory-tests`

Create a new laboratory test object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the observation
performer | [MedicalPractitioner](#medical-practitioners) | The medical practitioner who performed the diagnostics
result | Array of [Observation](#observations) | The lab test panels for the laboratory test
conclusion | String | The conclusion or narrative of the laboratory test
presentedForm | [DataSource](#data-sources) | The data source of the laboratory test

### Update laboratory test
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/laboratory-tests/b08c2faf-8cde-4075-b25f-aed2ebe0f657" \
  -u YOUR_API_KEY: \
  -d date="2015-10-19"
```

> Example response:

```json
{
  "object": "LaboratoryTest",
  "id": "b08c2faf-8cde-4075-b25f-aed2ebe0f657",
  "date": "2015-10-19",
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
`POST https://api.picnichealth.com/v1/laboratory-tests/:id`

Update an existing laboratory test object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date | String | The date of the laboratory test
performer | [MedicalPractitioner](#medical-practitioners) | The medical practitioner who performed the diagnostics
result | Array of [Observation](#observations) | The lab test panels for the laboratory test
conclusion | String | The conclusion or narrative of the laboratory test
presentedForm | [DataSource](#data-sources) | The data source of the laboratory test

### Delete laboratory test
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/laboratory-tests/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "deleted": true
}
```

Permanently delete a laboratory test

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/laboratory-tests/:id`

#### URL Parameters
Parameter | DataType | Description
--------- | -------- | -----------
id | String | The ID of the laboratory test to delete
