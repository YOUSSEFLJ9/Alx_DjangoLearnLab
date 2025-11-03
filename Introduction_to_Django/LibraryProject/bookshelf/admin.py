from django.contrib import admin
from .models import Book


# Register your models here.
# how to register models in admin site?
# admin.site.register(Book)
# after registering the model, we can see it in the admin site
# to access the admin site, we need to create a superuser
# run the command: python manage.py createsuperuser
# then follow the prompts to create a superuser
# after creating the superuser, run the server and go to /admin
# we can log in with the superuser credentials and see the Book model in the admin site
# we can also customize the admin interface by creating a ModelAdmin class
# for example, we can create a BookAdmin class to customize the display of the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
admin.site.register(Book, BookAdmin)
# admin.site.unregister(Book)


