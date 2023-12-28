# views.py
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserCreateSerializer, AuthSerializer, TokenLoginSerializer


class RegisterAPIView(APIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'user_id': user.id, 'key': token.key}, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthAPIView(ObtainAuthToken):
    serializer_class = AuthSerializer


class TokenLoginAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Получаем токен из запроса (если предоставлен в заголовке Authorization)
        client_token_key = request.headers.get('Authorization', '').split(' ')[-1]

        if not client_token_key:
            return Response(data={'message': 'Token not provided.'}, status=400)

        try:
            # Получаем текущий токен пользователя
            user = request.user
            current_token = Token.objects.get(user=user)

            # Сравниваем токены
            if client_token_key == current_token.key:
                message = 'You are authenticated with a token!'
            else:
                message = 'Token mismatch. Access denied.'

            # Используем сериализатор для возврата данных
            serializer = TokenLoginSerializer({'message': message})
            return Response(serializer.data)
        except Token.DoesNotExist:
            return Response(data={'message': 'Token not found for the user.'}, status=400)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(data={'message': 'Successfully logged out.'})
