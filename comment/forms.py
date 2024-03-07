from django import forms
from .models import Comment


class CommentBookForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_user',)
