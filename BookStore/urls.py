from django.urls import path
from .views import BooksViewSet, CustomerViewSet, OrderViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BooksViewSet)
router.register('customer', CustomerViewSet)
router.register('order', OrderViewSet, basename='orders')

urlpatterns = router.urls