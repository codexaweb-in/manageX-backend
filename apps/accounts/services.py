from django.core.exceptions import ValidationError
from .models import User


class UserPermissionService:

    ROLE_HIERARCHY = {
        "SUPER_ADMIN": ["OWNER", "MANAGER", "HR", "ACCOUNTANT", "EMPLOYEE"],
        "OWNER": ["MANAGER", "HR", "ACCOUNTANT", "EMPLOYEE"],
        "MANAGER": ["HR","ACCOUNTANT", "EMPLOYEE"],
        "HR": ["EMPLOYEE"],
        "ACCOUNTANT": [],
        "EMPLOYEE": []
    }

    @staticmethod
    def can_create(request_user, target_role):

        allowed = UserPermissionService.ROLE_HIERARCHY.get(
            request_user.role,
            []
        )

        return target_role in allowed


class PlanLimitService:

    @staticmethod
    def check_limit(organization, role):

        counts = User.objects.filter(
            organization=organization,
            role=role
        ).count()

        plan = organization.plan

        limits = {
            "OWNER": plan.max_owners,
            "MANAGER": plan.max_managers,
            "HR": plan.max_hr,
            "ACCOUNTANT": plan.max_accountants,
            "EMPLOYEE": plan.max_employees
        }

        limit = limits.get(role)

        if limit is None:
            return True

        if counts >= limit:
            raise ValidationError(
                f"{role} limit reached for your plan. Upgrade required."
            )

        return True