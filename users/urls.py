from django.urls import path
from users import views

urlpatterns = [
    path('authorization/', views.authorization_api_view),
    path('register/', views.register, name='register')

]
