from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.db import models


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username
