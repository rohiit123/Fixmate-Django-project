from django.db import models
from django.conf import settings
from services.models import Service


class WorkerProfile(models.Model):

    EXPERIENCE_CHOICES = [
        ("0-1", "0-1 Year"),
        ("1-3", "1-3 Years"),
        ("3-5", "3-5 Years"),
        ("5+", "5+ Years"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    services = models.ManyToManyField(Service)

    experience = models.CharField(
        max_length=10,
        choices=EXPERIENCE_CHOICES
    )

    hourly_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    city = models.CharField(
        max_length=100
    )

    address = models.TextField()

    bio = models.TextField()

    profile_image = models.ImageField(
        upload_to="workers/",
        blank=True,
        null=True
    )

    verified = models.BooleanField(
        default=False
    )

    available = models.BooleanField(
        default=True
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0
    )

    total_jobs = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username