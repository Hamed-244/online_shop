from django.urls import path, include
from rest_framework import routers

# define viewsets urls
router = routers.DefaultRouter()

urlpatterns = [

]

# add viewsets urls to urlpatterns
urlpatterns += router.urls