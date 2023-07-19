from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http.request import HttpRequest
from .models import Book, Collection, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price', 'get_genre', 'author', 'description']
    list_editable = ['unit_price']

    def get_genre(self, objects):
        return '\n'.join([i.genre for i in objects.genre.all()]).upper()
     # list comprehension method for all genre is in that book's object. Also for fun i add upper..

                                                                          
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'books_count']

    def books_count(self, author):
        return author.books_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            books_count = Count('book')
        )
    
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['genre']

    

