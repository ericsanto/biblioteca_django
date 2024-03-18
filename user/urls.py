from django.urls import path
from .views import UserCreateView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('cadastro-usuario/', UserCreateView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
