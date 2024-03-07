from django.db import models
from library.models import Book
from user.models import UserCustom


class Comment(models.Model):
    comment_user = models.TextField()
    user = models.ForeignKey(UserCustom, blank=True,
                             null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, blank=True, null=True, on_delete=models.CASCADE)
