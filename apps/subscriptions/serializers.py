from rest_framework import serializers

from .models import (
    Plan,
    Subscription
)


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):

    organization_name = serializers.CharField(
        source="organization.name",
        read_only=True
    )

    plan_name = serializers.CharField(
        source="plan.name",
        read_only=True
    )

    class Meta:
        model = Subscription

        fields = [
            "id",
            "organization",
            "organization_name",
            "plan",
            "plan_name",
            "status",
            "is_active",
            "start_date",
            "expiry_date",
            "created_at"
        ]