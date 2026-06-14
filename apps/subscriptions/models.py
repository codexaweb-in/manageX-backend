from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)

    max_owners = models.PositiveIntegerField(default=1)
    max_managers = models.PositiveIntegerField(default=0)
    max_hr = models.PositiveIntegerField(default=0)
    max_accountants = models.PositiveIntegerField(default=0)
    max_employees = models.PositiveIntegerField(default=0)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name