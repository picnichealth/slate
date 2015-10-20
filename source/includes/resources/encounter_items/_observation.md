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
[
  {
    "object": "Observation",
    "id": "d3a0b758-47ca-414b-9f9e-400bb2539b81",
    "effectiveDate": "2015-10-17",
    "name": "BASIC METABOLIC PANEL",
    "coding": {
      "object": "Code",
      "referenceId": "288EBF7A-9F6F-4E14-8AAD-7E1490C5FA80"
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
