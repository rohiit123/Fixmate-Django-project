from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.worker_register, name="worker_register"),
]