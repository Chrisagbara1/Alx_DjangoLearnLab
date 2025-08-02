
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create the router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Original ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # ViewSet CRUD endpoints
    path('', include(router.urls)),
]