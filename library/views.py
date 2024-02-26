from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.urls import reverse_lazy
from .models import Category, Book
from .forms import CategoryForm, BookForm


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class CatalogBookListView(ListView):
    model = Book
    template_name = 'catalog_books.html'
    context_object_name = 'books'


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
