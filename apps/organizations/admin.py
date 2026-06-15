from django.contrib import admin
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "gst_number",
        "phone",
        "email",
        "plan",
        "is_active"
    )

    search_fields = (
        "name",
        "gst_number",
        "email",
        "phone"
    )