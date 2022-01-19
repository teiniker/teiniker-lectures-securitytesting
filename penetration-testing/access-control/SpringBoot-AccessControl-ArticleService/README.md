# Example: SpringBoot REST Service (Authentication & Authorization)

## Start the Application

To run the application, change into the application's directory and type:
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

## Service Configuration

In this application, the following **users and roles**  has been configured:
```
username: homer
password: homer
role: USER

username: marge
password: marge
role: USER
```

**Authorization** is configured based on **URL patterns**:
```
/infos         can be used by all clients
/articles/**   can only be accessed by users in the role USER
```

Also, **transport layer security (TLS)** is configured and uses a **self-signed certificate**.
```
* Connected to localhost (::1) port 8443 (#0)
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* Server certificate:
*  subject: C=org; O=lab; CN=se
*  start date: Oct  9 07:33:58 2021 GMT
*  expire date: Jan  7 07:33:58 2022 GMT
*  issuer: C=org; O=lab; CN=se
*  SSL certificate verify result: self signed certificate (18), continuing anyway.
```

## References

[YouTube: Secure REST Controllers](https://youtu.be/OYr9HUPmhSw)

*Egon Teiniker, 2020 - 2022, GPL v3.0*