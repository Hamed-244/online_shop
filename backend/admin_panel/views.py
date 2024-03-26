from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from admin_panel.serializers import (UserSerializer, ProductSerializer)
from admin_panel.models import (Product,)

User = get_user_model()

class UsersCrudViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProductCrudViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]