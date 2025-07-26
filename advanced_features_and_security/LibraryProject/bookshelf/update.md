---

### ✅ `update.md`

```markdown
# UPDATE: Change the title of the book

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the change
updated_book = Book.objects.get(pk=book.pk)
print(updated_book)

# Expected output:
# Nineteen Eighty-Four (1949)