from django.shortcuts import render
from rest_framework import viewsets, mixins

from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from .models import Category, Product


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
