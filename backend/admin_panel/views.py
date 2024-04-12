from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from admin_panel.serializers import (UserSerializer,UserListSerializer,UserModifySerializer, ProductSerializer, CategorySerializer ,ProductImagesSerializer ,ShippingAddressSerializer,
    OrderSerializer ,OrderItemSerializer ,PaymentSerializer,FeedbackSerializer,NoticeSerializer)
from admin_panel.models import (Product, Category, ProductImage, ShippingAddress,Order,OrderItem,Payment,Feedback,Notice)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()

class UsersCrudViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['username' , 'first_name' , 'last_name', 'email']
    ordering_fields = '__all__'
    filterset_fields = ['username' , 'first_name' , 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']
    
    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        elif self.action in ["update" , "partial_update" , "create"] :
            return UserModifySerializer
        return UserSerializer
    
    permission_classes = [permissions.IsAdminUser]


class CategoryCrudViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name' , 'description']
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    
    permission_classes = [permissions.IsAdminUser]


class ProductCrudViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name' , 'description' , 'slug']
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    
    permission_classes = [permissions.IsAdminUser]


class ProductImagesCrudViewSet(viewsets.ModelViewSet):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImagesSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['id' , 'product__name']
    ordering_fields = '__all__'
    filterset_fields = ['id', 'product', 'created_at']
    
    permission_classes = [permissions.IsAdminUser]


class ShippingAddressCrudViewSet(viewsets.ModelViewSet):

    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['title' , 'address_line1', 'address_line2', 'city', 'state' ,'postal_code']
    ordering_fields = '__all__'
    filterset_fields = ['user' ,'city' ,'state' ,'postal_code']
    
    permission_classes = [permissions.IsAdminUser]
    

class OrderCrudViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['id','user__first_name' , 'user__last_name', 'user__username', 'shipping_address__city', 'shipping_address__state']
    ordering_fields = '__all__'
    filterset_fields = ['user', 'shipping_address', 'status']
    
    permission_classes = [permissions.IsAdminUser]


class OrderItemCrudViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser]


class PaymentCrudViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]


class FeedbackCrudViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAdminUser]


class NoticeCrudViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAdminUser]