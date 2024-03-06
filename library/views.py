
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Book, Category, Comment, History
from .forms import BookForm, CategoryForm, CommentBookForm
from reserve.models import ReserveBook


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
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            context['reserve'] = ReserveBook.objects.filter(
                user=self.request.user)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_book = self.kwargs['pk']
        book = Book.objects.get(id=id_book)
        category_book = book.category
        context['category_books'] = Book.objects.filter(
            category__name=category_book).exclude(id=id_book)[:9]
        context['comments'] = Comment.objects.all()
        context['form'] = CommentBookForm()

        return context

    def post(self, request, *args, **kwargs):
        form = CommentBookForm(request.POST)

        if self.request.user.is_authenticated:
            if form.is_valid():
                book_id = self.kwargs['pk']
                comment = form.cleaned_data['comment_user']
                Comment.objects.create(comment_user=comment,
                                       user=self.request.user, book_id=book_id)
                return self.get(request, *args, **kwargs)
            else:
                return self.get(request, *args, **kwargs)
        else:
            return redirect('book_detail', self.kwargs['pk'])
