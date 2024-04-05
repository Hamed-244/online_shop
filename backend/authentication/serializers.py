from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken
if api_settings.BLACKLIST_AFTER_ROTATION:
    from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
    
from dj_rest_auth.registration.serializers import RegisterSerializer
from authentication.validators import phonenumber_validator , profile_picture_validator , username_validator
try:
    from allauth.account.models import EmailAddress
    from allauth.account import app_settings as allauth_account_settings
    from allauth.account.adapter import get_adapter
    from allauth.utils import get_username_max_length
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')
from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
        validators=[username_validator]
    )
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED, validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    phone_number = serializers.CharField(max_length=15, required=False,validators=[phonenumber_validator])
    last_name = serializers.CharField(max_length=50, required=False)
    first_name = serializers.CharField(max_length=50, required=False)
    profile_image = serializers.ImageField(required=False,validators=[profile_picture_validator])

    def get_cleaned_data(self):
        super_data = super().get_cleaned_data()
        return {
            'username': super_data.get('username', ''),
            'email': super_data.get('email', ''),
            'password1': super_data.get('password1', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'profile_image': self.validated_data.get('profile_image', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.profile_image = self.cleaned_data.get('profile_image')
        user.save()
        return user


class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField()
    def validate(self, attrs):
        token = UntypedToken(attrs["token"])

        if (
            api_settings.BLACKLIST_AFTER_ROTATION
            and "rest_framework_simplejwt.token_blacklist" in settings.INSTALLED_APPS
        ):
            jti = token.get(api_settings.JTI_CLAIM)
            if BlacklistedToken.objects.filter(token__jti=jti).exists():
                raise ValidationError("Token is blacklisted")

        return {'detail' : 'ok'}
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude  = ['password', 'groups', 'user_permissions', 'is_active',]
  
