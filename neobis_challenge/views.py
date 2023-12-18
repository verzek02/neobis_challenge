from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.mixins import RetrieveModelMixin

from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer
from .models import Category, Product


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
