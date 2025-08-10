from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create', BookViewSet.as_view({'post': 'create'}), name='book-create'),
    path('books/update', BookViewSet.as_view({'put': 'update'}), name='book-update'),
    path('books/delete', BookViewSet.as_view({'delete': 'destroy'}), name='book-delete'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]