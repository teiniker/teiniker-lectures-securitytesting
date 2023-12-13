# Service-Level Authorization

## Setup 

We can start the service as a separate process:
```
$ mvn spring-boot:run
```

## Access the REST Service

We can access the public `infos` resource **without authentication**.
```
$ curl -i -k https://localhost:8443/infos

HTTP/1.1 200 
Content-Type: text/plain;charset=UTF-8
Content-Length: 36
Date: Sat, 16 Oct 2021 08:21:56 GMT

Public API Information (Version 1.0)
```

If we try the same with the `articles` resource, we get an **401 Unauthorized** error.
```
$ curl -i -k https://localhost:8443/articles
```

Thus, **only an authenticated user** in the role `USER` has access to the `articles` resource.
```
$ curl -i -k -u homer:homer https://localhost:8443/articles

HTTP/1.1 200 
Content-Type: application/json
Date: Sat, 16 Oct 2021 08:26:54 GMT

[{"id":1,"description":"Design Patterns","price":4295},{"id":2,"description":"Effective Java","price":3336}]
```


## References

[YouTube: Secure REST Controllers](https://youtu.be/OYr9HUPmhSw)

*Egon Teiniker, 2020 - 2023, GPL v3.0*