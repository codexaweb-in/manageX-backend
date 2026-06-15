from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from .services import UserPermissionService, PlanLimitService
from rest_framework.pagination import PageNumberPagination
from rest_framework import status




class StandardResultSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page_size"
    max_page_size = 30



class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Registration successful"
            },
            status=status.HTTP_201_CREATED
        )


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user

        if user.role == "SUPER_ADMIN":
            return User.objects.all()

        return User.objects.filter(organization=user.organization)

    def perform_create(self, serializer):

        request_user = self.request.user
        target_role = self.request.data.get("role")

        # 1. Role permission check
        if not UserPermissionService.can_create(request_user, target_role):
            raise Exception("You are not allowed to create this role")

        # 2. Plan limit check
        PlanLimitService.check_limit(request_user.organization, target_role)

        serializer.save(
            created_by=request_user,
            organization=request_user.organization
        )

 
class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),

            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role,
                "organization": user.organization.id if user.organization else None
            }
        })