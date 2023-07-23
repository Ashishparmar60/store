from django.db import models
from django.conf import settings
from django.contrib import admin

class Collection(models.Model):
    genre = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.genre

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    length = models.PositiveIntegerField()
    genre = models.ManyToManyField(Collection)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    phone = models.CharField(max_length=255)
    birth_day = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
        
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Order(models.Model):
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateField()
    payment = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderedBook(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='book')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


    

