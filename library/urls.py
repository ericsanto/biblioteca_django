from django.urls import path
from .views import CategoryCreateView, BookCreateView


urlpatterns = [
    path('cadastrar-categoria/', CategoryCreateView.as_view(),
         name='create_category'),
    path('cadastrar-livro/', BookCreateView.as_view(), name='create_book'),
]
