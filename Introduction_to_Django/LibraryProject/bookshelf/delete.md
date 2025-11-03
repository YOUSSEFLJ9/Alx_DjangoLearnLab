## Delete
from bookshelf.models import Book
book.delete()
Book.objects.all()
# Output: (1, {'library.Book': 1})
# Output: <QuerySet []>