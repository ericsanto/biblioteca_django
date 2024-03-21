from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ReserveBook
from library.models import Book
from user.models import UserCustom


@login_required
def reserve_book_create(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        user = UserCustom.objects.get(email=request.user)
        if not user.has_a_scheduling:
            reserve = ReserveBook.objects.create(
                user=user,
                book=book,
            )
            reserve.save()
            book.quantity -= 1
            book.quantity_reserve += 1
            book.save()
            user.has_a_scheduling = True
            user.save()
            messages.success(
                request, f'Parabéns, você agendou o livo')
            return redirect('catalog')
        else:
            messages.error(request, 'Você já tem um livro agendado')
            return redirect('catalog')


@login_required
def reserve_book_devolution(request, id_reserve):
    reserve = ReserveBook.objects.get(id=id_reserve)
    user = UserCustom.objects.get(email=request.user)

    if user.has_a_scheduling:
        user.has_a_scheduling = False
        user.save()
        reserve.book.quantity += 1
        reserve.book.save()
        reserve.devolution = True
        reserve.save()
        messages.success(request, f'Livro devolvido com sucesso.')
        return redirect('catalog')
    else:
        messages.warning(request, 'Você não possui livro reservado')
    return redirect('catalog')


class ReserveBookListView(LoginRequiredMixin, ListView):
    model = ReserveBook
    template_name = 'list_book_reserve.html'
    context_object_name = 'books'

    def get_queryset(self):
        try:
            user = self.request.user
            resever_book_user = ReserveBook.objects.filter(
                user=user)
            return resever_book_user

        except user.DoesNotExist:
            messages.error(self.request, 'Usuário não existe')


@login_required
def renew_reserve_book(request, id_reserve):
    if request.method == 'POST':
        reserve = ReserveBook.objects.get(id=id_reserve)

        if not reserve.renew_book:
            reserve.renew_book = True
            reserve.save()
            messages.success(request, 'Livro renovado com sucesso')
        else:
            messages.warning(request, 'Você já renovou esse livro uma vez')
        return redirect('catalog')
    return redirect('catalog')
