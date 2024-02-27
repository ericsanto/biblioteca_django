from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.urls import reverse_lazy
from .models import Book, Category, History
from .forms import BookForm, CategoryForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        books = Book.objects.all()
        search = self.request.GET.get('search')
        category_url = self.request.GET.get('category')

        if search:
            books = books.filter(name__icontains=search)

        if category_url:
            books = books.filter(category__name=category_url)

        return books


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list_all')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list_all')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
