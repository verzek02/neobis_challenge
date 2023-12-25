from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'description', 'price', 'category', 'created_at')


# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ('id', 'product', 'quantity')
#
#
# class CartSerializer(serializers.ModelSerializer):
#     cartitem_set = CartItemSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Cart
#         fields = ('id', 'user', 'total_price', 'total_quantity', 'cartitem_set')
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ('id', 'cart', 'order_number', 'phone_number', 'address', 'landmark', 'comment')
