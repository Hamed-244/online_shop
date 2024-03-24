from django.contrib import admin
from admin_panel.models import Category , Product , ProductImage , ShippingAddress \
    , Order , OrderItem



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)