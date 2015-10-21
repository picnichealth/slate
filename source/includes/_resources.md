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
id | String | The ID of the patient to be retrieved.


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
  "name": "Neutrophils (%)",
  "observation": {
    "object": "Observation",
    "referenceId": "fcc0a4c8-5910-4031-889d-d06623d05030"
  },
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
    "name": "Neutrophils (%)",
    "observation": {
      "object": "Observation",
      "referenceId": "fcc0a4c8-5910-4031-889d-d06623d05030"
    },
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
  -d observation='{ "object": "Observation", "referenceId": "fcc0a4c8-5910-4031-889d-d06623d05030" }
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
  "name": "C-Reactive Protein",
  "observation": {
    "object": "Observation",
    "referenceId": "fcc0a4c8-5910-4031-889d-d06623d05030"
  },
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
name | String | The name of the lab test result
observation | [Observation](#observations) | The observation which the lab test result belongs to
textValue | String | The text value of the lab test result
positiveOrNegativeValue | String | The positive or negative value of the lab test result. The value must be `positve` or `negative`
numberValue | Number | The numeric value of the lab test result
valueRangeType | Number | The range type of the value. The value must be one of the following: <ul><li>`exact`</li><li>`greaterThan`</li><li>`lessThan`</li><li>`greaterThanOrEqualTo`</li><li>`lessThanOrEqualTo`</li><li>`between`</li><li>`text`</li><li>`positiveNegative`</li></ul>
valueRangeLowValue | Number | The lower bound value of the lab test result
valueRangeHighValue | Number | The upper bound value of the lab test result
valueRangeBorderValue | Number | The border value of the lab test result
referenceRangeType | String | The range type of the reference range. The value must be one of the following: <ul><li>`exact`</li><li>`greaterThan`</li><li>`lessThan`</li><li>`greaterThanOrEqualTo`</li><li>`lessThanOrEqualTo`</li><li>`between`</li><li>`text`</li><li>`positiveNegative`</li></ul>
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
  "name": "C-Reactive Protein",
  "observation": {
    "object": "Observation",
    "referenceId": "fcc0a4c8-5910-4031-889d-d06623d05030"
  },
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
name | String | The name of the lab test result
observation | [Observation](#observations) | The observation which the lab test result belongs to
textValue | String | The text value of the lab test result
positiveOrNegativeValue | String | The positive or negative value of the lab test result. The value must be `positve` or `negative`
numberValue | Number | The numeric value of the lab test result
valueRangeType | Number | The range type of the value. The value must be one of the following: <ul><li>`exact`</li><li>`greaterThan`</li><li>`lessThan`</li><li>`greaterThanOrEqualTo`</li><li>`lessThanOrEqualTo`</li><li>`between`</li><li>`text`</li><li>`positiveNegative`</li></ul>
valueRangeLowValue | Number | The lower bound value of the lab test result
valueRangeHighValue | Number | The upper bound value of the lab test result
valueRangeBorderValue | Number | The border value of the lab test result
referenceRangeType | String | The range type of the reference range. The value must be one of the following: <ul><li>`exact`</li><li>`greaterThan`</li><li>`lessThan`</li><li>`greaterThanOrEqualTo`</li><li>`lessThanOrEqualTo`</li><li>`between`</li><li>`text`</li><li>`positiveNegative`</li></ul>
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
This is an object representing an encounter.

> End point

```shell
"https://api.picnichealth.com/v1/encounters"
```

An interaction between a patient and healthcare providers to assess the patient health status is represented by an encounter.

## Encounter Types
An encounter can be one of the following types:

<table>
  <thead>
    <tr>
      <th></th>
      <th>Encounter Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.</td>
      <td>Examination (see <a href="#example-examination">example</a>)</td>
    </tr>
    <tr>
      <td>2.</td>
      <td>Hospitalization (see <a href="#example-hospitalization">example</a>)</td>
    </tr>
    <tr>
      <td>3.</td>
      <td>Procedure (see <a href="#example-procedure">example</a>)</td>
    </tr>
    <tr>
      <td>4.</td>
      <td>PathologyStudy (see <a href="#example-pathology-study">example</a>)</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="2"><em>Each of the above encounters can have <a href="#notes">Notes</a>, <a href="#medication-statements">MedicationStatements</a> and <a href="#conditions">Conditions</a> associated with it as child encounter items.</em></td>
    </tr>
    <tr>
      <td>6.</td>
      <td>ImagingStudy (see <a href="#example-imaging-study">example</a>)</td>
    </tr>
    <tr>
      <td>7.</td>
      <td>LaboratoryTest (see <a href="#example-laboratory-test">example</a>)</td>
    </tr>
    <tr>
      <td>
      </td>
      <td colspan="2"><em>A laborary test is a special encounter reserved for lab test data. An encounter for laboratory tests will only have <a href="#observations">Observations</a> associated with it as child encounter items.</em></td>
    </tr>
  </tbody>
</table>


<br/>

The following entity relationship diagram illustrates the associations between encounter type and encounter items:

<img src="images/picnichealth_entity_relationship.svg"/>

## Get a specific encounter
Return an encounter

#### HTTP Request
`GET https://api.picnichealth.com/v1/encounters/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the encounter to be retrieved.

### Example: Examination
> Example response:

```json
{
  "object": "Encounter",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "type": "Examination",
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
      "object": "Note",
      "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
    }
  ],
  "medicationStatements": [
    {
      "object": "MedicationStatement",
      "referenceId": "82107fa4-10bb-4210-b6d9-ea53bdd46f1d"
    },
    {
      "object": "MedicationStatement",
      "referenceId": "912f716a-1a0b-4b08-a397-db70ca6e503d"
    }
  ],
  "conditions": [
    {
      "object": "Condition",
      "referenceId": "32f61b2a-b0e2-4b3b-ae93-73797dd1dc62"
    }
  ]
}
```

Attributes | Description
---------- | -----------
id | The ID of the encounter
type | The type of the encounter
date | The date of the encounter
patient | The patient
doctorList | The list of doctors involved in the encounter
location | The location of the encounter
notes | The list of notes recorded at the encounter
medicationStatements | The list of medication statements recorded at the encounter
conditions | The list of conditions recorded at the encounter

### Example: Hospitalization
> Example response:

```json
{
  "object": "Encounter",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "type": "Hospitalization",
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
  ],
  "medicationStatements": null,
  "conditions": null
}
```

Attributes | Description
---------- | -----------
id | The ID of the encounter
type | The type of the encounter
date | The date of the encounter
patient | The patient
doctorList | The list of doctors involved in the encounter
location | The location of the encounter
notes | The list of notes recorded at the encounter
medicationStatements | The list of medication statements recorded at the encounter
conditions | The list of conditions recorded at the encounter


### Example: Procedure
> Example response:

```json
{
  "object": "Encounter",
  "id": "1b26577b-04ea-4fc8-895a-1f466b707e63",
  "type": "Procedure",
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
      "object": "Note",
      "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
    }
  ],
  "medicationStatements": null,
  "conditions": null
}
```

Attributes | Description
---------- | -----------
id | The ID of the encounter
type | The type of the encounter
date | The date of the encounter
patient | The patient
doctorList | The list of doctors involved in the encounter
location | The location of the encounter
notes | The list of notes recorded at the encounter
medicationStatements | The list of medication statements recorded at the encounter
conditions | The list of conditions recorded at the encounter


### Example: Pathology Study
```json
{
  "object": "Encounter",
  "id": "79689692-b639-4c56-b57e-1528d2550b5e",
  "type": "PathologyStudy",
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
      "object": "Note",
      "referenceId": "df6f12d9-be67-4644-8a73-6ac9843684df"
    }
  ],
  "medicationStatements": null,
  "conditions": null
}
```

Attributes | Description
---------- | -----------
id | The ID of the encounter
type | The type of the encounter
date | The date of the encounter
patient | The patient
doctorList | The list of doctors involved in the encounter.
location | The location of the encounter
notes | The list of notes recorded at the encounter
medicationStatements | The list of medication statements recorded at the encounter
conditions | The list of conditions recorded at the encounter

### Example: Imaging Study
> Example response:

```json
{
  "object": "Encounter",
  "id": "ad37701d-7228-4904-9945-7c537b2c7848",
  "type": "ImagingStudy",
  "date": "2015-10-17",
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

Attributes | Description
---------- | -----------
id | The ID of the encounter
type | The type of the encounter
date | The date of the encounter
patient | The patient
doctorList | The list of doctors involved in the encounter
location | The location of the encounter
dicom | The list of objects with attributes `studyUid` and `viewerUrl` representing a dicom image

### Example: Laboratory Test
> Example response:

```json
{
  "object": "Encounter",
  "type": "LaboratoryTest",
  "id": "a15ad9e5-d96b-4ebf-9781-bccc3707932d",
  "date": "2015-10-17",
  "doctorList": {
    "performer": {
      "object": "MedicalPractitioner",
      "referenceId": "ad5ea88e-a79a-4431-98ae-45b3ef254f8a"
    }
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
  "conclusion": null
}
```

Attributes | Description
---------- | -----------
id | The ID of the encounter
type | The type of the encounter
date | The date of the encounter
patient | The patient
doctorList | The list of doctors involved in the encounter
result | The list of observations recorded in the encounter
conclusion | The summary of the laboratory test

## List encounters
> Example request:

```shell
curl "https://api.picnichealth.com/v1/encounters" \
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
      "object": "Encounter",
      "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
      "type": "Examination",
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
          "object": "Note",
          "referenceId": "8ca8f80d-951a-46af-bc70-8ccd6e0955b0"
        }
      ],
      "medicationStatements": [
        {
          "object": "MedicationStatement",
          "referenceId": "82107fa4-10bb-4210-b6d9-ea53bdd46f1d"
        },
        {
          "object": "MedicationStatement",
          "referenceId": "912f716a-1a0b-4b08-a397-db70ca6e503d"
        }
      ],
      "conditions": [
        {
          "object": "Condition",
          "referenceId": "32f61b2a-b0e2-4b3b-ae93-73797dd1dc62"
        }
      ]
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of encounters

## Create an encounter
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/encounters" \
  -d date="2015-10-17" \
  -d type="Examination" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" } \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Encounter",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "type": "Examination",
  "date": "2015-10-17",
  "patient": {
    "object": "Patient",
    "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d"
  },
  "doctorList": null,
  "location": null,
  "notes": null,
  "medicationStatements": null,
  "conditions": null
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/encounters`

Create a new encounter object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date <sub>required</sub> | String | The date of the encounter
patient <sub>required</sub> | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved in the encounter. Each object has attributes `doctor` and `role`, where `doctor` is a reference object to [MedicalPractitioner](#medical-practitioners) and `role` is a string with possible values <ul><li>`performer`</li><li>`referrer`</li><li>`consultant`</li><li>`requester`</li>
location | [MedicalFacility](#medical-facilities) | The location of the encounter

<br/>

Parameters exclusive to **RadiologyStudy** type

Parameter | Data Type | Description
--------- | --------- | -----------
dicom | Array of objects | The list of objects representing dicom images. Each object has attributes `studyUid` and `viewerUrl`.

<br/>

Parameters exclusive to **LaboratoryTest** type

Parameter | Data Type | Description
--------- | --------- | -----------
conclusion | String | The summary of the encounter of *LaboratoryTest* type

Note: The attributes representing [encounter items](#encounter-items) such as `notes`, `medicationStatements`, `conditions` and `result` are read-only in encounter objects and needs to be referenced from the encounter items to add to the parent encounter.

## Update an encounter
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/encounters/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -d date="2015-10-19" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Encounter",
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "type": "Examination",
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
`POST https://api.picnichealth.com/v1/encounters/:id`

Update an existing encounter object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
date <sub>required</sub> | String | The date of the encounter
patient <sub>required</sub> | [Patient](#patients) | The patient
doctorList | Array of Objects | The list of doctors involved in the encounter. Each object has attributes `doctor` and `role`, where `doctor` is a reference object to [MedicalPractitioner](#medical-practitioners) and `role` is a string with possible values <ul><li>`performer`</li><li>`referrer`</li><li>`consultant`</li><li>`requester`</li>
location | [MedicalFacility](#medical-facilities) | The location of the encounter

<br/>

Parameters exclusive to **RadiologyStudy** type

Parameter | Data Type | Description
--------- | --------- | -----------
dicom | Array of objects | The list of objects representing dicom images. Each object has attributes `studyUid` and `viewerUrl`.

<br/>

Parameters exclusive to **LaboratoryTest** type

Parameter | Data Type | Description
--------- | --------- | -----------
conclusion | String | The summary of the laboratory test

Note: The attributes representing [encounter items](#encounter-items) such as `notes`, `medicationStatements`, `conditions` and `result` are read-only in encounter objects and needs to be referenced from the encounter items to add to the parent encounter.


## Delete an encounter
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/encounters/516fe3e3-386b-4c3a-8744-20f2211254b4" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "516fe3e3-386b-4c3a-8744-20f2211254b4",
  "deleted": true
}
```

Permanently delete an encounter.

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/encounters/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the encounters to delete
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
  "date": "2015-10-16",
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
      "date": "2015-10-16",
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
  -d date="2015-10-17" \
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
  "date": "2015-10-16",
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
date | String | The date of the medication recorded
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
  "date": "2015-10-16",
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
date | String | The date of the medication recorded
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
  "date": "2015-10-17",
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
      "date": "2015-10-17",
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
  -d date="2015-10-17" \
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
  "date": "2015-10-17",
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
date | String | The date of the observation
name | String | The name of the observation. Usually it is the name of the lab test panel.
coding | [Code](#codes) | The code representing the observation
component | Array of [LabTestResult](#lab-test-results) | The component lab test resuts of the observation

### Update an observation
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/observations/d3a0b758-47ca-414b-9f9e-400bb2539b81" \
  -d date="2015-10-19" \
  -d component='[ { object: "LabTestResult", referenceId: "14f360b1-c5ae-40b2-967f-5670315295e0" } ]' \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "Observation",
  "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
  "date": "2015-10-19",
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
date | String | The date of the observation
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
