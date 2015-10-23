# Lab Test Results
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
