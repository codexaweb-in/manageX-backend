from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(ModelViewSet):

    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.role == "SUPER_ADMIN":
            return Organization.objects.all()

        return Organization.objects.filter(
            id=user.organization_id
        )