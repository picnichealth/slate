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

<!--- begin private -->
### List medical practitioners
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medical-practitioners" \
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
    },
    {
      "...": "..."
    }
  ]
}
```

Return a list of medical practitioner objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/medical-practitioners`

### Create a medical practitioner
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medical-practitioners" \
  -d name="Gillian Hanson" \
  -d address='{ "line1": "2519 Mission St", "city": "San Francisco", "state": "California", "postalCode": "94103" }'" \
  -d speciality="General Surgeon" \
  -d email="gillian@picnichealth.com" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "MedicalPractitioner",
  "id": "68e0c31f-481d-4b56-98e5-e9b88fc8f601",
  "name": "Gillian Hanson",
  "address": {
      "line1": "2519 Mission St",
      "line2": null,
      "city": "San Francisco",
      "state": "California",
      "postalCode": "94103"
  },
  "specialty": "General Surgeon",
  "email": "gillian@picnichealth.com"
}
```


#### HTTP Request
`POST https://api.picnichealth.com/v1/medical-practitioners`

Create a new medical practitioner object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
name | String | The name of the medical practitioner
address | String | The address of the medical practitioner
speciality | String | The specialty of the medical practitioner
email | String | The email address of the medical practitioner

### Update medical practitioner
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medical-practitioners/3ed5b72f-6214-4839-9107-7d2b3b6d2a9d" \
  -d name="Gillian Hanson" \
  -d speciality="General Surgeon" \
  -d email="gillian@picnichealth.com" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "MedicalPractitioner",
  "id": "68e0c31f-481d-4b56-98e5-e9b88fc8f601",
  "name": "Gillian Hanson",
  "address": {
    "line1": "2519 Mission St",
    "line2": null,
    "city": "San Francisco",
    "state": "California",
    "postalCode": "94103"
  },
  "specialty": "General Surgeon",
  "email": "gillian@picnichealth.com"
}
```


#### HTTP Request
`POST https://api.picnichealth.com/v1/medical-practitioners/:id`

Update a medical practitioner

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
name | String | The name of the medical practitioner
address | Object | The address of the medical practitioner
speciality | String | The specialty of the medical practitioner
email | String | The email address of the medical practitioner

### Delete medical practitioner
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/medical-practitioners/68e0c31f-481d-4b56-98e5-e9b88fc8f601" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "68e0c31f-481d-4b56-98e5-e9b88fc8f601",
  "deleted": true
}
```

Permanently delete a medical practitioner

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/medical-practitioners/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the medical practitioner to delete
<!--- end private -->
