from django.urls import path
from .views import UserCreate, UserList
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user_register'),
    path('users/', UserList.as_view(), name='user_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
