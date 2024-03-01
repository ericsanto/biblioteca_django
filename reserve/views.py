from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import ReserveBook
from library.models import Book
from user.models import UserCustom


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
            book.save()
            user.has_a_scheduling = True
            user.save()
            messages.success(
                request, f'Parabéns, você agendou o livo {book.name}')
            return redirect('catalog')
        else:
            messages.error(request, 'Você já tem um livro agendado')
            return redirect('catalog')


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


class ReserveBookListView(ListView):
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
            messages.error(self.request, f'Usuário não existe')


def renew_reserve_book(request, id_reserve):
    if request.method == 'POST':
        reserve = ReserveBook.objects.get(id=id_reserve)
        print(reserve)

        if reserve.renew_book == False:
            reserve.renew_book = True
            reserve.save()
            messages.success(request, 'Livro renovado com sucesso')
        else:
            messages.warning(request, 'Você já renovou esse livro uma vez')
        return redirect('catalog')
    return redirect('catalog')


"""def book_suggestion_based_on_research(request, id_book):
    if request.method == 'GET':
        book = Book.objects.get(id=id_book)
        category_book = book.category
        print(category_book)"""
