from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import DEFAULT_FROM_EMAIL
from users.models import User
from users.serializers import UserSerializer, UserResetPasswordSerializer
from users.services import generate_password, send_email


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserResetPasswordView(APIView):
    serializer_class = UserResetPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        user = User.objects.get(email=email)
        uid = user.pk
        token = generate_password(8)
        user.token = token
        user.save()
        send_email(uid, token, user.email)

        return Response(
            {"success": "Письмо с восстановлением пароля отправлено"},
            status=status.HTTP_200_OK,
        )


class UserResetPasswordConfirmView(APIView):
    serializer_class = UserResetPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        uid = request.data.get("uid")
        token = request.data.get("token")
        new_password = request.data.get("new_password")

        user = User.objects.get(
            id=uid
        )  # todo обработать exception, что все поля заполнены
        if user.token.strip() == token.strip():
            user.set_password(new_password)
            user.token = "-"
            user.save()
            return Response(
                {"success": "Отлично! Ваш пароль обновлён"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Что-то не так"}, status=status.HTTP_400_BAD_REQUEST
            )
