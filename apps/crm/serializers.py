from rest_framework import serializers

from .models import (
    Lead,
    Customer,
    FollowUp,
    Task
)


class LeadSerializer(serializers.ModelSerializer):

    assigned_to_name = serializers.CharField(
        source="assigned_to.username",
        read_only=True
    )

    class Meta:
        model = Lead

        fields = [
            "id",
            "organization",
            "name",
            "company_name",
            "phone",
            "email",
            "source",
            "status",
            "assigned_to",
            "assigned_to_name",
            "expected_value",
            "remarks",
            "created_at",
            "updated_at"
        ]

        read_only_fields = (
            "organization",
            "created_at",
            "updated_at"
        )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer

        fields = "__all__"

        read_only_fields = (
            "organization",
            "created_at"
        )


class FollowUpSerializer(serializers.ModelSerializer):

    created_by_name = serializers.CharField(
        source="created_by.username",
        read_only=True
    )

    class Meta:
        model = FollowUp

        fields = "__all__"

        read_only_fields = (
            "created_by",
            "created_at"
        )


class TaskSerializer(serializers.ModelSerializer):

    assigned_to_name = serializers.CharField(
        source="assigned_to.username",
        read_only=True
    )

    created_by_name = serializers.CharField(
        source="created_by.username",
        read_only=True
    )

    class Meta:
        model = Task

        fields = "__all__"

        read_only_fields = (
            "organization",
            "created_by",
            "created_at"
        )