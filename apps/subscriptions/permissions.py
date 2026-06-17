from rest_framework.permissions import BasePermission


class HasActiveSubscription(BasePermission):

    def has_permission(self, request, view):

        user = request.user

        if user.role == "SUPER_ADMIN":
            return True

        subscription = getattr(
            user.organization,
            "subscription",
            None
        )

        if not subscription:
            return False

        return subscription.is_active