from rest_framework import serializers


class RegisterOrganizationSerializer(serializers.Serializer):

    company_name = serializers.CharField(max_length=255)

    gst_number = serializers.CharField(max_length=15)

    pan_number = serializers.CharField(max_length=10)

    email = serializers.EmailField()

    phone = serializers.CharField(max_length=15)

    owner_name = serializers.CharField(max_length=150)

    password = serializers.CharField(
        min_length=8,
        write_only=True
    )