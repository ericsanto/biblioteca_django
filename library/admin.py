from django.contrib import admin
from .models import Author, Book, Comment, History


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(History)
