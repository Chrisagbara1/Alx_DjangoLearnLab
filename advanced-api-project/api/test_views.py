from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create an APIClient
        self.client = APIClient()

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test description"
        )

    def test_create_book_authenticated(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login, "Login failed in test_create_book_authenticated")

        url = reverse('book-create')  # Ensure this name matches your urls.py
        data = {
            "title": "New Book",
            "author": "New Author",
            "description": "New description"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_authenticated(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login, "Login failed in test_update_book_authenticated")

        url = reverse('book-update', args=[self.book.id])  # Ensure this matches your urls.py
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "description": "Updated description"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login, "Login failed in test_delete_book_authenticated")

        url = reverse('book-delete', args=[self.book.id])  # Ensure this matches your urls.py
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())