from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from comment.models import Comment
from .forms import BookForm, CategoryForm
from .models import Author, Book, Category, History
from reserve.models import ReserveBook
import os


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historys'] = History.objects.all()
        return context


class CatalogBookListView(ListView):
    model = Book
    template_name = 'catalog_books.html'
    context_object_name = 'books'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if user.is_authenticated:
            context['reserve'] = ReserveBook.objects.filter(
                user=user)
        context['authors'] = Author.objects.all()[:7]
        context['books_informatics'] = Book.objects.filter(
            category__name='Computação, Informática e Mídias Digitais')
        context['books_literary'] = Book.objects.filter(
            category__name='Literatura')
        context['book_more_reserved'] = Book.objects.all().order_by(
            '-quantity_reserve')[:4]

        if user.is_authenticated:
            reservations = ReserveBook.objects.filter(user=user)

            if reservations:
                last_reserve_id = ReserveBook.objects.order_by(
                    '-id', )[:1].get().id
                last_reserve_book = ReserveBook.objects.get(id=last_reserve_id)
                last_category_reserved_book = last_reserve_book.book.category

                book_id = last_reserve_book.book.id

                last_reserve_category_book = Book.objects.filter(
                    category__name=last_category_reserved_book).order_by('-quantity_reserve').exclude(id=book_id)[:5]
                context['suggestion'] = last_reserve_category_book

        return context

    def get_queryset(self):
        books = Book.objects.all()
        search = self.request.GET.get('search')
        category_url = self.request.GET.get('category')
        author_url = self.request.GET.get('author')

        if search:
            books = books.filter(name__icontains=search)

        if category_url:
            books = books.filter(category__name=category_url)

        if author_url:
            books = books.filter(author__name=author_url)

        return books


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list_all')


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list_all')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_book = self.kwargs['pk']
        book = Book.objects.get(id=id_book)
        category_book = book.category
        context['category_books'] = Book.objects.filter(
            category__name=category_book).exclude(id=id_book)[:9]
        context['comment'] = Comment.objects.filter(book_id=id_book)
        return context


def download_pdf(request, book_id):
    pdf_book = get_object_or_404(Book, id=book_id)
    path_pdf = os.path.join(settings.MEDIA_ROOT, str(pdf_book.pdf_books))
    with open(path_pdf, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf_book.pdf_books.name}"'
        return response
