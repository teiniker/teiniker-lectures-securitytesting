# Role-Based Authorization

In this example, we can see how simple a RESTful service can be implemented with
**Flask** using Basic Authentication and Role-Based Authorization.

## Setup 
```
$ pip3 install Flask-HTTPAuth
```

We start the web service from the command line:
```
$ python3 article_service.py
```

## Role-Based Authorization

Flask-HTTPAuth includes a simple role-based authentication system that can optionally 
be added to provide an additional layer of granularity in filtering accesses to routes. 

To enable role support, write a function that returns the list of roles for a given user 
and decorate it with the `get_user_roles` decorator.


## Access the REST Service


### Find all Articles

```
$ curl -i -k -u homer:duffbeer https://localhost:8443/articles

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:18:31 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money https://localhost:8443/articles

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 09:56:44 GMT
Content-Type: application/json
Content-Length: 286
Connection: close

{
  "data": [
    {
      "description": "Effective Python",
      "id": 1,
      "price": 2390
    },
    {
      "description": "Effective Python",
      "id": 2,
      "price": 2390
    },
    {
      "description": "Effective Python",
      "id": 3,
      "price": 2390
    }
  ]
}
```


### Find a particular Article
```
$ curl -i -k -u homer:duffbeer https://localhost:8443/articles/1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 09:58:02 GMT
Content-Type: application/json
Content-Length: 68
Connection: close

{
  "description": "Effective Python",
  "id": 1,
  "price": 2390
}
```

```
$ curl -i -k -u burns:money https://localhost:8443/articles/1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:20:04 GMT
Content-Type: application/json
Content-Length: 68
Connection: close

{
  "description": "Effective Python",
  "id": 1,
  "price": 2390
}
```

### Insert an Article
```
$ curl -i -k -u homer:duffbeer -X POST https://localhost:8443/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:22:01 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money -X POST https://localhost:8443/articles -H "Content-Type: application/json" -d '{"id":7, "description":"Learning Python", "price":5448}'

HTTP/1.1 201 CREATED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:22:47 GMT
Content-Type: application/json
Content-Length: 67
Connection: close

{
  "description": "Learning Python",
  "id": 7,
  "price": 5448
}
```


### Update an Article
```
$ curl -i -k -u homer:duffbeer -X PUT https://localhost:8443/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:25:58 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money -X PUT https://localhost:8443/articles/2 -H "Content-Type: application/json" -d '{"description":"Clean Code in Python", "price":3700}'

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:26:45 GMT
Content-Type: application/json
Content-Length: 72
Connection: close

{
  "description": "Clean Code in Python",
  "id": 2,
  "price": 3700
}
```

### Delete an Article

```
$ curl -i -k -u homer:duffbeer -X DELETE https://localhost:8443/articles/1

HTTP/1.1 403 FORBIDDEN
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:27:56 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
WWW-Authenticate: Basic realm="Authentication Required"
Connection: close

Unauthorized Access
```

```
$ curl -i -k -u burns:money -X DELETE https://localhost:8443/articles/1

HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 10:28:44 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```

## References
* [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)

*Egon Teiniker, 2020-2023, GPL v3.0*