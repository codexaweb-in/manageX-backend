from rest_framework.routers import DefaultRouter

from .views import (
    PlanViewSet,
    SubscriptionViewSet
)

router = DefaultRouter()

router.register(
    "plans",
    PlanViewSet
)

router.register(
    "subscriptions",
    SubscriptionViewSet
)

urlpatterns = router.urls