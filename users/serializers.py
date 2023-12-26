from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import CustomUser


class UserValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def validate_username(self, username):
        try:
            CustomUser.objects.get(username=username)
            raise ValidationError("This username is already taken.")
        except CustomUser.DoesNotExist:
            return username