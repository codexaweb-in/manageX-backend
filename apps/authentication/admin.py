from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import OTPVerification


@admin.register(OTPVerification)
class OTPVerificationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "email",
        "phone",
        "otp",
        "is_verified",
        "expires_at"
    )