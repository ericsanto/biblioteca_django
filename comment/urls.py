from django.urls import path
from .views import CommentCreateView


urlpatterns = [
    path('comentar-livro/<int:pk>/',
         CommentCreateView.as_view(), name='comment_book'),
]
