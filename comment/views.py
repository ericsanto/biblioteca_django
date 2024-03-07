from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib import messages
from library.models import Book
from .models import Comment
from .forms import CommentBookForm


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentBookForm
    template_name = 'comment_book.html'

    def post(self, request, *args, **kwargs):
        form = CommentBookForm(request.POST)
        id_book = self.kwargs['pk']
        book = Book.objects.get(id=id_book)
        if request.method == 'POST':
            if form.is_valid():
                comment = form.cleaned_data['comment_user']
                comment_created = Comment.objects.create(comment_user=comment, user=self.request.user,
                                                         book=book)
                messages.success(
                    request, 'Comentário adicionado com sucesso! Obrigado por expor sua opinião')
            return redirect('book_detail', pk=book.pk)
        return super().get(request, *args, **kwargs)
