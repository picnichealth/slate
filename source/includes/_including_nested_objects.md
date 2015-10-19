# Including Nested Objects

By default, the nested objects returned from the API are referenced in the following form:

`{ "object": "OBJECT_MODEL_NAME", "referenceId": "OBJECT_ID" }`

These nested objects can be included in the API response by using the url query parameter 'include'. You can include multiple nested objects at once by joining the object's property separated by commas. Also deeper nested objects can be included by joining the child and decendent's properties separated by comma.

> For example, to include performer and result in a diagnostic report

```
curl "https://api.picnichealth.com/v1/diagnostic-reports/a15ad9e5-d96b-4ebf-9781-bccc3707932d?include=performer,result.components" \
  -H "Authorization: YOUR_API_KEY"
```
