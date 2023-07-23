from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializer import BookSerializer, CustomerSerializer, OrderSerializer, BookFileSerializer
from .models import Book, Customer, Order, BookFiles
from .filters import BooksFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author').prefetch_related('genre', 'files').all() # Here we use select_related for OneToOne
    # prefetch_related for ManyToMany relationship after this our quries will be almost 6 under 3.1 ms.
    serializer_class = BookSerializer
    filter_backends = [ DjangoFilterBackend, SearchFilter]
    filterset_class = BooksFilter
    search_fields = ['name']
    permission_classes = [AllowAny]

class BookFileViewSet(ModelViewSet):
    serializer_class = BookFileSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'book_id':self.kwargs['book_pk']}
    
    def get_queryset(self):
        return BookFiles.objects.filter(book_id=self.kwargs['book_pk'])
    
    
class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAdminUser]
    # Permission is for filtering is user is admin he can see all the customer, if not only his data will be shown...
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
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
    
class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Order.objects.all()
        # If user is staff we will return all the data from all the customer...
        customer_id = Customer.objects.only('id').get(user_id=user.id)
        return Order.objects.select_related('customer__user').filter(customer_id=customer_id)
        # If user is not staff it will return only data related from that perticular user...