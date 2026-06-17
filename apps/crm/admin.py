from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    Lead,
    Customer,
    FollowUp,
    Task
)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "company_name",
        "phone",
        "source",
        "status",
        "assigned_to",
        "expected_value",
        "created_at"
    )

    list_filter = (
        "status",
        "source",
        "created_at"
    )

    search_fields = (
        "name",
        "company_name",
        "phone",
        "email"
    )

    ordering = (
        "-created_at",
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "company_name",
        "contact_person",
        "phone",
        "email",
        "gst_number",
        "industry",
        "created_at"
    )

    search_fields = (
        "company_name",
        "contact_person",
        "phone",
        "email",
        "gst_number"
    )

    ordering = (
        "-created_at",
    )


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "lead",
        "follow_up_type",
        "follow_up_date",
        "next_follow_up",
        "created_by",
        "created_at"
    )

    list_filter = (
        "follow_up_type",
        "follow_up_date"
    )

    search_fields = (
        "lead__name",
        "lead__phone"
    )

    ordering = (
        "-follow_up_date",
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "assigned_to",
        "priority",
        "status",
        "due_date",
        "created_at"
    )

    list_filter = (
        "status",
        "priority"
    )

    search_fields = (
        "title",
        "description"
    )

    ordering = (
        "-created_at",
    )