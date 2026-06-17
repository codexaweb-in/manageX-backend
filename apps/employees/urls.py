from rest_framework.routers import DefaultRouter

from .views import (
    EmployeeViewSet,
    SalaryStructureViewSet
)

router = DefaultRouter()

router.register(
    "employees",
    EmployeeViewSet,
    basename="employees"
)

router.register(
    "salary-structures",
    SalaryStructureViewSet,
    basename="salary-structures"
)

urlpatterns = router.urls