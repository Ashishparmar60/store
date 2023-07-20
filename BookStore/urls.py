from django.urls import path
from .views import BooksViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BooksViewSet)

urlpatterns = router.urls