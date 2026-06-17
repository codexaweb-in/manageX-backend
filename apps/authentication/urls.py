from django.urls import path

from .views import (
    RegisterOrganizationView
)

urlpatterns = [

    path(
        "register-organization/",
        RegisterOrganizationView.as_view(),
        name="register-organization"
    ),
]