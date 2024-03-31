from django.shortcuts import render
from django.http import HttpResponseRedirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

from dj_rest_auth.registration.views import RegisterView as DefaultRegisterView
from .serializers import CustomRegisterSerializer

class RegisterView(DefaultRegisterView):
    serializer_class = CustomRegisterSerializer

    def get_response_data(self, user):
        return {
            'name': user.name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
            'profile_image': user.profile_image.url if user.profile_image else None,
        }


