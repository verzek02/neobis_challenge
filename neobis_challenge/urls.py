from django.urls import path
from .views import (
    CategoryListView,
    ProductListView, ProductDetailView, AddToCart, CartDetail
)

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list-create'),

    path('products/', ProductListView.as_view(), name='product-list-create'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartDetail.as_view(), name='cart-detail'),
    path('add-to-cart/', AddToCart.as_view(), name='add-to-cart'),
]
