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
