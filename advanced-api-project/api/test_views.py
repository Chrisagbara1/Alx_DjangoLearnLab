# api/tests/test_views.py

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

User = get_user_model()

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(
            username="regularuser",
            password="testpass123"
        )
        self.staff_user = User.objects.create_user(
            username="staffuser",
            password="staffpass123",
            is_staff=True
        )
    def test_create_book_authenticated(self):
        # ✅ Login before making POST request
        self.client.login(username='testuser', password='testpass123')

        data = {
            "title": "New Book",
            "author": "Another Author",
            "published_date": "2024-02-01"
        }
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_book_unauthenticated(self):
        # ❌ No login here — should be denied
        data = {
            "title": "Fail Book",
            "author": "Fail Author",
            "published_date": "2024-02-01"
        }
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, 403)  # Forbidden


        # Define endpoints
        self.list_url = reverse('book-list')     # e.g., /api/books/
        self.create_url = reverse('book-create') # e.g., /api/books/create/
        self.update_url = reverse('book-update', args=[1])  # placeholder book id
        self.delete_url = reverse('book-delete', args=[1])  # placeholder book id

        # Create a sample book as staff user
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post(self.create_url, {
            "title": "Sample Book",
            "author": "Author Name",
            "isbn": "1234567890",
            "publication_year": 2024
        }, format="json")
        self.book_id = response.data.get("id")
        self.update_url = reverse('book-update', args=[self.book_id])
        self.delete_url = reverse('book-delete', args=[self.book_id])
        self.client.logout()

    def test_list_books_unauthenticated(self):
        """Anyone should be able to list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books."""
        response = self.client.post(self.create_url, {
            "title": "Another Book",
            "author": "New Author",
            "isbn": "0987654321",
            "publication_year": 2025
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated_non_staff(self):
        """Authenticated non-staff users cannot create books if restricted."""
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url, {
            "title": "User Book",
            "author": "User Author",
            "isbn": "5555555555",
            "publication_year": 2025
        }, format="json")
        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_201_CREATED])

    def test_create_book_staff_user(self):
        """Staff user should be able to create books."""
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post(self.create_url, {
            "title": "Staff Book",
            "author": "Staff Author",
            "isbn": "2222222222",
            "publication_year": 2025
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_authenticated(self):
        """Authenticated staff should be able to update a book."""
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.put(self.update_url, {
            "title": "Updated Book",
            "author": "Updated Author",
            "isbn": "3333333333",
            "publication_year": 2026
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book_authenticated(self):
        """Authenticated staff should be able to delete a book."""
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_book_unauthenticated(self):
        """Unauthenticated user cannot delete a book."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)