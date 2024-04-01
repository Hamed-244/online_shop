from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from django.http import JsonResponse
from admin_panel.serializers import (UserSerializer,UserListSerializer, ProductSerializer, CategorySerializer ,ProductImagesSerializer ,ShippingAddressSerializer,
    OrderSerializer ,OrderItemSerializer ,PaymentSerializer,FeedbackSerializer,NoticeSerializer)
from admin_panel.models import (Product, Category, ProductImage, ShippingAddress,Order,OrderItem,Payment,Feedback,Notice)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()

class UsersCrudViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = '__all__'
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    
    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        elif self.action == "update":
            return UserUpdateSerializer
        return UserSerializer
    
    # permission_classes = [permissions.IsAdminUser]


class CategoryCrudViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAdminUser]


class ProductCrudViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser]


class ProductImagesCrudViewSet(viewsets.ModelViewSet):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImagesSerializer
    # permission_classes = [permissions.IsAdminUser]


class ShippingAddressCrudViewSet(viewsets.ModelViewSet):

    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    # permission_classes = [permissions.IsAdminUser]
    

class OrderCrudViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAdminUser]


class OrderItemCrudViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    # permission_classes = [permissions.IsAdminUser]


class PaymentCrudViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # permission_classes = [permissions.IsAdminUser]


class FeedbackCrudViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = [permissions.IsAdminUser]


class NoticeCrudViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    # permission_classes = [permissions.IsAdminUser]