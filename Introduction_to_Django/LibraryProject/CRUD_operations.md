# CRUD Operations for Book Model

## Create
from library.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984 by George Orwell>

## Retrieve
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell>]>

b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
# Output: ('1984', 'George Orwell', 1949)

## Uodate
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
# Output: Successfully updated title

Book.objects.get(id=b.id).title
# Output: 'Nineteen Eighty-Four'

## Delete
b.delete()
Book.objects.all()
# Output: (1, {'library.Book': 1})
# Output: <QuerySet []>