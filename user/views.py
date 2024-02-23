from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserForm
from .models import UserCustom


class UserCreateView(CreateView):
    model = UserCustom
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('home')