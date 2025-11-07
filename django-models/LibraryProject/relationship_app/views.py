from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView


# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    response_text = ""

    for book in books:
        response_text += f"Title: {book.title} , Author: {book.author.name}<br>"

    return render(request, 'relationship_app/list_books.html', {'books': books})

class BookView(DetailView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'book'
