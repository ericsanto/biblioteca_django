from django.urls import path
from .views import (
    BookCreateView,
    BookDetailView,
    CategoryCreateView,
    CatalogBookListView,
    HomeTemplateView,
    download_pdf,
)


urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('cadastrar-categoria/', CategoryCreateView.as_view(),
         name='create_category'),
    path('cadastrar-livro/', BookCreateView.as_view(), name='create_book'),
    path('', CatalogBookListView.as_view(), name='catalog'),
    path('detalhe-livro/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('baixar-pdf/<book_id>/', download_pdf, name='download_pdf'),
]
