from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceViewSet(ModelViewSet):

    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Attendance.objects.filter(
            organization=self.request.user.organization
        )

    def perform_create(self, serializer):

        serializer.save(
            organization=self.request.user.organization
        )