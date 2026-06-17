from django.contrib import admin

from .models import (
    Employee,
    SalaryStructure
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        "employee_code",
        "user",
        "department",
        "designation",
        "joining_date",
        "is_active"
    )

    search_fields = (
        "employee_code",
        "user__username",
        "department"
    )


@admin.register(SalaryStructure)
class SalaryStructureAdmin(admin.ModelAdmin):

    list_display = (
        "employee",
        "basic_salary",
        "hra",
        "allowance"
    )