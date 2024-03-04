from django import forms
from django.contrib.auth.forms import PasswordResetForm


class FormPasswordResetView(PasswordResetForm):
    email = forms.EmailField(
        max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}))
