from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryListView,
    ProductListView, ProductDetailView,
    OrderViewSet,
)



urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list-create'),

    path('products/', ProductListView.as_view(), name='product-list-create'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('order/', OrderViewSet.as_view(), name='product-list-create'),
    # path('add/<int:product_id>/', basket_add, )
]
