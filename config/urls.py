from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/organizations/",
        include("apps.organizations.urls")
    ),
    path(
        "api/v1/subscriptions/",
        include("apps.subscriptions.urls")
    ),
    path(
    "api/v1/accounts/",
    include("apps.accounts.urls")
    ),
]