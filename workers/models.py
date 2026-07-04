from django.db import models
from accounts.models import User
from services.models import Service


class Worker(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="worker_profile"
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    experience = models.PositiveIntegerField()

    starting_price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    about = models.TextField()

    address = models.CharField(
        max_length=250
    )

    profile_photo = models.ImageField(
        upload_to="workers/",
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    rating = models.FloatField(default=5.0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username