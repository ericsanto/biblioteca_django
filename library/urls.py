from django.urls import path
from .views import (
    BookCreateView,
    BookDetailView,
    CategoryCreateView,
    CatalogBookListView,
    HomeTemplateView
)


urlpatterns = [
    path('inicio/', HomeTemplateView.as_view(), name='home'),
    path('cadastrar-categoria/', CategoryCreateView.as_view(),
         name='create_category'),
    path('cadastrar-livro/', BookCreateView.as_view(), name='create_book'),
    path('catalogo/', CatalogBookListView.as_view(), name='catalog'),
    path('detalhe-livro/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
