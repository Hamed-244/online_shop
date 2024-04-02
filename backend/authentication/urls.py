from django.urls import path
from dj_rest_auth.views import LoginView, LogoutView
from .views import RegisterView, CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("register/", RegisterView.as_view(), name="rest_register"), 
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/confirm/<slug:uidb64>/<slug:token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
