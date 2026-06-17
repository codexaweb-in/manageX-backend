from django.db import models

# Create your models here.
from django.db import models


class Lead(models.Model):

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        CONTACTED = "CONTACTED", "Contacted"
        QUALIFIED = "QUALIFIED", "Qualified"
        PROPOSAL_SENT = "PROPOSAL_SENT", "Proposal Sent"
        NEGOTIATION = "NEGOTIATION", "Negotiation"
        WON = "WON", "Won"
        LOST = "LOST", "Lost"

    class Source(models.TextChoices):
        WEBSITE = "WEBSITE", "Website"
        GOOGLE = "GOOGLE", "Google"
        FACEBOOK = "FACEBOOK", "Facebook"
        INSTAGRAM = "INSTAGRAM", "Instagram"
        WHATSAPP = "WHATSAPP", "WhatsApp"
        REFERRAL = "REFERRAL", "Referral"
        MANUAL = "MANUAL", "Manual"

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="leads"
    )

    name = models.CharField(max_length=255)

    company_name = models.CharField(
        max_length=255,
        blank=True
    )

    phone = models.CharField(max_length=15)

    email = models.EmailField(
        blank=True,
        null=True
    )

    source = models.CharField(
        max_length=20,
        choices=Source.choices,
        default=Source.MANUAL
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.NEW
    )

    assigned_to = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_leads"
    )

    expected_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Customer(models.Model):

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="customers"
    )

    lead = models.OneToOneField(
        Lead,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="customer"
    )

    company_name = models.CharField(
        max_length=255
    )

    contact_person = models.CharField(
        max_length=255
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    gst_number = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    industry = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.company_name


class FollowUp(models.Model):

    class FollowUpType(models.TextChoices):
        CALL = "CALL", "Call"
        WHATSAPP = "WHATSAPP", "WhatsApp"
        EMAIL = "EMAIL", "Email"
        MEETING = "MEETING", "Meeting"

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        related_name="followups"
    )

    follow_up_type = models.CharField(
        max_length=20,
        choices=FollowUpType.choices
    )

    remarks = models.TextField()

    follow_up_date = models.DateTimeField()

    next_follow_up = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.lead.name} - {self.follow_up_type}"


class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    assigned_to = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks"
    )

    due_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    priority = models.CharField(
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_tasks"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title