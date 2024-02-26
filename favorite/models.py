from django.db import models
from library.models import Book


class Favorite(models.Model):
    book = models.ManyToManyField(Book)

    def __str__(self):
        return ''.join([book.name for book in self.book.all()])
