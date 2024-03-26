from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from admin_panel.serializers import (UserSerializer, ProductSerializer, CategorySerializer ,ProductImagesSerializer ,ShippingAddressSerializer)
from admin_panel.models import (Product, Category, ProductImage, ShippingAddress)

User = get_user_model()

class UsersCrudViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryCrudViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class ProductCrudViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductImagesCrudViewSet(viewsets.ModelViewSet):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImagesSerializer
    permission_classes = [permissions.IsAdminUser]


class ShippingAddressCrudViewSet(viewsets.ModelViewSet):

    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [permissions.IsAdminUser]