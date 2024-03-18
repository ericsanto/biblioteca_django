from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from .forms import FormPasswordResetView


class CustomPasswordResetView(PasswordResetView):
    form_class = FormPasswordResetView
    template_name = 'registration/password_reset.html'


class CustomResetPasswordDone(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
