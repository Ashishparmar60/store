from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializer import BookSerializer
from .models import Book
from .filters import BooksFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author').prefetch_related('genre').all() # Here we use select_related for OneToOne
    # prefetch_related for ManyToMany relationship after this our quries will be almost 6 under 3.1 ms.
    serializer_class = BookSerializer
    filter_backends = [ DjangoFilterBackend, SearchFilter]
    filterset_class = BooksFilter
    search_fields = ['name']









