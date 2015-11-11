from django.contrib import admin
from books.models import  Author, Book, BookAdmin, AuthorAdmin

#admin.site.register(Book)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)