from django.db import models
from library.models import Book
from user.models import UserCustom
from datetime import date, timedelta


class ReserveBook(models.Model):
    user = models.ForeignKey(
        UserCustom, on_delete=models.PROTECT, verbose_name='Usuário')
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, verbose_name='Livro')
    date_of_devolution = models.DateField(
        'Data de devolução', blank=True, null=True)
    date_of_reserve = models.DateField(
        verbose_name='Data da reserva', blank=True, null=True)

    def __str__(self):
        return self.book.name

    def save(self, *args, **kwargs):
        if not self.date_of_devolution:
            date_actually = date.today()
            time_delta = timedelta(7)
            self.date_of_devolution = date_actually + time_delta

        self.date_of_reserve = date.today()
        super().save(*args, **kwargs)
