from django.urls import path
from .views import reserve_book_create, reserve_book_devolution, ReserveBookListView

urlpatterns = [
    path('reservar-livro/<int:book_id>/',
         reserve_book_create, name='reserve_create'),
    path('devolver-livro-reservado/<int:id_reserve>/',
         reserve_book_devolution, name='reserve_devolution'),
    path('livros-reservado/<int:pk>/',
         ReserveBookListView.as_view(), name='book_reserve')
]
