from django.contrib import admin
from .models import Author, Book, Category, History


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(History)
