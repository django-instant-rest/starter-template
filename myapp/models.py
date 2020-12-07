from django.db import models
from django_instant_rest.models import TimeStampedModel

class Author(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length= 255, unique=True)

class Book(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length= 255, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
