from .models import Author, Book, Library, Librarian

def sample_queries(library_name, author_name):
    # One-to-Many: Get all books by a specific author
    # author_name = "Robert Green"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    
    # Many-to-Many: Get all books in a specific library
    # library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    
    # One-to-One: Get the librarian of a specific library
    librarian = Librarian.objects.get(library=library)
    
    return {
        "books_by_author": books_by_author,
        "books_in_library": books_in_library,
        "librarian": librarian,
    }