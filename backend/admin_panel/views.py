from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from admin_panel.serializers import (UserSerializer,UserListSerializer,UserModifySerializer, ProductSerializer, CategorySerializer ,ProductImagesSerializer ,ShippingAddressSerializer,
    OrderSerializer ,OrderItemSerializer ,PaymentSerializer,FeedbackSerializer,NoticeSerializer,AdminLogSerializer)
from admin_panel.models import (Product, Category, ProductImage, ShippingAddress,Order,OrderItem,Payment,Feedback,Notice,AdminLog)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from datetime import date , timedelta , datetime
from collections import OrderedDict
from functools import wraps

User = get_user_model()

def log_action(action, model):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            instance = func(self, *args, **kwargs)
            if action == "delete":
                details = f"delete {model.__name__.lower()}: {instance}"
            else:
                details = f"{action} {model.__name__.lower()}: {instance}"
            AdminLog.objects.create(user=self.request.user, ip_address=self.request.META.get('REMOTE_ADDR', None), action=action, details=details)
            return instance
        return wrapper
    return decorator


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
    @log_action("create", User)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", User)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", User)
    def perform_destroy(self, instance):
        instance.delete()


class CategoryCrudViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name' , 'description']
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", Category)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", Category)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", Category)
    def perform_destroy(self, instance):
        instance.delete()


class ProductCrudViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['name' , 'description' , 'slug']
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", Product)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", Product)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", Product)
    def perform_destroy(self, instance):
        instance.delete()


class ProductImagesCrudViewSet(viewsets.ModelViewSet):

    queryset = ProductImage.objects.all()
    serializer_class = ProductImagesSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['id' , 'product__name']
    ordering_fields = '__all__'
    filterset_fields = ['id', 'product', 'created_at']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", ProductImage)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", ProductImage)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", ProductImage)
    def perform_destroy(self, instance):
        instance.delete()


class ShippingAddressCrudViewSet(viewsets.ModelViewSet):

    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['title' , 'address_line1', 'address_line2', 'city', 'state' ,'postal_code']
    ordering_fields = '__all__'
    filterset_fields = ['user' ,'city' ,'state' ,'postal_code']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", ShippingAddress)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", ShippingAddress)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", ShippingAddress)
    def perform_destroy(self, instance):
        instance.delete()


class OrderCrudViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__first_name' , 'user__last_name', 'user__username', 'shipping_address__city', 'shipping_address__state','shipping_address__title']
    ordering_fields = '__all__'
    filterset_fields = ['user', 'shipping_address', 'status']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", Order)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", Order)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", Order)
    def perform_destroy(self, instance):
        instance.delete()


class OrderItemCrudViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['order__user__username','product__slug', 'product__name', 'quantity']
    ordering_fields = '__all__'
    filterset_fields = ['order', 'product', 'quantity']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", OrderItem)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", OrderItem)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", OrderItem)
    def perform_destroy(self, instance):
        instance.delete()


class PaymentCrudViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['order__id','status', 'payment_method',]
    ordering_fields = '__all__'
    filterset_fields = ['order','status', 'payment_method','payment_date','updated_at']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", Payment)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", Payment)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", Payment)
    def perform_destroy(self, instance):
        instance.delete()


class FeedbackCrudViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['id','comment',]
    ordering_fields = '__all__'
    filterset_fields = ['order', 'rating','feedback_date','updated_at']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", Feedback)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", Feedback)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", Feedback)
    def perform_destroy(self, instance):
        instance.delete()


class NoticeCrudViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['title','message',]
    ordering_fields = '__all__'
    filterset_fields = ['user' ,'type']
    
    permission_classes = [permissions.IsAdminUser]
    @log_action("create", Notice)
    def perform_create(self, serializer):
        return serializer.save()

    @log_action("update", Notice)
    def perform_update(self, serializer):
        return serializer.save()

    @log_action("delete", Notice)
    def perform_destroy(self, instance):
        instance.delete()


class AdminLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdminLog.objects.all()
    serializer_class = AdminLogSerializer
    
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['ip_address' ,'action','details']
    ordering_fields = '__all__'
    filterset_fields = ['user__username','ip_address' ,'action']
    
    permission_classes = [permissions.IsAdminUser]


def get_payment_data():
    tomorrow = date.today() + timedelta(1)
    this_week = tomorrow - timedelta(7)

    payments = Payment.objects.filter(payment_date__range=[this_week , tomorrow])

    payment_date = {}

    today = datetime.today()
    for i in range(7):
        this_day = today - timedelta(i)
        date_str = this_day.strftime('%m-%d')
        payment_date[date_str] = 0
    for obj in payments:
        created_time = obj.payment_date
        date_str = created_time.strftime('%m-%d')
        payment_date[date_str] += 1
    reversed_dict = OrderedDict(reversed(list(payment_date.items())))
    return reversed_dict

def get_weekly_payments():
    tomorrow = date.today() + timedelta(1)
    this_week = tomorrow - timedelta(7)

    payments = Payment.objects.filter(payment_date__range=[this_week , tomorrow])
    return payments.count()

def get_total_revenue():
    tomorrow = date.today() + timedelta(1)
    this_week = tomorrow - timedelta(7)

    payments = Payment.objects.filter(payment_date__range=[this_week , tomorrow])
    total = 0
    for item in payments:
        total += item.amount
    return total

def get_weekly_sales():
    tomorrow = date.today() + timedelta(1)
    this_week = tomorrow - timedelta(7)

    payments = Payment.objects.filter(payment_date__range=[this_week , tomorrow])
    total = 0
    for item in payments:
        for item in item.order.items.all():
            total+=item.quantity
    return total

def get_popular_products():
    payments = Payment.objects.filter()
    products = {}
    for item in payments:
        for item in item.order.items.all():
            if products.get(item.product.name , None):
                products[item.product.name] += item.quantity
            else:
                products[item.product.name] = item.quantity

    sorted_products = sorted(products.items(), key=lambda x: x[1], reverse=True)
    top_products = sorted_products[:7]
    popular_products = dict(top_products)

    return popular_products


class DashboardInfoApi(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        
        payment_date = get_payment_data()
        weekly_payments = get_weekly_payments()
        total_revenue = get_total_revenue()
        weekly_sales = get_weekly_sales()
        popular_products = get_popular_products()
        data = {
            "payment": payment_date,
            "weekly-sales": weekly_sales,
            "weekly-payments": weekly_payments,
            "total-revenue": total_revenue,
            "popular": popular_products
        }

        return Response(data)