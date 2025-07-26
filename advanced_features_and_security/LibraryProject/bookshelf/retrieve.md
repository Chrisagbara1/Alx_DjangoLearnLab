---

### ✅ `retrieve.md`

```markdown
# RETRIEVE: Fetch all book attributes

```python
from bookshelf.models import Book

# Retrieve all Book instances
books = Book.objects.get()

# View the book we created
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Expected output:
# Title: 1984, Author: George Orwell, Year: 1949