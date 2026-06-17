from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
import uuid


class User(AbstractUser):

    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN"
        OWNER = "OWNER"
        MANAGER = "MANAGER"
        HR = "HR"
        ACCOUNTANT = "ACCOUNTANT"
        EMPLOYEE = "EMPLOYEE"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.EMPLOYEE)

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True
    )

    phone = models.CharField(max_length=15, blank=True)

    created_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_users"
    )

    is_verified = models.BooleanField(default=False)
    

    current_session_id = models.UUIDField(
        null=True,
        blank=True
    )

    objects = UserManager()

    def __str__(self):
        return self.username