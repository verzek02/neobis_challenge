from django.urls import path
from .views import (
    CategoryListView, ProductListView,
    ProductDetailView, CartDetail,
    AddToCart, CreateOrder, OrderList, OrderDetail,
)

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartDetail.as_view(), name='cart-detail'),
    path('cart/add/', AddToCart.as_view(), name='add-to-cart'),
    path('order/', OrderList.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order/create/', CreateOrder.as_view(), name='create-order'),
]
