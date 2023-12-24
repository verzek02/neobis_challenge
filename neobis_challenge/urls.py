from django.urls import path
from .views import (
    UserRegistrationView, UserLoginView,
    CategoryListView, ProductListView, ProductDetailView,
    CartDetail, AddToCart, CreateOrder
)

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', UserLoginView.as_view(), name='user-login'),
    path('', CategoryListView.as_view(), name='category-list'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/cart/', CartDetail.as_view(), name='cart-detail'),
    path('api/cart/add/', AddToCart.as_view(), name='add-to-cart'),
    path('api/order/create/', CreateOrder.as_view(), name='create-order'),
]
