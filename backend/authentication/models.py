from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .validators import username_validator , phonenumber_validator , profile_picture_validator


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and -/_ only.'),
        validators=[username_validator,],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), blank=True)
    profile_image = models.ImageField(_('profile image'), upload_to='user_profile/', default="defaults/user.png", validators=[profile_picture_validator])
    phone_number = models.CharField(_('phone number'), max_length=15, blank=True, null=True,validators=[phonenumber_validator])