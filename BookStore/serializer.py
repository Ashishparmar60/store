from rest_framework import serializers
from .models import Book, Customer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'author', 'unit_price', 'genre']
    author = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True) 

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'user_id', 'phone', 'birth_day']    

