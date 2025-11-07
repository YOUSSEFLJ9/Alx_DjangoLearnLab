## Retrieve
Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell>]>

b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
# Output: ('1984', 'George Orwell', 1949)
