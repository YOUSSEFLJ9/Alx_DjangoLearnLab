## Uodate
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
# Output: Successfully updated title

Book.objects.get(id=b.id).title
# Output: 'Nineteen Eighty-Four'
