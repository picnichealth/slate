# Medical Facilities
This is an object representing a medical facility

### Get a specific medical facility
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medical-facilities/2b442547-d98d-4788-9bc0-46a5229dd2b5" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "MedicalFacility",
  "id": "2b442547-d98d-4788-9bc0-46a5229dd2b5",
  "name": "Stanford Health Care",
  "address": {
    "line1": "430 Broadway St",
    "line2": null,
    "city": "Redwood City",
    "state": "California",
    "postalCode": "94063"
  },
  "phone": "6507235721",
  "fax": "6507259821"
}
```
Return a medical facility object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/medical-facilities/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the medical facility to be retrieved.

# Medical Practitioners
This is an object representing a medical practitioner

### Get a specific medical practitioner
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medical-practitioners/2b442547-d98d-4788-9bc0-46a5229dd2b5" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "MedicalPractitioner",
  "id": "b034557d-5dbe-4812-ab13-4678c1ef8daf",
  "name": "Steven Lim",
  "address": {
    "line1": "144 17 St",
    "line2": null,
    "city": "San Francisco",
    "state": "California",
    "postalCode": "94303"
  },
  "specialty": "Internal Medicine",
  "email": "lim.steven.123@gmail.com"
}
```
Return a medical practitioner object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/medical-practitioners/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the medical practitioner to be retrieved.

# Patients
This is an object representing a patient.

### Get a specific patient
> Example request:

```shell
curl "https://api.picnichealth.com/v1/patients/388d2e58-b3fd-45a2-84b2-c95108a54b7e" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Patient",
  "email": "KathyBTorres@teleworm.us",
  "legalName": "Kathy Torres",
  "birthDate": "1964-01-16",
  "address": {
    "line1": "1572 Grove Street",
    "line2": null,
    "city": "Selden",
    "state": "New York",
    "postalCode": "11784"
  },
  "gender": "female"
}
```
Return a patient object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/patients/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | The ID of the patient to be retrieved.


### List patients
> Example request:

```shell
curl "https://api.picnichealth.com/v1/patients" \
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
      "object": "Patient",
      "email": "KathyBTorres@teleworm.us",
      "legalName": "Kathy Torres",
      "birthDate": "1964-01-16",
      "address": {
        "line1": "1572 Grove Street",
        "line2": null,
        "city": "Selden",
        "state": "New York",
        "postalCode": "11784"
      },
      "gender": "female"
    },
    {
      "...": "..."
    }
  ]
}

```

Return a list of patient objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/patients`

## Lab Test Results
This is an object representing a lab test result.

### Get a specific lab test result
> Example request:

```shell
curl "https://api.picnichealth.com/v1/lab-test-results/c8d5df8c-67ad-491e-958a-ffdd8913ff6e" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "LabTestResult",
  "id": "c8d5df8c-67ad-491e-958a-ffdd8913ff6e",
  "effectiveDate": "2015-10-17",
  "name": "Neutrophils (%)",
  "textValue": null,
  "positiveOrNegativeValue": null,
  "numberValue": 52.2,
  "valueRangeType": null,
  "valueRangeLowValue":  null,
  "valueRangeHighValue": null,
  "valueRangeBorderValue": null,
  "referenceRangeType": "between",
  "referenceRangeLowValue": 42,
  "referenceRangeHighValue": 75,
  "referenceRangeBorderValue": null,
  "referenceRangePositiveOrNegativeValue": null,
  "referenceRangeTextValue": null,
  "resultUnit": "%",
  "important": 1,
  "coding": {
    "object": "Code",
    "referenceId": "98f391e1-eff0-4f1e-98c5-0ddab280b42a"
  }
}
```
Return a lab test result object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/lab-test-results/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the lab test result to be retrieved.

### List lab test results
> Example request:

```shell
curl "https://api.picnichealth.com/v1/lab-test-results" \
  -u YOUR_API_KEY:
