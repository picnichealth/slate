## Medication Statements
This is an object representing a medication statement.

### Get a specific medication
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medication-statements/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "MedicationStatement",
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "patient": {
    "object": "Patient",
    "referenceId": "c519a0a5-98a4-4cbe-81a7-4d41e9002d49"
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
Return a medical practitioner object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/medication-statements/:id`

#### URL Parameters
Parameter | Description
--------- | -----------
id | The ID of the medication to be retrieved.


### List medications
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medication-statements" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "MedicationStatement",
    "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
    "patient": {
      "object": "Patient",
      "referenceId": "c519a0a5-98a4-4cbe-81a7-4d41e9002d49"
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
```

Return a list of medical practitioner objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/medication-statements`

### Create an medication
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medication-statements" \
  -d patient='{ "object": "Patient", "referenceId": "c519a0a5-98a4-4cbe-81a7-4d41e9002d49" }' \
  -d status="active" \
  -d effectiveDate="2015-10-17" \
  -d medicationCoding='{ "object": "Code", "referenceId:": "eb8992d8-3117-47b3-a660-b9156b2b35bc" }' \
  -d instruction="18 units every morning, 12 units every evening" \
  -H "Authorization: YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> Example response:

```json
{
  "object": "MedicationStatement",
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "patient": {
    "object": "Patient",
    "referenceId": "c519a0a5-98a4-4cbe-81a7-4d41e9002d49"
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
Parameter | DataType | Description
--------- | -------- | -----------
patient | Patient | The patient with whom the medication is associated
status | String | The status of the medication
effectiveDate | String | The date of the medication recorded
medicationCoding | Code | The coding of the medcation
instruction | String | The instruction for the medication
note | String | The note for the medication statement

### Update an medication
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medication-statements/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -d id="50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  -d note="Take 2 cap by mouth 2 times a day before meals"
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "MedicationStatement",
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "patient": {
    "object": "Patient",
    "referenceId": "c519a0a5-98a4-4cbe-81a7-4d41e9002d49"
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

Update a medical practitioner

#### URL Parameters
Parameter | DataType | Description
--------- | -------- | -----------
patient | Patient | The patient with whom the medication is associated
status | String | The status of the medication
effectiveDate | String | The date of the medication recorded
medicationCoding | Code | The coding of the medcation
instruction | String | The instruction for the medication
note | String | The note for the medication statement

### Delete a medication statement
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/medication-statements/50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "50f372c6-1aeb-4b21-9fbe-b2d0d1a8968e",
  "deleted": true
}
```

Permanently delete a medical practitioner

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/medication-statements/:id`

#### URL Parameters
Parameter | DataType | Description
--------- | -------- | -----------
id | String | The ID of the medication statements
