from django.contrib.auth import get_user_model
from rest_framework import serializers
from admin_panel.models import (Product,Category,ProductImage,ShippingAddress,Order,OrderItem,Payment,Feedback,Notice)
from django.contrib.auth.hashers import make_password

User = get_user_model()

# User Model Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id" , "username" ,"email", "first_name" , "last_name" , "profile_image" , "is_staff", "is_active")

class UserModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=["profile_image",]
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserModifySerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserModifySerializer, self).update(instance, validated_data)


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