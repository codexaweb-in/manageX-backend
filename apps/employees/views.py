from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    Employee,
    SalaryStructure
)

from .serializers import (
    EmployeeSerializer,
    SalaryStructureSerializer
)


class EmployeeViewSet(ModelViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Employee.objects.filter(
            organization=self.request.user.organization
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            organization=self.request.user.organization
        )


class SalaryStructureViewSet(
    ModelViewSet
):

    serializer_class = (
        SalaryStructureSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    queryset = SalaryStructure.objects.all()