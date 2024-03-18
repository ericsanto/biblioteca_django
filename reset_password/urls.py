from django.urls import path
from django.contrib.auth.views import PasswordResetCompleteView
from .views import (
    CustomPasswordResetView,
    CustomResetPasswordDone,
    CustomPasswordResetConfirmView,
)


urlpatterns = [
    path('reset-password/', CustomPasswordResetView.as_view(),
         name='reset_password'),
    path('reset-password-done/', CustomResetPasswordDone.as_view(),
         name='password_reset_done'),
    path('reset-password-confirm/<slug:uidb64>/<slug:token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete_view')

]
