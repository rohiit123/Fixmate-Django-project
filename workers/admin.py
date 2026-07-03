from django.contrib import admin
from .models import WorkerProfile


@admin.register(WorkerProfile)
class WorkerProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "city",
        "hourly_rate",
        "verified",
        "available",
    )

    list_filter = (
        "verified",
        "available",
        "city",
    )

    search_fields = (
        "user__username",
        "city",
    )

    filter_horizontal = (
        "services",
    )