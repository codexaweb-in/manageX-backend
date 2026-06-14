from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "plan",
        "is_active",
    )

    search_fields = (
        "name",
        "email",
        "phone",
    )