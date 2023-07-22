from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.db.models.aggregates import Count
from .models import Book, Collection, Author, Customer, Order, OrderedBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price', 'get_genre', 'author', 'description']
    list_editable = ['unit_price']
    list_filter = ['author', 'genre']
    list_select_related = ['author']
    search_fields = ['name']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('genre')
    # I add this get less querise because Book is main page in our Project 
    
    def get_genre(self, objects):
        return ',\n'.join([i.genre for i in objects.genre.all()])
    # list comprehension method for all genre is in that book's object. Also for fun i add upper..

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'books_count']

    def books_count(self, author):
        url = (
            reverse('admin:BookStore_book_changelist')
            + '?'
            + urlencode({
                'author__id__exact' : str(author.id)
            })
        )
        return format_html('<a href="{}">{} Books</a>', url, author.books_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            books_count = Count('book')
        )
    
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['genre', 'Books_count']

    @admin.display(ordering='Books_count') # We add this decorater for sorthing the Books Count list.
    def Books_count(self, collection):
        url = (
            reverse('admin:BookStore_book_changelist')
            + '?'
            + urlencode({
                'genre__id__exact' : str(collection.id) # 'genre__id__exact' is new table in our database cuz ManyToMany relationship. 
            })
        )
        return format_html('<a href="{}">{} Books</a>', url, collection.Books_count)

    # Here We Overide the base queryset..
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            Books_count = Count('book')
        )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'birth_day']
    ordering = ['user__first_name', 'user__last_name']
    
class OrderBookInline(admin.TabularInline):
    autocomplete_fields = ['book']
    model = OrderedBook

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment', 'customer']    
    inlines = [OrderBookInline]
