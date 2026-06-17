from rest_framework.routers import DefaultRouter

from .views import (
    LeadViewSet,
    CustomerViewSet,
    FollowUpViewSet,
    TaskViewSet
)

router = DefaultRouter()

router.register(
    "leads",
    LeadViewSet,
    basename="leads"
)

router.register(
    "customers",
    CustomerViewSet,
    basename="customers"
)

router.register(
    "followups",
    FollowUpViewSet,
    basename="followups"
)

router.register(
    "tasks",
    TaskViewSet,
    basename="tasks"
)

urlpatterns = router.urls