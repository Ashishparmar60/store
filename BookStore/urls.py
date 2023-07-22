from django.urls import path
from .views import BooksViewSet, CustomerViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BooksViewSet)
router.register('customer', CustomerViewSet)

urlpatterns = router.urls