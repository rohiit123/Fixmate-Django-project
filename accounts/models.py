from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('worker', 'Worker'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='customer'
    )

    phone = models.CharField(
        max_length=15,
        unique=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"