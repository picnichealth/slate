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
  -u YOUR_API_KEY: \
  -d date="2015-10-17" \
  -d type="Examination" \
  -d patient='{ "object": "Patient", "referenceId": "651ec5f6-b2c9-4c15-8c01-47e0dd942d3d" }
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
  -u YOUR_API_KEY:
  -d date="2015-10-19"
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
  -u YOUR_API_KEY:
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
