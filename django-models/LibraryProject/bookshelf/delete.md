---

### ✅ `delete.md`

```markdown
# DELETE: Remove the book instance

```python
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()

# Expected output:
# <QuerySet []>