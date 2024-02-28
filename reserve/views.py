from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ReserveBook
from .forms import ReserveBookForm
from library.models import Book


def reserve_book_create(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        user = request.user
        existing_reserve = ReserveBook.objects.filter(user=user).exists()
        print(existing_reserve)
        if not existing_reserve:
            reserve = ReserveBook.objects.create(
                user=user,
                book=book,
            )
            reserve.save()
            book.quantity -= 1
            book.save()
            return redirect('catalog')
        else:
            messages.error(request, 'Você já tem um livro agendado')
            return redirect('catalog')
