from django.urls import path
from apps.users.views import *


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api-register'),
    path('login/', AuthAPIView.as_view(), name='api-login'),
    path('token-login/', TokenLoginAPIView.as_view(), name='api-token-login'),
    path('logout/', LogoutAPIView.as_view(), name='api-logout'),
]

