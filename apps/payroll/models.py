from django.db import models
from apps.employees.models import Employee

# Create your models here.
class Payroll(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    month = models.PositiveIntegerField()

    year = models.PositiveIntegerField()

    basic_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    allowances = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    deductions = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    is_paid = models.BooleanField(
        default=False
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )