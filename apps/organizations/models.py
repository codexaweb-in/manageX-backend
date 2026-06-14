from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=15,
        unique=True
    )

    plan = models.ForeignKey(
        "subscriptions.Plan",
        on_delete=models.PROTECT,
        related_name="organizations"
    )

    is_active = models.BooleanField(
        default=True
    )

    email_verified = models.BooleanField(
        default=False
    )

    phone_verified = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name