# System Dependencies

- [python](https://www.python.org/downloads/) >= 3 
- [pip]() >= 20.1.1
- [pipenv](https://pipenv.pypa.io/en/latest/) >= 2020.6.2

# Getting Started
```sh
# clone this repository into a local directory
git clone https://github.com/django-instant-rest/starter-template.git rest_api

# navigate into the newly cloned project
cd rest_api

# setting up virtual env and installing dependencies
pipenv install

# generating database migrations from django models
pipenv run python manage.py makemigrations

# applying migrations to the database
pipenv run python manage.py migrate

# replacing the secret key in django settings
pipenv run python scripts/replace_secret_key.py

# starting REST API
pipenv run python manage.py runserver
```
# API Endpoints
## Resource Pattern
django-instant-rest uses a function called `patterns.resource()` which uses a model to expose CRUD functionality for any model that inherits from `RestResource` class.
```py
# mysite/urls.py
urlpatterns = [
    patterns.resource('authors', Author),
]
```
### `POST /authors` - creates a new `Author` object
Example request using cURL:
```
  curl --location --request POST 'http://localhost:8000/authors' \
  --header 'Content-Type: application/json' \
  --data-raw '{"first_name": "JK","last_name":"Rowling"}'
```
Example response body:
```JSON
{
  "data": {
    "id": 1,
    "created_at": "2021-02-09T20:26:57.928000+00:00",
    "updated_at": "2021-02-09T20:26:57.928000+00:00",
    "first_name": "JK",
    "last_name": "Rowling"
  }
}
```
---
### `GET /authors` - gets list of all `Author` objects
Query Parameters: 
- Pagination:
  - `first` - number of objects per page when paginating forawrd
  - `after` - cursor of first result when paginating forward
  - `last` - number of objects per page when paginating backward
  - `before` - cursor of first result when paginating backward
- Filtering:
  - By default, django-instant-rest supports all [queryset filters supported by django](https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-specific-objects-with-filters).

Example request using cURL:
  ```
  curl --location --request GET 'http://localhost:8000/authors?last_name__contains=R' \
  --header 'Content-Type: application/json'
  ```
Example response body:
  ```JSON
  {
    "first_cursor": "MXwyMDIxLTAyLTA5IDIwOjI2OjU3LjkyODAwMCswMDowMA==",
    "last_cursor": "MXwyMDIxLTAyLTA5IDIwOjI2OjU3LjkyODAwMCswMDowMA==",
    "has_next_page": false,
    "data": [
      {
        "id": 1,
        "created_at": "2021-02-09T20:26:57.928000+00:00",
        "updated_at": "2021-02-09T20:26:57.928000+00:00",
        "first_name": "JK",
        "last_name": "Rowling"
      }
    ]
  }
  ```
---
### `GET /authors/:id` - retrieve an existing `Author` object
Example request using cURL:
  ```
  curl --location --request GET 'http://localhost:8000/authors/1' \
  --header 'Content-Type: application/json' \
  ```
Example response body:
```JSON
{
  "data": {
    "id": 1,
    "created_at": "2021-02-09T20:26:57.928000+00:00",
    "updated_at": "2021-02-09T20:53:19.012390+00:00",
    "first_name": "JK",
    "last_name": "Rowling"
  }
}
```
---
### `PUT /authors/:id` - updates an existing `Author` object
Example request using cURL:
  ```
  curl --location --request PUT 'http://localhost:8000/authors/1' \
  --header 'Content-Type: application/json' \
  --data-raw '{"first_name":"Joanne Kathleen"}'
  ```
Example response body:
```JSON
{
  "data": {
    "id": 1,
    "created_at": "2021-02-09T20:26:57.928000+00:00",
    "updated_at": "2021-02-09T20:53:19.012390+00:00",
    "first_name": "Joanne Kathleen",
    "last_name": "Rowling"
  }
}
```
---
### `DELETE /authors/:id` - deletes existing `Author` object
Example request using cURL:
```
curl --location --request DELETE 'http://localhost:8000/authors/1'
```
Example response body:
```JSON
{
  "data": {
    "id": null,
    "created_at": "2021-02-09T20:26:57.928000+00:00",
    "updated_at": "2021-02-09T20:53:19.012390+00:00",
    "first_name": "Joanne Kathleen",
    "last_name": "Rowling"
  }
}
```

## Client Pattern
django-instant-rest uses a function called `patterns.client()` which receives a post request whose body is a JSON object with the parameters username and password. If they are valid pair, the database will respond with a [JSON Web Token](https://jwt.io/) used for authentication.

url pattern:
```py
urlpatterns = [
  patterns.client('users', User),
]
```

### `POST /users/authenticate` - Exchange username + password for a [JWT](https://jwt.io/)

Example request using cURL:
```
# mysite/urls.py
curl --location --request POST 
'http://localhost:8000/users/authenticate' 
--header 'Content-Type: application/json' 
--data-raw '{"username" : "dragondude", "password" : "I have a dragon"}
```
Example response body:
```JSON
{
    "data": {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjEtMDItMTFUMTg6MDk6MTkuNTU1MDUzKzAwOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMDItMTFUMTg6MDk6MTkuNTU1MDUzKzAwOjAwIiwidXNlcm5hbWUiOiJUYWRDb3VwZXJAZ21haWwuY29tIiwiZW1haWwiOiIifQ.VnzlwphZ0Cu9QY9CNclkY-qb9HY63HiqbNi2bltyDpM"
    }
}
```