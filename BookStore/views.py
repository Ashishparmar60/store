from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializer import BookSerializer, CustomerSerializer
from .models import Book, Customer
from .filters import BooksFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response


class BooksViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Book.objects.select_related('author').prefetch_related('genre').all() # Here we use select_related for OneToOne
    # prefetch_related for ManyToMany relationship after this our quries will be almost 6 under 3.1 ms.
    serializer_class = BookSerializer
    filter_backends = [ DjangoFilterBackend, SearchFilter]
    filterset_class = BooksFilter
    search_fields = ['name']
    
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        else:
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    



