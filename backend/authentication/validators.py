from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def username_validator(value):
    allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
    for char in value:
        if char not in allowed_characters:
            raise ValidationError(_("Invalid character in the username. Only English letters, numbers, hyphens, and underscores are allowed."))

def phonenumber_validator(value):
    pattern = r'^(\+98|0)9\d{9}$'

    if not re.match(pattern, value):
        raise ValidationError(_('The phone number entered is not correct.'))

def national_id_validator(value):

    if len(value) != 10:
        raise ValidationError(_('The entered national code must be 10 digits.'))

    control_digit = int(value[9])
    sum = 0
    for i in range(9):
        sum += int(value[i]) * (10 - i)
    remainder = sum % 11

    if remainder < 2 and control_digit != remainder:
        raise ValidationError(_('The entered national code is not correct.'))
    elif remainder >= 2 and control_digit != 11 - remainder:
        raise ValidationError(_('The entered national code is not correct.'))

def profile_picture_validator(value):
    if not value.name.endswith('.png') and not value.name.endswith('.jpg') and not value.name.endswith('.jpeg'):
        raise ValidationError(_('The type of entered file must be png, jpg or jpeg.'))