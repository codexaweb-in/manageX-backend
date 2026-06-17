from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)

    gst_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True
    )

    pan_number = models.CharField(
        max_length=10,
        blank=True
    )

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=15,
        unique=True,
        blank=True
    )

    address = models.TextField(blank=True)

    business_type = models.CharField(
        max_length=100,
        blank=True
    )

    plan = models.ForeignKey(
        "subscriptions.Plan",
        on_delete=models.PROTECT
    )

    is_active = models.BooleanField(
        default=False
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