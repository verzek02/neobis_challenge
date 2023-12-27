# views.py
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserCreateSerializer, AuthSerializer


class RegisterAPIView(APIView):
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
        return Response(data={'message': 'You are authenticated with a token!'})


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(data={'message': 'Successfully logged out.'})
