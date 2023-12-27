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
HTTP/1.1 401 UNAUTHORIZED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 27 Dec 2023 09:55:33 GMT
Content-Type: application/json
Content-Length: 41
Connection: close

{
  "ERROR": "Role admin is required!"
}
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


## References
* [Python-API-Development-Fundamentals: Lesson01](https://github.com/TrainingByPackt/Python-API-Development-Fundamentals/blob/master/Lesson01/Activity02/basic-api/app.py)

* [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)