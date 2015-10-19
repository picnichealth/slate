# Errors

The PicnicHealth API uses the following error codes:


Error Code | Meaning
---------- | -------
400 | Bad Request -- Probably one or more url parameter is missing or invalid.
401 | Unauthorized -- Your API key is wrong.
403 | Forbidden -- You do not have permission to access this
404 | Not Found -- The specified item doesn't exist
406 | Not Acceptable -- You requested a format that isn't json
500 | Internal Server Error -- Oh no! We had a problem with our server. Try again later.
503 | Service Unavailable -- We're temporarially offline for maintanance. Please try again later.
