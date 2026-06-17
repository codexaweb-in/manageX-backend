from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    Plan,
    Subscription
)

from .serializers import (
    PlanSerializer,
    SubscriptionSerializer
)


class PlanViewSet(ModelViewSet):

    queryset = Plan.objects.all()

    serializer_class = PlanSerializer

    permission_classes = [
        IsAuthenticated
    ]


class SubscriptionViewSet(ModelViewSet):

    queryset = Subscription.objects.all()

    serializer_class = SubscriptionSerializer

    permission_classes = [
        IsAuthenticated
    ]