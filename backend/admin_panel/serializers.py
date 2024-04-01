from django.contrib.auth import get_user_model
from rest_framework import serializers
from admin_panel.models import (Product,Category,ProductImage,ShippingAddress,Order,OrderItem,Payment,Feedback,Notice)


User = get_user_model()

# User Model Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id" , "username" ,"email", "first_name" , "last_name" , "email" , "is_staff", "is_active")

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("id" , "date_joined" , "groups" , "user_permissions")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
        

class OrderSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = "__all__"
        
    def get_final_price(self , obj):
        return obj.final_price()


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = "__all__"
        
    def get_total_price(self , obj):
        return obj.total_price()


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = "__all__"


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = "__all__"