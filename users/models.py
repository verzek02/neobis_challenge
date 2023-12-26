from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from users.manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
