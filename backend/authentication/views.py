from django.shortcuts import render
from django.http import HttpResponseRedirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

def ConfirmEmailRedirectView(request , key = None) :
    # this will redirect to our frontend page 
    redirect_url = settings.CONFIRM_EMAIL_REDIRECT_URL
    if key :
        redirect_url += f'?key={key}'
    return HttpResponseRedirect(redirect_url)


def PasswordResetRedirectView(request , uid = None , token = None) :
    # this will redirect to our frontend page 
    redirect_url = settings.PASSWORD_RESET_REDIRECT_URL
    if uid and token :
        redirect_url += f'?uid={uid}&token={token}'
    return HttpResponseRedirect(redirect_url)


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_CALLBACK_URL
    client_class = OAuth2Client


class GetGoogleLoginEndpointView(APIView) :

    def get(self , request) :
        url = f"https://accounts.google.com/o/oauth2/v2/auth?\
redirect_uri={settings.GOOGLE_CALLBACK_URL}&prompt=consent&response_type=code&client_id={settings.GOOGLE_CLINET_ID}\
&scope=openid%20email%20profile&access_type=online"
        data = {
            'url' : url
        }
        return Response(data , status=200)