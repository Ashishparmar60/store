from django_filters.rest_framework import FilterSet
from .models import Book
from django_filters import filters

class BooksFilter(FilterSet):
    genre = filters.ChoiceField() # We add ChoiceField() here because we have many choice in genre.(ManyToMany fields)
    class Meta:
        model = Book
        fields = {
            'author_id':['exact'],
            'genre':['exact']
        }