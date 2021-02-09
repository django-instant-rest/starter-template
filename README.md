# System Dependencies

- [Python](https://www.python.org/downloads/) >= 3 
- [pip]() >= 20.1.1
- [pipenv](https://pipenv.pypa.io/en/latest/) >= 2020.6.2

# Getting Started
```sh
# setting up virtual env and installing dependencies
pipenv install

# generating database migrations from django models
pipenv run python manage.py makemigrations

# applying migrations to the database
pipenv run python manage.py migrate

# starting REST API
pipenv run python manage.py runserver
```
# API Endpoints
## Resource Pattern
django-instant-rest uses a function called `patterns.resource` which uses a model to expose CRUD functionality for any model that inherits from `RestResource` class.
```py
# mysite/urls.py
urlpatterns = [
    patterns.resource('books', Book),
]
```
- `GET /books` - gets list of all `Book` objects
  -  Query Parameters: 
      - Pagination:
        - `first` - number of objects per page when paginating forawrd
        - `after` - cursor of first result when paginating forward
        - `last` - number of objects per page when paginating backward
        - `before` - cursor of first result when paginating backward
      - Filtering:
        - By default, django-instant-rest supports all [queryset filters supported by django](https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-specific-objects-with-filters).
  - Request using cURL:
  ```
  curl --location --request GET 'http://localhost:8000/authors?last_name__contains=R' \
  --header 'Content-Type: application/json'
  ```
  - Response body:
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

    
- `POST /books` - creates a new `Book` object
  - Request using cURL:
  ```
    curl --location --request POST 'http://localhost:8000/authors' \
    --header 'Content-Type: application/json' \
    --data-raw '{"first_name": "JK","last_name":"Rowling"}'
  ```
  - Response body:
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


- `PUT /books/:id` - updates an existing `Book` object
- `DELETE /books/:id` - deletes existing `Book` object