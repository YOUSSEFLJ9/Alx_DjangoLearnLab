## Uodate
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Output: Successfully updated title

Book.objects.get(id=b.id).title
# Output: 'Nineteen Eighty-Four'
