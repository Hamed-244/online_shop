from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from admin_panel.serializers import UserSerializer

User = get_user_model()

class UsersCrudViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]