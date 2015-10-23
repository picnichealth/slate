# Codes

> End point

```shell
"https://api.picnichealth.com/v1/codes"
```

This is an object representing a code.

## Code Systems
Currently, PicnicHealth uses the following standard code systems for each encounter and encounter items:

* <a target="_blank" href="http://loinc.org/">LOINC</a> for [Observation](#observations) and [LabTestResult](#lab-test-results) objects
* <a target="_blank" href="https://www.nlm.nih.gov/research/umls/rxnorm">RxNorm</a> for [MedicationStatement](#medication-statements) objects
* <a target="_blank" href="http://www.cdc.gov/nchs/icd/icd9cm.htm">ICD9-CM</a> for [Problem](#problems) objects

There are some cases where a codeable encounter or encounter items cannot be associated with any code in the above standard code systems. For those cases, we use a PicnicHealth temporary code system as an extension of the associated code. This temporary code is replaced by the standard code as an equivalent code is added to the standard code system. This allows any codes to be easily managable and reuseable.

## Get a specific code
Return a code

#### HTTP Request
`GET https://api.picnichealth.com/v1/codes/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the code to be retrieved.

### Example Code System: LOINC
> Example response:

```json
{
  "object": "Code",
  "id": "98f391e1-eff0-4f1e-98c5-0ddab280b42a",
  "code": "198-5",
  "codeSystem": "Loinc",
  "display": "C reactive protein"
}
```
Attributes | Description
---------- | -----------
id | The ID of the code
code | The LOINC code
codeSystem | The code system associated with the code
display | The display name of the LOINC code


### Example Code System: RxNorm
> Example response:

```json
{
  "object": "Code",
  "id": "5172cfcf-0ec9-4c43-ba97-5d6a34182d2b",
  "code": "1368960",
  "codeSystem": "RxNorm",
  "display": "DELZICOL (Oral Pill) 400 mg"
}
```
Attributes | Description
---------- | -----------
id | The ID of the code
code | The unique identifier `rx_cui` from RxNorm
codeSystem | The code system associated with the code
display | The display name of the RxNorm code

### Example Code System: ICD9-CM
> Example response:

```json
{
  "object": "Code",
  "id": "4d43dbad-72f9-4ea9-b895-87a92e757fdc",
  "code": "401.9",
  "codeSystem": "ICD9-CM",
  "display": "Unspecified essential hypertension"
}
```
Attributes | Description
---------- | -----------
id | The ID of the code
code | The ICD9-CM code
codeSystem | The code system associated with the code
display | The display name of the ICD9-CM code

### Example Code System: temporary code
> Example response:

```json
{
  "object": "Code",
  "id": "3a1270ff-8144-401d-801f-1d5f2552da95",
  "code": null,
  "codeSystem": null,
  "target": "MedicationStatement",
  "display": "Mulitivitamins"
}
```

Attributes | Description
---------- | -----------
id | The ID of the code
code | The unique code ID from the code system
codeSystem | The code system associated with the code
target | The object name of the [encounter](#encounters) or [encounter items](#encounter-items)
display | The display name of the code
