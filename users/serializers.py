from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from users.models import CustomUser


class UserValidateSerializer(serializers.Serializer):
    model = CustomUser


class UserCreateSerializer(serializers.Serializer):
    model = CustomUser

    def validate_username(self, username):
        try:
            CustomUser.objects.get(username=username)
            raise ValidationError("This username is already taken.")
        except CustomUser.DoesNotExist:
            return username
