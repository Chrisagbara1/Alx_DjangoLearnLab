from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Router for ViewSets
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Token retrieval endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # ViewSet CRUD endpoints
    path('', include(router.urls)),
]