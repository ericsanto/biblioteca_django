from django.urls import path
from .views import reserve_book_create

urlpatterns = [
    path('reserve-book/<int:book_id>/',
         reserve_book_create, name='reserve_create'),
]
