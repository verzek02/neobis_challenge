from django.http import HttpResponseRedirect
from rest_framework import generics,  status
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer, ProductDetailSerializer, CartSerializer
from .models import Category, Product, Cart, CartItem


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CartDetail(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user

        try:
            cart = user.cart
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class AddToCart(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartSerializer

    def update(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user
        cart, created = CartItem.objects.get_or_create(user=user)

        # Проверяем, есть ли товар уже в корзине
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        # Если товар уже в корзине, увеличиваем количество
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            # Если товар только что добавлен, обновляем общую стоимость и количество
            cart.total_price += product.price
            cart.total_quantity += 1
            cart.save()

        # Получаем данные о корзине
        serializer = self.get_serializer(cart)

        # Дополняем данные о корзине общей стоимостью и количеством
        cart_data = serializer.data
        cart_data['total_price'] = float(cart.total_price)  # Преобразуем Decimal в float
        cart_data['total_quantity'] = cart.total_quantity

        return Response(cart_data)
