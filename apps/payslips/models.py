from django.db import models
from apps.payroll.models import Payroll

# Create your models here.
class Payslip(models.Model):

    payroll = models.OneToOneField(
        Payroll,
        on_delete=models.CASCADE,
        related_name="payslip"
    )

    pdf_file = models.FileField(
        upload_to="payslips/"
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )