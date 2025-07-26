# CREATE: Add a Book instance

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Check the created object
book
# Expected output:
# <Book: 1984 (1949)>