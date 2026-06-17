from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.accounts.models import User
from apps.organizations.models import Organization
from apps.subscriptions.models import (
    Plan,
    Subscription
)

from .serializers import (
    RegisterOrganizationSerializer
)


class RegisterOrganizationView(APIView):

    def post(self, request):

        serializer = RegisterOrganizationSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        starter_plan = Plan.objects.get(
            name="Starter"
        )

        organization = Organization.objects.create(
            name=data["company_name"],
            gst_number=data["gst_number"],
            pan_number=data["pan_number"],
            email=data["email"],
            phone=data["phone"],
            plan=starter_plan,
            is_active=True
        )

        owner = User.objects.create_user(
            username=data["email"],
            email=data["email"],
            password=data["password"],
            phone=data["phone"],
            role=User.Role.OWNER,
            organization=organization,
            is_verified=True
        )

        Subscription.objects.create(
            organization=organization,
            plan=starter_plan,
            start_date=timezone.now(),
            expiry_date=timezone.now() + timedelta(days=7),
            status="TRIAL",
            is_active=True
        )

        return Response(
            {
                "message":
                "Organization registered successfully",

                "organization_id":
                organization.id,

                "owner_id":
                owner.id
            },
            status=status.HTTP_201_CREATED
        )