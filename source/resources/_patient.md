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
<!--- begin private -->
  "activatedAt": "2014-10-13T03:09:46.555Z",
  "ssnLastFourDigits": 1234,
<!--- end private -->
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
<!--- begin private -->
      "activatedAt": "2014-10-13T03:09:46.555Z",
      "ssnLastFourDigits": 1234,
<!--- end private -->
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

<!--- begin private -->
### Create a patient
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/patients" \
  -d fullName="Dennis Thome" \
  -d email="DennisAThome@dayrep.com" \
  -d activatedAt="2015-10-17T07:09:46.555Z" \
  -d birthDate="1967-05-05" \
  -d address='{ "line1": "2537 Diane Street", "city": "Thousand Oaks", "state": "California", "postalCode": "91362" }' \
  -d gender="male" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Patient",
  "id": "30febccb-00d0-41eb-ad15-9041a734cafa",
  "fullName": "Dennis Thome",
  "email": "DennisAThome@dayrep.com",
  "activatedAt": "2015-10-17T07:09:46.555Z",
  "birthDate": "1967-05-05"
  "address": {
    "line1": "2537 Diane Street",
    "line2": null,
    "city": "Thousand Oaks",
    "state": "California",
    "postalCode": "91362"
  },
  "gender": "male"
}
```

#### HTTP Request
`POST https://api.picnichealth.com/v1/patients`

Create a new patient object.

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
email | String | The email address of the patient
fullName | String | The full name of the patient
activatedAt | String | The date and time of the patient account activation
birthDate | String | The birth date of the patient. It must be formatted as "YYYY-MM-DD".
address | Object | The address of the patient
gender | String | The gender of the patient


### Update patient
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/patients/30febccb-00d0-41eb-ad15-9041a734cafa" \
  -d fullName="Dennis Thome" \
  -d email="DennisAThome2@dayrep.com" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "object": "Patient",
  "id": "30febccb-00d0-41eb-ad15-9041a734cafa",
  "fullName": "Dennis Thome",
  "email": "DennisAThome2@dayrep.com",
  "birthDate": "1967-05-05"
  "activatedAt": "2015-10-17T07:09:46.555Z",
  "address": {
    "line1": "2537 Diane Street",
    "line2": null,
    "city": "Thousand Oaks",
    "state": "California",
    "postalCode": "91362"
  },
  "gender": "male"
}
```


#### HTTP Request
`POST https://api.picnichealth.com/v1/patients/:id`

Update a patient

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
email | String | The email address of the patient
fullName | String | The full name of the patient
activatedAt | String | The date and time of the patient account activation
birthDate | String | The birth date of the patient. It must be formatted as "YYYY-MM-DD"
address | Object | The address of the patient
gender | String | The gender of the patient

### Delete patient
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/patients/30febccb-00d0-41eb-ad15-9041a734cafa" \
  -u YOUR_API_KEY:
```

> Example response:

```json
{
  "id": "30febccb-00d0-41eb-ad15-9041a734cafa",
  "deleted": true
}
```

Permanently delete a patient

#### HTTP Request
`DELETE https//api.picnichealth.com/v1/patients/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | String | The ID of the patient to delete
<!--- end private -->
