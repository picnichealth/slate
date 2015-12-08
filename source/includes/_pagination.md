# Pagination

```shell
curl "https://api.picnichealth.com/v1/medical-facilities?limit=10&offset=2" \
  -u YOUR_API_KEY:
```

#### URL Parameters

Parameter | Description
--------- | -----------
count | The limit on the numbers of objects to be responsed. The maximum limit is 100. The default is 20.
offset | The offset for use in pagination.