```

> Example response:

```json
[
  {
    "object": "LabTestResult",
    "id": "c8d5df8c-67ad-491e-958a-ffdd8913ff6e",
    "effectiveDate": "2015-10-17",
    "name": "Neutrophils (%)",
    "textValue": null,
    "positiveOrNegativeValue": null,
    "numberValue": 52.2,
    "valueRangeType": null,
    "valueRangeLowValue":  null,
    "valueRangeHighValue": null,
    "valueRangeBorderValue": null,
    "referenceRangeType": "between",
    "referenceRangeLowValue": 42,
    "referenceRangeHighValue": 75,
    "referenceRangeBorderValue": null,
    "referenceRangePositiveOrNegativeValue": null,
    "referenceRangeTextValue": null,
    "resultUnit": "%",
    "important": 1,
    "coding": {
      "object": "Code",
      "referenceId": "98f391e1-eff0-4f1e-98c5-0ddab280b42a"
    }
  },
  {
    "...": "..."
  }
]
```

Return a list of lab test result objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/lab-test-results`

### Create a lab test result
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/lab-test-results" \
  -d name="C-Reactive Protein" \
  -d positiveOrNegativeValue="positive" \
  -d referenceRangeType="positiveNegative"
  -d referenceRangePositiveOrNegativeValue="positive" \
  -d important=1 \
  -d coding='{ "object": "Code", "referenceId": "98f391e1-eff0-4f1e-98c5-0ddab280b42a" }',
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "LabTestResult",
  "id": "133651e7-2ada-45bd-91ab-d91fde4612fa",
  "effectiveDate": "2015-10-18",
  "name": "C-Reactive Protein",
  "textValue": null,
  "positiveOrNegativeValue": "positive",
  "numberValue": null,
  "valueRangeType": null,
  "valueRangeLowValue":  null,
  "valueRangeHighValue": null,
  "valueRangeBorderValue": null,
  "referenceRangeType": "positiveNegative",
  "referenceRangeLowValue": null,
  "referenceRangeHighValue": null,
  "referenceRangeBorderValue": null,
  "referenceRangePositiveOrNegativeValue": "positive",
  "referenceRangeTextValue": null,
  "resultUnit": null,
  "important": 1,
  "coding": {
    "object": "Code",
    "referenceId": "C62C39B8-99B2-433F-AAC9-4EC23E88C7AF"
  }
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/lab-test-results`

Create a new lab test result object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The collection date of the lab test result
name | String | The name of the lab test result
textValue | String | The text value of the lab test result
positiveOrNegativeValue | String | The positive or negative value of the lab test result. The value must be `positve` or `negative`
numberValue | Number | The numeric value of the lab test result
valueRangeType | Number | The range type of the value. The value must be one of the following: `exact`, `greaterThan`, `lessThan`, `greaterThanOrEqualTo`, `lessThanOrEqualTo`, `between`, `text`, `positiveNegative`
valueRangeLowValue | Number | The lower bound value of the lab test result
valueRangeHighValue | Number | The upper bound value of the lab test result
valueRangeBorderValue | Number | The border value of the lab test result
referenceRangeType | String | The range type of the reference range. The value must be one of the following: `exact`, `greaterThan`, `lessThan`, `greaterThanOrEqualTo`, `lessThanOrEqualTo`, `between`, `text`, `positiveNegative`
referenceRangeLowValue | Number | The lower bound value of the reference range
referenceRangeHighValue | Number | The upper bound value of the reference range
referenceRangeBorderValue | Number | The border value of the reference range
referenceRangePositiveOrNegativeValue | String | The reference value of positive or negative lab test result. The value must be `positive` or `negative`
referenceRangeTextValue | String | The text value of the reference range
resultUnit | String | The unit of the lab test result
important | Integer | The positive integer indicating the importance of the lab test result. The value `0` is the most important.
coding | [Code](#codes) | The code for the lab test result. This is usually referenced to a LOINC code.

### Update a lab test result
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/lab-test-results/133651e7-2ada-45bd-91ab-d91fde4612fa" \
  -d positiveOrNegativeValue="negative"
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "LabTestResult",
  "id": "133651e7-2ada-45bd-91ab-d91fde4612fa",
  "effectiveDate": "2015-10-18",
  "name": "C-Reactive Protein",
  "textValue": null,
  "positiveOrNegativeValue": "negative",
  "numberValue": null,
  "valueRangeType": null,
  "valueRangeLowValue":  null,
  "valueRangeHighValue": null,
  "valueRangeBorderValue": null,
  "referenceRangeType": "positiveNegative",
  "referenceRangeLowValue": null,
  "referenceRangeHighValue": null,
  "referenceRangeBorderValue": null,
  "referenceRangePositiveOrNegativeValue": "positive",
  "referenceRangeTextValue": null,
  "resultUnit": null,
  "important": 1,
  "coding": {
    "object": "Code",
    "referenceId": "C62C39B8-99B2-433F-AAC9-4EC23E88C7AF"
  }
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/lab-test-results/:id`

