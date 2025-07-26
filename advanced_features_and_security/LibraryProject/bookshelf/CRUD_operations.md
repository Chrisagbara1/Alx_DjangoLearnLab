---

### ✅ `CRUD_operations.md` (optional but often required)

This file consolidates all operations into a single log.

```markdown
# CRUD Operations for Book Model

## CREATE
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 (1949)>