from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='product')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def total_price(self):
        product_price = self.product.price if self.product else 0
        return self.quantity * product_price



