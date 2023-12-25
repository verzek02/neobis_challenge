from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username


CustomUser.groups.related_name = 'customuser_groups'

# Добавьте related_name для user_permissions
CustomUser.user_permissions.related_name = 'customuser_user_permissions'
