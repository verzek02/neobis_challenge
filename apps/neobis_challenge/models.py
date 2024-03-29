import random
from django.db import models
from apps.users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, null=True, decimal_places=2, editable=False)
    total_quantity = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def find_total_price(self):
        total_price = 0
        total_price += self.product.price * self.quantity
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in cart"


class Order(models.Model):
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=6, editable=False, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        random_number = [random.randint(0, 9) for _ in range(6)]

        self.order_number = random_number

        super().save(*args, **kwargs)

        return self.order_number

    def __str__(self):
        return self.address
