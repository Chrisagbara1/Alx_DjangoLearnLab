from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-area/', views.admin_view, name='admin_view'),
    path('librarian-area/', views.librarian_view, name='librarian_view'),
    path('member-area/', views.member_view, name='member_view'),
    
    # Add, Edit, Delete Book URLs
    path('add_book/', views.add_book, name='add_book'),  # ✅ matches "add_book/"
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # ✅ matches "edit_book/"
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]