from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "role",
        "phone",
        "city",
        "is_verified",
    )

    list_filter = ("role", "is_verified")

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "role",
                    "phone",
                    "city",
                    "profile_image",
                    "is_verified",
                )
            },
        ),
    )