import string
from random import choice

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import CustomUser, Category, Product, Cart, CartItem, Order
from .serializers import CustomUserSerializer, CategorySerializer, ProductSerializer, CartSerializer, \
    CartItemSerializer, OrderSerializer


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Создаем Refresh Token
            refresh_token = self.get_refresh_token(user)
            access_token = AccessToken.for_user(user)

            data = {
                'refresh': str(refresh_token),
                'access': str(access_token),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_refresh_token(self, user):
        refresh_token = RefreshToken.for_user(user)
        return refresh_token


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        login_field = request.data.get('login_field')  # Поле для входа (номер телефона или электронная почта)
        password = request.data.get('password')

        # Проверяем, является ли login_field номером телефона или электронной почтой
        if '@' in login_field:
            user = CustomUser.objects.filter(email=login_field).first()
        else:
            user = CustomUser.objects.filter(phone_number=login_field).first()

        if user and user.check_password(password):
            login(request, user)

            # Создаем Access Token и Refresh Token
            refresh_token = RefreshToken.for_user(user)
            access_token = AccessToken.for_user(user)

            data = {
                'refresh': str(refresh_token),
                'access': str(access_token),
            }
            return Response(data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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
        cart_data = serializer.data

        # Включаем информацию о товарах внутри корзины
        cart_data['products'] = CartItemSerializer(cart.cartitem_set.all(), many=True).data

        return Response(cart_data)


class AddToCart(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

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


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user

        try:
            cart = user.cart
        except Cart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        order, _ = Order.objects.get_or_create(cart=cart, order_number=''.join(choice(string.digits) for _ in range(5)))

        order.phone_number = cart.user.phone_number
        order.address = cart.user.address
        order.landmark = cart.user.landmark
        order.save()

        cart.cartitem_set.all().delete()
        cart.total_price = 0
        cart.total_quantity = 0
        cart.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
