from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_orwell = Book.objects.filter(author=author)
print("Books by", author_name + ":", list(books_by_orwell))

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of", library_name + ":", librarian.name)