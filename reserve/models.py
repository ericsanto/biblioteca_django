from django.db import models
from library.models import Book
from user.models import UserCustom
from datetime import date, timedelta


STATUS = (
    ('DEVOLVIDO', 'Devolvido'),
    ('RESERVADO', 'Reservado')
)


class ReserveBook(models.Model):
    user = models.ForeignKey(
        UserCustom, on_delete=models.PROTECT, verbose_name='Usuário')
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, verbose_name='Livro')
    devolution_deadline = models.DateField(
        'Prazo de devolução', blank=True, null=True)
    date_of_reserve = models.DateField(
        verbose_name='Data da reserva', blank=True, null=True)
    devolution = models.BooleanField('Devolvido', default=False)
    renew_book = models.BooleanField('Renovado', default=False)
    return_date_after_renew = models.DateField(
        'Data de devolução após a renovação', blank=True, null=True)

    def __str__(self):
        return self.book.name

    def save(self, *args, **kwargs):
        if not self.devolution_deadline:
            date_actually = date.today()
            time_delta = timedelta(7)
            self.devolution_deadline = date_actually + time_delta

        self.date_of_reserve = date.today()

        if self.renew_book:
            self.return_date_after_renew = self.devolution_deadline + \
                timedelta(7)
        else:
            self.return_date_after_renew = None

        super().save(*args, **kwargs)


