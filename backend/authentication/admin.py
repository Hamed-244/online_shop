from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User

UserAdmin.fieldsets[0][1]['fields'] = ("username" , "phone_number" , "password")
UserAdmin.list_display = ("username", "email", "phone_number" , "first_name", "last_name", "is_staff" )

admin.site.register(User, UserAdmin)