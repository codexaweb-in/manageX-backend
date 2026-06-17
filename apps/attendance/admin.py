from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "employee",
        "date",
        "status",
        "check_in",
        "check_out",
        "working_hours"
    )

    list_filter = (
        "status",
        "date"
    )

    search_fields = (
        "employee__employee_code",
        "employee__user__username"
    )