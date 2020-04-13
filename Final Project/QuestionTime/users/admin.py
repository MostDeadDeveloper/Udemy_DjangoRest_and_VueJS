from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
# Register your models here.


class CustomerUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username",
                    "email",
                    "is_staff"]

admin.site.register(CustomUser, CustomerUserAdmin)
