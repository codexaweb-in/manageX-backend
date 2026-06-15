from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "role",
            "password",
            "organization",
            "created_by"
        ]

        read_only_fields = [
            "organization",
            "created_by"
        ]

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        user = authenticate(
            username=data["username"],
            password=data["password"]
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid credentials"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "Account is disabled"
            )

        data["user"] = user

        return data
    


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "phone",
            "password"
        ]

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = User(
            **validated_data,
            role="OWNER"
        )

        user.set_password(password)

        user.save()

        return user