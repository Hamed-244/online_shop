from django.urls import path, include
from rest_framework import routers
from admin_panel import views

# define viewsets urls
router = routers.DefaultRouter()
router.register(r'users', views.UsersCrudViewSet)

urlpatterns = [

]

# add viewsets urls to urlpatterns
urlpatterns += router.urls