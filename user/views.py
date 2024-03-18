from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import UserForm
from .models import Profile, UserCustom


class UserCreateView(CreateView):
    model = UserCustom
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('home')


class ProfileUser(ListView):
    model = Profile
    template_name = 'profile_user.html'
    context_object_name = 'profile'
