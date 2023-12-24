from django.contrib.auth.models import AbstractUser, PermissionsMixin, Permission, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, verbose_name=_('groups'))
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        verbose_name=_('user permissions'),
        help_text=_('Specific permissions for this user.'),
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile for {self.user.username}"
