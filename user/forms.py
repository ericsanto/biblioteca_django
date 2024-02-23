from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserCustom


class UserForm(UserCreationForm):

    class Meta:
        model = UserCustom
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
