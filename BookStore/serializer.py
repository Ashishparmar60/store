from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'unit_price', 'genre']
    author = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True) 
    
