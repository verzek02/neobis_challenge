from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .serializers import OrderDetailSerializer
from .views import (
    CategoryListView,
    ProductListView, ProductDetailView,
    OrderViewSet, OrderDetailView,
)



urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list-create'),

    path('products/', ProductListView.as_view(), name='product-list-create'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('order/', OrderViewSet.as_view(), name='product-list-create'),
    path('order/detail/<int:pk>/', OrderDetailView.as_view(), name='order-detail')
]
