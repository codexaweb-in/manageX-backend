from django.contrib import admin

from .models import Plan, Subscription


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "max_managers",
        "max_hr",
        "max_accountants",
        "max_employees",
        "is_active"
    )

    search_fields = (
        "name",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "organization",
        "plan",
        "status",
        "is_active",
        "start_date",
        "expiry_date"
    )

    search_fields = (
        "organization__name",
    )

    list_filter = (
        "status",
        "is_active"
    )