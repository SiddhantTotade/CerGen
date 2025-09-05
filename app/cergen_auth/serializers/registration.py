from rest_framework import serializers

from django.core.cache import cache
from ..models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    key = serializers.CharField(write_only=True)
    password2 = serializers.CharField(style={"input-type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_key(self, value):
        if not cache.get(value):
            raise serializers.ValidationError("Invalid of expired key.")
        return value

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password are not matching"
            )

        return attrs

    def create(self, validated_data):
        key = validated_data.pop("key")
        user = User.objects.create_user(**validated_data)
        cache.delete(key)
        return user