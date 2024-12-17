# Object-Level Authorization

Object-level authorization refers to a security mechanism where **access control 
is applied at the level of individual objects** of resources. This means that the 
system checks whether a user has permission to perform a specific action (like read, 
update, delete) on a particular object (like a database record, file, or data entry).

One way to implement object-level authorization is to use Universally Unique 
Identifiers (UUID). 
When using UUIDs for identifiers we cannot infer from one ID to another ID.

In Python we can use the method `uuid.uuid4()` from the module `uuid`  which is part 
of the Python Standard Library.
The UUID generated by `uuid4()` is based on random numbers and is considered 
cryptographically secure.

To convert a UUID into a string representation, we can use `str(uuid.uuid4())`.


## Setup 

We start the web service from the command line:
```
$ python3 article_service.py
```


## Access REST Service via cURL

Note that the used UUIDs in the following examples are randomly generated and
will differ from the ones shown here.

### Find all Articles
```
$ curl -i http://localhost:8080/articles

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 20 Dec 2023 17:22:51 GMT
Content-Type: application/json
Content-Length: 145
Connection: close

{
  "data": [
    {
      "description": "Effective Python",
      "id": "e020c5fe-aad0-448b-a291-ddbedd2ad384",
      "price": 2390
    }
  ]
}
```


### Find a particular Article
```
$ curl -i http://localhost:8080/articles/e020c5fe-aad0-448b-a291-ddbedd2ad384

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 20 Dec 2023 17:22:58 GMT
Content-Type: application/json
Content-Length: 105
Connection: close

{
  "description": "Effective Python",
  "id": "e020c5fe-aad0-448b-a291-ddbedd2ad384",
  "price": 2390
}
```

### Insert an Article
```
$ curl -i -X POST http://localhost:8080/articles -H "Content-Type: application/json" -d '{"description":"Learning Python", "price":5448}'

HTTP/1.1 201 CREATED
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 20 Dec 2023 17:24:49 GMT
Content-Type: application/json
Content-Length: 104
Connection: close

{
  "description": "Learning Python",
  "id": "cc1fcf7f-93f0-4f2e-b49b-e2d5277275e7",
  "price": 5448
}
```

Insert some more articles:
```
$ curl -i -X POST http://localhost:8080/articles -H "Content-Type: application/json" -d '{"description":"Python Crash Course", "price":3731}'
```
```
$ curl -i -X POST http://localhost:8080/articles -H "Content-Type: application/json" -d '{"description":"Automate the Boring Stuff with Python", "price":3032}'
```


### Update an Article
```
$ curl -i -X PUT http://localhost:8080/articles/e020c5fe-aad0-448b-a291-ddbedd2ad384 -H "Content-Type: application/json" -d '{"description":"Effective Python", "price":1199}'

HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 20 Dec 2023 17:30:55 GMT
Content-Type: application/json
Content-Length: 105
Connection: close

{
  "description": "Effective Python",
  "id": "e020c5fe-aad0-448b-a291-ddbedd2ad384",
  "price": 1199
}
```

### Delete an Article

```
$ curl -i -X DELETE http://localhost:8080/articles/e020c5fe-aad0-448b-a291-ddbedd2ad384

HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.3.7 Python/3.11.2
Date: Wed, 20 Dec 2023 17:32:24 GMT
Content-Type: text/html; charset=utf-8
Connection: close
```
