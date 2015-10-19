# Pagination

```shell
curl GET https://api.picnichealth.com/v1/medical-facilities?limit=10&offset=2 \
  -H "api_key: YOUR_API_KEY"
```

#### URL Parameters

Parameter | Description
--------- | -----------
limit | The limit on the numbers of objects to be responsed. The maximum limit is 200.
offset | The offset for use in pagination.
