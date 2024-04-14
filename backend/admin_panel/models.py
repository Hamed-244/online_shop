from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# define main variables
User = get_user_model()


class Category(models.Model):
    image = models.ImageField(upload_to='category_images', blank=True, null=True)
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True , max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=1)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="shipping_addresses")
    title = models.CharField(max_length=128)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=32)
    created_at = models.DateField(auto_created=True, null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):

    status_choices = (
        ('pending', 'Pending'),
        ('delivering', 'Delivering'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, related_name="orders")
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True, related_name="orders")
    status = models.CharField(max_length=10, choices=status_choices , default='pending')
    order_date = models.DateTimeField(blank=True, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def final_price(self):
        order_items = self.items
        count = Decimal('0.00')
        for item in order_items.all() :
            count += Decimal(str(item.total_price()))
        return count

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL , null=True, related_name="orders")
    quantity = models.IntegerField(default=1)
    purchase_price = models.DecimalField(max_digits=10 , decimal_places=2 , default=0)
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.purchase_price = self.product.price
        super().save(*args, **kwargs)

    def total_price(self):
        price = self.purchase_price
        quantity = self.quantity
        total_price = price * quantity
        return total_price

    def __str__(self):
        return self.product.name


class Payment(models.Model):
    status_choices = (
        ('done', 'Done'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded')
    )

    payment_method_choices = (
        ('paypal', 'PayPal'),
        ('zarinpal', 'ZarinPal')
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE , related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=status_choices , default="done")
    payment_method = models.CharField(max_length=10, choices=payment_method_choices)
    payment_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.order.user.username


class Feedback(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="feedback")
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    comment = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order.user.username


class Notice(models.Model):
    type_choices = (
        ('danger', 'Danger'),
        ('success', 'Success'),
        ('warn', 'Warn')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="دotifications")
    type = models.CharField(max_length=10, choices=type_choices, default="success")
    title = models.CharField(max_length=128)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title