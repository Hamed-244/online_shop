from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=15, required=False)
    name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)
    profile_image = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        super_data = super().get_cleaned_data()
        return {
            'name': self.validated_data.get('name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'username': super_data.get('username', ''),
            'email': super_data.get('email', ''),
            'password1': super_data.get('password1', ''),
            'password2': super_data.get('password2', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'profile_image': self.validated_data.get('profile_image', ''),
        }

