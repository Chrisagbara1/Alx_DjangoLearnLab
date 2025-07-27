
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # create logic here
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # edit logic here
    pass