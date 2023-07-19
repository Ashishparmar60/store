from django.urls import path
from .views import sayhello

urlpatterns = [
    path('', sayhello)
]