from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="parent")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True , max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
