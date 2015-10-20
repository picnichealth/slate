# Patients
This is an object representing a patient.

### Get a specific patient
> Example request:

```shell
curl "https://api.picnichealth.com/v1/patients/388d2e58-b3fd-45a2-84b2-c95108a54b7e" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Patient",
  "email": "KathyBTorres@teleworm.us",
  "fullName": "Kathy Torres",
  "activatedAt": "2014-10-13T03:09:46.555Z",
  "birthMonth": 0,
  "birthDayOfMonth": 16,
  "birthYear": 1964,
  "address1": "1572 Grove Street",
  "address2": null,
  "city": "Selden",
  "state": "New York",
  "postalCode": "11784",
  "country": "United States",
  "primaryPhone": "6317369763",
  "gender": "female",
  "ssLastFourDigits": 1234
}
```
Return a patient object.

#### HTTP Request
`GET https://api.picnichealth.com/v1/patients/:id`

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
id | The ID of the patient to be retrieved.


### List patients
> Example request:

```shell
curl "https://api.picnichealth.com/v1/patients" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
[
  {
    "object": "Patient",
    "email": "KathyBTorres@teleworm.us",
    "fullName": "Kathy Torres",
    "activatedAt": "2014-10-13T03:09:46.555Z",
    "birthMonth": 0,
    "birthDayOfMonth": 16,
    "birthYear": 1964,
    "address1": "1572 Grove Street",
    "address2": null,
    "city": "Selden",
    "state": "New York",
    "postalCode": "11784",
    "country": "United States",
    "primaryPhone": "6317369763",
    "gender": "female",
    "ssLastFourDigits": 1234
  },
  {
    "...": "..."
  }
]
```

Return a list of patient objects

#### HTTP Request
`GET https://api.picnichealth.com/v1/patients`

### Create a patient
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/patients" \
  -d fullName="Dennis Thome" \
  -d email="DennisAThome@dayrep.com" \
  -d activatedAt="2015-10-17T07:09:46.555Z" \
  -d birthMonth=4 \
  -d birthDayOfMonth=5 \
  -d birthYear=1967 \
  -d address1="2537 Diane Street" \
  -d city="Thousand Oaks" \
  -d state="California" \
  -d postalCode="91362" \
  -d country="United States" \
  -d primaryPhone="8053819600" \
  -d gender="male" \
  -d ssLastFourDigits="2345" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Patient",
  "id": "30febccb-00d0-41eb-ad15-9041a734cafa",
  "fullName": "Dennis Thome",
  "email": "DennisAThome@dayrep.com",
  "activatedAt": "2015-10-17T07:09:46.555Z",
  "birthMonth": 4,
  "birthDayOfMonth": 5,
  "birthYear": 1967,
  "address1": "2537 Diane Street",
  "address2": null,
  "city": "Thousand Oaks",
  "state": "California",
  "postalCode": "91362",
  "country": "United States",
  "primaryPhone": "8053819600",
  "gender": "male",
  "ssLastFourDigits": "2345"
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
birthMonth | Integer | The birth month of the patient. Note: The month starts from 0. (January is 0, February is 1, and so on.)
birthDayOfMonth | Integer | The birth day of the patient
birthYear | Integer | The birth year of the patient
address1 | String | The address line 1
address2 | String | The address line 2
city | String | The city of the patient address
state | String | The state of the patient address
postalCode | String | The postal code of the patient address
country | String | The country of the patient address
primaryPhone | String | The primary phone number
gender | String | The gender of the patient
ssLastFourDigits | String | The last four digits of the patient social security number


### Update patient
> Example request:

```shell
curl -X POST "https://api.picnichealth.com/v1/patients/30febccb-00d0-41eb-ad15-9041a734cafa" \
  -d fullName="Dennis Thome" \
  -d email="DennisAThome@dayrep.com" \
  -d activatedAt="2015-10-17T07:09:46.555Z" \
  -d birthMonth=4 \
  -d birthDayOfMonth=5 \
  -d birthYear=1967 \
  -d address1="2537 Diane Street" \
  -d city="Thousand Oaks" \
  -d state="California" \
  -d postalCode="91362" \
  -d country="United States" \
  -d primaryPhone="8053819600" \
  -d gender="male" \
  -d ssLastFourDigits="2345" \
  -H "Authorization: YOUR_API_KEY"
```

> Example response:

```json
{
  "object": "Patient",
  "id": "30febccb-00d0-41eb-ad15-9041a734cafa",
  "fullName": "Dennis Thome",
  "email": "DennisAThome@dayrep.com",
  "activatedAt": "2015-10-17T07:09:46.555Z",
  "birthMonth": 4,
  "birthDayOfMonth": 5,
  "birthYear": 1967,
  "address1": "2537 Diane Street",
  "address2": null,
  "city": "Thousand Oaks",
  "state": "California",
  "postalCode": "91362",
  "country": "United States",
  "primaryPhone": "8053819600",
  "gender": "male",
  "ssLastFourDigits": "2345"
  }
```


#### HTTP Request
`POST https://api.picnichealth.com/v1/paitents/:id`

Update a patient

#### URL Parameters
Parameter | Data Type | Description
--------- | --------- | -----------
email | String | The email address of the patient
fullName | String | The full name of the patient
activatedAt | String | The date and time of the patient account activation
birthMonth | Integer | The birth month of the patient. Note: The month starts from 0. (January is 0, February is 1, and so on.)
birthDayOfMonth | Integer | The birth day of the patient
birthYear | Integer | The birth year of the patient
address1 | String | The address line 1
address2 | String | The address line 2
city | String | The city of the patient address
state | String | The state of the patient address
postalCode | String | The postal code of the patient address
country | String | The country of the patient address
primaryPhone | String | The primary phone number
gender | String | The gender of the patient
ssLastFourDigits | String | The last four digits of the patient social security number

### Delete patient
> Example request:

```shell
curl -X DELETE "https://api.picnichealth.com/v1/patients/30febccb-00d0-41eb-ad15-9041a734cafa" \
  -H "Authorization: YOUR_API_KEY
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
