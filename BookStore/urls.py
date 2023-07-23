from django.urls import path
from .views import BooksViewSet, CustomerViewSet, OrderViewSet, BookFileViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('books', BooksViewSet, basename='book')
router.register('customer', CustomerViewSet, basename='customer')
router.register('order', OrderViewSet, basename='orders')

books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('file', BookFileViewSet, basename='product-image')


urlpatterns = router.urls + books_router.urls