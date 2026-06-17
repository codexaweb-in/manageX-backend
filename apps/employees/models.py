from django.db import models


class Employee(models.Model):

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="employees"
    )

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="employee_profile"
    )

    employee_code = models.CharField(
        max_length=50,
        unique=True, blank=True
    )

    department = models.CharField(
        max_length=100
    )

    designation = models.CharField(
        max_length=100
    )

    joining_date = models.DateField()

    reporting_manager = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subordinates"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.employee_code} - {self.user.username}"
    

class SalaryStructure(models.Model):

    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="salary_structure"
    )

    basic_salary = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    hra = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    allowance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.employee.employee_code