Update a lab test result

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The collection date of the lab test result
name | String | The name of the lab test result
textValue | String | The text value of the lab test result
positiveOrNegativeValue | String | The positive or negative value of the lab test result. The value must be `positve` or `negative`
numberValue | Number | The numeric value of the lab test result
valueRangeType | Number | The range type of the value. The value must be one of the following: `exact`, `greaterThan`, `lessThan`, `greaterThanOrEqualTo`, `lessThanOrEqualTo`, `between`, `text`, `positiveNegative`
valueRangeLowValue | Number | The lower bound value of the lab test result
valueRangeHighValue | Number | The upper bound value of the lab test result
valueRangeBorderValue | Number | The border value of the lab test result
referenceRangeType | String | The range type of the reference range. The value must be one of the following: `exact`, `greaterThan`, `lessThan`, `greaterThanOrEqualTo`, `lessThanOrEqualTo`, `between`, `text`, `positiveNegative`
referenceRangeLowValue | Number | The lower bound value of the reference range
referenceRangeHighValue | Number | The upper bound value of the reference range
referenceRangeBorderValue | Number | The border value of the reference range
referenceRangePositiveOrNegativeValue | String | The reference value of positive or negative lab test result. The value must be `positive` or `negative`
referenceRangeTextValue | String | The text value of the reference range
resultUnit | String | The unit of the lab test result
important | Integer | The positive integer indicating the importance of the lab test result. The value `0` is the most important.
coding | [Code](#codes) | The code for the lab test result. This is usually referenced to a LOINC code.

### Delete a lab test result
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/lab-test-results/133651e7-2ada-45bd-91ab-d91fde4612fa" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "133651e7-2ada-45bd-91ab-d91fde4612fa",
  "deleted": true
}
```

Permanently delete a lab test result

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/lab-test-results/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the lab test result to delete
# Encounters
## Examinations
This is an object representing an examination.

### Get a specific examination
> Example request:

```shell
curl "https://api.picnichealth.com/v1/examinations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Examination",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "effectiveDate": "2015-10-17",
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
      "object": "Examination",
      "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
      "effectiveDate": "2015-10-17",
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
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Examination",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "effectiveDate": "2015-10-17",
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
effectiveDate | String | The date of the examination
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the examination
notes | Array of [TextSection](#text-sections) | The notes for the examination

### Update an examination
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/examinations/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Examination",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "effectiveDate": "2015-10-19",
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
effectiveDate | String | The date of the examination
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the examination
notes | Array of [TextSection](#text-sections) | The notes for the examination

### Delete an examination
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/examinations/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -H "Authorization: YOUR_API_KEY
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
{
  "object": "List",
  "length": 20,
  "hasMore": true,
  "data": [
    {
      "object": "Consult",
      "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
      "effectiveDate": "2015-10-17",
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
}
```

Return a list of consults

### Create a consult
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/consults" \
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
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
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "doctorList": null,
  "location": null,
  "title": "Office Visit",
  "subtitle": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/consults`

Create a new consult object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the consult
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
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
  "patient": {
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
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
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
## Procedures
This is an object representing an procedure.

### Get a specific procedure
> Example request:

```shell
curl "https://api.picnichealth.com/v1/procedures/1b26577b-04ea-4fc8-895a-1f466b707e63" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Procedure",
  "id": "1b26577b-04ea-4fc8-895a-1f466b707e63",
  "effectiveDate": "2015-10-17",
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
      "role": "requester",
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
      "object": "Procedure",
      "id": "1b26577b-04ea-4fc8-895a-1f466b707e63",
      "effectiveDate": "2015-10-17",
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
          "role": "requester",
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

Return a list of procedures

### Create a procedure
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/procedures" \
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -u YOUR_API_KEY \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Procedure",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "effectiveDate": "2015-10-17",
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
`POST https://api.picnichealth.com/v1/procedures`

Create a new procedure object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the procedure
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the procedure
notes | Array of [TextSection](#text-sections) | The notes for the procedure


### Update a procedure
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/procedures/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -d effectiveDate="2015-10-19" \
  -u YOUR_API_KEY \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Procedure",
  "id": "2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b",
  "effectiveDate": "2015-10-19",
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
`POST https://api.picnichealth.com/v1/procedures/:id`

Update an existing procedure object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the procedure
patient | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the procedure
notes | Array of [TextSection](#text-sections) | The notes for the procedure


### Delete a procedure
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/procedures/2fdc49ac-bc0b-407d-a6f8-7e23d3db0f4b" \
  -H "Authorization: YOUR_API_KEY:
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
  "effectiveDate": "2015-10-17",
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
      "effectiveDate": "2015-10-17",
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
  -d effectiveDate="2015-10-17" \
  -d patient='{ object: "Patient", referenceId: "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca" }' \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "PathologyStudy",
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
  "effectiveDate": "2015-10-17",
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
effectiveDate | String | The date of the pathology study
patient | [Patient](#patients) | The patient of the pathology study
doctorList | Array of Objects | The list of doctors involved
location | [MedicalFacility](#medical-facilities) | The location of the pathology study
notes | Array of [TextSection](#text-sections) | The notes for the pathology study


### Update a pathology study
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/pathology-studies/79689692-b639-4c56-b57e-1528d2550b5e" \
  -d effectiveDate="2015-10-19" \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "PathologyStudy",
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
  "effectiveDate": "2015-10-19",
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
effectiveDate | String | The date of the pathology study
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
## Genetic Screens
This is an object representing a genetic screen.

### Get a specific genetic screen
> Example request:

```shell
curl "https://api.picnichealth.com/v1/genetic-screens/2c5f5800-6bda-4018-9c11-f4275880495b \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "GeneticScreen",
  "id": "2c5f5800-6bda-4018-9c11-f4275880495b",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
  },
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

Return a genetic screen

#### HTTP Request
`GET https://api.picnichealth.com/v1/genetic-screens/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the genetic screen to be retrieved.


### List genetic screens
> Example request:

```shell
curl "https://api.picnichealth.com/v1/genetic-screens" \
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
      "object": "GeneticScreen",
      "id": "2c5f5800-6bda-4018-9c11-f4275880495b",
      "effectiveDate": "2015-10-17",
      "patient": {
        "object": "Patient",
        "referenceId": "d0f2fe0b-2cf8-4bd6-99c3-fa9c0b3b98ca"
      },
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
    }, {
      "...": "..."
    }
  ]
}
```

Return a list of genetic screens

### Create a genetic screen
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/genetic-screens" \
  -d effectiveDate="2015-10-17" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Genetic Screen",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "effectiveDate": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "participant": null,
  "location": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/genetic-screens`

Create a new genetic screen object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the genetic screen
patient | [Patient](#patients) | The patient of the genetic screen
location | [MedicalFacility](#medical-facilities) | The location of the genetic screen
title | String | The title of the genetic screen
subtitle | String | The subtitle of the genetic screen
notes | Array of [TextSection](#text-sections) | The notes for the genetic screen

### Update a genetic screen
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/genetic-screens/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "GeneticScreen",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "effectiveDate": "2015-10-19",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "participant": null,
  "location": null,
  "title": "Genetic Screen",
  "subtitle": null,
  "notes": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/genetic-screens/:id`

Update an existing genetic screen object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the genetic screen
patient | [Patient](#patients) | The patient of the genetic screen
location | [MedicalFacility](#medical-facilities) | The location of the genetic screen
title | String | The title of the genetic screen
subtitle | String | The subtitle of the genetic screen
notes | Array of [TextSection](#text-sections) | The notes for the genetic screen

### Delete an genetic screen
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/genetic-screens/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "deleted": true
}
```

Permanently delete a genetic screen.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/genetic-screens/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the genetic screen to delete
## Laboratory Tests
This is an object representing a laboratory test. A `LaboratoryTest` object includes Clinical Chemistry, Hematology, Migrobiology, etc.

### Get a specific laboratory test
> Example request:

```shell
curl "https://api.picnichealth.com/v1/laboratory-tests/a15ad9e5-d96b-4ebf-9781-bccc3707932d" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "LaboratoryTest",
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
      "object": "LaboratoryTest",
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
}
```

Return a list of laboratory test objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/laboratory-tests`

### Create a laboratory test
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/laboratory-tests" \
  -d effectiveDate="2015-10-17" \
  -d performer='{ "object": "MedicalPractitioner", "referenceId": "b034557d-5dbe-4812-ab13-4678c1ef8daf" }' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "LaboratoryTest",
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
`POST https://api.picnichealth.com/v1/laboratory-tests`

Create a new laboratory test object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the observation
performer | [MedicalPractitioner](#medical-practitioners) | The medical practitioner who performed the diagnostics
result | Array of [Observation](#observations) | The lab test panels for the laboratory test
conclusion | String | The conclusion or narrative of the laboratory test
presentedForm | [DataSource](#data-sources) | The data source of the laboratory test

### Update laboratory test
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/laboratory-tests/b08c2faf-8cde-4075-b25f-aed2ebe0f657" \
  -d effectiveDate="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "LaboratoryTest",
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
`POST https://api.picnichealth.com/v1/laboratory-tests/:id`

Update an existing laboratory test object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the laboratory test
performer | [MedicalPractitioner](#medical-practitioners) | The medical practitioner who performed the diagnostics
result | Array of [Observation](#observations) | The lab test panels for the laboratory test
conclusion | String | The conclusion or narrative of the laboratory test
presentedForm | [DataSource](#data-sources) | The data source of the laboratory test

### Delete laboratory test
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/laboratory-tests/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY
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
# Encounter Items
## Notes
This is an object representing a note.

### Get a specific note
> Example request:

```shell
curl "https://api.picnichealth.com/v1/notes/89460ec2-323a-4f2f-b2d8-bfc8ef535c99" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Note",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": "Assessment",
  "note": "Malignant neoplasm of unspecified site"
}
```
Return a note object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/notes/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the note to be retrieved.


### List notes
> Example request:

```shell
curl "https://api.picnichealth.com/v1/notes" \
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
      "object": "Note",
      "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
      "encounter": {
        "object": "Examination",
        "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
      },
      "title": "Assessment",
      "note": "Malignant neoplasm of unspecified site"
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of note objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/notes`

### Create a note
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/notes" \
  -d encounter='{ object: "Examination", referenceId: "a8ddb870-c65c-4b31-ba42-8f7b55f37e96" }' \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Note",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": null,
  "note": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/notes`

Create a new note object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | String | The encounter with which the note is associated
title | String | The title of the note
note | String | The content of the note

### Update a note
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/notes/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d title="Impression" \
  -d node="Doing well"
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Note",
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "title": "Impression",
  "note": "Doing well"
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/notes/:id`

Update an existing note

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | String | The encounter with which the note is associated
title | String | The title of the note
note | String | The content of the note

### Delete a note
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/notes/89460ec2-323a-4f2f-b2d8-bfc8ef535c99" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "89460ec2-323a-4f2f-b2d8-bfc8ef535c99",
  "deleted": true
}
```

Permanently delete a note

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/notes/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the note to delete

## Medication Statements
This is an object representing a medication statement.

### Get a specific medication
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medication-statements/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "MedicationStatement",
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "status": "active",
  "effectiveDate": "2015-10-16",
  "medicationCoding": {
    "object": "Code",
    "referenceId": "5172cfcf-0ec9-4c43-ba97-5d6a34182d2b"
  },
  "instruction": "Take 1 cap by mouth 4 times a day before meals and at bedtime.",
  "note": "Below 325mg: negative personality changes. Above 350mg: slow increase in tremors"
}
```
Return a medication statement object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/medication-statements/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | The ID of the medication statement to be retrieved.


### List medication statements
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medication-statements" \
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
      "object": "MedicationStatement",
      "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
      "encounter": {
        "object": "Examination",
        "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
      },
      "status": "active",
      "effectiveDate": "2015-10-16",
      "medicationCoding": {
        "object": "Code",
        "referenceId": "5172cfcf-0ec9-4c43-ba97-5d6a34182d2b"
      },
      "instruction": "Take 1 cap by mouth 4 times a day before meals and at bedtime.",
      "note": "Below 325mg: negative personality changes. Above 350mg: slow increase in tremors"
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of medication statement objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/medication-statements`

### Create an medication
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medication-statements" \
  -d encounter='{ "object": "Examination", "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96" }' \
  -d status="active" \
  -d effectiveDate="2015-10-17" \
  -d medicationCoding='{ "object": "Code", "referenceId:": "eb8992d8-3117-47b3-a660-b9156b2b35bc" }' \
  -d instruction="18 units every morning, 12 units every evening" \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "MedicationStatement",
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "status": "active",
  "effectiveDate": "2015-10-16",
  "medicationCoding": {
    "object": "Code",
    "referenceId": "5172cfcf-0ec9-4c43-ba97-5d6a34182d2b"
  },
  "instruction": "Take 1 cap by mouth 4 times a day before meals and at bedtime.",
  "note": "Below 325mg: negative personality changes. Above 350mg: slow increase in tremors"
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/medication-statements`

Create a new medication statement object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter when the medication statement was recorded
status | String | The status of the medication. It must be `active` or `discontinued`
effectiveDate | String | The date of the medication recorded
medicationCoding | [Code](#codes) | The coding of the medcation
instruction | String | The instruction for the medication
note | String | The note for the medication statement

### Update a medication statement
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medication-statements/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d note="Take 2 cap by mouth 2 times a day before meals"
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "MedicationStatement",
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "encounter": {
    "object": "Examination",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "status": "active",
  "effectiveDate": "2015-10-16",
  "medicationCoding": {
    "object": "Code",
    "referenceId": "5172cfcf-0ec9-4c43-ba97-5d6a34182d2b"
  },
  "instruction": "Take 2 cap by mouth 2 times a day before meals.",
  "note": "Below 325mg: negative personality changes. Above 350mg: slow increase in tremors"
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/medication-statements/:id`

Update a medication statement

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter when the medication statement was recorded
status | String | The status of the medication. It must be `active` or `discontinued`
effectiveDate | String | The date of the medication recorded
medicationCoding | [Code](#codes) | The coding of the medcation
instruction | String | The instruction for the medication
note | String | The note for the medication statement

### Delete a medication statement
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/medication-statements/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "deleted": true
}
```

Permanently delete a medication statement

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/medication-statements/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the medication statement to delete
## Observations
This is an object representing an observation. An `Observation` object includes

* Laboratory Data
* Imaging results like bone density or fetal measurements
* Devices Measurements such EKG data or Pulse Oximetry data
* Clinical assessment tools such as APGAR

### Get a specific observation
> Example request:

```shell
curl "https://api.picnichealth.com/v1/observations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Observation",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "effectiveDate": "2015-10-17",
  "name": "BASIC METABOLIC PANEL",
  "coding": {
    "object": "Code",
    "referenceId": "288EBF7A-9F6F-4E14-8AAD-7E1490C5FA80"
  },
  "encounter": {
    "object": "DiagnosticReport",
    "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
  },
  "component": [
    {
      "object": "LabTestResult",
      "referenceId": "2532abb0-e5d8-4f19-9396-57db85a32a4c"
    },
    {
      "object": "LabTestResult",
      "referenceId": "db621bec-d1ea-42ee-9001-c0b03fde7444"
    },
    {
      "object": "LabTestResult",
      "referenceId": "4afedf9f-894c-4f0c-8af9-60051485731b"
    },
    {
      "object": "LabTestResult",
      "referenceId": "24b2049a-fd3c-48e4-b0b4-6fc37435b0a8"
    },
    {
      "object": "LabTestResult",
      "referenceId": "83c33e9d-d080-4d95-a932-b85594dfd08d"
    },
    {
      "object": "LabTestResult",
      "referenceId": "7e691e49-12a4-4a9b-abca-4cc16f00657a"
    },
    {
      "object": "LabTestResult",
      "referenceId": "7d15c42d-1e8d-480f-83ed-2757522ad4b1"
    },
    {
      "object": "LabTestResult",
      "referenceId": "ceca3d0c-1448-4a42-b4b3-c03f0f5e49c3"
    }
  ]
}
```
Return a lab test result object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/lab-test-results/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the observation to be retrieved.

### List observations
> Example request:

```shell
curl "https://api.picnichealth.com/v1/observations" \
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
      "object": "Observation",
      "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
      "effectiveDate": "2015-10-17",
      "name": "BASIC METABOLIC PANEL",
      "coding": {
        "object": "Code",
        "referenceId": "288EBF7A-9F6F-4E14-8AAD-7E1490C5FA80"
      },
      "encounter": {
        "object": "DiagnosticReport",
        "referenceId": "a8ddb870-c65c-4b31-ba42-8f7b55f37e96"
      },
      "component": [
        {
          "object": "LabTestResult",
          "referenceId": "2532abb0-e5d8-4f19-9396-57db85a32a4c"
        },
        {
          "object": "LabTestResult",
          "referenceId": "db621bec-d1ea-42ee-9001-c0b03fde7444"
        },
        {
          "object": "LabTestResult",
          "referenceId": "4afedf9f-894c-4f0c-8af9-60051485731b"
        },
        {
          "object": "LabTestResult",
          "referenceId": "24b2049a-fd3c-48e4-b0b4-6fc37435b0a8"
        },
        {
          "object": "LabTestResult",
          "referenceId": "83c33e9d-d080-4d95-a932-b85594dfd08d"
        },
        {
          "object": "LabTestResult",
          "referenceId": "7e691e49-12a4-4a9b-abca-4cc16f00657a"
        },
        {
          "object": "LabTestResult",
          "referenceId": "7d15c42d-1e8d-480f-83ed-2757522ad4b1"
        },
        {
          "object": "LabTestResult",
          "referenceId": "ceca3d0c-1448-4a42-b4b3-c03f0f5e49c3"
        }
      ]
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of observation objects

### Create an observation
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/observations" \
  -d effectiveDate="2015-10-17" \
  -d name="CBC with Differential Panel"
  -d coding='{ "object": "Code", "referenceId": "F4AA6E3E-26EC-4EA6-A4A6-C2A3108F8C3C" }
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Observation",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "effectiveDate": "2015-10-17",
  "name": "BASIC METABOLIC PANEL",
  "encounter": null,
  "coding": {
    "object": "Code",
    "referenceId": "288EBF7A-9F6F-4E14-8AAD-7E1490C5FA80"
  },
  "component": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/observations`

Create a new observation object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the observation
name | String | The name of the observation. Usually it is the name of the lab test panel.
coding | [Code](#codes) | The code representing the observation
component | Array of [LabTestResult](#lab-test-results) | The component lab test resuts of the observation

### Update an observation
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/observations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -d effectiveDate="2015-10-19" \
  -d component='[ { object: "LabTestResult", referenceId: "14f360b1-c5ae-40b2-967f-5670315295e0" } ]' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Observation",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "effectiveDate": "2015-10-19",
  "name": "BASIC METABOLIC PANEL",
  "encounter": null,
  "coding": {
    "object": "Code",
    "referenceId": "288EBF7A-9F6F-4E14-8AAD-7E1490C5FA80"
  },
  "component": [
    {
      "object": "LabTestResult",
      "referenceId": "14f360b1-c5ae-40b2-967f-5670315295e0"
    }
  ]
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/observations/:id`

Update an existing observation object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
effectiveDate | String | The date of the observation
name | String | The name of the observation. Usually it is the name of the lab test panel.
coding | [Code](#codes) | The code representing the observation

### Delete an observation
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/observations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "deleted": true
}
```

Permanently delete a observation

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/observations/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the observation to delete
## Conditions
This is an object representing a condition.

### Get a specific condition
> Example request:

```shell
curl "https://api.picnichealth.com/v1/conditions/0507420d-fcf8-4ec9-8bf0-c10bf408e6cd" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Condition",
  "id": "0507420d-fcf8-4ec9-8bf0-c10bf408e6cd",
  "encounter": {
    "object": "Examination",
    "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
  },
  "coding": {
    "object": "Code",
    "referenceId": "f60d40f2-dc3a-49f1-a7e2-a599c2be36dc"
  }
}
```
Return a condition object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/conditions/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | The ID of the condition to be retrieved.


### List conditions
> Example request:

```shell
curl "https://api.picnichealth.com/v1/conditions" \
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
      "object": "Condition",
      "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
      "encounter": {
        "object": "Examination",
        "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
      },
      "coding": {
        "object": "Code",
        "referenceId": "f60d40f2-dc3a-49f1-a7e2-a599c2be36dc"
      }
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of condition objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/conditions`

### Create a condition
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/conditions" \
  -d encounter='{ "object": "Code", "referenceId:": "72314206-32df-4777-9a26-73b37bae9a5a" }' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Condition",
  "id": "0507420d-fcf8-4ec9-8bf0-c10bf408e6cd",
  "encounter": {
    "object": "Examination",
    "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
  },
  "coding": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/conditions`

Create a new condition object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter when the condition was recorded
coding | [Code](#codes) | The coding of the condition

### Update a condition
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/conditions/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d coding='{ object: "Code", referenceId: "e04d504c-ab2e-4126-9180-b8384c315590" }' \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Condition",
  "id": "0507420d-fcf8-4ec9-8bf0-c10bf408e6cd",
  "encounter": {
    "object": "Examination",
    "referenceId": "72314206-32df-4777-9a26-73b37bae9a5a"
  },
  "coding": {
    "object": "Code",
    "referenceId": "e04d504c-ab2e-4126-9180-b8384c315590"
  }
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/conditions/:id`

Update a condition

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
encounter | [Encounter](#encounters) | The encounter when the condition was recorded
coding | [Code](#codes) | The coding of the condition

### Delete a condition
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/conditions/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "deleted": true
}
```

Permanently delete a condition

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/conditions/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the condition to delete
# Codes
Currently, PicnicHealth uses the following standard code systems for each encounter and encounter items:

* <a target="_blank" href="http://loinc.org/">LOINC</a> for [Observation](#observations) and [LabTestResult](#lab-test-results) objects
* <a target="_blank" href="https://www.nlm.nih.gov/research/umls/rxnorm">RxNorm</a> for [MedicationStatement](#medication-statements) objects
* <a target="_blank" href="http://www.cdc.gov/nchs/icd/icd9cm.htm">ICD9-CM</a> for [Problem](#problems) objects

There are some cases where a codeable encounter or encounter items cannot be associated with any code in the above standard code systems. For those cases, we use a PicnicHealth built-in code system `Buffet` as an extension of the associated code. This `Buffet` code is a temporary code and is replaced by the standard code as an equivalent code is added to the standard code system. This allows any codes to be easily managable and reuseable.
