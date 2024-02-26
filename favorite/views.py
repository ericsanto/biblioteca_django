from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Favorite


class ListFavoriteBookListView(ListView):
    model = Favorite
    template_name = 'list_favorite_book.html'
    context_object_name = 'favorites'
    