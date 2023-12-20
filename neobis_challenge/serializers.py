import string
from random import random

from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import serializers
from neobis_challenge.models import Category, Product, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title', 'image', 'price',


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = 'product', 'quantity', 'total_price'

    def create(self, validated_data):
        # Генерация случайного номера перед созданием объекта Order
        validated_data['order_number'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return super().create(validated_data)



