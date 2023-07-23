from rest_framework import serializers
from .models import Book, Customer, Order, OrderedBook, BookFiles

class BookFileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book_id = self.context['book_id']
        return BookFiles.objects.create(book_id=book_id, **validated_data)
    
    class Meta:
        model = BookFiles
        fields = ['id', 'file']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'unit_price', 'genre', 'files']
    author = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True) 
    files = BookFileSerializer(many=True, read_only=True)

class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'unit_price']

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'user_id', 'phone', 'birth_day']  

class OrderedBookSerializer(serializers.ModelSerializer):
    book = SimpleBookSerializer()
    class Meta:
        model = OrderedBook
        fields = ['book', 'unit_price']
  
class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.CharField()
    book = OrderedBookSerializer(many=True)
    class Meta:
        model = Order
        fields = ['customer', 'payment', 'placed_at', 'book']

