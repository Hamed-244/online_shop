from django.urls import path
from dj_rest_auth.views import LoginView, LogoutView
from .views import RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("register/", RegisterView.as_view(), name="rest_register"), 
]
