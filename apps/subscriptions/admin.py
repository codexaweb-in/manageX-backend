from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "max_owners",
        "max_managers",
        "max_hr",
        "max_accountants",
        "max_employees",
    )