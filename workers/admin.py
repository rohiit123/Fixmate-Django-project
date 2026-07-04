from django.contrib import admin
from .models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "service",
        "experience",
        "starting_price",
        "available",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
    )

    list_filter = (
        "service",
        "available",
    )