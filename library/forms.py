from django import forms
from .models import Book, Category, Comment


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('__all__')


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('__all__')


