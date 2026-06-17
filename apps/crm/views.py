from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (
    Lead,
    Customer,
    FollowUp,
    Task
)

from .serializers import (
    LeadSerializer,
    CustomerSerializer,
    FollowUpSerializer,
    TaskSerializer
)


class LeadViewSet(ModelViewSet):

    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Lead.objects.filter(
            organization=self.request.user.organization
        ).select_related(
            "assigned_to"
        )

    def perform_create(self, serializer):

        serializer.save(
            organization=self.request.user.organization
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def convert(self, request, pk=None):

        lead = self.get_object()

        customer = Customer.objects.create(
            organization=lead.organization,
            lead=lead,
            company_name=lead.company_name or lead.name,
            contact_person=lead.name,
            phone=lead.phone,
            email=lead.email,
        )

        lead.status = Lead.Status.WON
        lead.save()

        return Response(
            {
                "message": "Lead converted successfully",
                "customer_id": customer.id
            },
            status=status.HTTP_201_CREATED
        )


class CustomerViewSet(ModelViewSet):

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Customer.objects.filter(
            organization=self.request.user.organization
        )

    def perform_create(self, serializer):

        serializer.save(
            organization=self.request.user.organization
        )


class FollowUpViewSet(ModelViewSet):

    serializer_class = FollowUpSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return FollowUp.objects.filter(
            lead__organization=self.request.user.organization
        )

    def perform_create(self, serializer):

        serializer.save(
            created_by=self.request.user
        )


class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Task.objects.filter(
            organization=self.request.user.organization
        )

    def perform_create(self, serializer):

        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )