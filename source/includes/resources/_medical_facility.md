# Medical Facilities
This is an object representing a medical facility

### Get a specific medical facility
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medical-facilities/2b442547-d98d-4788-9bc0-46a5229dd2b5" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "MedicalFacility",
  "id": "2b442547-d98d-4788-9bc0-46a5229dd2b5",
  "name": "Stanford Health Care",
  "address": "430 Broadway St, Redwood City, CA 94063",
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


### List medical facilities
> Example request:

```shell
curl "https://api.picnichealth.com/v1/medical-facilities" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "MedicalFacility",
    "id": "2b442547-d98d-4788-9bc0-46a5229dd2b5",
    "name": "Stanford Health Care",
    "address": "430 Broadway St, Redwood City, CA 94063",
    "phone": "6507235721",
    "fax": "6507259821"
  },
  {
    "...": "..."
  }
]
```

Return a list of medical facility objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/medical-facilities`

### Create a medical facility
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medical-facilities" \
  -d name="Picnic Hospital" \
  -d address="2519 Mission St, San Francisco, CA 94103" \
  -d phone="4158010572" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "MedicalFacility",
  "id": "3ed5b72f-6214-4839-9107-7d2b3b6d2a9d",
  "name": "Picnic Hospital",
  "address": "2519 Mission St, San Francisco, CA 94103",
  "phone": "4158010572",
  "fax": null
}
```


#### HTTP Request
`POST https://api.picnichealth.com/v1/medical-facilities`

Create a new medical facility object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
name | String | The name of the medical facility
address | String | The address of the medical facility
phone | String | The phone number of the medical facility
fax | String | The fax number of the medical facility

### Update medical facility
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/medical-facilities/3ed5b72f-6214-4839-9107-7d2b3b6d2a9d" \
  -d name="Picnic Hospital" \
  -d address="2519 Mission St, San Francisco, CA 94103" \
  -d phone="4158010572" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "MedicalFacility",
  "id": "3ed5b72f-6214-4839-9107-7d2b3b6d2a9d",
  "name": "Picnic Hospital",
  "address": "2519 Mission St, San Francisco, CA 94103",
  "phone": "4158010572",
  "fax": null
}
```


#### HTTP Request
`POST https://api.picnichealth.com/v1/medical-facilities/:id`

Update a medical facility

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the medical facility
name | String | The name of the medical facility
address | String | The address of the medical facility
phone | String | The phone number of the medical facility
fax | String | The fax number of the medical facility

### Delete medical facility
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/medical-facilities/3ed5b72f-6214-4839-9107-7d2b3b6d2a9d" \
  -H "Authorization: YOUR_API_KEY
```

> Example response:

```json
{
  "id": "3ed5b72f-6214-4839-9107-7d2b3b6d2a9d",
  "deleted": true
}
```

Permanently delete a medical facility

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/medical-facilities/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the medical facility to delete
