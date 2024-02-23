from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCustom(AbstractUser):
    email = models.EmailField('Email', max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name',)


class Profile(models.Model):
    name = models.CharField('Nome', max_length=255)
    user = models.OneToOneField(UserCustom, on_delete=models.PROTECT)
