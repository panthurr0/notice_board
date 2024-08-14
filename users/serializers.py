from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['token', 'role']


class UserResetPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class UserResetPasswordConfirmSerializer(ModelSerializer):
    uid = serializers.IntegerField()
    token = serializers.CharField(max_length=10)
    new_password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ["uid", "token", "new_password"]
