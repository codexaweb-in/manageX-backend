from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserViewSet, LoginView


router = DefaultRouter()
router.register("", UserViewSet)


urlpatterns = [
    # User CRUD APIs (ViewSet)
    path("", include(router.urls)),

    # Auth APIs
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]