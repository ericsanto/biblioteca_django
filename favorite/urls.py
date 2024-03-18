from django.urls import path
from .views import ListFavoriteBookListView


urlpatterns = [
    path('', ListFavoriteBookListView.as_view(), name='list_favorite_book')
]
