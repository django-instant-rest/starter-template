
from django.db import models
from django_instant_rest.models import RestResource, RestClient
from mysite import settings


class Author(RestResource):
    '''All models that inherit from `RestResource` will have a `created_at`
    and `updated_at` field by default.'''

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length= 255, unique=True)


class Book(RestResource):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length= 255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class User(RestResource, RestClient):
    '''All models that inherit from `RestClient` will have a `username`
    and `password` field by default.'''

    email = models.CharField(max_length=255)

    class Hashing:
        '''Providing a secret value for encoding and decoding passwords.
        This should never be hard-coded when running in production.'''
        secret_key = settings.SECRET_KEY

    class Serializer:
        '''Listing fields that should be hidden from API consumers'''
        hidden_fields = ['password']
