from myapp.models import *
from django_instant_rest import patterns

urlpatterns = [
    patterns.resource('authors', Author),
    patterns.resource('books', Book),
    patterns.resource('users', User),
    patterns.client('users', User),
]