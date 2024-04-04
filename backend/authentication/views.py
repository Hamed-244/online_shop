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

from dj_rest_auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

from dj_rest_auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    pass
