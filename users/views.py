from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
# from django.contrib.auth.models import User
from users.serializers import UserValidateSerializer, UserCreateSerializer
from users.models import CustomUser


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        user = CustomUser.objects.create_user(**serializer.validated_data)
        return Response(data={'user_id': user.id})



@api_view(['POST'])
def authorization_api_view(request):
    if request.method == 'POST':
        serializer = UserValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
