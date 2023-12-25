from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


# class Cart(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     total_quantity = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return f"Cart for {self.user.username}"
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.quantity} x {self.product.title} in cart"
#
#
# class Order(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     order_number = models.CharField(max_length=10, unique=True, editable=False)
#     phone_number = models.CharField(max_length=15)
#     address = models.CharField(max_length=255)
#     landmark = models.CharField(max_length=255)
#     comment = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"Order {self.order_number}"
#
#
# @receiver(post_save, sender=CartItem)
# def create_order_item(sender, instance, created, **kwargs):
#     if created:
#         order = instance.cart.order
#         order.phone_number = instance.cart.user.phone_number
#         order.address = instance.cart.user.address
#         order.landmark = instance.cart.user.landmark
#         order.save()
