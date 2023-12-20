import string
from random import random

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


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
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_number = models.CharField(max_length=10, blank=True, unique=True, null=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.name

    def total_price(self):
        product_price = self.product.price if self.product else 0
        return self.quantity * product_price


